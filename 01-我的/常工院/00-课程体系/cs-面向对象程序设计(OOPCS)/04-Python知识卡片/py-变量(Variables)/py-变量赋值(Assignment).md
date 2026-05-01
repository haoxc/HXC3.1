---
category:
  - 永久笔记 (perNote)
  - 知识点 (knPoint)
domain: Python 文法 (syntax)
topic: 语句 (statement)
tags:
aliases:
  - 变量赋值(Assignment)
description:
type: 知识点(knlowledge point)
create-date: 2026-04-29
---
## 概述
在python中,定义变量, 同时给变量一个初始值.

`类型操作`
- 变量赋值(Assignment)
- *理解*
	- Python 中的*变量不需要声明*。每个变量在*使用前都必须赋值*，变量赋值以后该变量才会被创建。
	- 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量*所指的内存中对象的类型*。
	- 等号（=）用来给*变量赋值*。
	- 等号（=）运算符左边是一个==变量名==,等号（=）运算符右边是==存储在变量中的值==.
	- 用户
		- ![[Pasted image 20220425162223.png|500]]
- *示例*
	- 简单赋值
		- counter =100
	- 多个变量赋值 (Multiple assignment)
		- a=b=c =1
		- a, b, c = 1, 2, "john"
		- 对象
			- ![[Pasted image 20220425162512.png]]
		- 对象
			- ![[Pasted image 20220425162552.png]]
			- ![[Pasted image 20220425162528.png]]
			- ![[Pasted image 20220425162537.png]]
- 删除对象
- *文法*:  **del** `variableName`