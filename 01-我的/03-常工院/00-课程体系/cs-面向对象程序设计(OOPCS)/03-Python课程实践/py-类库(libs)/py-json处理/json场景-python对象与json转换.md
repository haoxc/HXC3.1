### Python 对象 → JSON 字符串（`dumps`）
-   **存档**: 把游戏场景中所有的对象转换为 json 格式, 用于数据存档, 数据交换; ( #能力/数据处理/序列化  )
 -  **目标**: Python 对象 → JSON 字符串（`dumps`）

**示例**:
```python
import json

# 定义一个包含嵌套结构的 Python 字典
data = {
    "name": "图片配置",
    "size": {"width": 1080, "height": 1920},
    "format": "png",
    "is_valid": True,
    "tags": ["风景", "高清"]
}

# 转换为 JSON 字符串（保留中文+格式化输出）
json_str = json.dumps(data, ensure_ascii=False, indent=2)
# 参数说明：
# - ensure_ascii=False：避免中文被转义为 Unicode 编码  
# - indent=2：按 2 空格缩进，美化输出格式  

print(json_str)
```

> 💡 和字典定义结构非常类似

 结果:
 ```json
{
  "name": "图片配置",
  "size": {
    "width": 1080,
    "height": 1920
  },
  "format": "png",
  "is_valid": true,
  "tags": [
    "风景",
    "高清"
  ]
}
```

---
### JSON 字符串 → Python 对象（`loads`）
```python
import json

# 定义一个 JSON 字符串
json_str = '''
{
  "audio_name": "背景音乐",
  "duration": 180,
  "bitrate": 320,
  "metadata": null
}
'''

# 转换为 Python 字典
data = json.loads(json_str)

print(type(data))  # 输出：<class 'dict'>
print(data["audio_name"])  # 输出：背景音乐
print(data["metadata"])    # 输出：None（对应 JSON 的 null）
```

