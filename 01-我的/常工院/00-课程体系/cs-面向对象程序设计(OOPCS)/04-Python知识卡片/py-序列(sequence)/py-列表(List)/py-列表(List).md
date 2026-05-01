---
aliases:
  - 序列/列表(List)
category:
  - 序列
tags:
  - 序列
type: note
description: - [列表](https://www.w3cschool.cn/python3/python3-list.html)可以完成大多数集合类的数据结构实现。
create-date: 2026-04-29
---
### 列表(List)
- [列表](https://www.w3cschool.cn/python3/python3-list.html)可以完成大多数集合类的数据结构实现。
- 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓*嵌套*）。
列表是写在方括号 \[\] 之间、用`逗号`分隔开的元素列表。
- 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
![[Pasted image 20220405182508.png|600]]

---
> `ris:CheckboxMultiple`  **思考** 操作符和string操作符是否一致?
>
> - [!Important]
> - Python 中最常用的**可变序列类型**，具有**有序、可修改、元素可重复**的特点，支持添加、删除、修改等操作，元素可以是任意数据类型（包括列表自身，即嵌套列表）
    
---
### 操作
- **基本操作**
	- 创建： `[]`或 list（）；
	- 访问/修改元素 ：
		- 索引： `[index]`
		- 切片（范围）： `1:3`
	- 添加元素(append/extend/insert)
	- 删除元素（del/pop/remove)
	- 
- **进阶操作**
	- 排序(sort) : 对元素内容升序或降序排列
	- 反转(reverse): 原地反转列表
	- 统计(count(x)) : python 统计元素x出现的次数
	  列表推导式
---
### 实践
- [[实践-列表练习]]
---
### 总结
列表的核心特性是**有序、可变、可重复**，常用操作包括：

- 创建：`[]` 或 `list()`；
- 访问 / 修改：索引、切片；
- 增删：`append()`/`extend()`/`insert()`、`del`/`pop()`/`remove()`；
- 进阶：排序（`sort()`）、反转（`reverse()`）、列表推导式。

列表是 Python 中最灵活的数据结构之一，适合存储需要动态修改的序列数据，多练习推导式和嵌套列表能显著提升编码效率