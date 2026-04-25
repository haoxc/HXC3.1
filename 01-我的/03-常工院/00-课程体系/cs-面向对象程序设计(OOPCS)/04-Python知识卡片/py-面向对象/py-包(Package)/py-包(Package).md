---
aliases:
---

## 包概述
- 包是一个**包含 `__init__.py` 文件的目录**（Python 3.3+ 可省略，但建议保留）。
- 包可以包含多个模块，甚至子包。
- 包本身也是一个`命名空间`。
- 包是一个分层次的文件目录结构，它定义了一个由[[讲授-模块(Module)]]及子包，和子包下的子包等组成的 Python 的应用环境。
-  包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
- 
> [!hint] 理解
>  - 模块的“文件夹容器”


---
## 构成
###  属性
- 目录只有包含一个叫做 `__init__.py` 的*文件才会被认作是一个包*，主要是为了避免一些==滥俗的名字==（比如叫做 string）不小心的影响搜索路径中的有效模块
- 属性列表
	- `__all__`: 包的列表变量,在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入. 


---

## 实际案例

### 示例
- art_project项目的目录结构：
```python
art_project/
├── __init__.py
├── drawing.py
├── color.py
└── effects/
    ├── __init__.py
    └── blur.py
```
### 使用

```python
from art_project.drawing import draw_circle
from art_project.effects.blur import gaussian_blur
```

> 🎯 **包的作用**：把你的“数字艺术项目”按功能分类管理，避免所有代码堆在一个文件里。


---
## 学习资料
- [Python3 模块 | 菜鸟教程](https://www.runoob.com/python3/python3-module.html)