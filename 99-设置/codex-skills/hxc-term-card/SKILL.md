---
name: hxc-term-card
description: Create or update Obsidian terminology cards in the Vault knowledge layer. Use when the user asks to create term, create a 术语卡片, 知识术语笔记, concept/term card, 快速理解术语, 写入术语库, or normalize terminology notes. Routes general terms to 03-领域/00-概念术语, discipline terms to the matching field terminology directory, keeps temporary topic terms in workspace only until they flow back to 03-领域, and enforces type: note plus retrieval-oriented aliases.
type: note
tags: [工具]
create-date: 2026-04-25
---
# HXC Term Card

## Purpose

Create fast-understanding terminology cards for the Vault knowledge layer. Stable terminology belongs under `03-领域/`, not under the temporary workspace.

This skill is for stable knowledge cards, not broad topic surveys. If the user asks for a multi-source technical landscape or decision-oriented research report, use `hxc-topic-svy`. If the user asks only to compare multiple terms without creating a term card, use `bx`.

## Style

- Write in Chinese unless the user asks otherwise.
- Use a calm, expert, Claude-like tone: precise, direct, low-noise, and readable.
- Avoid greetings, AI self-reference, generic background, and encyclopedic padding.
- Keep every core term bilingual on first mention: `中文术语 (English Term)`.
- Prefer established English terms. If the user's Chinese term is inaccurate or ambiguous, state the risk first, give better Chinese-English alternatives, and confirm the chosen label before writing a file when the ambiguity would affect the card title or meaning.

## Vault Rules

Workflow authority:
- This section defines where the term card lives, how it should be named, and how the MOC must be maintained.
- If there is any ambiguity about folder choice, naming, or whether the MOC must be updated, this section takes precedence.

Terminology routing:

| Term type | Target |
| --- | --- |
| 通用术语 | `03-领域/00-概念术语/` |
| 通用术语卡片默认目录 | `03-领域/00-概念术语/01-一般术语知识库(Common DB)/` |
| 学科术语 | 对应领域下的现有术语目录，如 `03-领域/31-人工智能学科/00-AI术语/` |
| 课题中的临时术语表 | 可暂存在 workspace；课题完成后必须回流到 `03-领域/` |

When a user gives a preferred discipline terminology directory, use that directory if it exists. If the requested directory would create a duplicate terminology library beside an existing one, report the conflict and ask before creating it.

When creating a card:

1. Put the note under the most relevant existing terminology folder in `03-领域/`. If no better folder is clear, use the general term-card folder.
2. Name the file as `中文术语(English Term).md` when the English term is stable. For ambiguous English, use the confirmed Chinese title and include alternatives in the body.
3. Always include minimal YAML frontmatter in the generated term card. `aliases` is required.
4. Use `type: note`. Do not use `type: 术语卡片` because Vault type is an enum.
5. Do not put an alias that is identical to the full displayed title, such as `术语解析：中文术语 (English Term)`. Aliases should serve search and alternate lookup.
6. Add or update one Obsidian wiki link in the target folder's MOC. Wikilink aliases are allowed only for disambiguation or grammar, not display beautification.
7. Preserve existing MOC content and avoid duplicate links.

## Output Structure

Structure authority:
- This section defines the required internal structure of the term card artifact.
- It does not decide where the file should be placed. Placement and MOC maintenance are governed by `Vault Rules`.

Generated term cards must start with minimal frontmatter and then use exactly this main structure:

```markdown
---
aliases:
  - 中文术语
  - English Term
tags:
  - 术语
description:
type: note
---

# 术语解析：中文术语 (English Term)

> [!IMPORTANT] 快速理解
> 用一句话说明这个术语最值得记住的本质。

## 1. 概念界定 (Concept Definition)

...

## 2. 替代范式 (Alternative Paradigms)

...

## 3. 边界辨析 (Boundary Analysis)

...

> [!IMPORTANT] 实践指南
>
> ...
```

Do not omit frontmatter. Keep it minimal, especially `aliases`. Avoid bloated metadata, opening prefaces, source dumps, or generic conclusion sections unless the user asks.

Alias rule:

- prefer short retrieval aliases such as Chinese term, English term, common abbreviation, or an alternate accepted translation;
- include a necessary retrieval path alias only when it improves search, such as `AI/模型/扩散模型(DM, Diffusion Model)`;
- do not repeat the full note title as an alias.
- do not use Wikilink aliases for beautification; `[[目标标题|显示文本]]` is only for disambiguation or grammar.

## Section Requirements

### 1. 概念界定 (Concept Definition)

Explain the essence and underlying logic:

- what the term means;
- what problem it helps name;
- its core mechanism or judgment standard;
- why it matters for understanding or practice.

### 2. 替代范式 (Alternative Paradigms)

List adjacent concepts, alternate framings, or thinking models. This section should help the user choose better words, not merely list synonyms.

Good patterns:

- `术语 A (English A)`: use when ...
- `术语 B (English B)`: use when ...
- `术语 C (English C)`: use when ...

### 3. 边界辨析 (Boundary Analysis)

Use a compact comparison table when there are 2 or more confusable terms.

Default columns:

`维度 | 本术语 | 相近术语 A | 相近术语 B`

Prioritize:

- core purpose;
- abstraction level;
- operating object;
- output/result;
- common misuse;
- teaching or project-management implication.

### 4. 实践指南 (Practice Guide)

Use an Obsidian callout, normally `[!IMPORTANT] 实践指南`.

Include:

- 2-4 actionable usage rules;
- one strong analogy or metaphor;
- a short example sentence or scenario;
- when not to use the term.

## Quality Bar

A good card should let the user answer within one minute:

- What exactly does this term mean?
- What does it help me distinguish?
- What should I call it instead in a different context?
- Where is the boundary of use?
- How can I explain it to a student, colleague, or future self?

Remove anything that does not serve those questions.

## File-Editing Workflow

Execution authority:
- This section defines the required editing workflow when the user asks to write the card into the Vault.
- Do not stop after drafting the card body; the workflow includes duplicate check, file creation, MOC update, and verification.

When the user asks to write the card into the Vault:

1. Inspect the term-library root and MOC entry before editing.
2. Classify the term as general, discipline-specific, or temporary topic terminology.
3. Inspect the target terminology folder and MOC entry before editing.
4. Check whether the term or close aliases already exist.
5. Create or update the card with the required structure.
6. Update the MOC entry with a relative wiki link.
7. Verify with `rg` that the card exists and the MOC links to it.

## Completion Rule

Completion authority:
- A term-card task is complete only when the card file exists, the MOC entry has been updated or confirmed, and the final `rg` verification passes.
- A drafted card body without Vault integration is still in progress.

Completion for Vault-written term cards means:

1. card file written in the correct folder;
2. frontmatter exists and `aliases` is populated without repeating the full note title;
3. title and body follow the required structure;
4. MOC entry updated or confirmed without duplication;
5. `rg` verification confirms both file existence and MOC linkage.

## Verification Integration

Verification authority:
- `rg` is the executable check layer for this skill.
- Use it to confirm that the card exists and that the MOC points to the card before finishing.

Default verification intent:

- confirm the new or updated card file exists under `03-领域/`;
- confirm the MOC contains a wiki link to the card;
- confirm no duplicate entry was introduced.
