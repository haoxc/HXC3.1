---
aliases:
  - 集合(Set)
tags:
  - 序列
type: note
description: -  [集合](https://www.w3cschool.cn/python3/python3-set.html)（set）一种无序、可变的容器，用于存储唯一
create-date: 2026-04-29
---
### 概述
 -  [集合](https://www.w3cschool.cn/python3/python3-set.html)（set）一种无序、可变的容器，用于存储唯一的[[py-不可变|不可变 ]] 元素（元素不可重复）
- 基本功能是进行成员关系测试和删除重复元素。
- 可以使用大括号 `{ } ` 或者 `set() ` 函数创建集合，
- 注意：创建一个空集合必须用 *set()* 而不是 { }，因为 { } 是用来创建一个空字典。

### 定义

#### 非空集合
```python
# 包含整数的集合
num_set = {1, 2, 3, 4, 5}
print(num_set)  # 输出可能为 {1, 2, 3, 4, 5}（顺序不确定）

# 包含字符串的集合
str_set = {"apple", "banana", "cherry"}
print(str_set)  # 输出可能为 {'banana', 'apple', 'cherry'}（顺序不确定）

# 包含混合类型的集合（元素必须是不可变类型）
mix_set = {1, "hello", 3.14, (4, 5)}  # 元组是不可变的，可作为元素
print(mix_set)
```

---
#### 空集合
 ```Python
#空集合定义
emptySet= set()
 ```
> [!ERROR] 易错点
    > - 空集合定义用 `set()` ，**而非** `{}`

---
####  从其他可迭代对象创建集合（去重特性）

通过 `set()` 函数可将列表、元组等可迭代对象转换为集合，自动去除重复元素：

```python
# 从列表创建集合（去重）
list_data = [1, 2, 2, 3, 3, 3]
set_from_list = set(list_data)
print(set_from_list)  # 输出：{1, 2, 3}（重复元素被去除）

# 从字符串创建集合（每个字符作为元素，去重）
str_data = "hello"
set_from_str = set(str_data)
print(set_from_str)  # 输出：{'h', 'e', 'l', 'o'}（重复的'l'只保留一个）
```

### 操作
- **集合操作**
	-  `in`
	- `-`(差集)
	- `|`(并集)
	- `&`(交集)
	- `^`(与或xor)
- **其他操作**
	-  删除(Remove)
		- 集合中没有时,会抛出`异常`KeyError
	- 抛弃(Discard)
		- 集合中没有时,*不会*抛出`异常`KeyError
	- 清除(Clear)
	- 排序(Sort)
		- sorted(setVariable, reverse = True)
	- 去重( Remove Duplicates from a List)
		- list(set([]))

---
### 实践
- [[实践-集合练习]]
