### 缩进
- `缩进`指的是**代码行开头**的空格。
- Python 使用缩进来指示**代码块**。

示例代码
```python
# 画一朵花（缩进表示画花瓣的层次）
def draw_flower():
    for i in range(36):  # 画36个花瓣
        turtle.circle(50)  # 画一个圆
        turtle.right(10)   # 旋转10度
```