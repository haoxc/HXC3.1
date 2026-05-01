---
tags: [工具]
description: import json
type: note
create-date: 2026-04-29
---

### Python 对象 → JSON 文件（`dump`）

```python
import json

data = {
    "video_name": "旅行记录",
    "duration": 360,
    "resolution": "4K",
    "chapters": ["出发", "沿途", "终点"]
}

# 打开文件，将数据写入为 JSON 格式
with open("video_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON 文件写入完成！")
```

执行后，当前目录会生成 `video_info.json` 文件，内容为格式化的 JSON 数据。

---
### JSON 文件 → Python 对象（`load`）
假设已有 `user_data.json` 文件，内容如下：
```json
{
  "username": "小明",
  "age": 20,
  "preferences": ["摄影", "编程"],
  "settings": {"theme": "dark", "notifications": true}
}
```

读取并解析该文件：
```python
import json

# 打开文件，读取 JSON 内容并转为 Python 对象
with open("user_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"用户名：{data['username']}")  # 输出：用户名：小明
print(f"第一个偏好：{data['preferences'][0]}")  # 输出：第一个偏好：摄影
print(f"主题设置：{data['settings']['theme']}")  # 输出：主题设置：dark
```

---
### 注意事项
- JSON 中的键必须是 `字符串`，Python 字典中非字符串类型的键（如整数）会被自动转为字符串。
- JSON 不支持 Python 元组（tuple），`dumps` 会自动将元组转为列表（list）。
- 处理中文时，需在 `dumps` / `dump` 中指定 `ensure_ascii=False`，并在文件操作中设置 `encoding="utf-8"`，否则中文可能被转义。
- 复杂嵌套的 JSON 数据（如多层字典 / 列表），可通过循环或递归遍历，操作方式与处理 Python 嵌套字典 / 列表一致。
