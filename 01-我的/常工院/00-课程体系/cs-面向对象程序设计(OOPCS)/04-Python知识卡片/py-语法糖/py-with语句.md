---
category:
  - 永久笔记 (perNote)
  - 知识点(knPoint)
  - "#方法"
domain: 文法(syntax)
topic: oop(python)
tags:
  - 上下文管理器
  - 资源
aliases:
type: note
description: - 一种[[py-语法糖]]：[[py-try-final语句]]**资源**管理使用和释放的便捷方式。
create-date: 2026-04-29
---
## 概述
- 一种[[py-语法糖]]：[[py-try-final语句]]**资源**管理使用和释放的便捷方式。
- **作用**： 
	- with 语句的核心是“上下文管理器协议”实现资源自动化适当
---
## 价值 
- 简化代码 ： 无须手动编写 try-finally 语句释放资源
- 安全可靠： 确保资源释放
- 可读性强： 明确资源使用范围，代码逻辑更清晰。