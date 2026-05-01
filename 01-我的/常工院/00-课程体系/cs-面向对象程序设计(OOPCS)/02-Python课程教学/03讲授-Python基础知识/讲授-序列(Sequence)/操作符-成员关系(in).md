---
type:
  - course
aliases:
  - 成员关系(in)
subject: Python基础
category:
  - python/基础知识/操作
description: 成员关系测试
tags: [工具]
create-date: 2026-04-29
---
### 成员关系(in)
`in` 是一个关键字，主要用于**成员关系测试**，检查某个元素是否存在于一个可迭代对象（如列表、字符串、元组、字典、集合等）中，返回布尔值 `True`（存在）或 `False`（不存在） ### 常用方法

#### 1. **在列表 / 元组中**：检查元素是否存在
```python
lst = [1, 2, 3, 4]
print(2 in lst)    # True（2是列表中的元素）
print(5 in lst)    # False（5不在列表中）

tpl = ("a", "b", "c")
print("b" in tpl)  # True
```
---
#### 2. **在字符串中**：检查子串是否存在
    ```python
    s = "hello world"
    print("llo" in s)  # True（"llo"是s的子串）
    print("xyz" in s)  # False
    ```
---
#### 3. **在字典中**：检查**键（key）** 是否存在（不检查值）

```python
d = {"name": "Alice", "age": 30}
print("name" in d)  # True（"name"是字典的键）
print(30 in d)      # False（30是值，不是键）
```
---
#### 4. **在集合中**：检查元素是否存在（效率比列表高）
```python
s = {10, 20, 30}
print(20 in s)  # True
print(40 in s)  # False
```
---
### 补充：`not in`

与 `in` 相反，`not in` 用于检查元素**不存在**的情况：

```python
lst = [1, 2, 3]
print(4 not in lst)  # True（4不在列表中）
```

`in` 是 Python 中非常实用的关键字，常用于条件判断（如 `if x in list:`），帮助快速判断元素是否存在于容器中。


