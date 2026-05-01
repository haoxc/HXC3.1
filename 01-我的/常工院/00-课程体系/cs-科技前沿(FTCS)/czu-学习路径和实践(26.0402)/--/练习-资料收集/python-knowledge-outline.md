---
tags: [工具]
description: 1. **环境配置**
type: note
create-date: 2026-04-29
---

# Python 知识大纲

## 一、Python 基础
1. **环境配置**
   - Python 安装与版本管理（pyenv, conda）
   - 虚拟环境（venv, virtualenv）
   - 包管理工具（pip, pipenv, poetry）
   - 开发环境配置（VS Code, PyCharm, Jupyter）

2. **基础语法**
   - 变量与数据类型（int, float, str, bool, None）
   - 运算符与表达式
   - 输入输出（print, input）
   - 注释与文档字符串

3. **流程控制**
   - 条件语句（if, elif, else）
   - 循环语句（for, while）
   - 循环控制（break, continue, pass）
   - 异常处理（try, except, finally, raise）

## 二、Python 核心数据结构
1. **序列类型**
   - 列表（list） - 可变序列
   - 元组（tuple） - 不可变序列
   - 字符串（str） - 不可变文本序列
   - 范围（range） - 数字序列

2. **集合类型**
   - 集合（set） - 无序不重复元素
   - 冻结集合（frozenset） - 不可变集合

3. **映射类型**
   - 字典（dict） - 键值对映射
   - 默认字典（defaultdict）
   - 有序字典（OrderedDict）

4. **数据结构操作**
   - 切片与索引
   - 推导式（列表、字典、集合推导式）
   - 生成器表达式
   - 迭代器与可迭代对象

## 三、函数与模块
1. **函数定义与使用**
   - 函数定义（def, lambda）
   - 参数传递（位置参数、关键字参数、默认参数）
   - 可变参数（*args, **kwargs）
   - 返回值与多返回值
   - 作用域与命名空间（global, nonlocal）

2. **高级函数特性**
   - 装饰器（@decorator）
   - 闭包
   - 高阶函数
   - 函数注解

3. **模块与包**
   - 模块导入与使用（import, from...import）
   - 模块搜索路径
   - 包的结构与组织
   - __init__.py 文件的作用
   - 相对导入与绝对导入

## 四、面向对象编程
1. **类与对象**
   - 类定义与实例化
   - 属性与方法（实例方法、类方法、静态方法）
   - 构造函数与析构函数（__init__, __del__）
   - 访问控制（公有、保护、私有）

2. **继承与多态**
   - 单继承与多继承
   - 方法重写（override）
   - super() 函数
   - 抽象基类（ABC）
   - 多态与鸭子类型

3. **特殊方法与运算符重载**
   - 常用特殊方法（__str__, __repr__, __len__）
   - 运算符重载（__add__, __eq__, __lt__）
   - 上下文管理器（__enter__, __exit__）
   - 迭代器协议（__iter__, __next__）

## 五、Python 标准库
1. **常用内置模块**
   - os, sys - 系统操作
   - datetime, time - 日期时间
   - math, random - 数学运算
   - json, csv - 数据格式
   - re - 正则表达式
   - collections - 扩展容器
   - itertools - 迭代工具
   - functools - 函数工具
   - typing - 类型提示

2. **文件与IO**
   - 文件读写（open, read, write）
   - 路径操作（pathlib, os.path）
   - 序列化（pickle, json）
   - 压缩文件（gzip, zipfile）

3. **并发与异步**
   - 多线程（threading）
   - 多进程（multiprocessing）
   - 异步编程（asyncio）
   - 协程与任务

## 六、Web 开发
1. **Web 框架**
   - Flask - 轻量级框架
   - Django - 全栈框架
   - FastAPI - 高性能API框架

2. **网络编程**
   - HTTP 请求与响应（requests）
   - WebSocket 编程
   - RESTful API 设计
   - 微服务架构

3. **数据库操作**
   - SQLAlchemy - ORM 框架
   - Django ORM
   - 数据库连接（sqlite3, psycopg2, pymysql）

## 七、数据科学与机器学习
1. **数据分析**
   - NumPy - 数值计算
   - Pandas - 数据分析
   - Matplotlib - 数据可视化
   - Seaborn - 统计可视化

2. **机器学习**
   - Scikit-learn - 机器学习算法
   - TensorFlow - 深度学习框架
   - PyTorch - 深度学习框架
   - Keras - 深度学习高级API

3. **数据处理**
   - 数据清洗与预处理
   - 特征工程
   - 模型训练与评估
   - 超参数调优

## 八、自动化与脚本
1. **系统自动化**
   - 文件批量处理
   - 定时任务（cron, schedule）
   - 系统监控与日志
   - 进程管理

2. **测试与调试**
   - 单元测试（unittest, pytest）
   - 测试驱动开发（TDD）
   - 调试工具（pdb, ipdb）
   - 性能分析（cProfile, line_profiler）

3. **项目开发实践**
   - 代码规范（PEP 8）
   - 版本控制（Git）
   - 持续集成（CI/CD）
   - 文档生成（Sphinx, MkDocs）

## 九、高级主题
1. **元编程**
   - 装饰器进阶
   - 元类（metaclass）
   - 描述符（descriptor）
   - 属性访问控制

2. **性能优化**
   - 代码优化技巧
   - 内存管理
   - C扩展开发（Cython）
   - 并行计算

3. **部署与运维**
   - Docker 容器化
   - 云平台部署（AWS, GCP, Azure）
   - 监控与日志
   - 安全最佳实践
