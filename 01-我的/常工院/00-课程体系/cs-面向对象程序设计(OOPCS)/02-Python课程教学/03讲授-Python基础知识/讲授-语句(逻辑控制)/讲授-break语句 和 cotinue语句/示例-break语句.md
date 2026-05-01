---
tags: [工具]
description: numbers = [5, 8, 12, 3, 15]
type: note
create-date: 2026-04-29
---

### 示例
```python
# 示例：查找列表中第一个大于10的数字，找到后停止循环 
numbers = [5, 8, 12, 3, 15] 
for num in numbers: 
	if num > 10: 
		print(f"找到目标数字：{num}") 
		break # 终止循环，后续数字不再检查
	print(f"当前数字：{num}") 
```
### 结果分析
```
当前数字: 5
当前数字: 8
找到目标数字：12
```
