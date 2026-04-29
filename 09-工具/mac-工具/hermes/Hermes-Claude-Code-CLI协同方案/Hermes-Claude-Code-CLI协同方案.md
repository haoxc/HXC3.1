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
description: 评估在 Mac 上同时安装 Hermes Agent 与 Claude Code CLI 的协同方式、安装顺序、验证清单和风险边界。
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
> 推荐结论：可以协同安装，但不要把二者理解成替代关系。**Hermes Agent** 更适合做常驻入口、跨会话记忆、任务调度、消息平台和技能编排；**Claude Code CLI** 更适合做具体代码库里的深度编码、修改、测试和 Git 工作流。最稳妥的路径是：先把 Claude Code CLI 独立跑通，再安装 Hermes，让 Hermes 在需要时委派 Claude Code 执行边界清晰的 coding task。

## 1. 定位辨析

| 维度 | Hermes Agent | Claude Code CLI |
| --- | --- | --- |
| 核心定位 | 常驻型 agent 工作台 | 项目级 coding agent |
| 主要价值 | 跨会话记忆、skills、gateway、cron、工具编排、模型提供商切换 | 读写代码库、跑命令、修 bug、写测试、Git 操作 |
| 最佳入口 | `hermes` / `hermes --tui` / gateway 消息平台 | `claude` / `claude -p` |
| 运行姿势 | 长期使用、可跨项目积累上下文 | 进入某个 repo，围绕一次工程任务推进 |
| 上下文来源 | Hermes memory、skills、profiles、sessions、MCP、消息平台 | 当前项目文件、`CLAUDE.md`、`.claude/rules`、命令输出 |
| 协同关系 | 编排者 / 调度者 / 记忆层 | 被委派的代码执行器 |

一句话边界：

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

如果沿用本地已有的 LiteLLM 方案，注意 endpoint 不要混：

| 客户端 | 推荐 endpoint | 说明 |
| --- | --- | --- |
| Claude Code CLI | `http://localhost:4000` | Anthropic-compatible，不加 `/v1` |
| Hermes 自身若走 LiteLLM custom endpoint | `http://localhost:4000/v1` | OpenAI-compatible，需要模型满足长上下文和工具调用要求 |
| Aider / OpenCode 等 OpenAI 客户端 | `http://localhost:4000/v1` | OpenAI-compatible |

关联笔记：

- [[liteLLM-mac配置]]
- [[endpoint]]
- [[claude-code-使用备忘录|Claude Code 使用备忘录]]
- [[claude-安装]]

## 3. 是否值得安装 Hermes

适合安装 Hermes 的情况：

- 希望有一个长期运行的 agent 入口，而不只是每次打开一个 CLI 会话。
- 需要 Telegram / Discord / Slack / WhatsApp / Email 等消息平台接入。
- 希望把任务沉淀成 skills，并跨会话复用。
- 希望做定时任务，例如每天巡检 repo、总结 issue、生成日报。
- 希望在 Claude Code 之外接入 OpenRouter、Nous、OpenAI、DeepSeek、Ollama、LiteLLM 等多模型来源。

暂不必安装 Hermes 的情况：

- 主要需求只是“在当前 repo 里写代码、修 bug、跑测试”。
- 还没有稳定的模型 provider / API key / LiteLLM 网关。
- 对本机 agent 执行 shell 命令的权限边界还没有想清楚。
- 不需要跨平台消息、自动化调度和长期记忆。

结论：如果当前重点是代码交付，Claude Code CLI 已经足够；如果下一步要构建“个人常驻 agent 工作台”，Hermes 值得作为上层编排层安装。

## 4. 推荐安装顺序

### 第一步：先验证 Claude Code CLI

Claude Code 当前官方推荐 Mac 安装方式优先使用 native installer 或 Homebrew：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

或：

```bash
brew install --cask claude-code
```

验证：

```bash
claude
claude doctor
claude --version
```

如果沿用本地 LiteLLM 链路，先确认：

```bash
proxy-on
claude -p "Reply with only: OK" --model deepseek-v4-pro
```

说明：部分 Hermes 文档和旧笔记仍会出现 `npm install -g @anthropic-ai/claude-code`。在 Mac 新装时，应优先参考 Claude Code 官方 Quickstart；旧 npm 路径可视为历史路径或特定环境下的兼容方案。

### 第二步：安装 Hermes Agent

Hermes 官方 quick install：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装后：

```bash
source ~/.zshrc
hermes setup
hermes doctor
hermes --tui
```

关键配置点：

- `hermes model`：选择 provider 和默认模型。
- `~/.hermes/.env`：放 secrets / tokens。
- `~/.hermes/config.yaml`：放普通配置。
- `hermes setup terminal`：配置 terminal backend。
- `hermes gateway setup`：仅在 CLI 跑通后再接消息平台。

如果用 LiteLLM 给 Hermes 供模型，优先走 custom OpenAI-compatible endpoint：

```text
baseURL: http://127.0.0.1:4000/v1
apiKey: LITELLM_MASTER_KEY
```

Hermes 要求模型至少具备较长上下文，官方文档给出的最低线是 64K tokens。选择本地或中转模型时，要先确认 context window 和 tool-calling 稳定性。

## 5. 两种协同模式

### 模式 A：人手动分层使用

适合日常开发。

```text
1. Hermes：记录背景、整理待办、沉淀长期偏好和跨项目上下文。
2. Claude Code CLI：进入 repo 执行具体改动。
3. Hermes：复盘结果、沉淀经验、生成下一步任务。
```

这条路径简单、风险低，适合先落地。

### 模式 B：Hermes 委派 Claude Code

适合 bounded coding task，例如局部 refactor、测试补充、PR review。

Hermes 官方内置 `claude-code` skill，可通过 Hermes terminal 调用 Claude Code。优先使用 Claude Code 的 print mode：

```bash
claude -p "Review the auth module and list the top 5 risks." --max-turns 8
```

使用原则：

- 一次只交付一个边界清楚的任务。
- 优先让 Claude Code 输出分析、diff 或 patch 意图，再决定是否写入。
- 对多轮复杂任务，再使用 interactive / tmux 模式。
- 不让 Hermes 和 Claude Code 同时改同一个文件。

## 6. 权限与安全边界

推荐规则：

1. 不开 `--yolo` 作为默认工作方式。
2. 涉及真实项目修改时，先开 Git 分支或 worktree。
3. Hermes 若承担长期自动化，优先考虑 Docker / SSH terminal backend，而不是直接放开本机 local shell。
4. secrets 只放在 `~/.hermes/.env`、`~/.litellm/.env`、`~/.claude/settings.json` 这类本机配置，不写入 Vault 或项目仓库。
5. Claude Code 与 Hermes 并发工作时，明确文件所有权：谁改哪几个文件，谁只 review。
6. Gateway / cron 不要在第一天就接入；先让 CLI 会话、provider、权限、日志稳定。

并发建议：

```text
小任务：同一 repo，手动串行。
中任务：一个 agent 写，一个 agent review。
大任务：用 git worktree / 独立分支隔离。
长期任务：Hermes cron 只做检查和汇报，代码修改仍需人工确认。
```

## 7. 分阶段落地路径

### Phase 0：基线确认

- 确认 `git --version` 可用。
- 确认当前 Claude Code 的 `cco` / `ccs` 或官方链路可独立工作。
- 确认 LiteLLM 的 `/v1` 与 Claude Code endpoint 区分清楚。

验收：

```bash
claude -p "Reply with only: OK"
```

或本地 LiteLLM 链路：

```bash
proxy-on
claude -p "Reply with only: OK" --model deepseek-v4-pro
```

### Phase 1：Hermes 最小安装

- 安装 Hermes。
- 运行 `hermes setup`。
- 只配置一个稳定 provider。
- 先不接 gateway、cron、voice。

验收：

```bash
hermes doctor
hermes --tui
```

在 Hermes 中问：

```text
检查当前目录，告诉我主要项目文件是什么。
```

### Phase 2：Claude Code 委派测试

选择一个小型 repo 或测试目录，让 Hermes 委派 Claude Code 做只读任务：

```text
请使用 claude-code skill，在当前项目中让 Claude Code 只读分析目录结构，并输出主要模块、测试命令和潜在风险。不要修改文件。
```

验收：

- Hermes 能调用 Claude Code。
- Claude Code 能正确读取项目。
- 没有非预期文件改动。

检查：

```bash
git status
```

### Phase 3：受控写入

只给一个小文件或一个小模块：

```text
请使用 claude-code skill，只修改 README 中的安装说明，不改其他文件。完成后列出 diff 摘要。
```

验收：

- diff 范围符合预期。
- 测试或格式检查可运行。
- Hermes 记录任务结论，但不替代人工 review。

### Phase 4：长期自动化

在基础稳定后再考虑：

- `hermes gateway setup`：接 Telegram / Slack 等入口。
- `hermes cron`：定时巡检、日报、资料汇总。
- `hermes skills`：沉淀本地工作流。
- `hermes --worktree`：并行 agent 工作流隔离。

## 8. 决策建议

当前建议采用“轻安装、慢放权”的策略：

```text
先把 Hermes 当作个人 agent 控制台；
不要一开始就让它变成自动改代码的后台服务。
```

推荐初始组合：

| 层级 | 工具 | 初始职责 |
| --- | --- | --- |
| 模型网关 | LiteLLM | 继续管理本地多模型 endpoint |
| 代码执行 | Claude Code CLI | 维持 `cco` / `ccs` 两条链路 |
| 长期编排 | Hermes Agent | 先做 TUI、memory、skills、只读委派 |
| 自动化 | Hermes gateway / cron | 第二阶段再启用 |

最终形态可以是：

```text
Hermes = 常驻调度中枢
Claude Code CLI = 深度代码执行器
LiteLLM = 本地模型路由层
Git worktree = 并发安全边界
```

> [!important] 压缩记忆
> Hermes 不替代 Claude Code。更合理的协同方式是：Hermes 负责长期记忆、任务入口、调度和自动化；Claude Code 负责代码库里的高强度执行。先独立跑通 Claude Code，再让 Hermes 以 `claude-code` skill 委派它，且所有写入任务都要有 Git 边界和人工 review。

## 资料来源

- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Hermes `claude-code` bundled skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code)
- [Hermes CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/)
- [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart)
