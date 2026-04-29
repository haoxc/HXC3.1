---
aliases: oop-C#Variable/Types/enum, 枚举类型(enum)
---

## 概要
- 枚举是一组命名整型常量。枚举类型是使用 **enum** 关键字声明的。
- C# 枚举是`值类型`。换句话说，枚举包含自己的值，且不能继承或传递继承。
- `枚举列表`中的每个符号代表一个`整数值`，一个比它前面的符号大的整数值
## 声明
声明枚举的一般语法：
```csharp
	enum <enum_name>
	{ 
	    enumeration list 
	};
```
其中，
- _enum_name_ 指定枚举的类型名称。
- _enumeration list_ 是一个用逗号分隔的标识符列表。

## 示例
```csharp
	enum Weeks{
		Sun,
		Mon,
		Tue,
		Wed,
		Thu,
		Fri,
		Sta
	};
```

下面的实例演示了枚举变量的用法：
```csharp
enum Day { Sun, Mon, Tue, Wed, Thu, Fri, Sat };  
enum Gender {
	Male,
	Female,
}
  
static void Main()  
{  
	int x = (int)Day.Sun;  
	int y = (int)Day.Fri;  
	Console.WriteLine("Sun = {0}", x);  
	Console.WriteLine("Fri = {0}", y);  
}
```



---
## 日志
- 创建时间
	- 2023年11月16日 20:30:13
- 变更时间
	