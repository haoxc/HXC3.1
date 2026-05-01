---
aliases:
type: note
tags: [工具]
description: *创建时间*：2022年4月28日 16:01:49
create-date: 2026-04-29
---
*创建时间*：2022年4月28日 16:01:49

## 第一次作业
- 目标
	- 熟悉掌握Jupyter的编程环境
		- cell操作(增加,删除)
		- cell类型操作(代码, markdown)
	- 练习
		- 基础类型定义及打印类型
		- 按照元组[,列表](https://www.w3cschool.cn/python3/python3-list.html),集合,字典的顺序分类,也就是根据W3School上的文档,分类练习他们操作方法
	- 文件命名格式
		- 数媒2-学号-姓名
		- 数媒1-学号-姓名

## 第二次作业
2022年5月2日 **15:11:46**
- 目标
	- 熟练掌握if, while, for等逻辑控制语句(Statement) 
	- 熟悉iter(),len(),int(),float(),str()等常用内联函数
		- 参考地址: [Python 内置函数_w3cschool](https://www.w3cschool.cn/python/python-built-in-functions.html)		
		- 转换
			- ![[Pasted image 20220405185245.png]]
		- 遍历器
			- iter(),len()
	- 编程训练
		- [链接](https://www.w3cschool.cn/python3/python3-examples.html)
			- -   [Python if 语句](https://www.w3cschool.cn/python3/python3-if-example.html)
			-   [Python 判断字符串是否为数字](https://www.w3cschool.cn/python3/python3-check-is-number.html)
			-   [Python 判断奇数偶数](https://www.w3cschool.cn/python3/python3-odd-even.html)
			-   [Python 判断闰年](https://www.w3cschool.cn/python3/python3-leap-year.html)
			-   [Python 获取最大值函数](https://www.w3cschool.cn/python3/python3-largest-number.html)
				- [max函数说明](https://www.w3cschool.cn/python/func-number-max.html)
			-   [Python 质数判断](https://www.w3cschool.cn/python3/python3-prime-number.html)
				- 要点
					- [range](https://www.w3cschool.cn/python3/python3-func-range.html)
			-   [Python 阶乘实例](https://www.w3cschool.cn/python3/python3-factorial.html)
			-   [Python 九九乘法表](https://www.w3cschool.cn/python3/python3-99-table.html)
				- 字符串格式:
					- [参考地址](https://www.w3cschool.cn/python/att-string-format.html)
			-   [Python 斐波那契数列](https://www.w3cschool.cn/python3/python3-fibonacci-sequence.html)
	- 文件命名格式
		- 数媒2-学号-姓名
		- 数媒1-学号-姓名

1. ## 第三次作业
2022年5月10日 **15:11:46**
- 目标
	- 熟练掌握 Class的属性,以及继承基本定义
	- 题干
		- [x]  `图形(Shape)`是图形学中重要的概念, 它包含图形名称(name), 绘画中的线的颜色(lineColor), 线的粗细(lineWidth), 以及文字显示大小; (fontSize); 同时,图形都能够计算出自己的面积(我们通过area成员函数返回一个数值).
		-  `子类`:`长方形(Rectange)`, `圆(Circle)`都分别是图形类的**子类**, 分别上述2个子类,并明确定义计算面积需要的特有属性,并*重载*计算**面积方法**
		- 分析:
			- ![[Pasted image 20220510160001.png]]
	- 文件命名格式
		- 数媒2-学号-姓名
		- 数媒1-学号-姓名


## 第四次作业
2022年5月10日 **15:11:46**
- `目标`
	-  **知识点**
		- 输入和输出
			- input 输入函数
		- 格式化(f-string)
		- 异常处理
		- 循环
	- `内容`
		- **入学登记程序**:  我们把每位同学作为一个Student的对象,编辑一个程序,帮助**入学登记员**, 循环登记入学人员,并生成==人员登记文件==(names.txt)
			- 1. 入学登记员通过该程序,输入姓名(*name*),年龄(*age*),班级(*grade*),籍贯(*hometown*)四个信息, 并保存到Student对象;( ==注意提示友好性==);
			- 2. 保存该同学的基本信息到人员登记文件中;
			- 3. 提示入学登记员*是否*(Y/N)继续, *是*的情况下,继续登记其他同学的基本信息,直到全部学生登记结束, *否*的情况下, 退出登记程序.
		- **要求**:
			- **基本**
				- 登记同学不能少于5人;
			- **高级**
				-  登记年龄必须是*15岁以上(包括)*, 否则提示**入学登记人员**重新输入;
				- 限定班级为:**1,2,3,4**


## 第五次作业
2022年5月23日 **15:11:46**
- `目标`
	-  **要点**
		- 熟练掌握游戏开发的过程
		- 运用脚本,UI和UE等知识对游戏的精灵,游戏场景,以及背景音乐等*文创*内容
	- `内容`
		- 变更公主精灵的形象和背景
		- 增加礼物等精灵的`种类`,增加游戏场景多样性
		- 根据礼物的种类不同,`碰撞`时,播放不同的背景




## 大作业
2022年5月23日 **15:11:46**
- `内容`
	- 根据目前学习的基础知识, 利用Pyglet多媒体引擎,设计键盘交互为主的游戏.
		- 游戏场景设计
		-  游戏精灵和交互不能少于4个场景
		- 游戏支持3个阶段
			- 游戏介绍
			- 游戏中
				- 支持暂停
				- 碰撞场景动效和声效
			- 游戏结束
		- `挑战`
			- 多人参与游戏