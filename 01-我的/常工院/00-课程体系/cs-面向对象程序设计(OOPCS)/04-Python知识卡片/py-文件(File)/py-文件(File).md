---
color: var(--mk-color-teal)
type: note
tags: [工具]
description: > [!note]
create-date: 2026-04-29
---
> [!note]
>[Python3 文件 | 菜鸟教程](https://www.runoob.com/python3/python3-file-methods.html)
## 文件(file) 概述
 
Python `open`() 方法用于打开一个文件，并返回*文件对象*，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 *OSError*。

**注意：**使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。


```python
 
file =open(filename,mode)
 

```

-   **filename**：包含了你要访问的文件名称的字符串值。
-   **mode**：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
- ![[Pasted image 20220512154838.png]]
## 写入文件
```python
	file = open("D:\\游戏引擎\\Python编程编程\pjx\\mine.text", mode="a+")

	file.write(str)
	#...
	file.close()
```


### 完善错误处理
```python
	try:
		file = open("D:\\游戏引擎\\Python编程编程\pjx\\mine.text", mode="a+")

		file.write(str)
		#...
	except OSError as err

	finally
		file.close()
```




## 文件和目录操作
[os](https://www.runoob.com/python3/python3-os-file-methods.html) 模块提供了非常丰富的方法用来处理文件和目录。 