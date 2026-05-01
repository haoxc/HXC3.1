---
tags: [obsidian, templater, 工具]
description: - Template(内置）
type: note
create-date: 2025-11-17
---

## 要点
- Template(内置）
	- 准备
		- 安装
	- 应用
		- 设计属性（Properties，元数据）
			- [[ob-属性]]
		- 创建模板
			- 创建笔记 并插入模板（ template: insert a template)
- Templater
	- 能力
		- [[#控制能力]]
---
## 控制能力
### 文件控制
**文件标题**：<% tp.file.title %>
**文件时间**： <% tp.file.creation_date() %>
**光标位置**： <%tp.file.cursor%>
### 日期控制
**当前时间**： tp.date.now("YYYY-MM-DD")
### 系统信息
**输入文本**： tp.system.prompt
**选择项**： tp.system.suggester 

## 示例

控制
[[176e3f5415ff3c070da036a4db33efa8_MD5.jpg|Open: Pasted image 20251026114703.png]]
![[176e3f5415ff3c070da036a4db33efa8_MD5.jpg]]
