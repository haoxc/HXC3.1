---
title: Hermes 模型配置
aliases:
  - hermes 如何配置模型
  - Hermes model config
  - Hermes 模型设置
tags:
  - mac-工具
  - AI工具
  - Hermes
description: 说明 Hermes Agent 在 Mac 上配置模型、Provider、endpoint、API key、LiteLLM 链路和常见排查方式。
type: 操作指南
create-date: 2026-04-29
ref-url:
  - https://hermes-agent.nousresearch.com/docs/user-guide/configuration
  - https://hermes-agent.nousresearch.com/docs/integrations/providers
---

# Hermes 模型配置

## 概述

Hermes 的模型配置由三层共同决定：CLI 临时参数、`~/.hermes/config.yaml` 配置文件、`~/.hermes/.env` 中的密钥。日常优先用 `hermes model` 或 `hermes setup model` 配置；需要精确控制时再改 `config.yaml`。

本机当前配置要点：

- 配置文件：`~/.hermes/config.yaml`
- 环境变量文件：`~/.hermes/.env`
- 当前默认模型：`deepseek-v4-pro-openai`
- 当前 provider：`custom`
- 当前 `base_url`：`http://localhost:4000/v1`
- 当前 API key 通过 `${LITELLM_MASTER_KEY}` 从本机环境变量读取，不应写入 Vault。

说明：`deepseek-v4-pro-openai` 是 LiteLLM 中为 Hermes 单独配置的 OpenAI-compatible DeepSeek 别名；原 `deepseek-v4-pro` 继续保留给 Claude Code 等 Anthropic-compatible 客户端。

详细链路见：[[Hermes-LiteLLM-DeepSeek-Docker-Postgres配置笔记]]

## 核心操作

### 1. 交互式选择模型

优先使用：

```bash
hermes model
```

或只配置模型相关项：

```bash
hermes setup model
```

适用场景：

- 不确定 provider 名称。
- 需要 OAuth 登录，例如 Nous、OpenAI Codex、Qwen OAuth。
- 想避免手写 `config.yaml` 出错。

### 2. 查看与编辑配置

查看当前配置：

```bash
hermes config
```

查看配置文件路径：

```bash
hermes config path
hermes config env-path
```

打开配置文件：

```bash
hermes config edit
```

检查配置：

```bash
hermes config check
hermes doctor
```

### 3. 用命令写入模型配置

设置默认模型：

```bash
hermes config set model.default "anthropic/claude-opus-4.6"
```

强制 provider：

```bash
hermes config set model.provider "openrouter"
```

设置 OpenAI-compatible endpoint：

```bash
hermes config set model.provider "custom"
hermes config set model.base_url "http://localhost:4000/v1"
```

> [!warning]
> 不建议把真实 API key 写进 Vault 笔记。key 应放在 `~/.hermes/.env`，或通过 `hermes login` / `hermes model` 处理。

### 4. 单次运行临时指定模型

不改全局配置，只对本次会话生效：

```bash
hermes chat -m "anthropic/claude-sonnet-4" --provider anthropic
```

或：

```bash
hermes chat -q "hello" -m "openai/gpt-5.4" --provider openrouter
```

## Provider 与密钥

Hermes 支持多种 provider。常见对应关系：

| Provider                | 配置方式                                   | 常见 key                              |
| ----------------------- | -------------------------------------- | ----------------------------------- |
| OpenRouter              | `provider: openrouter`                 | `OPENROUTER_API_KEY`                |
| Anthropic               | `provider: anthropic`                  | `ANTHROPIC_API_KEY`                 |
| Nous Portal             | `hermes login` / `hermes auth`         | OAuth                               |
| OpenAI Codex            | `hermes login --provider openai-codex` | OAuth                               |
| Gemini                  | `provider: gemini`                     | `GOOGLE_API_KEY` 或 `GEMINI_API_KEY` |
| DeepSeek                | provider/API key                       | `DEEPSEEK_API_KEY`                  |
| Kimi                    | `provider: kimi-coding`                | `KIMI_API_KEY`                      |
| GitHub Copilot          | `hermes model` 里走 Copilot 登录           | Copilot OAuth，不是普通 `gh auth login`  |
| 本地 OpenAI-compatible 服务 | `provider: custom`                     | `model.base_url` + `model.api_key`  |

## 本机 LiteLLM 链路

如果 Hermes 走本机 LiteLLM，需要使用 OpenAI-compatible endpoint：

```yaml
model:
  provider: "custom"
  default: "<LiteLLM 中配置的模型名或别名>"
  base_url: "http://localhost:4000/v1"
```

和 Claude Code CLI 的区别：

| 客户端 | endpoint |
| --- | --- |
| Claude Code CLI | `http://localhost:4000` |
| Hermes custom/OpenAI-compatible | `http://localhost:4000/v1` |

关键点：

```text
Claude Code 不加 /v1；Hermes 走 custom OpenAI-compatible 时通常要加 /v1。
```

## Token 限制

`config.yaml` 里有两个容易混淆的字段：

| 字段 | 含义 | 建议 |
| --- | --- | --- |
| `context_length` | 总上下文窗口，包含输入和输出 | 通常留空，让 Hermes 自动检测 |
| `max_tokens` | 单次输出上限 | 通常留空，除非需要刻意限制输出长度 |

不要把 `max_tokens` 当成上下文长度。它只控制模型一次最多生成多少 token。

## 高级配置

### OpenRouter 路由

如果使用 OpenRouter，可以用 `provider_routing` 控制供应商选择：

```yaml
provider_routing:
  sort: "throughput"
  order: ["anthropic", "google", "together"]
  require_parameters: true
```

常见策略：

- 想稳定：指定 `order`
- 想速度：`sort: "throughput"`
- 想省钱：`sort: "price"`
- 有隐私要求：关注 `data_collection`

### Delegation 模型

Hermes 的 `delegation` 可以和主模型分开配置：

```yaml
delegation:
  model: "<worker_model>"
  provider: "<provider>"
  base_url: "<optional_base_url>"
  max_iterations: 50
```

适用场景：

- 主模型用强模型做规划。
- 委派任务用更便宜或更快的模型执行。
- 避免所有子任务都消耗最高价模型。

### Auxiliary 模型

如果 vision、compression、session_search 之类辅助任务异常，可能是 `auto` 没找到可用 backend。可以显式配置：

```bash
hermes config set auxiliary.vision.provider <your_provider>
hermes config set auxiliary.vision.model <model_name>
```

## 常见问题

### 改了配置但没有生效

CLI 模式：

```text
退出 Hermes，再重新启动。
```

Gateway 模式：

```text
在 gateway 中执行 /restart。
```

Tools/skills 变化：

```text
新会话或 /reset 后生效。
```

### provider 报错或找不到模型

按顺序排查：

1. `hermes doctor`
2. `hermes config check`
3. 检查 `~/.hermes/.env` 是否有对应 provider 的 key
4. 检查 `model.provider` 与 `model.default` 是否属于同一体系
5. 如果是 LiteLLM/custom endpoint，确认 `base_url` 带 `/v1`

### OpenRouter 配了 base_url 但还是不可用

检查：

- `model.provider` 是否是 `openrouter` 或 `auto`
- 是否配置了 `OPENROUTER_API_KEY`
- 模型名是否使用 OpenRouter 可识别的 provider/model 格式

### Copilot 403

`gh auth login` 的 GitHub token 不能直接替代 Copilot API 登录。需要在 `hermes model` 中走 GitHub Copilot 专用 OAuth 流程。

## 相关链接

- [[hermes-mac安装笔记]]
- [[09-工具/mac-工具/Hermes-Claude-Code-CLI协同方案]]
- [[liteLLM]]

> [!important] 压缩记忆
> Hermes 配模型优先用 `hermes model`；精确配置看 `~/.hermes/config.yaml` 的 `model.default`、`model.provider`、`model.base_url`。本机 LiteLLM 给 Hermes 用时走 `http://localhost:4000/v1`，而 Claude Code CLI 继续用 `http://localhost:4000`。
