---
aliases:
  - abbr://Python知识点/解包(jb-kw)
  - 解包赋值（Unpacking Assignment）
  - '"python/符号/**"'
category:
  - Python 知识点
type: 永久笔记 (perNote)
domain: Python 文法 (syntax)
topic:
tags:
  - 解包
scenario:
  - 多变量赋值
  - 函数返回多值
description:
create-date: 2026-04-29
---
## 概述
- **定义描述**:  **解包赋值（Unpacking Assignment）** 是一种简洁的赋值方式，允许将**可迭代对象**（如列表、元组、字符串、字典等）中的元素 “拆分” 后，一次性赋值给多个变量。
- **核心作用**:是简化多变量赋值流程，让代码更简洁直观。

---
## 知识要点
### 基本解包：列表 / 元组的元素拆分
最常见的解包场景是对`列表`或`元组`进行操作，变量数量与可迭代对象的元素数量需一致。
####  示例 1：元组解包
```python
# 定义一个元组
person = ("Alice", 25, "female")

# 解包赋值：将元组的3个元素分别赋值给3个变量
name, age, gender = person

print(name)   # 输出：Alice
print(age)    # 输出：25
print(gender) # 输出：female
```

 ---
#### 示例 2：列表解包
```python
# 定义一个列表
scores = [90, 85, 95]

# 解包赋值给3个变量
math, english, chinese = scores

print(math)    # 输出：90
print(english) # 输出：85
```

#### 示例 3：字符串解包（字符串是字符的可迭代对象）

```python
s = "abc"

# 每个字符被解包给一个变量
#a, b  = s # 系统会抛出错误 ValueError
a, b, c = s


print(a) # 输出：a
print(b) # 输出：b
```

>  🚨 **解包后变量数量要与元素数量一致**

---
### 星号表达式（`*`）：处理数量不匹配的情况
当变量数量与可迭代对象的元素数量**不一致**时，可使用 `*` 修饰一个变量，让它接收 “多余” 的元素（会被打包成一个列表）。
#### 场景 1：变量少于元素（用`*`接收剩余元素）
```python
numbers = [1, 2, 3, 4, 5]

# 第一个变量接收1，*middle接收中间的2、3、4，last接收5
first, *middle, last = numbers

print(first)  # 输出：1
print(middle) # 输出：[2, 3, 4]（列表类型）
print(last)   # 输出：5
```

#### 场景 2：变量多于元素（需配合`*`接收空列表）
```python
# 只有2个元素，但要赋值给3个变量
info = ["Bob", 30]

# *others接收空列表（因没有多余元素）
name, age, *others = info

print(name)   # 输出：Bob
print(age)    # 输出：30
print(others) # 输出：[]
```

> [!WARNING] 📢 **注意**：
> - 一个解包表达式中**只能有一个带`*`的变量**（否则报错）。
> - `*` 修饰的变量**必须放在可迭代对象的 “连续元素” 位置**（不能单独存在）
---

---
### 字典的解包
字典的解包有两种方式，分别针对 “键” 和 “键值对”：
#### 场景1. 用 `*` 解包字典的 “键”

```python
user = {"name": "Charlie", "age": 28, "city": "Beijing"}

# * 解包字典的键，赋值给变量
key1, key2, key3 = user  # 等价于 *user 解包键
print(key1, key2, key3)  # 输出：name age city（字典键的顺序在Python 3.7+中与插入顺序一致）
```

---
#### 场景2. 用 `**` 解包字典的 “键值对”（主要用于函数参数）

`**` 会将字典的键值对解包为 “关键字参数”，常用于*函数调用时传递参数*：

```python
def introduce(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

user = {"name": "David", "age": 32, "city": "Shanghai" , "school":"czu"}

# **解包字典，将键值对作为关键字参数传入函数
introduce(** user)  # 等价于 introduce(name="David", age=32, city="Shanghai")
# 输出：姓名：David，年龄：32，城市：Shanghai
```


## 应用场景

 1. **交换变量的值**（无需临时变量）：
    ```python
    a, b = 10, 20
    a, b = b, a  # 解包赋值实现交换
    print(a, b)  # 输出：20 10
    ```
    
2. **处理函数返回的多个值**（函数返回元组时，直接解包给变量）：
    ```python
    def get_user():
        return ("Eve", 27)  # 返回一个元组
    
    # 直接解包函数返回值
    username, user_age = get_user()
    print(username, user_age)  # 输出：Eve 27
    ```
    
3. **遍历可迭代对象时拆分元素**（如遍历元组列表）：
    
    ```python
    students = [("张三", 90), ("李四", 88), ("王五", 95)]
    
    # 遍历的同时解包每个元组
    for name, score in students:
        print(f"{name}的成绩：{score}")
    ```

## 总结
解包赋值是 Python 的特色语法之一，核心优势是**简化多变量赋值**，尤其在处理可迭代对象（列表、元组、字典等）时能大幅提升代码简洁度和可读性。掌握`*`和`**`的用法，能应对绝大多数复杂的解包场景。