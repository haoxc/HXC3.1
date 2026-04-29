---
Type: course
importance:
status:
aliases:
  - if语句
orderNo: 110
subject: Python基础
category:
  - python/基础知识/语句
---
#必考

# 分支
- **基础知识**
	- 单条件判断 ^rNqoVTjh
	- 二次条件判断
	- 多条件判断
- **进阶知识**
	- 嵌套
	- **math-case**（配置值，匹配类型，匹配结构） 
---
## 意图
![[Pasted image 20220428114706.png|400]]
- Python条件语句是通过一条或多条语句的执行结果（​`True`​或者​`False`​）来决定执行的代码块。
- 可以通过下图来简单了解条件语句的执行过程:


---
## 语法

### 单条件
语法:
```python
if 条件：
	执行语句
#...
```
---
### 二次条件

```python
if 条件1：
	#满足条件1代码块
	执行语句
else：
	#不满足条件1代码块
	执行语句
```


---
### 多条件 


```python
if 条件1：
	#满足条件1代码块
	执行语句
elif 条件2:
	#满足条件2代码块
	执行语句+
elif 条件3：
	#..
else：
	#其他条件的代码块
	执行语句
```

---
## 实践


-  **实践 1**： ![[场景1-用户登录验证（if-elif-else）#要求]]
>  提交答案地址 : https://3willartlab.feishu.cn/share/base/form/shrcnEdQ8HTDHeWKtQvqcpsOL4f
 
- ---
- **实践 2**：
	- ![[场景 2-商品折扣计算（if-elif-else）#要求]]
		- float (xxx)
---
💡 小贴士（给初学者）
	•	缩进是灵魂：Python 完全靠缩进定义代码块，错误缩进会直接报错。
	•	[[py-逻辑表达式|逻辑运算符]]： and （且）、 or （或）、 not （非）是组合条件的关键。
	•	先写简单版：从单个  if  开始，逐步添加  elif  和  else 。


