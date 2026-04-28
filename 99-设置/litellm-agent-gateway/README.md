# LiteLLM Agent Gateway

本目录用于记录本机 agent 编程工具的 LiteLLM 网关配置方案。

## 目标

- LiteLLM 作为统一本地网关，监听 `http://localhost:4000`
- Claude Code 通过 Anthropic-compatible endpoint 调用 LiteLLM
- Aider / OpenCode / OpenAI-compatible 工具通过 OpenAI-compatible endpoint 调用 LiteLLM
- 真实 API Key 放在 `~/.litellm/.env`，不写入配置文件和知识库

## 常用命令

```bash
proxy-on
proxy-off
ccs
```

也可以直接运行：

```bash
~/.litellm/start_proxy.sh
```

## 工具接入

Claude Code:

```bash
ANTHROPIC_BASE_URL=http://localhost:4000 \
ANTHROPIC_AUTH_TOKEN=$LITELLM_MASTER_KEY \
claude --model deepseek-v4-pro
```

Aider:

```bash
OPENAI_API_BASE=http://localhost:4000/v1 \
OPENAI_API_KEY=$LITELLM_MASTER_KEY \
aider --model openai/sonnet-4-6
```

OpenCode 已配置自定义 `litellm` provider，默认模型为 `litellm/sonnet-4-6`。

## 当前验证结果

- LiteLLM `/v1/models` 已返回模型列表
- OpenAI-compatible 调用 `claude-haiku-4-5` 已返回 `OK`
- Claude Code 非交互调用 `deepseek-v4-pro` 已返回 `OK`

说明：Claude Code 使用 Anthropic Messages API，当前最稳路由是 `deepseek-v4-pro` / `deepseek-v4-flash`。OhMyGPT 的 Claude 模型保留给 Aider、OpenCode 等 OpenAI-compatible 客户端。
