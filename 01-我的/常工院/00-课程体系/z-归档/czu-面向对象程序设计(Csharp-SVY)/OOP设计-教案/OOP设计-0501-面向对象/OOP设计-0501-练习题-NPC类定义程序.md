---
aliases:
type: note
tags: [工具]
description: using System;
create-date: 2026-04-29
---
## 程序

```csharp
using System;

public class NPC
{
    // NPC的基本属性
    public string Name { get; set; }
    public int Level { get; set; }
    public float Health { get; set; }
	private  float x;
	private  float y;
	
    // 构造函数初始化NPC
    public NPC(string name, int level, float health, float x, float y, float z)
    {
        Name = name;
        Level = level;
        Health = health;
        Position = (x, y, z);
    }

    // NPC可以说话的方法
    public void Talk(string message)
    {
        Console.WriteLine($"{Name} says: {message}");
    }

    // NPC可以移动到新位置的方法
    public void Move(float newX, float newY)
    {
        this.x = newX;
        this.y = newY;
        Console.WriteLine($"{Name} has moved to a new position at ({newX}, {newY}, {newZ}).");
    }

    // NPC受到伤害的方法
    public void TakeDamage(float damage)
    {
        Health -= damage;
        Console.WriteLine($"{Name} has taken {damage} points of damage.");
    }

    // NPC进行治疗的方法
    public void Heal(float healingAmount)
    {
        Health += healingAmount;
        Console.WriteLine($"{Name} has healed {healingAmount} points of health.");
    }
}

class Program
{
    static void Main()
    {
        // 创建一个NPC对象
        NPC guard = new NPC("Guardian", 10, 100.0f, 0.0f, 0.0f, 0.0f);

        // 使用NPC的方法
        guard.Talk("Welcome, traveler!");
        guard.Move(10.0f, 0.0f, 5.0f);
        guard.TakeDamage(25.0f);
        guard.Heal(10.0f);
    }
}

```


## 日志
- 创建时间
	- 2023年11月10日 09:52:10
- 变更时间
	