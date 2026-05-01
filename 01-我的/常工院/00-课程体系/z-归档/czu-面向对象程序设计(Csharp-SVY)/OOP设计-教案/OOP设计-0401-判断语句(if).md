---
aliases: oop-C#@Statement/if, 判断语句
type: note
tags: [工具]
description: 当需要基于单个变量或表达式的*多个不同值*来执行不同操作时.
create-date: 2026-04-29
---
## 语法
当需要基于单个变量或表达式的*多个不同值*来执行不同操作时.
#csharp/pp-194

## If 语句
![[Pasted image 20231022140253.png|400]]
### If 语句
**if 语句**: 它由一个[[OOP设计-0303-布尔表达式|关系(比较)表达式/布尔表达式]]和一段随后的语句块组成。如果布尔表达式的结果为 `true`，则执行语句块。
```csharp
int score = 90;
if (score >= 60) //条件为True
{
    Console.WriteLine("及格了");
}

```

>[!error] 易错
```csharp
	int a  =5;
	if (a >6);
	{
		Console.WriteLine("ok");
	}
```
---
### If-else 语句
- 如果想在`条件不满足`时执行另一段代码，可以使用 if-else 结构。
- 也就是说,可以使用 `else` 子句扩展 `if` 语句，以在 `if` 表达式的结果为 `false` 时执行另一组代码。
```csharp
int score = 50;
if (score >= 60)
{
    Console.WriteLine("及格了");
}
else
{
    Console.WriteLine("不及格");
}
```
### If-else if-else 语句
当有多个条件需要判断时，可以使用 if-else if-else 结构。
**示例**:

```csharp
	int score = 85;
	if (score >= 90)
	{
	    Console.WriteLine("优秀");
	}
	else if (score >= 80)
	{
	    Console.WriteLine("良好");
	}
	else  if ( score <60)
	{
	    Console.WriteLine("需要加油");
	}
	
	
```

>[!error] 易错题 #csharp/复习/重点  #csharp/复习/难点 
> if ( 70 <=a <80) {
> }
 
## switch 语句
当需要基于单个变量或表达式的*多个不同值*来执行不同操作时，可以使用 `switch` 语句.
```csharp
	int dayOfWeek = 3;
	while (true) //c4
	{
		switch (dayOfWeek)
		{
		    case 1:
		        Console.WriteLine("星期一");
		        break;
		    case 2:
		        Console.WriteLine("星期二");
		        break;
		    case 3:
		        Console.WriteLine("星期三");
		        break;
		    // 更多情况...
		    default:
		        Console.WriteLine("输入的数字不在范围内");
		        break;
		}
		//c1
		//...
		if (xxxx){break;}
	    //c3
	    //...
	}
	//c2
	//...

```




---
## 练习
- **复习**
	- [[OOP设计-0202-控制输出|控制台输出]]
- **知识串讲**
	- [[OOP设计-0202-控制输入|控制台输入]]
	- [[OOP设计-0302-类型转换]]

![[OOP设计-0401-判断语句-作业]]

---
## 日志
- 创建时间
	- 2023年10月22日 13:57:20
- 变更时间
	