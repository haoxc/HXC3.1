---
aliases: Function Annotation
---
*创建时间*：2022年5月8日 11:46:28

## 概述
`函数注解语法 `可以让你在定义函数的时候`对参数和返回值添加注解`

```python
def foobar(a: int, b: "it's b", c: str = 5) -> tuple:
    return a, b, c
```

> **要点:** 注解内容既可以是个==类型==也可以是个==字符串==,甚至表达式：

``` python
def foobar(a: 1+1) -> 2 * 2:
    return a
```

## 注释获取
如何获取我们定义的函数注解呢？至少有两种办法：
- `__annotations__`
	- ![[Pasted image 20220508115015.png]]
- `inspect.signature`:
	- ![[Pasted image 20220508115033.png]]
	- 

## 类型检查 
#decorator #装饰器

>资料 [类型检查](https://mozillazg.com/2016/01/python-function-argument-type-check-base-on-function-annotations.html)


- 代码示例
``` python
# coding: utf8
import collections
import functools
import inspect

def check(func):
    msg = ('Expected type {expected!r} for argument {argument}, '
           'but got type {got!r} with value {value!r}')
    # 获取函数定义的参数
    sig = inspect.signature(func)
    parameters = sig.parameters          # 参数有序字典
    arg_keys = tuple(parameters.keys())   # 参数名称

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('anno', 'arg_name', 'value'))
        check_list = []

        # collect args   *args 传入的参数以及对应的函数参数注解
        for i, value in enumerate(args):
            arg_name = arg_keys[i]
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))

        # collect kwargs  **kwargs 传入的参数以及对应的函数参数注解
        for arg_name, value in kwargs.items():
           anno = parameters[arg_name].annotation
           check_list.append(CheckItem(anno, arg_name, value))

        # check type
        for item in check_list:
            if not isinstance(item.value, item.anno):
                error = msg.format(expected=item.anno, argument=item.arg_name,
                                   got=type(item.value), value=item.value)
                raise TypeError(error)

        return func(*args, **kwargs)

    return wrapper
```
