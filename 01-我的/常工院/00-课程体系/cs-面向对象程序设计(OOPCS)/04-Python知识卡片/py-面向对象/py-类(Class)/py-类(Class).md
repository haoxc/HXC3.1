---
aliases: 
---
>[!note] 资料
> [Python3 面向对象 | 菜鸟教程](https://www.runoob.com/python3/python3-class.html)
## 纲要
- **类**
	- `概要`
		- 描述具有相同性质(属性)事物及方法的**对象**的集合描述.
	- `要素`
		- **对象**: 通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
		- **实例变量**:(*成员变量*,对象变量)：描述*对象属性*的变量，只作用于当前类的实例(也就是对象)。
		- **实例方法**:, 也叫*对象方法*,类中定义的函数,这些方法大多数在`对象`上操作
		- **类属性**：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
	- [ ]
	- `要点`
		- **基本功能**
			- [[#定义类]]
				- 创建一个类的实例，类的具体对象。参见:[[py-变量赋值(Assignment)]]
			- [[#类实例化]]
				- 创建一个类的实例，类的具体对象。参见:[[py-变量赋值(Assignment)]]
			- [[#定义实例变量]]
			- [[#定义实例方法]]
				- 定义*对象*上的操作方法
			- [[#内置类属性(高级)]]
		- **高级功能**
			- [[#继承]]
				- `概要`
					- 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个 Dog 类型的对象派生自 Animal 类，这是==模拟"是一个（is-a）"关系==（例：Dog 是一个 Animal）。
			- [[#方法重载]]
				- `概要`
					- 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（*override*），也称为方法的重载。
	 


## 基础功能
### 定义类
明确化定义类的*名称*,语法如下:
```python
class ClassName:
   '''类的帮助信息'''   #类文档字符串
   class_suite     #类体
```

> 类的*帮助信息*可以通过ClassName.`__doc__`查看。

比如定义我们所有人得基本信息, 我们定义一个People基础类, 参考程序*类定义-01-类定义.py*
``` python
class People:  
    '''  
    说明:People类描述个人信息  
    '''
```

### 定义实例变量
在类的声明中，属性是 #变量 来表示的。这种变量就称为 #实例变量 ，是在类声明的内部但是在类的其他成员方法之外声明的
```python
class People:  
    '''  
    说明:People类描述个人信息  
    '''  
    #构造函数, 也成为实例初始化函数  
    def __init__(self, cName, eName, age, weight):  
        '''  
        :param cName: 中文名称  
        :param eName: 英文名称  
        :param age: 年龄  
        :param weight: 体重  
        '''        
        self.cName = cName  
        self.eName = eName  
        self.age = age  
        self.__weight = weight #这是秘密信息哟  
        #...
```

---
**要点:**
- `__init__` 是类的**构造函数**
	-  *私有属性*    
		- 前缀:`__`
	- *公开属性` 
1. 属性引用使用和 Python 中所有的属性引用一样的标准语法：**obj.name**
2. 参考 [[py-文档字符串(DocStrings）]]
---


### 定义实例方法
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 *self*
```python
class People:  
    '''  
    说明:People类描述个人信息  
    '''  
    #构造函数, 也成为实例初始化函数  
    def __init__(self, cName, eName, age, weight):  
        '''  
        :param cName: 中文名称  
        :param eName: 英文名称  
        :param age: 年龄  
        :param weight: 体重  
        '''        self.cName = cName  
        self.eName = eName  
        self.age = age  
        self.__weight = weight #这是秘密信息哟  
        #...  
  
    def introduce(self):  
        '''  
        自我介绍的方法  
        '''        print(f"Hi, my name is {self.eName},{self.age} year old.")
```
> **self**代表类的*实例*，而非类



### 内置类属性(高级)
-   `__dict__` : 类的属性（包含一个字典，由类的数据属性组成）
-   `__doc__` :类的文档字符串
-   `__name__`: 类名
-   `__module__`: 类定义所在的模块（类的全名是`__main__`.className，如果类位于一个导入模块mymod中，那么className.`__module__` 等于 mymod）
-   `__bases__` : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
> [[魔法函数(py)]]



## 高级功能
### 继承
面向对象一个重要概念就是继承,不支持继承，语言特性就不值得称为“类”. 
语法结构如下
```python
class DerivedClassName(BaseClassName):
	<statement-1> . . . 
	<statement-N>
```

 ### 方法重载
 > 实践