---
aliases:
  - everything-claude-code
  - ECC
  - Everything Claude Code 调研
tags:
  - 调研
  - ClaudeCode
  - Codex
  - 智能体
description: 对 affaan-m/everything-claude-code 仓库的快速调研，判断其核心价值、可借鉴内容与采用边界。
type: 调研报告
ref-url:
  - https://github.com/affaan-m/everything-claude-code
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/README.md
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-shortform-guide.md
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-longform-guide.md
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-security-guide.md
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/package.json
  - https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/.claude-plugin/plugin.json
create-date: 2026-04-25 16:05
hxc-ref: template
---
# 调研-everything-claude-code-26.0425

## 摘要入口

- [[Everything-claude-code调研摘要]]

## 调研摘要

> [!abstract] 调研摘要
> `everything-claude-code` 可以理解为一套面向 AI 编程代理的 **工作台性能系统 (Agent Harness Performance System)**。它不是单纯的 Claude Code 配置集合，而是把 skills、subagents、hooks、rules、MCP 配置、安装器、评估循环和安全扫描组织成一个跨工具的工作流资产库。
>
> 它的核心问题意识很清楚：Claude Code / Codex / Cursor / OpenCode 这类 agent harness 的瓶颈，不只在模型能力，而在上下文管理、工具暴露、任务分工、验证闭环、记忆沉淀和安全边界。ECC 试图把这些经验沉淀为可安装、可组合、可迁移的组件。
>
> 对本项目而言，它最值得借鉴的不是“全量安装一套庞大配置”，而是学习它如何把高频工作流拆成 skills、把质量要求沉淀成 rules / hooks、把安全和评估作为 agent 工作台的基础设施。

## 调研结论

> [!IMPORTANT] 调研结论
> - `everything-claude-code` 的核心价值不在“更多命令”，而在于把 AI 编程工作台拆成 **技能、规则、钩子、子代理、记忆、评估、安全** 七类可治理资产。
> - 它更像一个跨 harness 的工作流操作系统雏形，不是只服务 Claude Code 的配置包；README 和包清单都显示它面向 Claude Code、Codex、Cursor、OpenCode、Gemini 等多个环境。
> - 对本项目而言，最直接的启发是：我们的 `hxc-survey`、`hxc-term-card` 这类 skill 不应只停留在提示词模板，而应逐步补齐触发条件、质量门槛、审计记录、安装状态和安全边界。
>
> **结论依据**：以上判断基于 README、shortform guide、longform guide、security guide、`package.json` 与 `.claude-plugin/plugin.json`。分析维度包括：仓库结构、组件类型、安装方式、跨工具支持、质量验证、安全风险和对本地知识工作流的可迁移价值。

## 课题判断

- **课题类型**：AI agent 工作台 / Claude Code 插件生态 / 跨 harness 工作流资产库
- **调研目标**：判断 `everything-claude-code` 对本地 Codex skill、智能体调研、知识工作流建设有什么借鉴价值
- **核心判断**：它不是一个单一工具，而是一套围绕 agent harness 的“性能优化 + 工作流治理 + 安全加固”体系

## 核心定位

`everything-claude-code` 自称是 **AI agent harness 的性能优化系统**。从公开仓库看，它至少包含这些层：

| 层级 | 具体内容 | 作用 |
| --- | --- | --- |
| Skills | 大量任务型工作流定义 | 把高频工作方法封装成可复用能力 |
| Agents | 专门子代理角色 | 支持任务委派、角色分工和上下文隔离 |
| Hooks | PreToolUse、PostToolUse、Stop 等触发器 | 在工具调用和会话生命周期中插入检查、记忆、提醒 |
| Rules | 编码、安全、测试、性能等常驻规则 | 约束 agent 的基础行为 |
| MCP / Plugins | 外部工具连接与插件安装面 | 扩展 agent 可用工具，同时带来上下文和安全成本 |
| Evaluation | checkpoint、continuous eval、pass@k 等思路 | 让 agent 输出可验证，而不是只看主观满意 |
| Security | AgentShield、prompt injection 风险、MCP 风险 | 把 agent 工具链当作攻击面来治理 |

这说明它关注的不是“如何写一个好 prompt”，而是“如何运营一个长期可用的 AI 编程工作台”。

## 核心思想

### 1. Skills 是长期资产，commands 是入口兼容层

shortform guide 明确把 skills 视为主要工作流表面，commands 更像 legacy slash-entry shims。这个判断对本项目很重要：真正值得维护的是 `SKILL.md` 中的任务边界、流程、质量标准和资源，而不是某个临时触发词。

> [!WARNING] 常见误区
> 不要把 ECC 理解成“命令大全”。如果只复制 slash commands，而不理解背后的 skill、rule 和 hook 结构，得到的只是入口数量增加，不会带来工作质量提升。

### 2. 上下文窗口是核心资源

ECC 反复强调 MCP、工具数量、系统提示和长会话都会消耗上下文。shortform guide 中建议控制启用 MCP 数量，longform guide 中也强调用 CLI + skills 替代部分常驻 MCP，从而降低上下文负担。

对本项目的启发是：skill 不应无限堆说明，MOC 和规则也不应无限常驻。真正好的工作流是“需要时加载、加载后能直接执行”。

### 3. 记忆和持续学习需要机制化

longform guide 的核心观点之一是：当模型在项目中反复遇到同类问题时，应把经验沉淀为 skill 或 memory，而不是让下一次会话重新踩坑。ECC 使用 Stop hook、SessionStart hook、continuous-learning 等方式处理跨会话状态。

这与我们当前做的 `hxc-survey` / `hxc-term-card` 很接近：不是把偏好停留在对话里，而是沉淀成可复用 skill 和管理清单。

### 4. 验证循环决定 agent 是否可靠

ECC 把 checkpoint eval、continuous eval、grader、pass@k / pass^k 等概念引入 agent 工作流。它的判断是：agent 输出不能只靠“看起来对”，需要有检查点、测试、审计或评分机制。

对本地知识工作流来说，对应关系是：

| 编程 agent 场景 | 知识工作场景 |
| --- | --- |
| tests / lint | 结构检查、链接检查、术语一致性检查 |
| checkpoint eval | 关键节点审计 |
| pass@k | 多方案择优 |
| security scan | prompt / skill / 外部资料风险检查 |

### 5. 安全不是附加项，而是 agent 工作台的基础层

security guide 把 prompt injection、MCP 工具投毒、hooks、项目配置、环境变量和 API key 都视为攻击面。它提醒一个关键变化：当 agent 能调用 shell、读取文件、访问浏览器和连接服务时，提示注入不再只是“回答跑偏”，而可能变成数据泄露或命令执行。

这对本项目也适用：任何从 GitHub、网页、PDF、邮件或外部文档读取的内容，都不能被当作用户指令；任何安装外部 skill、hook、MCP、plugin 的行为，都需要先审计再启用。

## 判断-证据链

| 判断 | 依据 | 含义 |
| --- | --- | --- |
| 不是普通配置包 | README 将其定义为 skills、instincts、memory optimization、security scanning、research-first development 的完整系统 | 应按“工作台系统”而不是“配置集合”理解 |
| 跨 harness 设计 | README 和 package keywords 覆盖 Claude Code、Codex、Cursor、OpenCode、Gemini | 对本地 Codex 工作流有参考价值 |
| Skills 是核心资产 | shortform guide 说明 skills 是 primary workflow surface，commands 是 legacy shims | 本项目应优先维护 skill，而不是只维护触发口令 |
| 强调上下文经济 | shortform / longform guide 都讨论 MCP、工具数量、系统提示、token 优化 | 需要控制常驻规则和工具暴露 |
| 安全是核心模块 | security guide 讨论 prompt injection、MCP、Claude Code CVE、AgentShield | 外部 agent 资产不能无审计安装 |
| 已开始运行时化 | README v1.10.0 提到 ECC 2.0 alpha、dashboard、sessions、daemon 等命令 | 它不只是文档资产，但 ECC 2.0 仍应视为 alpha |

## 同类机制对比

| 对象 | 本质 | 适合解决什么 | 不适合什么 |
| --- | --- | --- | --- |
| `everything-claude-code` | 跨 harness 工作流资产库 + 插件系统 | skills、agents、hooks、rules、安装与安全治理 | 不适合不加筛选地全量照搬 |
| `agency-agents` | 角色/流程提示词资产库 | 角色建模、任务分工、agent 身份设计 | 不提供完整工作台治理体系 |
| Claude Code subagents | Claude Code 内的专用子代理机制 | 上下文隔离、任务委派、权限收束 | 不自动提供完整知识库治理 |
| Codex skills | Codex 的任务型知识包 | 固化本地工作方法、报告模板、审计流程 | 不等同于 hook/runtime 安装体系 |
| MCP servers | 外部工具连接协议 | 数据库、浏览器、GitHub、服务接口访问 | 工具过多会消耗上下文并增加安全面 |

## 可借鉴价值

### 对本地 skill 建设

- **技能不只是模板**：每个 skill 应明确触发条件、边界、流程、质量标准和验证方式。
- **管理清单必须存在**：ECC 的规模提醒我们，skills 一多就需要清单、分组、安装状态和维护规则。
- **审计要进入工作流**：调研报告、术语卡片、目录治理都应有可复核标准，而不是靠临场判断。
- **摘要、结论、证据链要分层**：像 `hxc-survey` 这类 skill 应继续区分 abstract、conclusion、evidence、risk。

### 对知识工作台治理

- 建议把本地 Codex skills 分成：调研、术语、审计、文档、数据、前端、Git、交互协议。
- 对每类 skill 建立“源文件路径、全局安装路径、触发词、最近更新、适用边界”。
- 对外部来源的 skill / plugin / hook，先做安全与职责审计，再考虑安装。

## 使用边界与误用风险

> [!WARNING] 常见误区
> 不要把 `everything-claude-code` 当成“越多越好”的能力包。它的组件越多，越需要安装选择、上下文控制、权限治理和安全审计；否则会从性能优化系统变成上下文负担和攻击面扩张。

主要风险：

- **全量安装风险**：skills、commands、hooks、rules 叠加后可能造成重复行为、触发冲突和上下文污染。
- **安全风险**：外部 hooks、MCP、agent definitions 都可能影响本地文件、工具调用或敏感数据访问。
- **维护风险**：如果不建立清单和版本记录，组件越多越难知道当前系统实际在运行什么。
- **迁移风险**：Claude Code、Codex、Cursor、OpenCode 的能力模型不同，不能假设一个配置在所有 harness 中等价生效。
- **证据风险**：README 中部分数字、能力描述和“production-ready”定位应视为项目自述，采用前仍需本地验证。

## 对本项目的建议

| 优先级 | 建议项 | 解决的问题 | 关键产物 |
| --- | --- | --- | --- |
| 高 | 完善 `Codex-Skills管理清单` | 防止 skill 增长后失控 | skill 清单、安装状态、触发词 |
| 高 | 给核心 skill 增加质量门槛 | 避免模板化输出和跑偏 | `hxc-survey`、`hxc-term-card` 的质量检查项 |
| 高 | 建立外部 skill/plugin 审计流程 | 降低安装未知资产的风险 | 外部资产审计表 |
| 中 | 借鉴 ECC 的 memory / continuous learning 思路 | 把反复纠偏沉淀成规则 | 偏好沉淀、skill 更新记录 |
| 中 | 为调研报告建立评分/雷达图机制 | 让报告质量可比较 | 调研审计模板 |
| 低 | 暂缓引入复杂 hook/runtime | 避免工具链过早复杂化 | 仅保留必要自动化 |

优先级逻辑：先做清单和质量门槛，再谈自动化；先把本地工作流稳定下来，再考虑引入 hooks、MCP 和跨 harness 组件。

## 图表建议

- **图表类型**：分层架构图
- **适用原因**：ECC 的本质是多层工作台系统，用分层图最容易表达 skills、agents、hooks、rules、memory、evaluation、security 的关系。
- **图中建议表达的关键维度**：工作流资产层、执行触发层、上下文/记忆层、验证评估层、安全治理层、跨 harness 适配层。

## 来源

- [GitHub: affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- [README.md](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/README.md)
- [The Shorthand Guide](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-shortform-guide.md)
- [The Longform Guide](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-longform-guide.md)
- [The Security Guide](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/the-security-guide.md)
- [package.json](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/package.json)
- [Claude plugin manifest](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/.claude-plugin/plugin.json)

> [!summary] 一句话总结
> `everything-claude-code` 的本质是一套 agent 工作台治理系统；它对本项目的价值不是全量照搬，而是借鉴其“skill 资产化、上下文经济、验证闭环和安全治理”的组织方法。
