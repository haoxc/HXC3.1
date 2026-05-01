---
tags: [工具]
description: void Test(string element, int count)
type: note
create-date: 2026-04-29
---

```csharp

void Test(string element, int count)
{
	
	for (int i =0; i< count; i++)
	{
		for(int j =0; j< i; j++)
		{
			Console.Write($"{element}");
		}
	}
	Console.WriteLine();
}

Test("*",4);

```



```csharp

void Test(string element)
{
	
	for (int i =0; i< 8; i+=2)
	{
		for(int j =0; j< i; j++)
		{
			Console.Write($"{element}");
		}
		Console.WriteLine();
	}
	
}

Test("*");

```




```csharp

void Test(string element,int count)
{
	
	for (int i = count; i>=0; i--)
	{
		if(i%2 ==0){
			continue;
		}
		for(int j =0; j< i; j++)
		{
			Console.Write($"{element}");
		}
		Console.WriteLine();
	}
	
}

Test("#",10);

```



```csharp

void Test(string element,int count)
{
	
	for (int i = count; i>=0; i--)
	{
		
		for(int j =0; j< i; j++)
		{
			if(i%2 ==0  && j%2!=0){
				Console.Write($"{element}");
			}
		}
		Console.WriteLine();
	}
	
}

Test("#",8);

```
