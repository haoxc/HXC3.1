---
aliases: oop-C#@Statement/OOP/access modifier(fwxsf访问修饰符), 访问修饰符
---

## 访问修饰符
![](https://www.runoob.com/wp-content/uploads/2014/04/csharp-public.png)
- 在类、方法、属性、字段或其他成员之前使用 `public` 修饰符时，它意味着该成员是公共的，可以从任何其他类或成员方法访问。
- 可以为: *public,internal, protected, private*
- **类**
	- 默认情况下，类不是公共的。
	- 如果你想从其他程序集中的类访问某个类，则需要明确将其标记为 `public`。
- **成员**
	- 除非另有说明，否则类的成员（如字段和方法）不是公共的。
	- 如果您想从类的外部访问它们，您必须明确地标记它们为 `public`。


- `public`：所有对象都可以访问；
- `private`：对象本身在对象内部可以访问；
- `protected`：只有该类对象及其子类对象可以访问
- `internal`：同一个程序集的对象可以访问；
- `protected internal`：访问限于当前程序集或派生自包含类的类型。

## 日志
- 创建时间
	- 2023年11月6日 15:51:16
- 变更时间
	