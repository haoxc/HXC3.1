---
tags: [工具]
description: username = input("请输入用户名：")
type: note
create-date: 2026-04-29
---

## 🎯 场景 1：用户登录验证（if-elif-else）

```python
# 模拟用户登录验证
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "admin" and password == "123456":
    print("登录成功！欢迎管理员。")
elif username == "user" and password == "654321":
    print("登录成功！欢迎普通用户。")
else:
    print("用户名或密码错误，登录失败。")
```

### 🔍 关键点：
- **`and` 运算符**：同时判断用户名和密码。
- **多条件分支**：区分管理员和普通用户。
- **缩进规则**：每个 `if/elif/else` 对应的代码块需统一缩进。
