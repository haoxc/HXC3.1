---
aliases: oop-c#@howtos/How to set the main entry,MainEntry-StartupObject
type: note
tags: [工具]
description: > [C# 编译器选项 - 高级方案 - C# | Microsoft Learn](https://learn.microsoft.com/zh-cn/dot
create-date: 2026-04-29
---
## 概要
> [C# 编译器选项 - 高级方案 - C# | Microsoft Learn](https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/compiler-options/advanced#mainentrypoint-or-startupobject)

###  编辑项目配置文件
- 通过以下操作
	- ![[Pasted image 20231001144304.png|600]]
在 `*.csproj` 文件中的 `<PropertyGroup>` 元素中添加以下任一选项：
```xml
<PropertyGroup>
    <StartupObject>...</StartupObject>
    ...
</PropertyGroup>
```

## MainEntryPoint 或 StartupObject
如果多个类包含 `Main` 方法，此选项将指定包含程序入口点的类。
```xml
<StartupObject>MyNamespace.Program</StartupObject>
```

或
```xml
<MainEntryPoint>MyNamespace.Program</MainEntryPoint>
```
其中 `Program` 是包含 `Main` 方法的类型。 提供的类名必须是完全限定类名；它必须包括完整命名空间（包含类），后跟类名。 例如，当 `Main` 方法位于 `MyApplication.Core` 命名空间中的 `Program` 类中时，编译器选项必须为 `-main:MyApplication.Core.Program`。 如果编译包含具有 [`Main`](https://learn.microsoft.com/zh-cn/dotnet/csharp/fundamentals/program-structure/main-command-line) 方法的多个类型，则可以指定哪个类型包含 `Main` 方法。

## 日志
- 创建时间
	- 2023年10月1日 14:39:03
- 变更时间
	