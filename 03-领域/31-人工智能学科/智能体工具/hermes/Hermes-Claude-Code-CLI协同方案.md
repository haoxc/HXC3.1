---
title: Hermes 与 Claude Code CLI 协同安装方案
aliases:
  - 辨析/Hermes 与 Claude Code CLI
  - bx/hermes-claude-code-cli
  - Hermes 与 Claude Code CLI 协同
  - hermes-claude-code-cli
  - mac/Hermes-Claude-Code-CLI协同方案
tags:
  - mac-工具
  - AI工具
  - Agent
description: 评估并记录在 Mac 上安装 Hermes Agent 与 Claude Code CLI 的协同方式、安装路径、验证结果和剩余配置项。
type: 方案笔记
create-date: 2026-04-29
ref-url:
  - https://hermes-agent.nousresearch.com/docs/
  - https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
  - https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code
  - https://hermes-agent.nousresearch.com/docs/reference/cli-commands/
  - https://code.claude.com/docs/en/quickstart
---

# Hermes 与 Claude Code CLI 协同安装方案

> [!summary]
> Hermes 不替代 Claude Code CLI。更合理的协同方式是：Hermes 负责常驻入口、长期记忆、skills、gateway、cron 和任务调度；Claude Code CLI 负责进入具体代码库执行代码修改、测试和 Git 工作流。先让 Claude Code 独立可用，再让 Hermes 通过内置 `claude-code` skill 委派边界清楚的 coding task。

## 1. 定位辨析

| 维度 | Hermes Agent | Claude Code CLI |
| --- | --- | --- |
| 核心定位 | 常驻型 agent 工作台 | 项目级 coding agent |
| 主要价值 | 跨会话记忆、skills、gateway、cron、工具编排、多模型提供商 | 读写代码库、跑命令、修 bug、写测试、Git 操作 |
| 最佳入口 | `hermes` / `hermes --tui` / gateway 消息平台 | `claude` / `claude -p` |
| 运行姿势 | 长期使用、跨项目积累上下文 | 进入某个 repo，围绕一次工程任务推进 |
| 协同关系 | 编排者 / 调度者 / 记忆层 | 被委派的代码执行器 |

```text
Hermes 负责“记住、调度、转交、长期自动化”；
Claude Code CLI 负责“进项目、改代码、跑验证、收口交付”。
```

## 2. 推荐协同架构

```text
用户
├─ 直接进入项目开发
│  └─ Claude Code CLI
│     ├─ cco：高质量 Claude Code 链路
│     └─ ccs：LiteLLM / DeepSeek 成本敏感链路
│
└─ 长期任务 / 跨项目任务 / 消息入口
   └─ Hermes Agent
      ├─ memory / skills / cron / gateway
      ├─ terminal backend：local / docker / ssh
      └─ claude-code skill
         └─ 调用 Claude Code CLI 执行 bounded coding task
```

如果沿用本地 LiteLLM 方案，endpoint 不要混：

| 客户端 | 推荐 endpoint | 说明 |
| --- | --- | --- |
| Claude Code CLI | `http://localhost:4000` | Anthropic-compatible，不加 `/v1` |
| Hermes 若走 LiteLLM custom endpoint | `http://localhost:4000/v1` | OpenAI-compatible |
| Aider / OpenCode 等 OpenAI 客户端 | `http://localhost:4000/v1` | OpenAI-compatible |

关联笔记：

- [[liteLLM-mac配置]]
- [[endpoint]]
- [[claude-code-使用备忘录|Claude Code 使用备忘录]]
- [[claude-安装]]

## 3. 本机执行记录

执行日期：2026-04-29

已完成：

- Claude Code CLI 已存在，版本：`2.1.122 (Claude Code)`。
- Claude Code 当前认证：`apiKeyHelper`。
- Claude Code 当前 base URL：`http://localhost:4000`。
- Hermes Agent 已安装到：`~/.hermes/hermes-agent`。
- Hermes 命令已链接到：`~/.local/bin/hermes`。
- Hermes 版本：`Hermes Agent v0.11.0 (2026.4.23)`。
- Hermes Python venv：`~/.hermes/hermes-agent/venv`，Python `3.11.9`。
- Hermes 配置模板已创建：`~/.hermes/.env`、`~/.hermes/config.yaml`。
- bundled skills 已同步，共 83 个，`claude-code` / `codex` / `opencode` 均为 enabled。
- TUI 依赖已安装：`~/.hermes/hermes-agent/ui-tui/node_modules`。
- Playwright Chromium 与 headless shell 已安装到 macOS Playwright cache。

关键路径：

```text
~/.hermes/hermes-agent
~/.hermes/.env
~/.hermes/config.yaml
~/.hermes/skills/autonomous-ai-agents/claude-code/SKILL.md
~/.local/bin/hermes
```

## 4. 验证结果

已验证命令：

```bash
hermes --version
hermes doctor
hermes skills list
claude --version
```

`hermes doctor` 基础项通过：

- Python、venv、required packages 正常。
- 配置目录、命令链接、`~/.hermes` 目录结构正常。
- `git`、`rg`、Docker、Node.js、agent-browser 正常。
- `browser`、`terminal`、`skills`、`memory`、`delegation` 等核心工具可用。
- DeepSeek API 连通性检查通过。
- built-in memory active。
- GitHub token 已配置。

剩余项：

- `hermes setup` 仍可用于补全更多 API keys 和 provider。
- Nous Portal、OpenAI Codex、Google Gemini OAuth 未登录。
- OpenRouter、Discord、web search、Spotify、Home Assistant、vision、image_gen 等外部工具缺少对应 token 或系统依赖。
- `tinker-atropos` 子模块未初始化；这是 RL 训练相关可选项，不影响 Hermes 基础使用。

## 5. 使用建议

日常使用优先：

```bash
hermes --tui
```

需要检查安装：

```bash
hermes doctor
```

查看 skills：

```bash
hermes skills list
```

Claude Code 协同测试：

```bash
claude --version
hermes skills list
```

建议先用只读任务测试委派：

```text
请使用 claude-code skill，在当前项目中让 Claude Code 只读分析目录结构，并输出主要模块、测试命令和潜在风险。不要修改文件。
```

## 6. 安全边界

1. 不把 `--yolo` 作为默认工作方式。
2. 涉及真实项目修改时，先开 Git 分支或 worktree。
3. Hermes 做长期自动化时，优先让 cron/gateway 做检查和汇报，代码修改仍需人工确认。
4. secrets 只放在 `~/.hermes/.env`、`~/.litellm/.env`、`~/.claude/settings.json` 等本机配置，不写入 Vault 或项目仓库。
5. Hermes 与 Claude Code 并发时，明确文件所有权：谁写、谁 review，不让两个 agent 同时改同一个文件。

> [!important] 压缩记忆
> 当前本机已经完成 Hermes + Claude Code CLI 基础协同安装。Hermes 可作为常驻调度中枢，Claude Code CLI 继续作为深度代码执行器；下一步只需要按需运行 `hermes setup` 补全更多外部服务 token。

## 资料来源

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Hermes `claude-code` bundled skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code)
- [Hermes CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/)
- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
