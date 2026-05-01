---
aliases:
type: note
tags: [工具]
description: - 在 C# 中，接口（`Interface`）是一种定义不含任何实现的方法、属性、索引器和事件的合约。
create-date: 2026-04-29
---
## 概要
- 在 C# 中，接口（`Interface`）是一种定义不含任何实现的方法、属性、索引器和事件的合约。
- 接口为类与类之间的交互提供了`规范的方式`，确保实现接口的类遵循特定的行为模式。
- 接口是实现多态和解耦的关键工具。

## 接口的特性
1. **仅声明，无实现**：接口只能声明成员，不能实现它们。
2. **成员是隐式公共的**：接口中声明的所有成员都是公共的，不能指定访问修饰符。
3. **可以包含方法、属性、事件和索引器**：但这些成员都不会有任何实现。
4. **支持多重继承**：一个类可以实现多个接口，而C#不支持类的多重继承。
5. **实现类必须实现接口的所有成员**：类实现接口时，必须提供所有接口成员的具体实现。

## 接口定义
![[Pasted image 20231116222807.png|400]]


```csharp
public interface IMediaPlayer
{
    void Play();
    void Pause();
}

public class AudioPlayer : IMediaPlayer
{
    public void Play()
    {
        Console.WriteLine("Playing audio");
    }

    public void Pause()
    {
        Console.WriteLine("Pausing audio");
    }
}

public class VideoPlayer : IMediaPlayer
{
    public void Play()
    {
        Console.WriteLine("Playing video");
    }

    public void Pause()
    {
        Console.WriteLine("Pausing video");
    }
}

class Program
{
    static void Main()
    {
        IMediaPlayer[] players = new IMediaPlayer[] { new AudioPlayer(), new VideoPlayer() };

        foreach (var player in players)
        {
            player.Play();
            player.Pause();
        }
    }
}

```

## 日志
- 创建时间
	- 2023年11月16日 22:24:00
- 变更时间
	