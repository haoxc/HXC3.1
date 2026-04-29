---
aliases: 
---
>[!important] 资料
[参考资料](https://www.runoob.com/w3cnote/python-func-decorators.html)

## 概述
简单地说, *他们是***修改**`其他函数`的**功能**的*函数*.
目的他们有助于让我们的代码更简短，也更Pythonic（*Python范*）。大多数初学者不知道在哪儿使用它们，所以我将要分享下，哪些区域里装饰器可以让你的代码更简洁。 首先，让我们讨论下如何写你自己的装饰器。

这可能是最难掌握的概念之一。我们会每次只讨论一个步骤，这样你能完全理解它。

## 核心概念
- 一切皆对象(包括,变量,类,函数)
- 在函数中也可以定义函数
- 从函数中返回函数
- 将函数作为参数传给另一个函数

## 使用场景

### 授权(Authorization)
装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：
``` python
from functools import wraps
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated

```
