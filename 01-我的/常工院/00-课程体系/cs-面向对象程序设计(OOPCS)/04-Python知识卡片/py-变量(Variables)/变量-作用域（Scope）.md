---
aliases:
  - 作用域（Scope）
type: note
tags: [工具]
description: - 变量的“可见范围”，决定了在某处能访问哪些命名空间
create-date: 2026-04-29
---
## 作用域（Scope）
- 变量的“可见范围”，决定了在某处能访问哪些命名空间
- Python 有 **LEGB 规则**（从内到外查找）

| 层级    | 名称            | 说明                             |
| ----- | ------------- | ------------------------------ |
| **L** | Local（局部）     | 函数内部定义的变量                      |
| **E** | Enclosing（嵌套） | 外层函数的变量（闭包）                    |
| **G** | Global（全局）    | 模块顶层定义的变量                      |
| **B** | Built-in（内置）  | Python 内置的名字（如 `print`, `len`） |

---
### 例子：
```python
color = "red"  # 全局作用域（G）

def draw():
    size = 100  # 局部作用域（L）
    print(color)  # 可以访问全局变量
    print(size)

draw()
# print(size)  # ❌ 报错！size 只在 draw() 内可见
```

> 💡 **提示**：就像你在“调色盘区”调的颜色，不能直接在“画布区”使用，除非你把它“传递”过去。
