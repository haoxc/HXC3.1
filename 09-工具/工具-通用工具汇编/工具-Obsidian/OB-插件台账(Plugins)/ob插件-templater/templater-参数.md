---
titleitled: templater-参数
aliases:
tags:
  - 
created: 2025-11-17 19:16
description:
---

## 内容
Obsidian 的 Templater 插件主要使用**变量（Variables）** 和**函数（Functions）** 来实现动态内容，而非传统编程语言中的“参数传递”概念（除非是用户自定义的 JavaScript 函数）。这些变量和函数通过特定的语法插入到模板中，并在应用模板时被 Templater 引擎解析和替换。 

主要的 Templater 参数（变量和函数）包括：

## 核心语法
Templater 使用 `<% ... %>` 或 `<%= ... %>`（用于输出结果）作为其语法标记。在这些标记内，可以使用内置变量、`tp.` 对象提供的函数以及用户自定义函数。

### 内置变量和函数
Templater 提供了几个主要的 API 对象来访问不同的信息和功能：

- `tp.file` (文件相关)
	- `tp.file.title`：当前笔记的标题。
	- `tp.file.path`：当前笔记的路径。
	- `tp.file.folder(absolute: boolean)`: 返回当前笔记所在的文件夹路径。`absolute` 参数可选，默认为 false（相对路径）。
	- `tp.file.content`：在 Templater 执行时将当前文档内容插入到所在位置。
	- `tp.file.rename(new_title)`: 重命名当前文件。
	- `tp.file.move(new_path)`: 移动当前文件。 

- `tp.date` (日期和时间相关)
    - `tp.date.now(format: string, offset: number, reference_date: string)`：生成当前日期和时间，支持 Moment.js 格式化字符串。例如：
        - `<% tp.date.now("YYYY-MM-DD") %>`
        - `<% tp.date.now("YYYY-MM-DD", 1) %>` (明天) 

`tp.system` (系统交互)
- `tp.system.prompt(prompt_text: string, default_value: string, single_line: boolean)`：弹出一个输入框，要求用户输入一个值。例如：
    - `<% tp.system.prompt("项目名称") %>`
- `tp.system.suggester(display_names: string[], values: string[], multi_select: boolean, prompt_text: string)`：弹出一个选择菜单，让用户从列表中选择一个值。
- `tp.system.clipboard`：获取剪贴板内容。
- `tp.system.exec(command: string)`：执行系统命令并返回输出。 

`tp.frontmatter` (YAML Frontmatter 相关)
- `tp.frontmatter.your_property_name`：获取当前笔记 YAML Frontmatter 中指定属性的值。例如，如果 frontmatter 中有 `type: meeting`，可以使用 `<% tp.frontmatter.type %>`。 

`tp.web` (网络请求)
- `tp.web.get_content(url: string)`：获取指定 URL 的内容。
示例
一个典型的 Templater 模板可能包含以下内容：
markdown
```
---
title: "<% tp.file.title %>"
date: "<% tp.date.now("YYYY-MM-DD") %>"
type: "<% tp.system.prompt("请输入笔记类型", "日常") %>"
---
# <% tp.file.title %>

创建日期: <% tp.date.now("YYYY年MM月DD日 HH:mm") %>

笔记类型: <% tp.frontmatter.type %> 

## 待办事项
- [ ] 任务一
```

请谨慎使用此类代码。

## 注意事项
- Templater 的功能远超核心插件的 Templates 功能，支持 JavaScript 语法，因此你可以编写复杂的逻辑（如循环、条件判断）和用户函数。
- 确保在 Obsidian 设置中为 Templater 指定一个模板文件夹，并且在插入模板时使用 Templater 的命令（例如“Templater: Insert template”）才能正确解析这些动态内容

## 其他
- [[templater-模板引擎语法]]
