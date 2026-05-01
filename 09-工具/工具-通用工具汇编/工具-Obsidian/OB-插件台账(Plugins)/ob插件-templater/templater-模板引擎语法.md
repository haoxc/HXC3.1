---
tags: [obsidian, templater, 工具]
description: 在 Templater 的语境中，`<%- ... -%>` 这种语法经常被用作一个**占位符（Placeholder）** 或在用户自定义函数中作为输出标记，
type: note
create-date: 2025-11-17
---

## 概述
在 Templater 的语境中，`<%- ... -%>` 这种语法经常被用作一个**占位符（Placeholder）** 或在用户自定义函数中作为输出标记，它本身并不是一个固定的*内置参数* `{{value}}`。

### Mustache 或 Liquid 模板引擎的语法
`{{value}}` 这种双大括号的语法（称为 "Mustache" 或 "Handlebars" 语法）在许多其他模板系统中非常常见（例如 Jekyll, Hugo, Vue.js, Angular 等），用来表示“在这里插入一个变量的值”。
**Obsidian 的 Templater 插件默认不使用这种双大括号语法。** 如果你想在 Templater 中实现类似的功能，你应该使用：
```
<%= value %> 
```


### 用户自定义的 Templater 函数参数

用户可以在 Templater 设置中创建自己的 JavaScript 用户函数（User Functions）。在这种情况下，`{{value}}` 可能是在该自定义函数的 JavaScript 代码中作为一个参数（或属性）名称被引用。

例如，一个用户自定义的 JavaScript 函数可能定义了一个名为 `value` 的输入参数。
