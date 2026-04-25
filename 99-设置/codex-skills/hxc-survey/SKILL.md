---
name: hxc-survey
description: Create, revise, or audit concise professional research reports in the user's Vault. Use when the user asks for hxc-survey, 调研报告, 快速调研, 课题调研, survey, research report, based on ref-url, 基于链接/资料建立调研, 结论先行, 快速理解, or wants to upgrade a memo into a professional but non-bloated report. Produces conclusion-first Claude-style Chinese reports with evidence chains, comparison, boundaries/risks, project recommendations, one chart suggestion, and a final Obsidian callout summary.
---

# HXC Survey

## Purpose

Create fast-understanding but professionally defensible research reports.

Use this skill when the user wants a report that is:

- conclusion-first;
- concise and readable;
- based on URLs, `ref-url`, existing notes, papers, docs, repositories, or user-provided materials;
- useful for decision-making, not just information collection;
- suitable for Obsidian / Markdown knowledge work.

Relation to `hxc-topic-svy`: `hxc-topic-svy` is the older quick topic overview pattern. Prefer `hxc-survey` when the user expects a stronger report with explicit evidence, comparison, risk boundaries, and auditability.

## Style Rules

- Default to Chinese unless the user asks otherwise.
- Write like a calm expert: direct, logical, low-noise, not promotional.
- Start with the judgment. Do not begin with background exposition.
- Avoid information overload: include only what changes understanding or decision-making.
- Avoid empty claims. Every important judgment should have a reason, evidence, or boundary.
- Use `中文术语 (English Term)` for important technical concepts on first mention when the English term is useful.
- Do not overuse visual emphasis. One callout should carry the first-screen conclusion; one final callout should carry the last takeaway.
- Keep vertical spacing tight in the first-screen conclusion. Prefer one callout with compact bullets over scattered paragraphs and large code blocks.
- Use compact warning callouts for misconceptions or adoption risks, such as `[!WARNING] 常见误区`; do not leave important risk notes as ordinary paragraphs.
- Avoid horizontal rules between every section. They create excessive vertical spacing in Obsidian. Use headings and short paragraphs as the main rhythm.

## Source Rules

When the topic includes URLs, `ref-url`, modern technical objects, GitHub repositories, product docs, framework docs, laws, current tools, or recent ecosystem claims:

1. Browse or inspect the referenced source.
2. Prefer primary sources: official docs, GitHub repositories, papers, standards, company engineering posts.
3. Use secondary sources only when they add interpretation, adoption context, or comparison.
4. Separate facts from inference. If a conclusion is inferred from repository shape, docs, or missing runtime features, say so.
5. Include source links in YAML `ref-url` and/or a `## 来源` section.

Do not pretend a repository is a runtime framework unless it contains actual runtime components such as scheduler, state management, task queue, tool execution layer, context transfer protocol, logs, or evaluation loops.

## Default File Rules

When writing into the Vault:

- Use filename: `调研-{主题}-{yy.MMDD}.md`.
- If revising a user-adjusted variant, preserve the user's clearer phrasing and structural decisions.
- Use Obsidian-friendly Markdown.
- Always include frontmatter for generated notes written into the Vault. `aliases` is required.
- Use compact YAML. Do not leave `aliases` empty unless the user explicitly requests no aliases.
- Do not put the full displayed note title into `aliases`. Aliases should be retrieval-oriented, not a duplicate title field.

Default frontmatter:

```yaml
---
aliases:
  - 调研-{主题}
tags: [调研]
description:
type: 调研报告
ref-url:
create-date: YYYY-MM-DD HH:mm
hxc-ref: template
---
```

## Orchestrated Survey Workflow

Workflow authority:
- This section defines the mandatory bundle workflow for formal Vault surveys.
- If there is any ambiguity about whether a standalone summary or MOC entry is required, this section takes precedence.

When the user asks to write a formal survey into the Vault, you MUST treat the deliverable as a small bundle rather than a single file.

Required steps:

1. Create the main report.
2. Create a standalone summary note.
3. Add a link from the main report to the summary note.
4. Add a backlink from the summary note to the main report.
5. Add at least one MOC or management entry that points to the report or summary.
6. Validate the bundle before finishing.

This is the default for formal surveys written to the Vault. Do not stop after writing only the main report unless the user explicitly says not to create a summary note or not to update a MOC.

The required minimal bundle is:

```text
主报告
  -> 独立摘要
  -> MOC / 管理入口
  -> 校验
```

Use the bundled validator when file paths are clear:

```bash
scripts/validate_survey_bundle.sh --report <report.md> --summary <summary.md> --moc <moc.md> --require-summary --require-moc
```

The only normal exception is a tiny draft or scratch note that is not intended to become a formal report artifact.

Before finishing, explicitly confirm these four conditions:

- report exists;
- summary exists;
- report and summary are linked both ways;
- a MOC or management page links the bundle.

## Report Structure

Structure authority:
- This section defines what the main report must contain.
- It does not replace the bundle workflow. It only defines the internal shape of the main report artifact.

Use this structure by default:

```markdown
# 调研-{主题}-{yy.MMDD}

## 调研摘要

> [!abstract] 调研摘要
> 用 2-3 段说明对象的本质图景：它是什么、解决什么问题、核心机制是什么、为什么值得看。
>
> 摘要负责帮助读者看清本质，不负责展开证据和行动建议。

## 调研结论

> [!IMPORTANT] 调研结论
> - ...
> - ...
> - ...
>
> **结论依据**：说明基于哪些核心来源、对比对象、分析维度得出判断。

## 课题判断

- **课题类型**：
- **调研目标**：
- **核心判断**：

## 核心定位

...

## 核心思想

先说明 2-4 条核心思想之间的递进关系，再展开。

## 技术框架 / 分析框架

...

## 可借鉴价值

...

## 使用边界与误用风险

...

## 对本项目的建议

...

## 图表建议

- **图表类型**：
- **适用原因**：
- **图中建议表达的关键维度**：

## 来源

- ...

> [!summary] 一句话总结
> ...
```

If a section does not fit the topic, rename it rather than forcing irrelevant content. Keep the same logic: abstract -> conclusion -> evidence -> analysis -> comparison -> boundary -> action.

## Completion Rule

Completion authority:
- This section decides whether the survey task is complete.
- A well-written main report is still not complete if the bundle workflow has not been finished.

Do not consider a formal survey task complete until the bundle workflow has finished.

Completion for Vault-written surveys means:

1. main report written;
2. standalone summary written;
3. MOC or management entry updated;
4. bundle validator run successfully.

If any of the four items is missing, the task is still in progress.

## Abstract Rules

Summary-note authority:
- This section defines when and how `调研摘要` should be used in the main report.
- It also defines the required structure of a standalone summary note.

Use `## 调研摘要` when the report needs to help the reader see the object's essence before the judgment details.

The abstract should answer:

1. What is this object in one precise framing?
2. What problem does it solve or expose?
3. What is the core mechanism, pattern, or paradigm?
4. Why does it matter for the user's knowledge work or project work?

Preferred shape:

```markdown
> [!abstract] 调研摘要
> A 可以理解为一种 ...：它不是 ...，而是 ...
>
> 它的价值不在于 ...，而在于 ...
>
> 从本项目视角看，最值得借鉴的不是 ...，而是 ...
```

Do not make the abstract sound more certain than the evidence allows. Use cautious wording such as "可以理解为", "更像是", "可视为" when the source is a repository, prompt collection, or early-stage framework rather than a mature product.

For standalone abstract notes, keep section headers Chinese-only for cleaner scanning. Preserve bilingual Chinese-English terms in body text on first mention, but avoid headings such as `核心设计哲学 (Core Design Philosophy)`.

Difference from conclusion:

- `调研摘要`: gives the essence and mental model.
- `调研结论`: gives the report's judgment, evidence basis, boundary, and action implication.

For a standalone summary note:

- include frontmatter, and make sure `aliases` is populated;
- do not repeat the full summary title in `aliases`;
- keep headers Chinese-only for quick scanning;
- preserve bilingual terms in body text on first mention;
- include a `## 关联报告` section with a backlink to the main report;
- end with a one-sentence `[!summary]` callout.

## First-Screen Conclusion Rules

The first-screen conclusion must answer:

1. What is the object really?
2. What is it not?
3. What is worth learning or using?
4. What is the implication for this project?
5. What evidence supports this conclusion?

Preferred shape:

```markdown
> [!IMPORTANT] 调研结论
> - A 的核心价值不在于 X，而在于 Y。
> - 它更像 ...，不是 ...。真正值得学习的是 ...
> - 对本项目而言，启发不是照搬，而是提炼 ...
>
> **结论依据**：基于 ...，并与 ... 横向对比；分析维度包括 ...
```

Avoid:

- a large red-box style warning tone;
- long separate paragraphs before the reader sees the judgment;
- code blocks in the first conclusion unless the diagram is essential;
- multiple highlighted phrases fighting for attention.
- turning ordinary explanatory paragraphs into oversized callouts.

Use a compact warning callout when the point is a misconception:

```markdown
> [!WARNING] 常见误区
> 不要把 A 理解成 B。真正关键的是 C；一旦 C 不稳定，结果会出现 D。
```

## Validator Integration

Validator authority:
- The validator is the executable enforcement layer for the bundle workflow.
- Use it to verify report existence, summary existence, cross-links, and MOC coverage before considering the task finished.

Default command:

```bash
scripts/validate_survey_bundle.sh --report <report.md> --summary <summary.md> --moc <moc.md> --require-summary --require-moc
```

Interpretation rule:

- `SKILL.md` defines the workflow and completion contract.
- `scripts/validate_survey_bundle.sh` checks whether the bundle actually satisfies that contract.

## Evidence Chain Requirement

For professional reports, include at least one compact evidence table when the report makes classification or boundary claims.

Example:

```markdown
| 判断 | 依据 | 含义 |
| --- | --- | --- |
| 不是 runtime | 仓库主要是 Markdown agent 定义，未见调度器、状态机、任务队列 | 不能直接当可运行平台 |
| 是角色资产库 | README 和 agent 文件围绕身份、流程、交付标准展开 | 适合作为 skill/agent 设计参考 |
```

Use evidence tables especially for:

- “不是 X，而是 Y”;
- “不适合直接部署”;
- “更像参考资产”;
- “适合本项目借鉴”;
- “需要补充某能力层”。

## Comparison Requirement

When the report mentions related frameworks, tools, or methods, include a minimum comparison table.

Default columns:

`对象 | 本质 | 适合解决什么 | 不适合什么`

This prevents vague name-dropping and makes positioning clearer.

## Boundary And Risk Rules

Always include boundaries when the report may influence adoption or implementation.

Good boundary prompts:

- What will fail if users over-adopt this?
- What is missing for production use?
- When does the missing layer become a real problem?
- What should not be copied?
- What requires governance, versioning, or quality checks?

For tooling / agent reports, explicitly check:

- runtime;
- state management;
- task queue;
- context transfer;
- tool permissions;
- logs and audit;
- evaluation and retry.

## Project Recommendation Rules

Recommendations should be prioritized, not just listed.

Use a table when useful:

```markdown
| 优先级 | 建议项 | 解决的问题 | 关键产物 |
| --- | --- | --- | --- |
| 高 | ... | ... | ... |
```

Include a short priority logic:

- frequency;
- stability of output format;
- ability to define quality standards;
- impact on downstream work;
- cost or risk of over-building.

Default decision rule:

> Only convert a task into a skill/agent when it recurs, has stable deliverables, and has describable quality standards.

## Chart Recommendation Rule

Always recommend exactly one chart type for technical or method reports.

Choose one:

- `分层架构图`: when the topic is about layers, capability boundaries, or missing runtime components.
- `判断-证据矩阵`: when the report's main job is proving a classification.
- `对象对比表`: when choosing among tools/frameworks.
- `流程闭环图`: when the topic is about workflow, feedback, or quality loops.
- `能力-场景矩阵`: when matching capabilities to use cases.

Do not recommend multiple chart types by default.

## Audit Mode

If the user asks to audit, review, evaluate, or score a report, use these dimensions:

- 问题界定;
- 证据支撑;
- 分析深度;
- 结构可读性;
- 决策价值;
- 边界与风险.

Default output:

1. Overall judgment.
2. Radar chart or score table if requested.
3. Strengths.
4. Main issues.
5. Specific revision suggestions.
6. Final `[!summary]` callout.

For radar charts, create a local SVG when the user asks for a visible chart and embed it in the audit note.

## Quality Bar

A good `hxc-survey` report should satisfy:

- The first screen gives a real judgment.
- The conclusion has explicit basis.
- Important claims are tied to evidence.
- Related objects are compared, not merely mentioned.
- Boundaries and risks are visible.
- Recommendations are prioritized.
- The report is concise enough to read, but not so compressed that it becomes empty.
- The final callout states the core takeaway in one sentence.
