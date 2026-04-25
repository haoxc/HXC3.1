---
aliases:
tags:
description:
type:
ref-url:
---

---

## 前提条件

确保已安装 **Docker Desktop**（含 Docker Compose v2）。可从 [docker.com](https://www.docker.com/products/docker-desktop/) 下载。验证安装：

```bash
docker --version
docker compose version
```

---

## 方法一：官方脚本（推荐）

**第一步：克隆仓库**

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
```

**第二步：运行官方 setup 脚本**

该脚本会自动完成：构建 Docker 镜像、运行引导向导、生成控制台 token、创建配置目录、并通过 Docker Compose 启动 gateway。

```bash
./scripts/docker/setup.sh
```

> 如果想跳过本地构建，直接使用预构建镜像：

```bash
export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
./scripts/docker/setup.sh
```

**第三步：完成 Onboarding 向导**

脚本会启动交互式引导，按提示填入：

- AI 模型 API Key（Anthropic / OpenAI 等）
- 端口、Gateway 配置（默认即可）

---

## 方法二：使用社区镜像（更简便）

直接拉取 `alpine/openclaw` 镜像，无需克隆源码：

```bash
git clone https://github.com/ozbillwang/openclaw-in-docker.git
cd openclaw-in-docker
export OPENCLAW_IMAGE="alpine/openclaw:latest"
docker pull alpine/openclaw:latest
./docker-setup.sh
```

---

## 数据持久化

setup 脚本会在 Mac 上自动创建两个目录并挂载到容器：

- `~/.openclaw` — 配置、记忆、API Key 等
- `~/openclaw/workspace` — Agent 的工作区，Agent 创建的文件也会保存在这里

---

## 启动 / 停止 / 访问面板

```bash
# 启动
docker compose up -d

# 停止
docker compose down

# 获取面板访问链接（含 token）
docker compose run --rm openclaw-cli dashboard --no-open
```

OpenClaw 默认在 `http://localhost:18789` 提供 Web UI，访问时需要带 `?token=...` 参数，可通过上面的命令获取完整链接。

---

## 安装 ClawDock（可选，日常管理更方便）

安装后可以用 `clawdock-start`、`clawdock-stop`、`clawdock-dashboard` 等简短命令管理实例：

```bash
mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/shell-helpers/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.sh
echo 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
```

---

## 常见问题

|问题|解决方法|
|---|---|
|内存不足（exit 137）|构建镜像需要至少 2GB RAM，在 Docker Desktop 设置中调大内存限制|
|权限错误 `/home/node/.openclaw`|容器以 `node`（uid 1000）运行，确保挂载目录属主为 uid 1000：`sudo chown -R 1000:1000 ~/.openclaw`|
|Gateway 启动失败（controlUi 报错）|在 `~/.openclaw/openclaw.json` 中添加 `allowedOrigins` 配置后重启容器|



> 踩坑指南 [[openclaw-踩坑指南(mac-docker)]]