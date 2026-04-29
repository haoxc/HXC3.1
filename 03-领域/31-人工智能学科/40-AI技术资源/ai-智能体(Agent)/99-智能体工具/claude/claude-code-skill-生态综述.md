---
aliases:
  - Claude Code Skill生态综述
  - Agent Skills生态综述
  - Claude Skills热门清单
  - skill综述
tags: [ai/智能体/工具/claude, Claude-Code, Agent-Skills, 综述]
description: 梳理 Claude Code / Agent Skills 的定位、热门 Skill、Vercel 系列、安装方式与选型风险
type: 综述笔记
ref-url:
  - https://github.com/anthropics/skills
  - https://skills.sh/
  - https://awesomeclaudeskills.com/
  - https://www.openaitoolshub.org/en/blog/best-claude-code-skills-2026
  - https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
create-date: 2026-04-29 00:00
---

# Claude Code Skill 生态综述

## 课题判断

- 类型：技术生态 / Agent 扩展机制
- 调研目标：快速判断当前 Claude Code / Agent Skills 生态里哪些 Skill 值得关注、如何筛选、如何安装，以及哪些风险需要提前识别。
- 时间口径：2026-04-29 检索结果。安装量、star、trending 数据会持续变化，后续应以 `skills.sh` 和 GitHub 仓库实时数据为准。

## 技术定位

**Skill** 是一种面向 AI Agent 的轻量能力包。它通常由一个目录和 `SKILL.md` 组成，里面写明触发场景、工作流程、约束、示例、可选脚本和参考资料。

它的定位不是“模型插件”本身，而是：

```text
Skill = 可复用的任务方法论 + 操作流程 + 领域规则 + 可选工具脚本
```

和 MCP 的区别：

| 项目 | Skill | MCP Server |
| --- | --- | --- |
| 核心作用 | 告诉 Agent 如何做事 | 给 Agent 新工具能力 |
| 主要形式 | Markdown / 资源文件 / 脚本 | 长驻服务 / JSON-RPC 工具 |
| 典型例子 | TDD 流程、Debug 方法、前端设计规范 | 浏览器自动化、Slack、数据库、GitHub API |
| 最佳搭配 | 定义流程和判断标准 | 执行外部动作或访问外部系统 |

GitHub 文档也把 Agent Skills 描述为可被 Agent 在相关任务中加载的 instructions、scripts 和 resources，并说明其已成为跨多种 AI 系统使用的开放标准。

## 生态结构

当前 Skill 生态大致分成五类：

| 类别 | 代表来源 | 典型用途 |
| --- | --- | --- |
| 官方参考 | `anthropics/skills` | 文档处理、前端设计、Skill 创建、Claude API、WebApp 测试 |
| 工程工作流 | `obra/superpowers` | Brainstorming、TDD、系统化 Debug、计划编写、代码评审 |
| Web / 前端 | `vercel-labs/agent-skills`、`shadcn/ui` | React / Next.js 性能、Web 设计规范、组件使用规范 |
| 云与平台 | `microsoft/azure-skills`、Supabase、Firebase、Expo | 云资源、数据库、React Native、平台最佳实践 |
| 内容与文档 | Anthropic 文档 Skills、marketing skills、Remotion | PDF / PPT / 表格 / 文档、营销、视频生成 |

## 热门 Skill 清单

以下按当前安装量、GitHub stars、目录曝光度综合整理。数字只作为热度信号，不等于质量保证。

| Skill / 集合 | 热度信号 | 适合用途 | 链接 |
| --- | --- | --- | --- |
| `find-skills` | `skills.sh` 显示约 1.2M installs | 查找、推荐、安装其他 Skills 的元技能 | [skills.sh](https://skills.sh/vercel-labs/skills/find-skills) / [GitHub](https://github.com/vercel-labs/skills) |
| `vercel-react-best-practices` | 约 357K installs | React / Next.js 性能优化与最佳实践 | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) |
| `frontend-design` | 约 348K installs | 生成更有设计感的前端界面，避免泛 AI 风格 | [skills.sh](https://skills.sh/anthropics/skills/frontend-design) / [GitHub](https://github.com/anthropics/skills) |
| `web-design-guidelines` | 约 284K installs | UI / UX / 可访问性审计 | [skills.sh](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines) |
| `remotion-best-practices` | 约 274K installs | 用 React / Remotion 生成视频 | [skills.sh](https://skills.sh/remotion-dev/skills/remotion-best-practices) |
| `microsoft-foundry` | 约 266K installs | Microsoft Foundry Agent 创建、部署、评估、管理 | [skills.sh](https://skills.sh/microsoft/azure-skills/microsoft-foundry) |
| `skill-creator` | 约 174K installs | 创建、评估、迭代自己的 Skill | [skills.sh](https://skills.sh/anthropics/skills/skill-creator) / [GitHub](https://github.com/anthropics/skills) |
| `supabase-postgres-best-practices` | 约 129K installs | Postgres / Supabase 性能、安全、RLS、索引 | [skills.sh](https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices) |
| `brainstorming` | 约 127K installs | 编码前做方案澄清、设计评审和取舍 | [skills.sh](https://skills.sh/obra/superpowers/brainstorming) |
| `systematic-debugging` | 约 75K installs | 根因分析式 Debug，避免随机试错 | [skills.sh](https://skills.sh/obra/superpowers/systematic-debugging) |
| `test-driven-development` | 约 64K installs | TDD：先写失败测试，再实现，再重构 | [skills.sh](https://skills.sh/obra/superpowers/test-driven-development) |
| `docx` / `pptx` / `xlsx` / `pdf` | 约 63K-88K installs | Word、PPT、Excel、PDF 文件处理 | [Anthropic skills](https://github.com/anthropics/skills) |
| `webapp-testing` | 约 57K installs | Web 应用测试流程 | [skills.sh](https://skills.sh/anthropics/skills/webapp-testing) |
| `shadcn` | 约 114K installs | shadcn/ui 组件上下文与使用规范 | [skills.sh](https://skills.sh/shadcn/ui/shadcn) |
| `playwright-skill` | Awesome Claude Skills 显示约 2.5K stars | Playwright 浏览器自动化、点击、填写、抓取 | [Awesome Claude Skills](https://awesomeclaudeskills.com/skill/lackeyjb/playwright-skill) |

## Vercel 系列 Skills

Vercel 相关 Skill 当前主要围绕 Web 开发、React / Next.js、设计规范和 Skill 发现。

| Skill | 作用 | 安装示例 |
| --- | --- | --- |
| `find-skills` | 查找和推荐生态内 Skill | `npx skills add https://github.com/vercel-labs/skills --skill find-skills` |
| `vercel-react-best-practices` | React / Next.js 性能优化规则 | `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices` |
| `web-design-guidelines` | 按 Vercel Web Interface Guidelines 做 UI 审计 | `npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines` |
| `vercel-composition-patterns` | 组件组合、页面结构和前端工程模式 | 见 [skills.sh](https://skills.sh/) 搜索 |
| `deploy-to-vercel` | Vercel 部署相关流程 | 见 [skills.sh](https://skills.sh/) 搜索 |

判断：Vercel 系列适合前端工程项目，尤其是 React / Next.js / Vercel 部署链路。如果当前工作是 Obsidian 知识库、课程资料、文档治理，则只需要保留 `find-skills` 和少量设计/文档类 Skill，不必整套安装。

## 安装方式

常见方式一：通过 `skills.sh` CLI 安装：

```bash
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
```

常见方式二：Claude Code 项目级 Skill：

```text
.claude/skills/{skill-name}/SKILL.md
```

常见方式三：Claude Code 个人级 Skill：

```text
~/.claude/skills/{skill-name}/SKILL.md
```

常见方式四：Anthropic 官方 Skills 作为 Claude Code Plugin 安装：

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## 筛选标准

安装第三方 Skill 前，至少看五点：

1. **来源可信度**：优先官方或成熟团队，如 Anthropic、Vercel、Microsoft、Supabase、Trail of Bits。
2. **安装量 / Stars**：只能作为热度信号，不等于质量保证。
3. **是否运行脚本**：凡是会执行 shell、安装依赖、写配置、调用外部 API 的 Skill，都要先读 `SKILL.md`。
4. **是否发送数据到外部服务**：涉及代码、文档、客户资料时尤其要小心。
5. **是否适配你的工作流**：Skill 是工作方法，不是越多越好；只装高频任务需要的。

## 推荐安装组合

### 通用起步

```text
find-skills
skill-creator
systematic-debugging
brainstorming
```

适合：建立自己的 Skill 体系、减少随机试错、让复杂任务先澄清再执行。

### 前端 / Web

```text
frontend-design
vercel-react-best-practices
web-design-guidelines
shadcn
playwright-skill
```

适合：React / Next.js / UI 设计 / 浏览器测试。

### 文档与知识生产

```text
docx
pptx
xlsx
pdf
doc-coauthoring
```

适合：报告、PPT、表格、PDF、知识库内容生产。

### 数据库 / 后端

```text
supabase-postgres-best-practices
systematic-debugging
test-driven-development
```

适合：SQL、性能优化、RLS、Bug 定位、回归测试。

## 决策要点

1. **先装元技能，再装领域技能。**  
   `find-skills` 和 `skill-creator` 能帮助发现、创建和维护自己的 Skill。

2. **优先装“流程型 Skill”。**  
   `systematic-debugging`、`brainstorming`、`test-driven-development` 这类 Skill 能直接改变 Agent 的工作方式，收益通常比单纯知识清单更稳定。

3. **领域 Skill 要按工作流选择。**  
   前端项目装 Vercel / shadcn / frontend-design；文档项目装 docx / pptx / xlsx / pdf；知识库治理则更适合自定义本地 Skill。

4. **第三方 Skill 当作代码依赖审查。**  
   只要它会运行脚本、安装依赖、调用外部 API，就不能只看 stars 或 installs。

## 图表建议

- 图表类型：场景-能力矩阵
- 适用原因：Skill 选型的关键不是“哪个最火”，而是“哪个场景需要哪类能力”。
- 建议维度：
  - 场景：前端、调试、测试、文档、数据库、云平台、知识生产
  - 能力：设计、审计、执行、生成、验证、部署
  - 风险：脚本执行、外部 API、数据暴露、依赖安装
  - 推荐等级：必装、按需装、谨慎装

> [!summary] 一句话总结
> Skill 生态正在从 Claude Code 专属扩展变成跨 Agent 的开放能力包体系；真正值得安装的不是“最多的 Skill”，而是能固化高频工作流、降低试错、且来源可信的 Skill。
