---
aliases:
  - "Garry Tan's gstack"
  - "gstack AI 编程角色工具集"
  - "gstack/Agent/角色工作流(JGSL, GRWF)"
tags: [AI, AI-Agent, Claude Code, 工具]
description: Garry Tan 的 AI 编程角色化 Agent 工具集——23 个角色技能将 Claude Code 变为虚拟工程团队，覆盖 CEO 评审、架构锁定、设计审计、安全扫描、QA 测试、发布部署全流程。
type: note
create-date: 2026-05-01
---

# gstack 介绍

**一句话定义**：gstack 是 Y Combinator CEO Garry Tan 开源的 Claude Code 技能集，用 23 个角色化 slash command 将单个 AI Agent 升级为虚拟工程团队。覆盖产品规划、架构设计、代码审查、安全审计、QA 测试、发布部署全流程。MIT 协议，87K+ GitHub stars。

**核心思路**：传统 AI 编程 = 一个 prompt + 写代码。gstack = 多个角色串行审核，每一步产出结构化文档送入下一步——CEO 质疑范围 → 架构师锁定数据流 → 设计师检测 AI 痕迹 → QA 打开真实浏览器 → 安全官跑 OWASP+STRIDE → 发布工程师合并 PR。

**出处**：[garrytan/gstack](https://github.com/garrytan/gstack)，Garry Tan 日常使用该工具集，2026 年至今逻辑代码产出是 2013 年手写代码的 810 倍。

## 核心角色（23 个）

### 规划阶段

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/office-hours` | YC Office Hours | 产品起点。6 个强制问题重新框定问题，挑战前提，生成实现方案。产出设计文档供下游技能消费。 |
| `/plan-ceo-review` | CEO / Founder | 重新思考问题。4 种模式（扩展/选择性扩展/保持范围/缩减），找出需求中隐藏的 10 星产品。 |
| `/plan-eng-review` | Eng Manager | 锁定架构、数据流、图表、边界条件和测试。迫使隐藏假设浮出水面。 |
| `/plan-design-review` | Senior Designer | 对每个设计维度 0-10 评分，解释满分标准，编辑计划达标。AI Slop 检测。交互式，每个设计选择问一个 AskUserQuestion。 |
| `/plan-devex-review` | Developer Experience Lead | 交互式 DX 审查：探索开发者画像、对比竞品 TTHW、设计关键体验时刻、逐步追踪摩擦点。3 种模式：DX EXPANSION / DX POLISH / DX TRIAGE。20-45 个强制问题。 |
| `/autoplan` | Review Pipeline | 一键全审：CEO → 设计 → 工程 → DX，自动判断哪些适用。仅产出需你确认的品味决策。 |

### 设计与实现

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/design-consultation` | Design Partner | 从零构建设计系统。调研竞品、提出创意风险、生成逼真产品 Mockup。 |
| `/design-shotgun` | Design Explorer | "给我看选项"。生成 4-6 个 AI Mockup 变体，浏览器对比板收集反馈，迭代。品味记忆学习你的偏好。 |
| `/design-html` | Design Engineer | Mockup → 生产级 HTML。Pretext 计算布局，文本回流、高度自适应。30KB 零依赖。自动检测 React/Svelte/Vue。输出可交付，非演示品。 |

### 审查与测试

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/review` | Staff Engineer | 找 CI 过但生产炸的 bug。自动修复明显问题。标记完整性缺口。 |
| `/investigate` | Debugger | 系统化根因调试。铁律：不调查不动手修。追踪数据流，测试假设，3 次修复失败后停止。 |
| `/design-review` | Designer Who Codes | 同 `/plan-design-review` 审计逻辑，然后动手修复发现的问题。原子化提交，修前/修后截图。 |
| `/devex-review` | DX Tester | 真实开发者体验审计。实际走一遍你的入门流程：浏览文档、试跑 Getting Started、计时 TTHW、截图报错。对比 `/plan-devex-review` 评分——检验计划与实际是否吻合的回旋镖。 |
| `/qa` | QA Lead | 测试应用、找 bug、原子化提交修复、重新验证。每次修复自动生成回归测试。 |
| `/qa-only` | QA Reporter | 同 `/qa` 方法论但仅报告，不修改代码。 |
| `/cso` | Chief Security Officer | OWASP Top 10 + STRIDE 威胁模型。零噪音：17 个误报排除规则，≥8/10 置信度门槛，独立发现验证。每个发现含具体攻击场景。 |
| `/codex` | Second Opinion | 通过 OpenAI Codex CLI 独立代码审查。3 种模式：审查（通过/不通过门禁）、对抗挑战、开放咨询。`/review` 和 `/codex` 都跑后触发跨模型交叉分析。 |

### 发布与运维

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/ship` | Release Engineer | 同步 main、跑测试、审计覆盖率、推送、开 PR。无测试框架时自动搭建。 |
| `/land-and-deploy` | Release Engineer | 合并 PR、等 CI 部署、验证生产健康。一条命令从"已批准"到"生产已验证"。 |
| `/canary` | SRE | 部署后监控循环。监控控制台错误、性能退化、页面故障。 |
| `/benchmark` | Performance Engineer | 基线页面加载时间、Core Web Vitals、资源大小。每个 PR 前后对比。 |
| `/document-release` | Technical Writer | 更新所有项目文档匹配刚发布内容。自动捕获过时 README。 |
| `/retro` | Eng Manager | 团队感知周回顾。按人拆解、交付连贯性、测试健康趋势、成长机会。`/retro global` 跨所有项目 + AI 工具（Claude Code、Codex、Gemini）。 |

### 浏览器与安全

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/browse` | QA Engineer | 给 Agent 眼睛。真实 Chromium 浏览器，真实点击，真实截图。约 100ms/命令。 |
| `/setup-browser-cookies` | Session Manager | 从真实浏览器（Chrome、Arc、Brave、Edge）导入 cookies 到头less 会话。测试需认证页面。 |

### 辅助工具

| Slash Command | 角色 | 职责 |
|---------------|------|------|
| `/careful` | Safety Guardrails | 危险命令（rm -rf、DROP TABLE、force-push）前警告。说"be careful"激活。 |
| `/freeze` | Edit Lock | 限制文件编辑到一个目录。调试时防止误改外部文件。 |
| `/guard` | Full Safety | `/careful` + `/freeze` 组合。生产工作最大安全级别。 |
| `/unfreeze` | Unlock | 解除 `/freeze` 边界。 |
| `/learn` | Memory | 管理跨会话学习。审查、搜索、清理、导出项目特定模式、坑位和偏好。学习跨会话累积。 |

### 独立 CLI 工具

| 命令 | 用途 |
|------|------|
| `gstack-model-benchmark` | 跨模型基准测试：同一 prompt 跑 Claude/GPT(Codex)/Gemini，对比延迟/Token/成本/质量分 |
| `gstack-taste-update` | 设计品味学习：将 `/design-shotgun` 的批准/拒绝写入持久化品味档案，5%/周衰减 |
| `gstack-config` | 配置管理：checkpoint 模式、推送策略等 |

## 工作流

角色间通过结构化文档串联，每一步产出自动输入下一步：

```
/office-hours → 设计文档
  ↓
/plan-ceo-review → 挑战范围 → 修订设计文档
  ↓
/plan-eng-review → 锁定架构 → 测试计划
  ↓
（编码实现）
  ↓
/review → 找 bug → 自动修复
  ↓
/qa → 浏览器测试 → 原子化修复 → 回归测试
  ↓
/cso → 安全审计
  ↓
/ship → 开 PR
  ↓
/land-and-deploy → 合并+部署+验证
```

**选择审查类型**：

| 构建目标 | 规划阶段（编码前） | 上线后审计 |
|----------|-------------------|-----------|
| 终端用户（UI、Web App） | `/plan-design-review` | `/design-review` |
| 开发者（API、CLI、SDK、文档） | `/plan-devex-review` | `/devex-review` |
| 架构（数据流、性能、测试） | `/plan-eng-review` | `/review` |
| 以上全部 | `/autoplan` | — |

## 安装

**前置条件**：[Claude Code](https://docs.anthropic.com/en/docs/claude-code)、Git、Bun v1.0+。

**个人模式（30 秒）**：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup
```

然后在 CLAUDE.md 中添加 gstack 配置段。

**团队模式**（共享仓库自动同步）：

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && \
  ~/.claude/skills/gstack/bin/gstack-team-init required && \
  git add .claude/ CLAUDE.md && \
  git commit -m "require gstack for AI-assisted work"
```

**多 Agent 支持**：gstack 支持 10 种 AI 编程 Agent，通过 `./setup --host <name>` 指定：Claude Code、OpenAI Codex、OpenCode、Cursor、Factory Droid、Slate、Kiro、Hermes、GBrain。

**OpenClaw 集成**：OpenClaw 通过 ACP 派生 Claude Code 会话时自动继承 gstack 技能。另有 4 个原生 OpenClaw 技能（通过 ClawHub 安装）：`gstack-openclaw-office-hours`、`gstack-openclaw-ceo-review`、`gstack-openclaw-investigate`、`gstack-openclaw-retro`。

## 产出数据

Garry Tan 自用数据（截至 2026-04-18）：

| 指标 | 数据 |
|------|------|
| 60 天内交付 | 3 个生产服务 + 40+ 功能 |
| 逻辑代码产速 | 2013 年的 810 倍（11,417 vs 14 条逻辑行/天） |
| 2026 年至今总产出 | 2013 全年的 240 倍 |
| 工作节奏 | 兼职开发 + YC CEO 全职 |
| 2026 GitHub 贡献 | 1,237+（持续增加中） |

## 相关

- [[Claude Code]] — gstack 的基础运行平台
- [[OpenClaw]] — 多 Agent 编排，与 gstack 深度集成
- [[Codex CLI]] — gstack `/codex` 命令调用的第二审查引擎
- [[GBrain]] — gstack 内置支持的记忆后端
