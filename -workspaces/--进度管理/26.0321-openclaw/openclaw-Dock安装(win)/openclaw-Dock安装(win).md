---
aliases:
tags:
description:
type:
ref-url:
  - https://cartopy.readthedocs.io/stable/
  - https://careers.thalesgroup.com/global/en/home
  - https://d2lang.com/tour/man/
create-date: 2026-03-22
---
## 内容

## 前提准备
- git
- docker

### 创建 openclaw 配置目录

- **创建目录**
```
mkdir -p ~/.openclaw/config
mkdir -p ~/.openclaw/workspace
```
会自动在你的用户目录下创建 `.openclaw` 文件夹！

- 写入配置文件

```
cat > ~/.openclaw/config/openclaw.json << 'EOF'
{
  "agents": {
    "defaults": {
      "workspace": "/home/node/.openclaw/workspace"
    }
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto",
    "restart": true,
    "ownerDisplay": "raw"
  },
  "gateway": {
    "mode": "local",
    "auth": {
      "token": "mytoken123"
    },
    "remote": {
      "token": "mytoken123"
    },
    "controlUi": {
      "dangerouslyAllowHostHeaderOriginFallback": true
    }
  },
  "meta": {
    "lastTouchedVersion": "2026.3.13",
    "lastTouchedAt": "2026-03-22T00:00:00.000Z"
  }
}
EOF
```

## 克隆代码
- **下载**
```
git clone --depth=1 https://ghfast.top/https://github.com/openclaw/openclaw.git
cd openclaw
```

- **确认**
```
ls
```
看到 `Dockerfile`、`docker-compose.yml` 等文件就说明克隆成功了
