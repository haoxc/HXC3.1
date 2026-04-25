---
aliases:
---

## 概要
在函数定义时，可以使用 `None` 作为默认参数值，以表示该参数是可选的。
```python
def my_function(param=None):
    if param is None:
        param = []
    # 其他处理逻辑
    return param

print(my_function())  # 输出: []
print(my_function([1, 2, 3]))  # 输出: [1, 2, 3]

```

 