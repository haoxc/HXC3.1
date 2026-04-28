---
name: moc-wiki-designer
description: Design, refactor, or audit Obsidian MOC/Wiki index pages as lightweight directory-tree navigation pages. Use when the user asks to create or adjust MOC, Wiki, index, navigation, folder note, directory map, content map, or knowledge-base overview pages, especially when they say "wiki形式", "MOC", "目录树", "索引页", "不要塞具体内容", "只放链接", or "拆成独立笔记".
---

# MOC / Wiki Designer

## Purpose

Keep MOC / Wiki pages as maps, not articles.

Use this skill when editing knowledge-base navigation pages, folder notes, MOC pages, overview pages, or tool/topic index pages. The output should help the reader navigate to notes, not consume long content on the index page itself.

## Core Rule

MOC / Wiki pages should contain:

- hierarchical bullet trees;
- Wiki links;
- short category labels;
- very short plain labels when a node is conceptual rather than a note.

MOC / Wiki pages should not contain:

- long explanations;
- configuration details;
- command blocks;
- long tables;
- full workflows;
- complete memo content;
- implementation notes that belong in a child note.

Memory phrase:

> A MOC / Wiki page is a map, not the territory.

## Default Shape

Prefer this structure:

```markdown
- 理念
	- 诚实(Honest)
	- 无害(Harmless)
	- 有用(Helpful)
- 亮点
	- Artifacts
	- 长上下文(Long Context window)
	- [[思维画布(Thinking Canvas)]]
- 学习规划
	- [[学习实战]]
	- [[claude-学习路径]]
- 实践
	- 准备
		- [[claude-安装]]
	- 指南
		- [[claude-code-使用备忘录]]
	- 工具
		- [[claude工具-切换模型-cc-switch]]
```

Use tabs or the existing file's indentation style for nested bullets. Preserve the user's established naming style, including Chinese-English mixed note names.

## Refactoring Workflow

1. Identify whether the target page is a MOC/Wiki/index page.
2. Preserve meaningful frontmatter.
3. Move long content into a new child note when needed.
4. Replace long content on the MOC page with one Wiki link.
5. Keep the MOC page as a compact bullet tree.
6. Verify that the MOC page contains no long prose blocks, command blocks, or large tables.

## When To Split Content

Create or update a child note when content is:

- a usage memo;
- a configuration guide;
- an operating procedure;
- a troubleshooting note;
- a concept definition;
- a comparison table;
- a full checklist;
- anything likely to be reused or maintained independently.

Recommended child note names:

| Content type | Naming pattern |
| --- | --- |
| 使用备忘录 | `xxx-使用备忘录.md` |
| 配置说明 | `xxx-配置.md` |
| 操作流程 | `xxx-操作流程.md` |
| 问题排查 | `xxx-问题排查.md` |
| 概念定义 | `xxx.md` or term-library note |
| 对比分析 | `xxx-对比.md` |

## MOC Page Quality Check

Before finishing, check:

- Does the MOC page read like a directory tree?
- Are concrete details moved into child notes?
- Are all child notes linked from the MOC page?
- Does each link label make the destination obvious?
- Did you avoid command blocks and long paragraphs in the MOC page?

## Response Guidance

When reporting completion, mention:

- the MOC/Wiki page kept as an index;
- any child notes created or updated;
- that concrete content was moved out of the index page.

