---
title: Hermes LiteLLM macOS 开机编排启动配置笔记
aliases:
  - Hermes LiteLLM macOS Ordered Startup
  - hermes LiteLLM 开机编排启动
  - hermes/配置/开机编排启动(KJBPQD, HLOS)
tags:
  - Hermes
  - LiteLLM
  - Docker
  - macOS
  - launchd
description: 记录 Hermes 依赖的本地 LiteLLM 在 macOS 登录后按 Docker Desktop、Postgres、LiteLLM 顺序编排启动的配置、诊断和回滚方式。
type: 操作指南
create-date: 2026-05-02
ref-url:
---

# Hermes LiteLLM macOS 开机编排启动配置笔记

## 问题背景

Hermes 当前通过本地 LiteLLM 代理访问模型：

```text
Hermes -> http://localhost:4000/v1 -> LiteLLM -> litellm-postgres
```

原配置中 `launchd` 登录即直接启动 LiteLLM：

```text
ProgramArguments = /Users/haoxc/.litellm/start_proxy.sh
KeepAlive = true
```

当 macOS 刚登录、Docker Desktop 尚未启动，或 Docker 中的 `litellm-postgres` 尚未监听 `127.0.0.1:5432` 时，LiteLLM 会先失败，再被 `KeepAlive=true` 反复拉起。表现为 Hermes 启动后持续报：

```text
APIConnectionError
Endpoint: http://localhost:4000/v1
Error: Connection error
```

LiteLLM 日志中的关键错误是：

```text
Can't reach database server at 127.0.0.1:5432
ERROR: [Errno 48] Address already in use
```

判断：这不是 Hermes 模型配置问题，根因是本地依赖启动顺序不稳定。

## 目标状态

开机或登录后的启动顺序必须固定为：

```text
Docker Desktop -> Docker daemon ready -> litellm-postgres -> 127.0.0.1:5432 reachable -> LiteLLM :4000 -> Hermes
```

核心原则：

- 只有一个 `launchd` 入口负责编排启动。
- Docker 或 Postgres 未就绪时，不启动 LiteLLM。
- 使用原子锁防止重复启动。
- 失败后由 `launchd` 温和重试，不再疯狂重启。

## 已落地文件

| 文件 | 作用 |
| --- | --- |
| `~/.litellm/start_litellm_stack.sh` | 新增编排脚本，负责 Docker、Postgres、LiteLLM 的顺序启动 |
| `~/.litellm/start_proxy.sh` | 原 LiteLLM 启动脚本，继续只负责启动 LiteLLM 本体 |
| `~/Library/LaunchAgents/com.haoxc.litellm.plist` | macOS 登录后启动编排脚本 |
| `~/.litellm/logs/litellm.launchd.err.log` | 编排脚本与 LiteLLM stderr 日志 |
| `~/.litellm/logs/litellm.launchd.out.log` | LiteLLM stdout 日志 |

备份文件：

```text
~/Library/LaunchAgents/com.haoxc.litellm.plist.bak-20260502104841
~/.litellm/start_proxy.sh.bak-20260502104841
```

## 编排脚本逻辑

脚本入口：

```bash
~/.litellm/start_litellm_stack.sh
```

关键配置：

```bash
LABEL="com.haoxc.litellm"
LOCK_DIR="${TMPDIR:-/tmp}/${LABEL}.startup.lock"
POSTGRES_CONTAINER="${LITELLM_POSTGRES_CONTAINER:-litellm-postgres}"
POSTGRES_HOST="${LITELLM_POSTGRES_HOST:-127.0.0.1}"
POSTGRES_PORT="${LITELLM_POSTGRES_PORT:-5432}"
LITELLM_HOST="${LITELLM_HOST:-127.0.0.1}"
LITELLM_PORT="${LITELLM_PORT:-4000}"
START_PROXY="/Users/haoxc/.litellm/start_proxy.sh"
```

核心流程：

```text
1. 创建启动锁，已有有效锁时直接退出。
2. 后台打开 Docker Desktop。
3. 等 `docker info` 成功。
4. 检查 `litellm-postgres` 容器是否存在。
5. 容器未运行时执行 `docker start litellm-postgres`。
6. 等 `127.0.0.1:5432` 可连接。
7. 若 `127.0.0.1:4000` 已被占用，则不重复启动 LiteLLM。
8. 执行 `~/.litellm/start_proxy.sh`，并让 launchd 管住该子进程生命周期。
```

端口等待使用带超时的 `nc`：

```bash
port_is_open() {
    nc -G 2 -z "$1" "$2"
}
```

这个处理避免 `nc` 探测在登录早期异常挂住。

## LaunchAgent 配置

LaunchAgent 文件：

```text
~/Library/LaunchAgents/com.haoxc.litellm.plist
```

当前关键项：

```text
ProgramArguments = /Users/haoxc/.litellm/start_litellm_stack.sh
RunAtLoad = true
KeepAlive.SuccessfulExit = false
ThrottleInterval = 60
WorkingDirectory = /Users/haoxc
```

含义：

| 配置项 | 作用 |
| --- | --- |
| `ProgramArguments` | 不再直接启动 LiteLLM，而是先执行编排脚本 |
| `RunAtLoad` | 用户登录后自动启动 |
| `KeepAlive.SuccessfulExit=false` | 只有异常退出时才重启 |
| `ThrottleInterval=60` | 失败后至少间隔 60 秒再试，避免重启风暴 |

## 手动操作

重载并启动：

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.haoxc.litellm.plist 2>/dev/null || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.haoxc.litellm.plist
launchctl kickstart -k gui/$(id -u)/com.haoxc.litellm
```

查看 LaunchAgent：

```bash
launchctl print gui/$(id -u)/com.haoxc.litellm
```

查看 Docker Postgres：

```bash
docker ps --filter name=litellm-postgres --format '{{.Names}}\t{{.Status}}\t{{.Ports}}'
```

查看 LiteLLM 端口：

```bash
lsof -nP -iTCP:4000 -sTCP:LISTEN
```

健康检查：

```bash
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:4000/health/liveliness
```

预期返回：

```text
200
```

## 当前验证结果

本次修复后已确认：

```text
LaunchAgent: running
litellm-postgres: Up, 127.0.0.1:5432->5432/tcp
LiteLLM: listening on 127.0.0.1:4000
health check: HTTP 200
```

日志中成功路径：

```text
starting Docker Desktop in background
waiting for Docker daemon
Docker daemon is ready
Postgres container already running: litellm-postgres
waiting for Postgres on 127.0.0.1:5432
Postgres is reachable
starting LiteLLM
Uvicorn running on http://127.0.0.1:4000
Application startup complete.
```

## 排障口径

如果 Hermes 仍报 `http://localhost:4000/v1` 连接失败，按顺序查：

```bash
docker info
docker ps --filter name=litellm-postgres
launchctl print gui/$(id -u)/com.haoxc.litellm
lsof -nP -iTCP:4000 -sTCP:LISTEN
tail -n 80 ~/.litellm/logs/litellm.launchd.err.log
```

判断边界：

| 现象 | 优先判断 |
| --- | --- |
| `docker info` 失败 | Docker Desktop 未启动或 daemon 未就绪 |
| `127.0.0.1:5432` 不通 | `litellm-postgres` 未运行或端口未映射 |
| `127.0.0.1:4000` 不通 | LiteLLM 未启动 |
| `Address already in use` | 旧 LiteLLM worker 或其他进程占用端口 |
| Hermes 连接 `:4000/v1` 失败 | 先查 LiteLLM，不先改 Hermes 模型配置 |

清理残留 LiteLLM 进程时，应先停 LaunchAgent，再清残留 worker：

```bash
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.haoxc.litellm.plist 2>/dev/null || true
pkill -TERM -f '/Users/haoxc/Library/Application Support/uv/tools/litellm/bin/litellm --config /Users/haoxc/.litellm/config.yaml'
pkill -TERM -f '/Users/haoxc/Library/Application Support/uv/tools/litellm/bin/python -c from multiprocessing'
```

## 回滚方式

如果需要回到旧配置：

```bash
cp ~/Library/LaunchAgents/com.haoxc.litellm.plist.bak-20260502104841 ~/Library/LaunchAgents/com.haoxc.litellm.plist
launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.haoxc.litellm.plist 2>/dev/null || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.haoxc.litellm.plist
launchctl kickstart -k gui/$(id -u)/com.haoxc.litellm
```

但旧配置会重新暴露 Docker/Postgres 未就绪时的重启循环问题。

## 相关链接

- [[Hermes-LiteLLM-DeepSeek-Docker-Postgres配置笔记]]
- [[hermes-模型配置]]
- [[hermes-mac安装笔记]]
- [[Hermes-后台进程管理]]

> [!summary]
> Hermes 的本地模型链路不要让 LiteLLM 在登录时直接启动。当前更稳的方式是由 `com.haoxc.litellm` 先执行 `start_litellm_stack.sh`：等 Docker Desktop、Docker daemon 和 `litellm-postgres` 全部 ready 后，再启动 LiteLLM。这样可以避免 `127.0.0.1:5432` 未就绪导致的重启循环。
