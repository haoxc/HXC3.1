---
title: Hermes mac 安装笔记
aliases:
  - hermes mac 安装笔记
  - Hermes Mac 安装
  - mac/Hermes安装笔记
tags:
  - mac-工具
  - AI工具
  - Hermes
  - Agent
description: 记录本机 Hermes Agent 在 macOS 上的安装结果、关键路径、验证命令、协同边界和安装过程中遇到的课题。
type: 安装笔记
create-date: 2026-04-29
ref-url:
  - https://hermes-agent.nousresearch.com/docs/
  - https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
---

# Hermes mac 安装笔记

> [!summary]
> 本机 Hermes Agent 已安装成功。当前可执行命令为 `hermes`，安装目录为 `~/.hermes/hermes-agent`，版本为 `Hermes Agent v0.11.0 (2026.4.23)`。Claude Code CLI 也已可用，版本为 `2.1.122 (Claude Code)`。

## 1. 安装结论

安装日期：2026-04-29

已完成：

- Hermes Agent 主体安装成功。
- `hermes` 命令已链接到 `~/.local/bin/hermes`。
- Hermes 项目目录位于 `~/.hermes/hermes-agent`。
- Hermes 当前运行 Python 为 `3.11.9`。
- OpenAI SDK 版本为 `2.33.0`。
- Claude Code CLI 已存在并可用，版本为 `2.1.122 (Claude Code)`。
- Hermes bundled skills 已同步，包含 `claude-code` skill。
- TUI 依赖、Node 依赖、Playwright Chromium/headless shell 已安装。
- `hermes doctor` 基础运行项通过；剩余多为可选 provider/token 配置。

核心状态：

```bash
command -v hermes
hermes --version
claude --version
```

当前验证结果：

```text
/Users/haoxc/.local/bin/hermes
Hermes Agent v0.11.0 (2026.4.23)
Project: /Users/haoxc/.hermes/hermes-agent
Python: 3.11.9
OpenAI SDK: 2.33.0
Up to date
2.1.122 (Claude Code)
```

## 2. 关键路径

```text
~/.hermes/hermes-agent
~/.hermes/hermes-agent/venv
~/.hermes/.env
~/.hermes/config.yaml
~/.hermes/skills/autonomous-ai-agents/claude-code/SKILL.md
~/.local/bin/hermes
```

相关 Obsidian 笔记：

- [[09-工具/mac-工具/Hermes-Claude-Code-CLI协同方案]]

## 3. 安装要点

Hermes 与 Claude Code CLI 的关系：

- Hermes 适合作为常驻 agent 工作台，负责 memory、skills、gateway、cron、任务调度和跨项目上下文。
- Claude Code CLI 适合作为项目级 coding agent，负责进入具体 repo，读写代码、跑命令、修 bug、写测试和处理 Git 工作流。
- 二者不是替代关系。更合理的协同方式是：Hermes 负责调度和长期自动化，Claude Code CLI 负责具体代码执行。

本机 Claude Code 链路：

- Claude Code CLI 已安装。
- 当前认证方式为 `apiKeyHelper`。
- 当前 base URL 为 `http://localhost:4000`。
- 这是 Anthropic-compatible 入口，不应加 `/v1`。

如果 Hermes 走 LiteLLM/OpenAI-compatible endpoint：

```text
Claude Code CLI: http://localhost:4000
Hermes/OpenAI-compatible client: http://localhost:4000/v1
```

## 4. 常用命令

检查版本：

```bash
hermes --version
claude --version
```

检查安装：

```bash
hermes doctor
```

查看 skills：

```bash
hermes skills list
```

启动 TUI：

```bash
hermes --tui
```

补全 provider/token：

```bash
hermes setup
```

## 5. 安装中遇到的课题

### 5.1 Python 版本

安装过程中确认过 Python 3.12 是否可以使用。当前本机 Hermes venv 实际使用的是 Python `3.11.9`。

判断：

- Python 3.12 未必不可用，但当前安装已经稳定在 Python 3.11.9。
- 对 Hermes 这类 agent 项目，不建议在安装成功后贸然切换 venv Python 版本。
- 后续若要切到 Python 3.12，应先确认 Hermes upstream 对 3.12 的支持状态，并重新跑 `hermes doctor`。

当前建议：

```text
保持 Hermes venv 使用 Python 3.11.9。
```

### 5.2 doctor 中的可选项

`hermes doctor` 中可能出现一些未配置项，例如：

- Nous Portal
- OpenAI Codex
- Gemini OAuth
- OpenRouter
- Discord
- web search
- Spotify
- Home Assistant
- vision/image generation
- RL 训练相关子模块

判断：

- 这些不是 Hermes 主体安装失败。
- 多数属于 provider、外部服务 token、消息平台或可选工具链。
- 基础使用 Hermes、skills、terminal、memory、delegation 不依赖全部补齐。

当前建议：

```text
先不追求 doctor 全绿；按真实使用场景逐项补 token。
```

### 5.3 LiteLLM endpoint 容易混淆

本机已有 LiteLLM/DeepSeek 相关链路。需要区分：

| 场景 | endpoint | 说明 |
| --- | --- | --- |
| Claude Code CLI | `http://localhost:4000` | Anthropic-compatible |
| Hermes 若走 OpenAI-compatible client | `http://localhost:4000/v1` | OpenAI-compatible |
| Aider/OpenCode 等 OpenAI 客户端 | `http://localhost:4000/v1` | OpenAI-compatible |

关键点：

```text
Claude Code 不加 /v1；OpenAI-compatible 客户端通常要加 /v1。
```

### 5.4 Hermes 不应直接替代 Claude Code

Hermes 有 `claude-code` skill，但不代表所有 coding task 都应直接丢给 Hermes。

更稳的边界：

- 直接开发某个 repo：优先 Claude Code CLI。
- 长期任务、跨项目任务、消息入口、定时检查：优先 Hermes。
- Hermes 调用 Claude Code 时，应给明确边界：目标 repo、文件范围、是否允许修改、验证命令、交付格式。

### 5.5 自动化权限边界

Hermes 支持 gateway、cron、skills、tools，能力会逐步扩大。

建议：

- 不把 `--yolo` 作为默认模式。
- 不把 secrets 写进 Vault 或项目仓库。
- 项目修改前先开 Git 分支或 worktree。
- 多 agent 并发时明确文件所有权，避免同时修改同一批文件。

## 6. 下一步

短期建议：

1. 日常先用 `hermes --version`、`hermes doctor`、`hermes skills list` 验证环境。
2. 需要 TUI 时使用 `hermes --tui`。
3. 需要外部服务时再运行 `hermes setup` 补 token。
4. 先用只读任务测试 `claude-code` skill，再开放代码修改权限。

推荐测试任务：

```text
请使用 claude-code skill，在当前项目中只读分析目录结构，并输出主要模块、测试命令和潜在风险。不要修改文件。
```

> [!important] 记忆压缩
> 本机 Hermes Agent 已安装成功，当前版本为 `v0.11.0`，命令路径为 `~/.local/bin/hermes`。Claude Code CLI 已可用，版本为 `2.1.122`。当前重点不是重装，而是按需补齐 provider/token，并明确 Hermes 与 Claude Code 的协同边界。
