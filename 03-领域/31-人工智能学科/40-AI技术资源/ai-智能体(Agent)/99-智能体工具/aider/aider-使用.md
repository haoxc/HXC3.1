---
aliases:
tags:
description:
type:
ref-url:
---
## 内容

### 配置参数
 创建或编辑 `~/.aider.conf.yml`
```
# ~/.aider.conf.yml
alias:
  - "s:claude-sonnet-4-5"
  - "h:claude-haiku-4-5"
  - "ds:deepseek/deepseek-chat"
```

### 启动
```
aider --model s     # 用 sonnet
aider --model ds    # 用 deepseek
```
> 注意: 全局配置文件 在`~/.aider.config.yml`

