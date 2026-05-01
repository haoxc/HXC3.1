---
title: Hermes LiteLLM DeepSeek Docker Postgres 配置笔记
aliases:
  - Hermes 通过 LiteLLM 访问 DeepSeek V4 Pro
  - Hermes DeepSeek V4 Pro 配置
  - LiteLLM Docker Postgres 自启动
tags:
  - mac-工具
  - AI工具
  - Hermes
  - LiteLLM
  - DeepSeek
  - Docker
description: 记录本机 Hermes 通过 LiteLLM 访问 DeepSeek V4 Pro，并由 Docker Postgres 与 launchd 支撑开机启动的配置要点、验证命令和工具调用兼容性修复。
type: 操作指南
create-date: 2026-04-29
ref-url:
---

# Hermes LiteLLM DeepSeek Docker Postgres 配置笔记

## 概述

本机目标是让 Hermes 使用本地 LiteLLM 代理访问 DeepSeek V4 Pro，并让 LiteLLM 在 macOS 登录后由 `launchd` 自动启动。LiteLLM 的数据库依赖放在 Docker 容器 `litellm-postgres` 中，因此完整链路需要同时关注 Docker Desktop、Postgres 容器、LiteLLM LaunchAgent 和 Hermes 配置。

当前结论：

- Docker Postgres 已启动：`litellm-postgres`
- Postgres 端口：`127.0.0.1:5432`
- Postgres restart policy：`unless-stopped`
- LiteLLM 已监听：`127.0.0.1:4000`
- LiteLLM 模型列表包含：`deepseek-v4-pro`、`deepseek-v4-pro-openai`
- Hermes 默认模型已指向：`deepseek-v4-pro-openai`
- Hermes 通过 LiteLLM 的 base URL：`http://localhost:4000/v1`

## 链路结构

| 层级 | 本机配置 | 作用 |
| --- | --- | --- |
| Hermes | `~/.hermes/config.yaml` | CLI/Agent 入口 |
| Hermes env | `~/.hermes/.env` | 保存 `LITELLM_MASTER_KEY` 等环境变量 |
| LiteLLM | `http://localhost:4000` | 本地模型代理 |
| LiteLLM OpenAI endpoint | `http://localhost:4000/v1` | Hermes custom provider 使用 |
| LiteLLM 配置 | `~/.litellm/config.yaml` | 模型别名与上游 provider |
| LiteLLM env | `~/.litellm/.env` | DeepSeek key、LiteLLM master key、数据库 URL |
| LiteLLM 启动脚本 | `~/.litellm/start_proxy.sh` | launchd 实际执行入口 |
| LaunchAgent | `~/Library/LaunchAgents/com.haoxc.litellm.plist` | macOS 登录后自动拉起 LiteLLM |
| Postgres | Docker 容器 `litellm-postgres` | LiteLLM 数据库 |

关键区别：

| 客户端 | endpoint |
| --- | --- |
| Claude Code CLI | `http://localhost:4000` |
| Hermes custom/OpenAI-compatible | `http://localhost:4000/v1` |

Claude Code CLI 走 Anthropic-compatible 入口，不加 `/v1`。Hermes 配成 `custom` provider 时走 OpenAI-compatible 入口，通常要加 `/v1`。

## Hermes 配置要点

Hermes 当前使用 `custom` provider 指向 LiteLLM：

```yaml
model:
  provider: custom
  default: deepseek-v4-pro-openai
  base_url: http://localhost:4000/v1
  api_key: ${LITELLM_MASTER_KEY}
```

配置命令：

```bash
hermes config set model.provider custom
hermes config set model.default deepseek-v4-pro-openai
hermes config set model.base_url http://localhost:4000/v1
hermes config set model.api_key '${LITELLM_MASTER_KEY}'
```

密钥不要写进 Vault。Hermes 侧只保留环境变量引用，真实值放在：

```text
~/.hermes/.env
~/.litellm/.env
```

## LiteLLM 配置要点

LiteLLM 中保留两个 DeepSeek V4 Pro 模型别名，分别服务不同客户端：

| 模型别名 | 上游格式 | 用途 |
| --- | --- | --- |
| `deepseek-v4-pro` | Anthropic-compatible | 保留给 Claude Code CLI 等 Anthropic 客户端 |
| `deepseek-v4-pro-openai` | OpenAI-compatible | 给 Hermes 使用，支持 Hermes 默认工具调用 |

`deepseek-v4-pro` 走 DeepSeek Anthropic-compatible endpoint：

```yaml
model_list:
  - model_name: deepseek-v4-pro
    litellm_params:
      model: anthropic/deepseek-v4-pro
      api_key: os.environ/DEEPSEEK_ANTHROPIC_API_KEY
      api_base: https://api.deepseek.com/anthropic
```

`deepseek-v4-pro-openai` 走 DeepSeek OpenAI-compatible endpoint：

```yaml
  - model_name: deepseek-v4-pro-openai
    litellm_params:
      model: openai/deepseek-v4-pro
      api_key: os.environ/DEEPSEEK_ANTHROPIC_API_KEY
      api_base: https://api.deepseek.com
```

关键判断：

```text
Claude Code 继续用 deepseek-v4-pro。
Hermes 默认用 deepseek-v4-pro-openai。
```

LiteLLM 启动脚本从 `~/.litellm/.env` 读取环境变量，并使用 Prisma DB push：

```bash
~/.litellm/start_proxy.sh
```

启动参数核心是：

```bash
litellm --config "$HOME/.litellm/config.yaml" \
  --host 127.0.0.1 \
  --port 4000 \
  --num_workers 4 \
  --use_prisma_db_push
```

## Docker Postgres 配置要点

Postgres 容器：

```text
litellm-postgres
```

当前映射：

```text
127.0.0.1:5432 -> 5432/tcp
```

启动容器：

```bash
docker start litellm-postgres
```

设置随 Docker daemon 自动启动：

```bash
docker update --restart unless-stopped litellm-postgres
```

确认状态：

```bash
docker ps --filter name=litellm-postgres
docker inspect -f '{{.Name}} {{.HostConfig.RestartPolicy.Name}} {{.State.Status}}' litellm-postgres
```

当前确认结果：

```text
/litellm-postgres unless-stopped running
```

> [!important]
> `unless-stopped` 的前提是 Docker Desktop 已经启动。它能保证 Docker daemon 启动后自动拉起 Postgres，但不等于 macOS 登录后自动打开 Docker Desktop。

## launchd 自启动配置

LiteLLM LaunchAgent：

```text
~/Library/LaunchAgents/com.haoxc.litellm.plist
```

关键项：

```text
ProgramArguments = /Users/haoxc/.litellm/start_proxy.sh
RunAtLoad = true
KeepAlive = true
WorkingDirectory = /Users/haoxc
stdout = /Users/haoxc/.litellm/logs/litellm.launchd.out.log
stderr = /Users/haoxc/.litellm/logs/litellm.launchd.err.log
```

手动重启 LiteLLM：

```bash
launchctl kickstart -k gui/$(id -u)/com.haoxc.litellm
```

查看运行状态：

```bash
launchctl print gui/$(id -u)/com.haoxc.litellm
lsof -nP -iTCP:4000 -sTCP:LISTEN
```

## 验证命令

确认 Docker Postgres：

```bash
docker ps --filter name=litellm-postgres
docker logs litellm-postgres
```

确认 LiteLLM 监听：

```bash
lsof -nP -iTCP:4000 -sTCP:LISTEN
```

确认模型列表：

```bash
source ~/.litellm/.env
curl -sS http://127.0.0.1:4000/v1/models \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
```

预期模型中包含：

```text
deepseek-v4-flash
deepseek-v4-pro
deepseek-v4-pro-openai
sonnet-4-6
opus-4-6
claude-haiku-4-5
```

确认 DeepSeek OpenAI-compatible 最小请求：

```bash
source ~/.litellm/.env
curl -sS http://127.0.0.1:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro-openai",
    "messages": [
      {
        "role": "user",
        "content": "只输出两个字母 OK，不要解释。"
      }
    ],
    "max_tokens": 64
  }'
```

当前已验证结果：

```text
deepseek-v4-pro-openai 可通过 LiteLLM 返回 OK。
```

确认工具调用：

```bash
source ~/.litellm/.env
curl -sS http://127.0.0.1:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-pro-openai",
    "messages": [
      {
        "role": "user",
        "content": "请调用 echo_answer 工具，参数 text 的值为 OK"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "echo_answer",
          "description": "Echo a short answer",
          "parameters": {
            "type": "object",
            "properties": {
              "text": {"type": "string"}
            },
            "required": ["text"]
          }
        }
      }
    ],
    "tool_choice": "auto",
    "max_tokens": 128
  }'
```

当前已验证结果：

```text
deepseek-v4-pro-openai 能返回 tool_calls，说明 DeepSeek OpenAI-compatible 路径可承载 Hermes 工具调用。
```

确认 Hermes 实际会话：

```bash
hermes chat -q '只回复 OK' -Q
hermes chat -q '请使用可用工具查看当前工作目录，只回复当前目录路径。' -Q
```

当前已验证结果：

```text
Hermes 默认模型 deepseek-v4-pro-openai 能完成普通回复，也能完成只读工具调用。
```

## 已解决课题

### Hermes 工具协议兼容

原问题：LiteLLM 到 DeepSeek 的最小文本请求可用，但 Hermes 默认会带工具定义。DeepSeek Anthropic-compatible endpoint 对 Hermes 经 LiteLLM 转换后的工具 schema 不兼容，会返回类似错误：

```text
tools[0]: unknown variant `custom`, expected `web_search_20250305` or `web_search_20260209`
```

判断：

- 这不是 Docker Postgres 问题。
- 这不是 LiteLLM 没启动。
- 这不是 `deepseek-v4-pro` 模型不可用。
- 这不是 LiteLLM、Postgres 或鉴权失败。
- 本质是 Hermes 工具定义经 LiteLLM 转到 DeepSeek Anthropic-compatible endpoint 时，工具 schema 没有对齐。

修复方式：

```text
保留 deepseek-v4-pro 作为 Anthropic-compatible 别名，继续服务 Claude Code。
新增 deepseek-v4-pro-openai 作为 OpenAI-compatible 别名，给 Hermes 使用。
Hermes 默认模型切到 deepseek-v4-pro-openai。
```

这比直接改掉 `deepseek-v4-pro` 更稳，因为不会破坏 Claude Code 的既有 Anthropic-compatible 配置。

### 启动顺序

当前启动链路依赖顺序是：

```text
Docker Desktop -> litellm-postgres -> LiteLLM LaunchAgent -> Hermes
```

如果系统刚登录时 Docker Desktop 尚未启动，LiteLLM 可能因数据库不可用而失败。`KeepAlive` 会尝试保活，但更稳的方案是：

- 将 Docker Desktop 加入 macOS 登录项；或
- 增加一个专门负责启动 Docker/Postgres 的 LaunchAgent；或
- 将 Postgres 从 Docker 迁到本机常驻服务。

## 相关链接

- [[hermes]]
- [[hermes-模型配置]]
- [[hermes-mac安装笔记]]
- [[09-工具/mac-工具/Hermes-Claude-Code-CLI协同方案]]

> [!summary]
> 本机 Hermes 已配置为通过 LiteLLM 的 `http://localhost:4000/v1` 使用 `deepseek-v4-pro-openai`。Docker 中的 `litellm-postgres` 已启动，并设置为 `unless-stopped`。LiteLLM 当前能列出 `deepseek-v4-pro` 与 `deepseek-v4-pro-openai`。Hermes 侧工具调用已通过 OpenAI-compatible 别名验证；Claude Code 侧可继续使用原 Anthropic-compatible `deepseek-v4-pro`。
