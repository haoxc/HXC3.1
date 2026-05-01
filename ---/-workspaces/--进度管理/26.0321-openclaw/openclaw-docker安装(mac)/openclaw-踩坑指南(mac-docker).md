---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-03-21
---
## 内容
## 安装过程问题总结

### 1. 环境变量缺失

`OPENCLAW_CONFIG_DIR` 和 `OPENCLAW_WORKSPACE_DIR` 没有设置，导致 docker compose 启动失败。需要每次带上这两个变量。

### 2. 本地镜像不存在

`docker-compose.yml` 默认使用 `openclaw:local`，但这个镜像需要本地构建，不能直接从 Docker Hub 拉取。

### 3. `discord-api-types` 依赖缺失

`pnpm prune --prod` 在构建时把这个包删掉了，但运行时代码仍然依赖它，导致容器一直崩溃重启。这是项目本身的一个 bug。

### 4. 切换预构建镜像

放弃本地构建，改用官方预构建镜像 `ghcr.io/openclaw/openclaw:latest`，绕过了依赖问题。

### 5. controlUi allowedOrigins 配置缺失

容器绑定的是非 loopback 地址，OpenClaw 出于安全要求必须显式配置 `allowedOrigins` 或开启 `dangerouslyAllowHostHeaderOriginFallback`。

### 6. 配置文件读取错误

误以为 `config.json` 是配置文件，实际上 OpenClaw 读取的是 `openclaw.json`，修改错文件导致多次重试无效。

### 7. JSON5 语法错误

写入配置时因为特殊字符（反斜杠）导致 JSON5 解析失败，简化配置后解决。

---

**核心教训：** 预构建镜像 + 正确的 `openclaw.json` 配置 + 环境变量，三者缺一不可！