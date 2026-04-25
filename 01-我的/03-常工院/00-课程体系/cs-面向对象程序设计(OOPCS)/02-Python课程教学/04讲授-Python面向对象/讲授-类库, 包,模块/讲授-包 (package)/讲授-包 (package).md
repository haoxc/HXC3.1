---
aliases:
- 包 (package)
---
## 包概述
- 包是一个**包含 `__init__.py` 文件的目录**（Python 3.3+ 可省略，但建议保留）。
- 包可以包含多个**模块**，甚至**子包**。
- 包是一个**分层次的文件目录结构**，它定义了一个由 [[讲授-模块(Module)]] 及子包，和子包下的子包等组成的 Python 的应用环境。
-  包是一种管理 Python 模块命名空间的形式，采用"**点模块名称**"。
- 包本身也是一个 `命名空间`。
> [!hint] 理解
>  - 模块的“文件夹容器”
>  - 

## 定义和使用
**art_project** 项目的目录结构：
```python
art_project/
├── __init__.py
├── drawing.py
├── color.py
└── effects/
    ├── __init__.py
    └── blur.py
```

![[Slide-包(Pakcage).canvas]]


**标识目录为包**:
- 空的 `__init__.py` 也有用 —— 告诉 Python “这个文件夹是一个包”，允许你用 `import` 导入包内的模块。
- `__init__.py` 中的 `__all__` 列表会指定 “哪些模块允许被批量导入”，避免导入无关内容。

**定义**art_project/ `__init__.py` 如下:
```python
# 只允许批量导入watermark和resize模块（filter暂不开放）  
__all__ = ["drawing", "color"]  
```

**使用**: 
```python
from art_project.drawing import draw_circle
from art_project.effects.blur import gaussian_blur
```

> 🎯 
> - **包的作用**：把你的“数字艺术项目”按功能分类管理，避免所有代码堆在一个文件里。
> - **如何理解**:  `__init__.py` 告诉 Python 该目录是一个包, 好比 “整理工具盒的说明书”

