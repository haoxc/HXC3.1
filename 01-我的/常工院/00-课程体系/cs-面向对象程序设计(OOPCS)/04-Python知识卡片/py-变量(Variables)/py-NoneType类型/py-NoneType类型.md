---
aliases: 空值
type: note
tags: [工具]
description: - **类型**：`NoneType`
create-date: 2026-04-29
---
## 概要
- **类型**：`NoneType`
    - `None` 是 `NoneType` 类型的唯一实例。
    - 你可以通过 `type(None)` 来验证其类型。

---
## 用法

- **默认值**
	- 1.  在函数定义时，可以使用 `None` 作为默认参数值，以表示该参数是可选的。

- **表示空值或缺失值**
	- `None` 可以表*示变量没有值*，或者用于初始化变量。

```python
	value = None
	if value is None:
	    print("Value is None")  # 输出: Value is None

```

- **结束循环或条件**
	- `None` 可以作为条件判断的终止符。
	
```python
data = [1, 2, 3, None, 5]
for item in data:
    if item is None:
        break
    print(item)
# 输出:
# 1
# 2
# 3

```

- **清理资源**
```python
	file = open('example.txt', 'r')
	# 进行文件操作
	file.close()
	file = None
```

---
## 总结
- `None` 是 Python 中用于表示空值或缺失值的特殊常量。
- 它是 `NoneType` 类型的唯一实例。
- `None` 经常用于函数默认参数、表示空值、终止循环或条件，以及清理资源。
- 使用 `is` 和 `is not` 进行 `None` 的比较。

 