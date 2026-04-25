---
aliases:
  - 布尔类型(bool)
---
### 布尔类型要点
- **定义**： `bool`（布尔）类型是一种基础数据类型，专门用于表示 “真”（`True`）或 “假”（`False`）两种状态，主要用于*逻辑判断*和*条件控制*。
- **取值**： `True` ,`False`
- **转换**： `bool()`
- **运算**： [[py-逻辑表达式]]
---
### 取值
`bool`类型只有两个取值：
- `True`：表示 “真”（逻辑上的成立）
- `False`：表示 “假”（逻辑上的不成立）

> [!WARNING]
    > **注意**：`True`和`False`的首字母必须大写（Python 大小写敏感），小写的`true`或`false`会被视为未定义的变量，导致报错。
    
---
### 转换（其他类型转布尔值）
Python 中，所有数据类型都可以通过`bool()`函数转换为布尔值，转换规则如下：

- **视为`False`的情况**（“空” 或 “零”）：
    - 数值：`0`、`0.0`、`0j`（复数零）
    - 空字符串：`""` 或 `''`
    - 空容器：`[]`（空列表）、`()`（空元组）、`{}`（空字典）、`set()`（空集合）
    - 特殊值：`None`（表示 “无”）
- **视为`True`的情况**：
    - 非零数值（如`1`、`-3.14`、`5+2j`）
    - 非空字符串（如`"hello"`、`" "`（含空格））
    - 非空容器（如`[1,2]`、`(3,)`、`{"name": "Python"}`）
    - 除上述 “False 情况” 外的所有值.
**示例**：
```python
print(bool(0))        # False（零值）
print(bool(""))       # False（空字符串）
print(bool([]))       # False（空列表）
print(bool(None))     # False（特殊值None）

print(bool(3.14))     # True（非零数值）
print(bool("hi"))     # True（非空字符串）
print(bool([1,2]))    # True（非空列表）

```

---
### 布尔运算
布尔类型常用的运算符用于组合或取反逻辑关系：
- `and`（与）：两边都为`True`时，结果才是`True`（否则`False`）
- `or`（或）：两边至少有一个`True`时，结果为`True`（否则`False`）
- `not`（非）：对布尔值取反（`not True`为`False`，`not False`为`True`）
**示例**：
```python
print(True and False)  # False（两边不同时为True）
print(True or False)   # True（至少一个为True）
print(not True)        # False（取反）
print(3 > 2 and 5 < 10)  # True（3>2为True，5<10为True，与运算结果为True）
```

---
### 应用场景
布尔类型最核心的应用是**条件判断**（如`if`语句、`while`循环），通过布尔值决定代码执行路径：
```python
age = 18
if age >= 18:  # 条件表达式的结果是bool类型（这里18>=18为True）
    print("已成年")  # 执行此句
else:
    print("未成年")

# while循环中，条件为True时持续执行
count = 0
while count < 3:  # 条件为True时循环
    print("循环中...")
    count += 1
```

### 总结
`bool`类型是 Python 逻辑判断的基础，通过`True`和`False`控制程序流程，配合类型转换和布尔运算符可实现复杂的逻辑处理。


> -  **命题**是指一个可以明确判断 “真”（True）或 “假”（False）的陈述句