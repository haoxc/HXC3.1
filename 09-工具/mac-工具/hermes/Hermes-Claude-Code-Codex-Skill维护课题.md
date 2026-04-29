---
title: Hermes Claude Code Codex Skill 维护课题
aliases:
  - Hermes Claude Code Codex Skill 如何维护
  - AI Agent Skill 维护
  - Hermes Claude Code Codex 技能维护
  - skill-maintenance-hermes-claude-code-codex
tags:
  - mac-工具
  - AI工具
  - Hermes
  - Claude-Code
  - Codex
  - Skill
description: 辨析 Hermes、Claude Code、Codex 三套 skill 机制的定位差异，并给出跨工具维护、迁移、同步、去重和版本管理规则。
type: 课题笔记
create-date: 2026-04-29
ref-url:
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
  - https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
  - https://code.claude.com/docs/en/slash-commands
---

# Hermes Claude Code Codex Skill 维护课题

## 一句话结论

Hermes、Claude Code、Codex 都可以使用 `SKILL.md` 风格的能力包，但三者的重点不同：Hermes 更像跨入口、跨工具的 Agent 编排 skill；Claude Code 更像代码仓库内的 coding playbook；Codex 更像当前工作环境中的专业化工作流与本地工具说明。维护时不要简单复制三份，而应采用“核心规范一份、运行时适配多份”的方式。

## 1. 概念界定

### Hermes Skill

**Hermes Skill(Hermes Skill)** 是 Hermes Agent 的按需知识与执行说明包。它可以作为 slash command 被调用，也可以由 Hermes 在自然语言任务中按需加载。Hermes 官方文档把 skill 描述为按需加载的知识文档，并支持 progressive disclosure、外部 skill 目录、skills hub、环境变量、config 注入等机制。

适合承载：

- 长期自动化任务。
- 跨入口任务，例如 CLI、TUI、Gateway、Cron、Webhook。
- 调度其他 agent 或 CLI 的操作手册。
- 需要通过 Hermes 管理、安装、搜索、更新的通用 skill。

本机相关位置：

```text
~/.hermes/skills/
~/.hermes/hermes-agent/skills/
~/.hermes/hermes-agent/optional-skills/
```

### Claude Code Skill

**Claude Code Skill(Claude Code Skill)** 是 Claude Code 的`可复用任务能力包`。Claude Code 文档显示，skill 通过 `SKILL.md` 扩展 Claude 的能力，支持直接用 `/skill-name` 调用，也能由 Claude 在相关场景下自动加载。旧的 `.claude/commands/` 仍可工作，但 custom commands 已与 skills 合流；skill 比 command 多了支持文件、调用控制、动态上下文、子 agent 等能力。

适合承载：

- 某个代码仓库的开发规范。
- PR review、debug、重构、测试、发布等 coding playbook。
- 团队共享的项目级 coding 约束。
- 与 `.claude/` 配置、CLAUDE.md、MCP、hooks 配套的编码工作流。

常见位置：

```text
~/.claude/skills/<skill-name>/SKILL.md
.claude/skills/<skill-name>/SKILL.md
.claude/commands/<command-name>.md
```

当前本机状态：

```text
未发现 ~/.claude/skills 目录。
```

这说明当前本机 Claude Code 已配置并可用，但个人级 Claude Code skill 目录尚未形成稳定资产库。

### Codex Skill

**Codex Skill(Codex Skill)** 是 Codex 工作环境中的专业化能力包，用来告诉 Codex 何时加载某类工作流、如何使用本地工具、脚本、参考资料和输出模板。Codex skill 的核心也是 `SKILL.md`，并可包含 `scripts/`、`references/`、`assets/`、`agents/openai.yaml` 等辅助资源。

适合承载：

- Vault 笔记生产与 MOC 维护。
- 文档、表格、PPT、SVG、前端、Git 等本地工作流。
- 本机 Codex 桌面环境下稳定复用的操作规程。
- 面向当前工具权限、插件、MCP、沙箱边界的执行说明。

本机相关位置：

```text
~/.codex/skills/
```

当前本机已有示例：

```text
~/.codex/skills/note-crafter/SKILL.md
~/.codex/skills/note-crafter/agents/openai.yaml
```

## 2. 边界辨析

| 维度        | Hermes Skill                                 | Claude Code Skill                                    | Codex Skill                                          |
| --------- | -------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| 核心定位      | Agent 编排与跨入口自动化                              | 代码仓库内的开发 playbook                                    | Codex 环境内的专业工作流                                      |
| 典型触发      | `/skill-name`、自然语言、Gateway、Cron              | `/skill-name`、自动匹配 coding 场景                         | 用户请求触发、本地 skill 描述匹配                                 |
| 主要对象      | 长期任务、外部系统、跨工具调度                              | repo、代码、测试、PR、发布                                     | Vault、文件、插件、命令、文档产物                                  |
| 运行环境      | Hermes CLI/Gateway/后台任务                      | Claude Code CLI / Web coding session                 | Codex 桌面或 CLI 会话                                     |
| 支持资源      | `SKILL.md`、references、scripts、env、config、hub | `SKILL.md`、supporting files、commands、subagents、hooks | `SKILL.md`、references、scripts、assets、agents metadata |
| 最适合做主控的场景 | 自动化、跨平台消息入口、多 agent 调度                       | 项目级代码执行与仓库约束                                         | 本机知识库与产物生产工作流                                        |
| 不适合承担     | 细粒度代码落地的唯一执行者                                | 跨系统长期调度中心                                            | 后台常驻自动化服务                                            |

最容易误用的是：看到三者都有 `SKILL.md`，就把同一个文件无差别复制到三处。这样短期省事，长期会形成三类问题：

- 同名 skill 行为不一致。
- 某个运行时特有配置污染另一个运行时。
- 改了一处忘记同步，导致实际执行规则分叉。

## 3. 维护原则

### 原则一：区分“核心知识”和“运行时适配”

一个 skill 通常可以拆成两层：

| 层级 | 内容 | 维护方式 |
| --- | --- | --- |
| 核心知识 | 任务目标、判断标准、步骤、输出规范、质量检查 | 尽量只维护一份 |
| 运行时适配 | 目录路径、工具名、权限模型、调用方式、环境变量、命令格式 | 按 Hermes / Claude Code / Codex 分开 |

例子：

```text
note-crafter 的核心知识：如何命名、如何挂 MOC、如何写 frontmatter。
Codex 适配：读取本地 Vault、使用 apply_patch、遵守当前技能触发规则。
Claude Code 适配：如果在 repo 中使用，应改成 .claude/skills 并适配 Claude Code 的 tools/permissions。
Hermes 适配：如果要远程触发或定时整理，则需要 Gateway/Cron/skills 配置。
```

### 原则二：不要让工具差异进入核心规范

核心规范中应避免出现：

- “必须使用 Codex 的某个 tool”。
- “必须通过 Claude Code 的某个 slash command”。
- “必须由 Hermes cron 启动”。

这些应放在运行时适配层。否则一个 skill 迁移到另一个工具时，会夹带错误假设。

### 原则三：按任务主战场选择主版本

不是所有 skill 都应该以同一个系统为主版本。

| Skill 类型 | 建议主版本 | 原因 |
| --- | --- | --- |
| Vault 笔记、MOC、术语、调研报告 | Codex Skill | 当前知识库生产主要发生在 Codex 工作区 |
| repo 开发、测试、PR、代码审查 | Claude Code Skill 或项目 `.claude/skills` | 最贴近代码执行现场 |
| 定时任务、消息入口、跨工具编排 | Hermes Skill | Hermes 适合常驻、调度、自动化 |
| 可跨工具复用的通用流程 | 独立核心规范 + 多端适配 | 避免三处重复发散 |

本机当前建议：

```text
Codex 作为知识库类 skill 的主维护环境。
Claude Code 作为 coding 类 skill 的项目级落地环境。
Hermes 作为跨工具调度和自动化入口。
```

## 4. 推荐目录策略

### 4.1 运行时目录

```text
~/.codex/skills/<skill-name>/SKILL.md
~/.claude/skills/<skill-name>/SKILL.md
.claude/skills/<skill-name>/SKILL.md
~/.hermes/skills/<category>/<skill-name>/SKILL.md
```

### 4.2 核心规范目录

如果某个 skill 需要跨 Hermes、Claude Code、Codex 复用，建议在 Vault 中保留一份“核心规范笔记”或“源规范目录”，例如：

```text
99-设置/agent-skills/<skill-name>/skill-core.md
99-设置/agent-skills/<skill-name>/codex/SKILL.md
99-设置/agent-skills/<skill-name>/claude-code/SKILL.md
99-设置/agent-skills/<skill-name>/hermes/SKILL.md
```

含义：

- `skill-core.md`：任务逻辑与质量标准。
- `codex/SKILL.md`：Codex 运行时适配。
- `claude-code/SKILL.md`：Claude Code 运行时适配。
- `hermes/SKILL.md`：Hermes 运行时适配。

只有确实需要多端复用的 skill 才采用这套结构。普通单端 skill 不要过度设计。

## 5. 迁移规则

### 从 Claude Code 迁移到 Codex

适用场景：

- 原来是 `.claude/commands` 或 `.claude/skills` 中的工作流。
- 现在主要在 Codex 中执行。
- 任务不是强绑定 Claude Code 的 repo session。

处理规则：

1. 抽出核心流程：目标、触发条件、步骤、质量标准。
2. 删除 Claude Code 特有假设：slash command、permission、CLAUDE.md、hooks。
3. 加入 Codex 特有约束：工作区、工具权限、`apply_patch`、MOC 挂载、验证方式。
4. 如需 UI 呈现，补 `agents/openai.yaml`。
5. 在旧位置保留迁移说明或停止维护标记，避免双主版本。

### 从 Codex 迁移到 Claude Code

适用场景：

- skill 已经变成具体 repo 的开发流程。
- 需要团队成员在 Claude Code 中共享。
- 依赖代码、测试、PR、CI 等项目上下文。

处理规则：

1. 将 Vault/Obsidian 逻辑移除或下沉为参考。
2. 改成项目级 `.claude/skills/<skill-name>/SKILL.md`。
3. 明确允许工具、验证命令、提交规范、测试范围。
4. 避免引用 Codex 专用工具和桌面插件。
5. 若团队共享，随 repo 提交；若个人使用，放 `~/.claude/skills`。

### 从 Codex 或 Claude Code 迁移到 Hermes

适用场景：

- 需要定时触发。
- 需要从消息入口触发。
- 需要编排多个工具或 agent。
- 需要长期记忆、外部系统、后台任务。

处理规则：

1. 把 skill 写成“编排说明”，而不是细节执行手册。
2. 明确它会调用哪些外部执行器，例如 Claude Code、Codex CLI、Shell、LiteLLM、MCP。
3. 把 secrets 放入 Hermes `.env` 或 required env 机制，不写入 skill 正文。
4. 给出验证方式，例如日志、输出文件、状态检查命令。
5. 将风险操作拆成确认步骤，避免长期任务误执行。

## 6. 去重规则

### 同名不一定同义

例如 `note-crafter`：

- 在 Codex 中：负责本 Vault 的 Obsidian 笔记生产。
- 在 Claude Code 中：如果存在，可能只负责 repo 文档或 README。
- 在 Hermes 中：可能是远程触发的知识库整理入口。

因此同名 skill 必须检查三件事：

```text
对象是否相同？
运行时是否相同？
输出物是否相同？
```

只要三者有一个不同，就不应盲目合并。

### 允许同核不同壳

允许多个系统中存在同名或近名 skill，但要在 frontmatter 或正文中写清楚：

```text
source-of-truth: codex
derived-from: 99-设置/agent-skills/note-crafter/skill-core.md
runtime: codex
last-sync: 2026-04-29
```

这样后续维护者能看懂：这是主版本、派生版本，还是运行时适配版本。

### 删除重复的判断标准

可以删除或归档的情况：

- 两个 skill 面向同一运行时、同一对象、同一输出。
- 只有措辞差异，没有真实功能差异。
- 其中一个长期未被调用，且没有独有脚本或参考资料。
- 新版本已经覆盖旧版本的触发条件和验证方式。

不应删除的情况：

- 一个是 Codex 版，一个是 Claude Code 版。
- 一个是核心规范，一个是运行时适配。
- 一个用于人工交互，一个用于 Hermes 自动化。
- 一个绑定个人环境，一个绑定项目仓库。

## 7. 版本管理规则

建议每个跨工具 skill 至少记录：

```yaml
version: 1.0.0
runtime: codex | claude-code | hermes
source-of-truth: codex | claude-code | hermes | vault-core
derived-from: path-or-url
last-sync: YYYY-MM-DD
```

语义：

- `version`：该运行时版本。
- `runtime`：当前文件服务哪个系统。
- `source-of-truth`：主版本在哪里。
- `derived-from`：迁移或派生来源。
- `last-sync`：最近同步日期。

版本号建议：

| 变更类型 | 版本变化 |
| --- | --- |
| 修错、补充一条验证命令 | `1.0.0 -> 1.0.1` |
| 增加新流程、新触发场景 | `1.0.0 -> 1.1.0` |
| 改变核心判断标准或输出结构 | `1.x.x -> 2.0.0` |

## 8. 维护流程

### 新建 skill

1. 判断任务是否值得做成 skill：是否反复出现、是否有稳定流程、是否有验证标准。
2. 判断主战场：Vault、repo、自动化、跨工具调度。
3. 选择运行时：Codex、Claude Code、Hermes。
4. 写最小可用版本，只包含触发条件、流程、坑点、验证。
5. 用 1-2 个真实任务试跑。
6. 如果需要跨工具，再抽出核心规范并生成适配版本。

### 更新 skill

1. 先确定改的是核心逻辑，还是某个运行时适配。
2. 如果是核心逻辑，更新主版本并标记所有派生版本待同步。
3. 如果只是运行时适配，只改对应运行时版本。
4. 检查 frontmatter 的 description 是否仍准确。
5. 检查 scripts、references、assets 是否仍被正文引用。

### 同步 skill

同步时不要全文覆盖。按顺序处理：

1. 对比触发条件。
2. 对比核心步骤。
3. 对比工具调用假设。
4. 对比输出格式。
5. 对比验证命令。
6. 只把可移植部分同步过去。

### 废弃 skill

废弃时不要直接删除，除非确定没有引用。建议先加：

```yaml
status: deprecated
replaced-by: new-skill-name
deprecated-date: YYYY-MM-DD
```

正文开头写：

```text
本 skill 已废弃，请使用 <new-skill-name>。
```

观察一段时间后再删除。

## 9. 当前本机维护建议

### 短期

- 继续以 `~/.codex/skills` 维护 Vault 笔记、调研、SVG、Git、文档类 workflow。
- 不急于恢复或复制一套 `~/.claude/skills`，除非出现明确的 Claude Code 高频工作流。
- Hermes 暂时优先维护“编排类 skill”，例如调用 Claude Code、Codex、LiteLLM、Docker 服务巡检。
- 对已迁移的 `note-crafter`，在 Codex 中作为主版本维护。

### 中期

- 建立 `99-设置/agent-skills/` 作为跨工具 skill 的源规范区。
- 对高价值 skill 增加 `runtime`、`source-of-truth`、`last-sync` 字段。
- 为每个跨工具 skill 写一个最小测试任务，作为迁移后验证用例。

### 长期

- Hermes 作为跨工具调度中心，不直接承载所有细节。
- Claude Code 只承载项目级 coding skill。
- Codex 承载知识库生产、文档产物、本地工作流 skill。
- 跨工具 skill 采用“核心规范 + 运行时适配”模式，避免三份正文长期漂移。

## 10. 判断清单

创建或维护 skill 前，先回答：

- 这个 skill 是给哪个运行时用的？
- 它服务的是知识库、代码仓库、自动化，还是跨工具调度？
- 是否已有同类 skill？
- 是否需要跨工具复用？
- 哪一份是主版本？
- 是否包含运行时专属命令？
- 是否有验证方式？
- 是否有 secrets 或本机路径泄露风险？

## 相关链接

- [[hermes]]
- [[hermes-mac安装笔记]]
- [[Hermes-LiteLLM-DeepSeek-Docker-Postgres配置笔记]]
- [[Hermes-典型应用场景逻辑架构图]]

> [!important] 压缩记忆
> Hermes、Claude Code、Codex 的 skill 不应按“三份复制”维护。更稳的模型是：核心规范只维护一份，运行时适配分别落到 Hermes、Claude Code、Codex。Codex 适合维护知识库与本地工作流，Claude Code 适合维护项目级 coding playbook，Hermes 适合维护长期自动化与跨工具编排。
