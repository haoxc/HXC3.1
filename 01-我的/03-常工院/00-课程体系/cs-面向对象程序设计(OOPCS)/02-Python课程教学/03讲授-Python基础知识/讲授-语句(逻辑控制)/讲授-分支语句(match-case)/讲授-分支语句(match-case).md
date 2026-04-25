---
aliases:
  - match-case语句
banner: 60-艺术学科/平面设计(Graphic Design, GD)/平面设计-案例集（GD casebook)/附件/bg_曲别针.png
type: course
subject: Python基础
category:
  - python/基础知识/语句
orderNo: 110
---
### 概述
- 在 Python 3.10 及以上版本中，引入了 **match-case** 语句 （模式匹配），它是一种更强大、更灵活的`分支控制`结构，类似于其他语言中的`switch-case`，但支持对数据结构（如列表、元组、字典、类实例等）进行 “模式匹配”，而非仅匹配值。
> [!Warning]
    > 仅 Python 3.10 及以上版本支持`match-case`，低版本会报错

### 文法
- 核心逻辑是：对一个**目标表达式**进行模式匹配，执行第一个匹配成功的`case`分支。基本结构如下：
```python
match 目标表达式:
    case 模式1:
        执行语句1
    case 模式2:
        执行语句2
    case _:  # 通配符，匹配所有未被前面case匹配的情况（类似default）
        执行默认语句
```

### 优势
- `match-case`支持结构化匹配（如直接匹配元组 / 列表的长度和内容），代码更简洁，逻辑更清晰

### 应用
#### 字面量模式（匹配具体值）
匹配常量（数字、字符串、布尔值等），类似传统`switch-case`：
```python
def check_value(x):
    match x:
        case 0:
            print("匹配到0")
        case 1:
            print("匹配到1")
        case "hello":
            print("匹配到字符串'hello'")
        case True:
            print("匹配到True")
        case _:  # 未匹配到上述情况时执行
            print("未匹配到已知值")

check_value(0)       # 输出：匹配到0
check_value("hello") # 输出：匹配到字符串'hello'
check_value(2)       # 输出：未匹配到已知值
```
