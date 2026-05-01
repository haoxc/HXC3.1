---
tags: [obsidian, 工具]
description: - frontmatter 是文件开头的元数据块，通常位于文件最顶部，用分隔符（如 `---`）包裹，用于存储文件的额外信息。
type: note
create-date: 2026-01-26
---

- frontmatter 是文件开头的元数据块，通常位于文件最顶部，用分隔符（如 `---`）包裹，用于存储文件的额外信息。
- 在 Obsidian 等工具中，frontmatter 常用来定义文件的属性，比如别名（alias）、标签（tags）、分类（categories）等。以示例中的内容为例：

**示例**：
```plaintext
---
alias: myfile
note type: seedling
categories:
- book
- movie
---
```

这里的 `alias`、`note type`、`categories` 都是 frontmatter 变量，可通过 Templater 等工具的 `tp.frontmatter` 模块访问和使用这些变量，方便在模板中动态调用文件的元数据。

如果变量名包含空格，可使用方括号语法访问，如 `tp.frontmatter["note type"]`；对于列表类变量（如 `categories`），还能借助 JavaScript 数组方法进行处理和展示。



## 应用
笔记中定义多级分类，通过模板自动生成导航链接
```yaml
---
category: ["编程", "JavaScript"]
tags: ["ES6", "异步编程"]
---
```
**
