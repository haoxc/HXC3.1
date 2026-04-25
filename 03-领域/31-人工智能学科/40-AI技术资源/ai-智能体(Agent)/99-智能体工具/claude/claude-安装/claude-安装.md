---
aliases:
  - claude/mac安装(eval-ok)
tags:
description:
type:
ref-url:
---
## 内容

### 前期准备
- **安装 Node.js**：确保系统中已安装 Node.js 18 或更高版本。
- **获取 API Key**：在 OhMyGPT 控制台 生成一个 API Key。
- **安装 Claude Code**：
```
npm install -g @anthropic-ai/claude-code
```


### 配置环境
由于 Claude Code 默认连接 Anthropic 官方服务器，你需要设置环境变量来重定向 API 请求。
在 Linux/macOS 中：
编辑你的 shell 配置文件（如 `~/.bashrc` 或 `~/.zshrc`），添加以下内容：
```
export ANTHROPIC_BASE_URL="https://api.ohmygpt.com"
export ANTHROPIC_API_KEY="你的OhMyGPT_API_Key"
```

执行 `source ~/.zshrc`（或对应文件）使配置生效。



### 跳过初始化引导

- 跳过初始化引导 `~/.claude.json` ,
-  将 `"hasCompletedOnboarding": false` 修改为 `"hasCompletedOnboarding": true`。
![[58168fa55736683622b2c4fcc4eee552_MD5.jpg]]
```
```

