---
aliases:
tags:
description:
type:
ref-url:
---
## 内容

### 启动
docker run --name pg-stable \
  -e POSTGRES_PASSWORD=postgres\
  -p 5432:5432 \
  -v ~/postgres_data:/var/lib/postgresql/data \
  -d postgres:16-alpine

## pwd
default: `postgres`