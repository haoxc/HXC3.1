---
aliases:
  - 基础类型(primitive type)
property: Immutable
type:
tags: [工具]
description: - [[py-字符串类型(str)|字符串类型(string)]]
create-date: 2026-04-29
---
### 基础类型
- [[py-字符串类型(str)|字符串类型(string)]]
- [[py-数字类型(number)|数字类型(number)]]
- [[py-布尔类型(bool)|布尔类型(bool)]]

---

## 类型操作
- 查看类型  #如何 
内置函数` type() `可以用来查询变量所指的对象类型。
```python
#参看变量类型
type(variable)
```


- `类型操作`
	- 变量赋值(Assignment)
		- *理解*
			- Python 中的*变量不需要声明*。每个变量在*使用前都必须赋值*，变量赋值以后该变量才会被创建。
			- 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量*所指的内存中对象的类型*。
			- 等号（=）用来给*变量赋值*。
			- 等号（=）运算符左边是一个==变量名==,等号（=）运算符右边是==存储在变量中的值==.
			- 用户
				- ![[Pasted image 20220425162223.png|500]]
		- *示例*
			- 简单赋值
				- counter =100
			- 多个变量赋值 (Multiple assignment)
				- a=b=c =1
				- a, b, c = 1, 2, "john"
				- 对象
					- ![[Pasted image 20220425162512.png]]
				- 对象
					- ![[Pasted image 20220425162552.png]]
					- ![[Pasted image 20220425162528.png]]
					- ![[Pasted image 20220425162537.png]]
	- 删除对象
		- *文法*:  **del** `variableName`

>`ris:AlarmWarning` *注意*：Python3 中，*bool* 是 int 的子类，True 和 False 可以和数字相加， $$True==1、False==0$$ 会返回 **True**，但可以通过 *isinstance* 来判断类型。


## 数据操作(概述)

### 字符串(String)

- 基本概念
	python中的[字符 串](https://www.w3cschool.cn/python3/python3-string.html)用*单引号*` ' `或*双引号*` " `括起来，同时使用反斜杠 `\` 转义特殊字符。字符串的截取的语法格式如下：文法(syntax)
> 变量[头下标:尾下标]

例子:
![[Pasted image 20220405181120.png|600]]

- 字符串操作
	- 取值(get)
		- 格式: 字符串[*头下标*:*尾小标*]
	- 重复(times)
		- 格式: *字符变量*\**倍数*
	- 连接(concatenate)
		- 格式: *字符变量*+*其他变量*
- 字符串格式化
	- `传统方式`
		- 参数
			- %c : char
			- %`s`:  str
			- %d:  int
			- %f: float
		- 示例
			- ![[Pasted image 20220503160531.png]]
	- `f-string`
		- 语法
			- f-string 格式化字符串以 `f` 开头，后面跟着字符串，字符串中的表达式用大括号` {} `包起来，它会将`变量`或`表达式`计算后的值替换进去(*python3.6以后支持*)
		- 示例
			- ![[Pasted image 20220503160656.png]]
	- `str.format`
		- 资料
			-  [Python format 格式化函数_w3cschool](https://www.w3cschool.cn/python/att-string-format.html)
		- *语法*  #important  #checklist
			- 根据参数顺序
				- 示例
					- ![[Pasted image 20220503170209.png]]
			- 根据参数名称
				- 变量占位参数占位符`{}`![[Pasted image 20220503170237.png]]
				- 字典设置
					- 字典定义后, 解析使用==\*\*==![[Pasted image 20220503170348.png]]
### 元组(Tuple)
[元组](https://www.w3cschool.cn/python3/python3-tuple.html)（tuple）与*列表*类似，不同之处在于*元组的元素不能修改*。元组写在小括号 () 里，元素之间用逗号隔开。


### 列表(List)
[列表](https://www.w3cschool.cn/python3/python3-list.html)可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓*嵌套*）。
列表是写在方括号 \[\] 之间、用`逗号`分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
![[Pasted image 20220405182508.png|600]]


> `ris:CheckboxMultiple`  **思考** 操作符和string操作符是否一致?



### 集合(Set)
 [集合](https://www.w3cschool.cn/python3/python3-set.html)（set）是由一个或数个*形态各异*的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 *set()* 而不是 { }，因为 { } 是用来创建一个空字典。
*创建格式：*
>parame = {value01,value02,...} 
>或者 
>set(value)

#### 集合操作
-  `in`
- `-`(差集)
- `|`(并集)
- `&`(交集)
- `^`(与或xor)

### 字典(Dictionary)
[字典](https://www.w3cschool.cn/python3/python3-dictionary.html)（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 **键(key) : 值(value)** 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。

## 类型转换
![[Pasted image 20220405185245.png]]


