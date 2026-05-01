---
category:
  - Python 知识点
type: 永久笔记 (perNote)
domain: Python 文法 (syntax)
topic: 语句(statement)
tags:
aliases:
  - 条件语句(Conditional Statement)
  - 分支
  - 条件语句
description:
create-date: 2026-04-29
---
## 概述

---
## 基本语法

---
## 应用场景

---
## 总结归纳

> 注意事项



### 意图
![[Pasted image 20220428114706.png|400]]
- Python条件语句是通过一条或多条语句的执行结果（​`True`​或者​`False`​）来决定执行的代码块。
- 可以通过下图来简单了解条件语句的执行过程:

### 文法 
![[Pasted image 20220504122949.png]]

---
**注意：**
-   1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
-   2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
-   3、在 Python 中没有 switch – case 语句，但在python3.10中添加了用法类似的[[讲授-分支语句(match-case)]]。
---
**示例**：

```Python
a = 200  
b = 33  
if b > a:  
  print("b is greater than a")  
elif a == b:  
  print("a and b are equal")  
else:  
  print("a is greater than b")
```

### 速记(Short Hand)
```Python
#单行语句
if a>b: print("a 大于 b")
```
## 逻辑操作
 且: `and`
 或: `or` 
 非: `not`
 空操作: `pass`


 `
