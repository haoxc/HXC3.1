---
aliases:
tags:
description:
type:
ref-url:
---
## 内容
### 安装
```shell
	pip install aider-chat
```

### 配置
为了让 Aider 走 **OhMyGPT** 的通道，你需要设置以下环境变量。建议直接写入你的 `~/.zshrc`：

 打开配置文件 `nano ~/.zshrc`
```
# 添加以下内容 (替换为你自己的 Key)
export ANTHROPIC_API_KEY="sk-xxxx你的OhMyGPT密钥"
export ANTHROPIC_API_BASE="https://api.ohmygpt.com"

# 保存退出后生效
source ~/.zshrc

```