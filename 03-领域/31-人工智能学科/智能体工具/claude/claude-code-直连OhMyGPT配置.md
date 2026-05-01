---
aliases: [Claude Code OhMyGPT配置, Claude Code直连OhMyGPT, cco]
tags: [ai/智能体/工具/claude, Claude-Code, OhMyGPT]
description: Claude Code 直连 OhMyGPT Claude Code 专用 endpoint 的配置要点
type: 配置笔记
ref-url:
  - https://docs.ohmygpt.com/docs/code-cli/claude-code
create-date: 2026-04-26 19:14
---

# Claude Code 直连 OhMyGPT 配置

> [!summary]
> 这是“方案 A”：Claude Code 不经过 LiteLLM，直接连接 OhMyGPT 提供的 Claude Code 专用 endpoint。适合在 Claude Code 中使用 OhMyGPT 的 Sonnet / Opus / Haiku 等模型。

## 核心结论

Claude Code 不能简单使用普通 OpenAI-compatible `/v1/chat/completions` endpoint。

它需要 Anthropic Messages API 兼容入口。OhMyGPT 提供了 Claude Code 专用 endpoint：

```text
https://c-z0-api-01.hash070.com/api/v1/ai/openai/cc-omg/
```

因此正确链路是：

```text
Claude Code
  ↓ Anthropic-compatible request
OhMyGPT Claude Code endpoint
  ↓
上游 Claude / 其他模型
```

不是：

```text
Claude Code
  ↓
OhMyGPT 普通 OpenAI /v1 endpoint
```

## 一次性启动方式

```bash
source ~/.litellm/.env

ANTHROPIC_BASE_URL="https://c-z0-api-01.hash070.com/api/v1/ai/openai/cc-omg/" \
ANTHROPIC_API_KEY="$OHMYGPT_API_KEY" \
claude --model sonnet
```

最小验证：

```bash
source ~/.litellm/.env

ANTHROPIC_BASE_URL="https://c-z0-api-01.hash070.com/api/v1/ai/openai/cc-omg/" \
ANTHROPIC_API_KEY="$OHMYGPT_API_KEY" \
claude -p "Reply with only: OK" --model sonnet
```

验证通过时应返回：

```text
OK
```

## 推荐封装命令

在 `~/.zshrc` 中增加：

```bash
function cco() {
    source "$HOME/.litellm/.env"
    ANTHROPIC_BASE_URL="https://c-z0-api-01.hash070.com/api/v1/ai/openai/cc-omg/" \
    ANTHROPIC_API_KEY="$OHMYGPT_API_KEY" \
    claude --model sonnet "$@"
}
```

使用：

```bash
cco
```

带参数使用：

```bash
cco -p "Reply with only: OK"
```

## 与 LiteLLM 方案的区别

| 方案               | 链路                                                  | 适合场景                                   |
| ---------------- | --------------------------------------------------- | -------------------------------------- |
| `cco`            | Claude Code → OhMyGPT Claude Code endpoint          | 在 Claude Code 中直接使用 OhMyGPT，链路短、稳定性更直接 |
| `ccs`            | Claude Code → LiteLLM → DeepSeek Anthropic endpoint | 保留 LiteLLM 本地网关，适合统一管理或使用 DeepSeek 路由  |
| Aider / OpenCode | 工具 → LiteLLM `/v1` → OpenAI-compatible 上游           | 这些工具本身更适合 OpenAI-compatible endpoint   |

## 易错点

### 误区 1：把 OhMyGPT 普通 `/v1` 当作 Claude Code endpoint

普通 OpenAI-compatible endpoint 通常类似：

```text
https://api.ohmygpt.com/v1
```

它适合 Aider、OpenCode、OpenAI SDK 类工具。

Claude Code 应使用：

```text
https://c-z0-api-01.hash070.com/api/v1/ai/openai/cc-omg/
```

### 误区 2：把 `ANTHROPIC_BASE_URL` 写成带 `/v1` 的 LiteLLM 地址

Claude Code 直连 OhMyGPT 时，`ANTHROPIC_BASE_URL` 应直接写 OhMyGPT 的 Claude Code 专用 endpoint。

不要混写成：

```bash
ANTHROPIC_BASE_URL=http://localhost:4000/v1
```

这会把 Anthropic Messages API 和 OpenAI-compatible 路径混在一起。

### 误区 3：以为 Claude Code 只能看到 DeepSeek

之前 Claude Code 默认使用 DeepSeek，是因为当时走的是：

```text
Claude Code → LiteLLM → DeepSeek Anthropic endpoint
```

不是因为 OhMyGPT 不能被 Claude Code 调用。

只要切换到 OhMyGPT 的 Claude Code 专用 endpoint，Claude Code 可以直接使用 OhMyGPT。

### 误区 4：把 OhMyGPT key 写入笔记或配置文件

笔记中不要记录真实 key。

推荐继续把 key 放在：

```text
~/.litellm/.env
```

并通过：

```bash
source ~/.litellm/.env
```

读取 `OHMYGPT_API_KEY`。

## 当前建议

保留两条命令：

```bash
ccs    # Claude Code -> LiteLLM -> DeepSeek
cco    # Claude Code -> OhMyGPT Claude Code endpoint
```

这样可以按任务切换：

- 要统一走 LiteLLM 网关时，用 `ccs`。
- 要 Claude Code 直接用 OhMyGPT 时，用 `cco`。

