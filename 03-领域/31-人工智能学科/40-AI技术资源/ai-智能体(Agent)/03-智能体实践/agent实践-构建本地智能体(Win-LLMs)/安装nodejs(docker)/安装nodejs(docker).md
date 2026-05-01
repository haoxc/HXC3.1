---
aliases:
tags:
category:
domain:
domain_en:
type: note
description: docker pull node:24-alpine
create-date: 2026-01-09
---
## 安装要点

### docker中安装
```powershell
# Docker 对每个操作系统都有特定的安装指导。
# 请参考 https://docker.com/get-started/ 给出的官方文档

# 拉取 Node.js Docker 镜像：
docker pull node:24-alpine

# 创建 Node.js 容器并启动一个 Shell 会话：
docker run -it --rm --entrypoint sh node:24-alpine

# 验证 Node.js 版本：
node -v # Should print "v24.12.0".

# 验证 npm 版本：
npm -v # Should print "11.6.2".

```
> 下载nodejs最新版 [Node.js — 下载 Node.js®](https://nodejs.org/zh-cn/download)

