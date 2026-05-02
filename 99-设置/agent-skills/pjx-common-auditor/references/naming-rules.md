# PJX Naming Rules — Software R&D Projects

> ⚠️ **适用范围**：以下规则仅适用于软件研发/Agent-Skill-Prompt 仓库及文档密集型技术项目。
> 知识管理型 Vault（Obsidian 个人知识库）审计规则见 SKILL.md 的 KV-1 至 KV-11 维度。

## Rule Authority

Use this authority order when applying naming rules:

1. Rules explicitly defined in `SKILL.md`.
2. Project-specific current standards in `01-规范`.
3. User-confirmed decisions in the current conversation.

If a naming or structure rule is not covered by these sources, treat it as undefined. Undefined rules must not be enforced, classified as findings, or used for directory changes until the user confirms them.

When a new rule is needed, first state the gap, list practical options, and ask the user to confirm the intended rule.

## Top-Level Directory Roles

| Directory | English | Role |
| --- | --- | --- |
| `00-总览` | Dashboard / Entry | Global entry, module index, status overview |
| `01-规范` | Standards / Published Rules | Current effective rules and reusable standards |
| `05-协同` | Collaboration | Temporary personal workspace and migration queue |
| `09-治理` | Governance Process | Current default governance evidence directory: ADR source records, change requests, reviews, retrospectives, audit evidence |
| `10-需求` | Business Requirements | Customer inputs, requirement ledger, scenario analysis, requirement definition, functional definition, baselines |
| `10-管理` | Management | Planning, plans, tasks, risks, issues, decisions, metrics in baseline projects without top-level requirements |
| `15-管理` | Management | Planning, tasks, risks, reports, metrics, decisions, meetings when `10-需求` occupies the `10` slot |
| `20-模块` | Modules | Agent / Skill / Prompt lifecycle materials |
| `60-资产` | Assets / Reuse | Cross-module templates, examples, snippets |
| `90-归档` | Archive | Historical, deprecated, or abandoned materials |
| `98-附件` | Attachments | Images, PDFs, media, non-text resources |
| `99-设置` | System | Obsidian, scripts, templates, tool configuration |

> **历史说明**：`00-总控` 为早期非标准名称，已弃用。当前唯一标准入口为 `00-总览`。存量项目若使用 `00-总控`，不建议重命名（历史 ADR 已引用），但新项目必须使用 `00-总览`。

Compatibility note: `02-治理` is legacy or external-project compatibility. Do not recommend it for new ZS/PJX projects unless the local project standard explicitly defines it.

## Numeric Prefix Semantics

Numeric prefixes are sorting codes. They should make the file system stable, not replace human-readable directory names.

| Range | Meaning | Examples |
| --- | --- | --- |
| `00` | Entry | `00-总览` |
| `01-09` | Control plane | `01-规范`, `05-协同`, `09-治理` |
| `10-19` | Requirements and overall management | `10-需求`, `10-管理`, `15-管理` |
| `20-59` | Module production | `20-模块` |
| `60-79` | Reusable assets | `60-资产` |
| `90-99` | Support and history | `90-归档`, `98-附件`, `99-设置` |

Use local numbering within each parent directory. Avoid encoding hierarchy into numbers such as `110 / 120 / 130`; the path already expresses hierarchy.

Numeric prefixes are allowed for first-level and second-level structure directories. Third-level and deeper directories must not start with numeric codes by default.

Rules for third-level and deeper directories:

- Use semantic structure names, for example `方案`, `参考`, `外发`, `承接`, `设计`, `开发`, `验收`, `发布`, `售前基线`.
- Do not use local numeric structure names such as `20-方案`, `90-参考`, `10-承接`, `20-设计`, or `10-售前基线`.
- Evidence package directories should use `{topic}-{yy.MMdd}`, not `{yy.MMdd}-{topic}` or `{yymmdd}-{topic}`.
- Customer raw material folders may retain source names when they are read-only external inputs and excluded from Git.

## Standard Project Structure

Baseline structure:

```text
00-总览
01-规范
05-协同
09-治理
10-管理
20-模块
60-资产
90-归档
98-附件
99-设置
```

Requirements-intensive structure:

```text
00-总览
01-规范
05-协同
09-治理
10-需求
15-管理
20-模块
60-资产
90-归档
98-附件
99-设置
```

Use the requirements-intensive structure when business-side participation, customer materials, pre-contract requirements, post-contract implementation requirements, and baseline confirmation are material to the project.

## Requirements Structure

```text
10-需求/
  10-需求.md
  01-客户资料/
  10-需求台账/
  20-场景分析/
  30-需求定义/
  40-功能定义/
  50-需求基线/
    售前基线/
    合同基线/
    实施基线/
    变更确认/
```

Role boundaries:

- `01-客户资料` stores customer-side source inputs. Raw customer materials are read-only and may be excluded from Git.
- `10-需求台账` tracks requirement source, phase, status, priority, related scenario, related function, owner, and baseline state.
- `20-场景分析` answers why the business needs something.
- `30-需求定义` answers what the customer needs.
- `40-功能定义` answers what the system must do.
- `50-需求基线` stores confirmed snapshots and replaces vague first-level `需求确认` folders.

| 规则 | ✓ | ✗ |
|------|---|---|
| `20-场景分析` 回答 "why" | 业务流程痛点、用户故事 | 系统功能列表 |
| `40-功能定义` 回答 "what to build" | 系统能力边界、功能清单 | 重复场景分析的 why |
| `50-需求基线` 替代 `需求确认` | `50-需求基线/售前基线/` | `需求确认/`（模糊一级目录） |
| 基线子目录用语义名 | `售前基线` `合同基线` | `10-售前基线` `20-合同基线` |

Stage logic:

- Pre-sales, contract, implementation, and change confirmation are states in the requirement lifecycle.
- Do not split every requirement artifact into separate first-level folders by stage.
- Use `10-需求台账` fields to track stage and status.
- Use `50-需求基线` subdirectories to store confirmed snapshots for each stage.

Common requirement findings:

- P2: `10-需求` exists but no `10-需求台账` exists.
- P2: `20-场景分析` and `40-功能定义` duplicate each other instead of separating business "why" from system "what".
- P2: Broad `需求确认` directories are used instead of `50-需求基线`.
- P2: `50-需求基线` subdirectories use numeric prefixes such as `10-售前基线`; use semantic names instead.
- P2: Customer raw materials are committed to Git when they should be treated as external, bulky, or sensitive inputs.
- P2: Module technical handoff uses `20-模块/{module}/10-需求` while top-level `10-需求` already owns business requirements.

## Management Structure

Baseline projects may use:

```text
10-管理/
  10-规划/
  20-计划/
  30-任务/
  40-风险/
  50-问题/
  60-决策索引/
  70-度量/
```

Requirements-intensive projects should avoid duplicate top-level `10` codes and may use:

```text
15-管理/
  15-管理.md
  10-规划/
  20-任务/
  30-风险/
  40-周报/
  50-指标/
  60-决策/
  90-会议/
```

Management files are project-level files. They should not be nested under one module unless the whole project is that module.

`10-管理/60-决策索引` or `15-管理/60-决策` is a management view for ADR status and key decision chains. It should link to `09-治理` for source records and should not store ADR source records.

| 规则 | ✓ | ✗ |
|------|---|---|
| ADR 源记录在 `09-治理/` | `09-治理/20-决策记录/ADR-0001-*.md` | `10-管理/60-决策索引/ADR-0001-*.md` |
| 管理视图仅索引 | `10-管理/60-决策索引.md`（含 [[ADR-0001]] 链接） | 在管理视图中粘贴完整 ADR 正文 |

Long-lived plan documents may use versioned planning identities when the project standard defines them:

```text
PLAN-V001-{topic}.md
PLAN-V002-{topic}.md
```

| 规划文件命名 | ✓ | ✗ |
|-------------|---|---|
| 长生命周期计划用版本号 | `PLAN-V001-数字孪生接口治理阶段规划.md` | `数字孪生接口治理阶段规划-26.0417.md` |
| 一次性执行记录用日期 | `TASK-0001-场景视觉整改-26.0417.md` | `TASK-0001-场景视觉整改-V001.md` |

Rules:

- Use `PLAN-V001-{topic}` for the current version of a long-lived plan.
- Store the same version in frontmatter, for example `version: V001` and `plan_id: PLAN-V001`.
- Do not use dates as the primary version marker for long-lived plans.
- Use `yy.MMdd` only for one-time process records or lifecycle retrieval aliases.
- A plan that governs module work should list related modules, execution units, or deliverables.
- A module governed by a plan should link back to that plan when the relationship is defined.

Finding guidance:

- A long-lived plan named with a date instead of a version is P2.
- A module linked to a plan only from the module side, without a management view from the plan side, is P2 when the plan is intended to govern the module.

## Module Structure

Baseline module lifecycle:

```text
20-模块/{module-code}-{module}/
  00-总览/
  10-需求/
  20-设计/
  30-研发/
  40-验收/
  50-发布/
```

When the project has top-level `10-需求`, use module承接 instead of module需求 to avoid mixing business analysis with technical handoff:

```text
20-模块/{module}/
  {module}-模块概览.md
  承接/
    {module}-承接说明.md
  设计/
    {module}-设计说明.md
  开发/
    {module}-开发说明.md
  验收/
    {module}-验收说明.md
  发布/
    {module}-实施发布说明.md
```

`承接` stores module scope, input sources, boundaries, dependencies, constraints, and acceptance口径. It should not become a second business requirement repository.

Module folders should not include permanent:

- `05-协同`
- `10-管理`
- `09-治理`

Module-related changes, reviews, and retrospectives belong in `09-治理`. Temporary work belongs in top-level `05-协同`.

ADR source records belong in `09-治理/20-决策记录`.

## File Naming

| Context | Rule | Example |
| --- | --- | --- |
| Project dashboard | `{project}总览.md` or `{project}-dashboard.md` | `haolabAgents总览.md` |
| Standards | `{topic}规范.md` | `目录规范.md` |
| ADR | `ADR-{number}-{topic}.md` | `ADR-0001-采用目录规范.md` |
| Change request | `CR-{number}-{topic}.md` | `CR-0001-优化模块命名.md` |
| Plan | `PLAN-{number}-{topic}.md` | `PLAN-0001-目录初始化方案.md` |
| Versioned plan | `PLAN-V{nnn}-{topic}.md` | `PLAN-V001-数字孪生接口治理阶段规划.md` |
| Requirement | `REQ-{number}-{topic}.md` | `REQ-0001-发布边界.md` |
| Requirement ledger | `需求台账.md` or `{project}-需求台账.md` | `需求台账.md` |
| Second-level directory MOC | `{directory-name}.md` | `20-场景分析.md` |
| Requirement baseline | `{stage}基线.md` or `{topic}-{yy.MMdd}.md` | `售前基线.md` |
| Evaluation | `EVAL-{number}-{topic}.md` | `EVAL-0001-目录方案评估.md` |
| Module stable file | `{module}-{file-topic}.md` | `bx-module-nav.md` |
| Module evidence file | `{module}-{file-topic}-{yy.MMdd}.md` | `bx-validation-26.0412.md` |
| Attachment | `{module}-{asset-topic}-{yy.MMdd}.{ext}` | `bx-diagram-26.0412.png` |

## Date Rule

Use `yy.MMdd` for one-time evidence, review records, validation samples, and dated artifacts.

Do not add dates to stable entry files, indexes, standards, dashboards, module navigation files, usage files, or living logs.

## Obsidian Metadata

Recommended Markdown frontmatter:

```yaml
---
title: "{title}"
aliases:
  - "{alias}"
tags:
  - "{project}"
  - "{type}"
created: "{date}"
status: draft
type: "{doc_type}"
module: "{module}"
stage: "{stage}"
description: "{description}"
---
```

Rules:

- Use `aliases` for Chinese terms, English short names, module names, and retrieval paths.
- Use topic-centered lifecycle aliases for fast retrieval when the project standard defines them.
- Lifecycle alias format is `{domain}/{object-or-module}/{lifecycle-stage}/{version}-{yy.MMdd}`.
- Recommended lifecycle stages include `规划`, `模块`, `承接`, `设计`, `开发`, `验收`, `发布`, `任务`, `检查`, `问题`, and `决策`.
- Example: `接口治理/场景资源统一接口/规划/V001-26.0417`.
- Example: `接口治理/场景资源统一接口/模块/V001-26.0417`.
- Example: `接口治理/场景资源统一接口/设计/V001-26.0417`.
- Legacy category-prefixed aliases such as `plan//...`, `module//...`, and `interface//...` are weaker retrieval aliases; prefer lifecycle aliases for new or updated files.
- Lifecycle aliases do not replace stable file names, `type`, `tags`, or stable IDs.
- Use `module` only for module-specific files.
- Use `stage` for lifecycle files: requirements, design, development, acceptance, release.
- Keep aliases searchable; avoid aliases that only repeat a verbose title.

## Common Findings

- P1: `default_prompt` or docs reference a nonexistent skill name.
- P1: current rules and historical process are mixed in the same standards file.
- P1: module files are scattered across work-domain folders without a module navigation entry.
- P2: module files lack `{module}` prefixes and cannot be identified outside the directory.
- P2: important terms lack aliases or bilingual/search-friendly names.
- P2: validation evidence lacks dates while stable living files include dates.
- P3: UI display name, title, and role name are inconsistent but behavior still works.
- P2: third-level or deeper directories start with numeric prefixes without being customer raw source folders.
- P3: first-level or second-level numeric prefixes are technically valid but not explained in user-facing docs.
