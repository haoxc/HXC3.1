---
aliases:
  - Codex Skills 管理清单
  - 我的 Codex Skills
tags:
  - Skills
  - Codex
  - 管理清单
description: 管理当前机器中用户维护和安装的 Codex skills，记录用途、触发词、安装状态与源文件位置。
type: 管理清单
ref-url:
create-date: 2026-04-25 15:30
---
# Codex-Skills管理清单

## 管理口径

本清单记录当前机器 `~/.codex/skills` 下的非系统 skills，并标注其中有 Vault 项目源文件的 skills。

- **项目源目录**：`99-设置/codex-skills`
- **全局安装目录**：`~/.codex/skills`
- **使用原则**：高频、产物稳定、质量标准可描述的工作，才值得沉淀为 skill。

> [!IMPORTANT] 当前判断
> 当前最核心的自建技能链是：`hxc-term-card` 负责术语卡片，`hxc-survey` 负责专业调研报告，`hxc-topic-svy` 保留为快速课题综述，`bx` / `concept-definer` 负责概念理解与辨析，`hxc-svg-workflow-designer` 负责 Obsidian 友好的 SVG 工作流图。

## 项目源可追踪 Skills

| Skill | 状态 | 主要用途 | 典型触发词 | 项目源 | 全局安装 |
| --- | --- | --- | --- | --- | --- |
| `hxc-term-card` | 已安装 | 创建术语库术语卡片，维护术语库 MOC | `create term`、术语卡片、写入术语库 | `99-设置/codex-skills/hxc-term-card` | `~/.codex/skills/hxc-term-card` |
| `hxc-survey` | 已安装 | 生成、修订、审计结论先行的专业调研报告 | `hxc-survey`、调研报告、ref-url、结论先行 | `99-设置/codex-skills/hxc-survey` | `~/.codex/skills/hxc-survey` |
| `hxc-svg-workflow-designer` | 已安装 | 创建和修复 Obsidian 友好的 SVG 工作流图、泳道图、Wiki 可视化索引 | SVG 工作流图、流程图、黑块、重叠、截断、Obsidian 渲染 | 待镜像 | `~/.codex/skills/hxc-svg-workflow-designer` |

## 全局 Skills 总表

| 分组 | Skill | 用途定位 | 备注 |
| --- | --- | --- | --- |
| 调研与知识建模 | `hxc-survey` | 专业调研报告：结论、证据、对比、风险、建议 | 新版调研主 skill |
| 调研与知识建模 | `hxc-topic-svy` | 快速课题综述和技术方向判断 | 旧版快速综述，可继续保留 |
| 调研与知识建模 | `hxc-term-card` | 术语卡片创建与术语库入口维护 | 已有项目源 |
| 调研与知识建模 | `concept-definer` | 单一概念快速定义卡 | 适合“什么是 X” |
| 调研与知识建模 | `bx` | 多概念辨析、边界分析 | 实际目录名为 `concepts-clarifier` |
| Wiki / MOC / 可视化 | `moc-wiki-designer` | MOC / Wiki 目录页设计与审计 | 索引页只放目录树和链接 |
| Wiki / MOC / 可视化 | `hxc-svg-workflow-designer` | Obsidian 友好的 SVG 工作流图与可视化索引 | 内联 SVG 属性，检查黑块、截断、重叠 |
| 审计治理 | `hxc-model-auditor` | 管理模型、课题生命周期、信息负载审计 | 顶层管理模型审计 |
| 审计治理 | `pjx-common-auditor` | 通用项目结构、命名、MOC 审计 | Agent / Skill / Prompt 项目适用 |
| 审计治理 | `pjx-kw-auditor` | 知识交付、课程、教学材料工作区审计 | 知识类项目适用 |
| 审计治理 | `pjx-zs-auditor` | 止善公司项目轻文档强闭环审计 | ZS 项目适用 |
| 写作与内容 | `doc-coauthoring` | 文档共创、方案、技术规格、决策文档 | 适合结构化文档生产 |
| 写作与内容 | `adaptive-editor` | 同一内容面向不同对象/语气/长度改写 | 学生版、教师版、PPT 版 |
| 数据整理 | `data-organizer` | 将散乱内容抽取成字段、表格、JSON、矩阵 | 适合结构化输入 |
| 表格文件 | `xlsx` | 创建、修改、清洗、格式化电子表格 | 以表格文件为交付物 |
| 前端产出 | `frontend-design` | 高质量前端界面设计与实现 | 视觉/交互类任务 |
| 前端产出 | `web-artifacts-builder` | 复杂 HTML artifacts 构建 | React / Tailwind / shadcn 场景 |
| Git 工作流 | `github-push` | GitHub push 失败诊断与恢复 | SSH/HTTPS/凭据问题 |
| 交互协议 | `qie-confirmation-flow` | QIE / 英文复述确认流程 | 显式触发才使用 |

## 使用优先级

### 高频优先

1. `hxc-term-card`：用于术语库卡片，产物格式稳定，复用频率高。
2. `hxc-survey`：用于调研报告，已吸收“结论先行、证据链、对比、风险、图表建议”的新规则。
3. `bx` / `concept-definer`：用于概念理解前置，避免调研和写作中术语漂移。

## 已落地的轻量编排

| Skill | 已落地编排 | 说明 |
| --- | --- | --- |
| `hxc-survey` | 主报告 -> 独立摘要 -> MOC -> 校验 | 已内置 bundle workflow，并提供 `scripts/validate_survey_bundle.sh` |
| `hxc-term-card` | 卡片 -> 术语库入口 -> 校验 | 仍为规则驱动，尚未单独脚本化 |

### 审计按对象选择

| 审计对象 | 优先 skill |
| --- | --- |
| 管理模型、课题生命周期、信息负载 | `hxc-model-auditor` |
| 通用项目目录、Agent / Skill / Prompt 仓库 | `pjx-common-auditor` |
| 知识交付、课程、教学材料 | `pjx-kw-auditor` |
| ZS 公司项目、轻文档强闭环 | `pjx-zs-auditor` |

## 维护规则

1. **先项目源，后全局安装**：新建或修改自建 skill 时，优先在 `99-设置/codex-skills/{skill}` 保存源文件，再同步到 `~/.codex/skills/{skill}`。
2. **修改后必须校验**：使用 `quick_validate.py` 验证项目源和全局安装版。
3. **新增触发词要写入 description**：Codex 主要依赖 `SKILL.md` frontmatter 的 `description` 判断是否触发。
4. **重要工作流要回写本清单**：新增 skill、废弃 skill、职责变化、触发词变化，都应更新本页。
5. **避免重复 skill**：如果只是输出模板变化，优先扩展现有 skill；只有当任务对象、触发条件、质量标准明显不同，才新建 skill。

## 后续待整理

- 为全局已安装但没有项目源的自建 skill 建立源镜像。
- 判断哪些安装型 skills 是长期保留，哪些只是临时能力。
- 为核心 skills 建立“版本 / 最近更新 / 适用仓库”字段。
