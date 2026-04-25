## 要求
编写计算折扣的程序，根据输入的消费金额计算 `打折额度` ，并折扣数值
- 不少于500 时，8 折
- 不少于 300 时，8.5 折
- 不少于 100 时，9折

---
## 程序

```python
# 根据消费金额计算折扣
amount = float(input("请输入消费金额（元）："))

if amount >= 500:
    discount = 0.8  # 满500元打8折
elif amount >= 300:
    discount = 0.85  # 满300元打85折
elif amount >= 100:
    discount = 0.9  # 满100元打9折
else:
    discount = 1.0  # 无折扣

final_price = amount * discount
print(f"折扣后价格：{final_price:.2f} 元")
```

### 🔍 关键点：

- **阶梯式判断**：按金额范围逐级判断。
- **浮点数处理**：输入金额为小数，需用 `float()` 转换。
- **格式化输出**：`:.2f` 保留两位小数。