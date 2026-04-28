---
aliases: [Claude Code备忘录, Claude Code使用备忘录]
tags: [ai/智能体/工具/claude, Claude-Code]
description: Claude Code 多链路、多模型与同目录多会话使用策略备忘
type: 备忘录
ref-url:
create-date: 2026-04-26 19:20
---

# Claude Code 使用备忘录

> [!summary]
> Claude Code 的“切模型”不只是模型名切换，还可能是在切 endpoint、协议、鉴权方式和上游供应商。当前最稳的实践是保留多条启动链路，并在同一项目目录下按角色分工使用。

## 当前推荐链路

| 命令 | 链路 | 适合任务 |
| --- | --- | --- |
| `cco` | Claude Code → OhMyGPT Claude Code endpoint | 顶层策划、复杂判断、Sonnet/Opus 类任务 |
| `ccs` | Claude Code → LiteLLM → DeepSeek | 细节丰富、批量补全、成本敏感任务 |

核心理解：

```text
模型切换
≠ 只改 model name
= endpoint + 协议适配 + 鉴权方式 + 模型路由 + 上游供应商
```

## 推荐角色分工

| 模型/链路 | 角色 | 使用场景 |
| --- | --- | --- |
| Opus | 顶层策划者 | 复杂方案、架构取舍、关键判断 |
| Sonnet | 落地设计者 | 方案细化、模块划分、稳定推进 |
| DeepSeek | 细节执行者 | 扩写、补充、局部实现、低成本迭代 |

## 同一项目下打开两条链路

可以在同一个项目目录中开两个 Claude Code 会话：

```bash
cd /path/to/project
cco
```

另一个终端：

```bash
cd /path/to/project
ccs
```

推荐工作流：

```text
1. cco 先做顶层判断、方案拆解、核心结构设计
2. ccs 根据方案补细节、扩内容、做局部实现
3. cco 最后 review、收口、统一风格
```

## 多会话协作注意事项

1. 不要让两个会话同时改同一个文件。
2. 一个会话改完一段后，另一个会话先看 `git status` 和 `git diff`。
3. 把任务边界说清楚：谁负责设计，谁负责补细节，谁负责 review。
4. 复杂任务优先让 `cco` 定方向，再让 `ccs` 执行细节。

## 会话内切换与跨链路切换

同一条 endpoint 内切模型，通常更容易：

```text
OhMyGPT endpoint
├─ opus
├─ sonnet
└─ haiku
```

跨 endpoint 切换，本质上是换基础设施：

```text
OhMyGPT Claude Code endpoint
↔
LiteLLM local endpoint
```

如果 Claude Code 启动后只读取一次 `ANTHROPIC_BASE_URL`，那跨链路切换通常需要重新启动会话。当前更稳的方式是同目录开两个会话，而不是强求一个会话里跨基础设施切换。

## 常用命令

启动 OhMyGPT Claude Code endpoint：

```bash
cco
```

启动 LiteLLM + DeepSeek：

```bash
proxy-on
ccs
```

检查 LiteLLM 是否启动：

```bash
lsof -iTCP:4000 -sTCP:LISTEN -P -n
```

验证 Claude Code 最小调用：

```bash
claude -p "Reply with only: OK" --model deepseek-v4-pro
```

## 常见误区

### 误区 1：以为 Claude Code 只能看见 DeepSeek

不是。之前默认 DeepSeek，是因为 `ccs` 走的是：

```text
Claude Code → LiteLLM → DeepSeek
```

OhMyGPT 也可以给 Claude Code 用，但要走它的 Claude Code 专用 endpoint，也就是 `cco` 这条链路。

### 误区 2：把普通 OpenAI `/v1` endpoint 给 Claude Code

Claude Code 走 Anthropic Messages API，不是普通 OpenAI `/v1/chat/completions`。

因此：

```text
cco: Claude Code → OhMyGPT Claude Code endpoint
ccs: Claude Code → LiteLLM Anthropic-compatible endpoint
```

不要把 Claude Code 简单配成普通 OpenAI-compatible `/v1` 地址。

### 误区 3：在同一目录开两个会话就可以随意并发改文件

同目录多会话可行，但要把文件写入边界管住。最危险的是两个会话同时修改同一个文件，容易覆盖或形成冲突。

## 压缩记忆

> `cco` 负责高层判断和优质设计，`ccs` 负责低成本细节推进。一个项目里可以同时开两条链路，但不要让它们抢同一个文件。

