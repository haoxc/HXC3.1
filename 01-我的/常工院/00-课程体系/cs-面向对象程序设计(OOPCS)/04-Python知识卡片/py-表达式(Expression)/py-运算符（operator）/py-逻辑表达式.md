---
category:
  - Python 知识点
type: 永久笔记 (perNote)
domain: Python 文法 (syntax)
aliases:
  - 逻辑表达式
topic:
tags:
description:
create-date: 2026-04-29
---
## 概述
- **逻辑表达式**-是由**逻辑运算符**连接布尔值（`True` / `False`）、[[py-关系表达式|关系表达式]] 或其他逻辑表达式组成的式子，用于表示复杂的逻辑判断，最终结果为一个**布尔值**（`True` 或 `False`）。
- 它是编程中组合多个条件、实现复杂逻辑判断的核心工具，广泛用于 `if` [[py-条件语句|条件语句]]、[[[循环控制]]] 等场景。

---
## 逻辑运算符
逻辑表达式的核心是**逻辑运算符**，用于组合或反转条件: 

| 运算符 | 逻辑表达式   | 描述                                                              | 实例                     |
| --- | ------- | --------------------------------------------------------------- | ---------------------- |
| and | x and y | 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。             | (a and b) 返回 20。       |
| or  | x or y  | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。                      | (a or b) 返回 10。        |
| not | not x   | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。对单个条件**取反** | not (a and b) 返回 False |


---
## 运算规则与特性
#### 1. 操作数类型
逻辑运算符的操作数通常是：
- 布尔值（`True`/`False`）；
- 关系表达式（结果为布尔值，如 `x > 5`）；
- 其他能被解释为 “真 / 假” 的表达式
>  💡Python 中除 `0`、`None`、空字符串 `""`、空列表 `[]` 等 “空值” 外，均视为 `True`。
#### 2. 优先级与结合性
- **优先级**（从高到低）：`not` > `and` > `or`（可通过括号 `()` 强制改变顺序）。
```python
# 先算 not b → True，再算 a and True → True，最后算 True or c → True
a, b, c = True, False, False
print(a and not b or c)  # 输出：True

# 括号改变顺序：先算 b or c → False，再算 not False → True，最后算 a and True → True
print(a and not (b or c))  # 输出：True
```
    
- **结合性**：`and` 和 `or` 是**左结合**（从左到右计算），`not` 是单目运算符（仅作用于右侧操作数）。

#### 短路求值（重要特性）
Python 中逻辑运算采用 “短路求值” 策略：当表达式的结果可提前确定时，不再计算剩余部分，提高效率。
- **`and` 的短路**：若左侧为 `False`，则直接返回 `False`，右侧不再计算。
**示例:**
```python
def func():
	print("函数被调用")
	return True

# 左侧 1 > 2 为 False，右侧 func() 不会执行（无打印），直接返回 False
print(1 > 2 and func())  # 输出：False
```
    
- **`or` 的短路**：若左侧为 `True`，则直接返回 `True`，右侧不再计算。
**示例**：
```python
# 左侧 1 < 2 为 True，右侧 func() 不会执行（无打印），直接返回 True
print(1 < 2 or func())  # 输出：True
```

### 四、注意事项
- **与位运算符区分**：逻辑运算符 `and`/`or`/`not` 用于布尔判断，而位运算符 `&`/`|`/`~` 用于二进制位运算，二者不可混淆。
> 例如：`True and False` 是逻辑运算（结果 `False`），而 `1 & 0` 是位运算（结果 `0`）。

- **非布尔值的逻辑判断**：Python 中非布尔值会被隐式转换为 “真 / 假”（如 `0` 为 `False`，非 `0` 数字为 `True`），但逻辑运算结果可能是原始值而非严格布尔值。
> 例如：`3 and 5` 结果为 `5`（因左侧为真，返回右侧值），`0 or "hello"` 结果为 `"hello"`（因左侧为假，返回右侧值）。
