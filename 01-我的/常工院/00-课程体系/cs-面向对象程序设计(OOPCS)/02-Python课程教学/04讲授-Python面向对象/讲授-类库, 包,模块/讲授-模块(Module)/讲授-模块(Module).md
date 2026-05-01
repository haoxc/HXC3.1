---
aliases:
- 模块(Module)
type: note
tags: [工具]
description: - [模块](https://www.w3cschool.cn/python/python-modules.html)是一个包含所有你定义的函数和变量的`文件`
create-date: 2026-04-29
---
## 概述
- [模块](https://www.w3cschool.cn/python/python-modules.html)是一个包含所有你定义的函数和变量的`文件`，其后缀名是`.py`。
- 模块可以被别的程序`引入`，*以使用该模块中的函数等功能*。这也是使用 python 标准库的方法。
- **模块（module）和包（package）的核心价值之一就是促进代码复用**
- ---
## 属性
- `__name__`: 每个模块都有一个 __name__ 属性 格式为==`__name__`==, 当其值是 `__main__` 时，表明该模块自身在运行，否则是被引入。
## 应用

### 场景1- 引入同一包中的模块
- 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
```python
[import module1[, module2[,... moduleN]]>)
```
**示例1**： 
```Python
# 文件名: using_sys.py
import sys
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')
```

---
### 场景2- 引入不同包的模块
- `文法`: From…import 语句
```python
from modname import name1[, name2[, ... nameN]]
```

**示例**:
```python
from fib import fibonacci
```
---
### 场景3-了解模块中的内容
[[内置函数-dir()]]
dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
返回的列表容纳了在一个模块里定义的*所有模块，变量和函数*。如下一个简单的实例
```python
#列出系统模块os对象的内容
dir(os)
```


## 标准库
- 模块列表
	- `os 模块`提供了不少与操作系统相关联的函数
	- `glob 模块`提供了一个函数用于从目录通配符搜索中生成文件列表
	- `sys 模块`: 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量
	- `re 模块`为高级字符串处理提供了正则表达式工具
	- `math 模块`为浮点运算提供了对底层 C 函数库的访问
	- `urllib.request模块` : 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 `smtplib`
	- `datetime 模块`为日期和时间处理同时提供了简单和复杂的方法。
	- `timeit` 证明了现代的方法更快一些.Python 提供了一个度量工具，为这些问题提供了直接答案。
	- `doctest 模块`提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试

>  [线上资源](https://www.w3cschool.cn/python3/python3-stdlib.html)

>[!faq] 帮助
>  安装外部包或模块: https://pypi.org/  
