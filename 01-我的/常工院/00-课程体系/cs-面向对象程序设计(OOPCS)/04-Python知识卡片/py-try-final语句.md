---
category:
  - 知识点(knPoint)
  -  Python
type: 永久笔记(perNote)
domain: Python文法 (syntax)
topic: 语句(statement)
tags:
  - "#异常处理"
  - "#机制"
aliases:
description:
---
## 概述
- `try-finally` 是一种跨语言的异常处理机制，确保无论代码块是否发生异常，`finally` 中的清理代码都会被执行，从而保障资源安全和程序健壮性;
- `try-finally` 是复合`语句`
- **作用**
	- 保障资源安全和程序健壮性
## 文法
```python
try:
	with open("temp.txt", "w") as f:
		f.write("临时数据")
	raise new 
finally:
	if os.path.exists("temp.txt"):
		os.remove("temp.txt") #清除临时文件
```
## 常见误区

| 误区                    | 正确实践                                            |
| --------------------- | ----------------------------------------------- |
| 忽略 `finally` 中的异常     | 嵌套 `try-except` 捕获并记录日志，避免覆盖主流程错误。              |
| 未处理跨平台路径差异            | 使用 `os.path` 模块处理文件路径，避免硬编码 `/` 或 `\`。          |
| 在 `finally` 中编写复杂业务逻辑 | 仅在 `finally` 中放置清理代码，业务逻辑移至 `try` 或 `except` 块。 |
