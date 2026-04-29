---
aliases: 数字类型(number)
---
*创建时间*：2022年5月3日 17:44:08

### 数字类型要点
- 定义
	- **三种数字类型**
		- int，float，complex
- 转换函数
	- `int()`, `float() `
- [[py-算术表达式|数值运算]]
---
## 内容
### 定义
为变量赋值时，将创建数值类型的变量：

```python
x =100 #整数(int)
y =6.5 #浮点型（float）
z= 2j   #Complex
```

### 类型转换
，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
- **int(x)** 将x转换为一个整数。
- **float(x)** 将x转换到一个浮点数。
- **complex(x)** 将x转换到一个复数，实数部分为 x，虚数部分为 0。
- **complex(x, y)** 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
### 验证
```python
#输出变量x,y,z类型
print(type(x))
print(type(y))
print(type(z))
```
### 格式化

```python
import math

r = 5  # 圆的半径
area = math.pi * r **2  # 面积公式：πr²
circumference = 2 * math.pi * r  # 周长公式：2πr

print(f"半径为{r}的圆：")
print(f"面积 = {domain:.2f}")  # 保留2位小数，输出：78.54
print(f"周长 = {circumference:.2f}")  # 保留2位小数，输出：31.42
```
### 操作
[[py-运算符(operator)]] 
``` python
+, -, *, / ,++,--,%, 
#返回浮点数
/  
#返回整数

详细参照 