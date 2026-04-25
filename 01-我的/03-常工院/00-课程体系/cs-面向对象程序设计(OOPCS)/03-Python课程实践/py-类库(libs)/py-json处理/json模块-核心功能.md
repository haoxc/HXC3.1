
###  内置模块-json核心方法
python 内置 [[json概述|json]] 模块

| 方法             | 作用                       | 输入                | 输出        |
| -------------- | ------------------------ | ----------------- | --------- |
| `json.dumps()` | 将 Python 对象转为 JSON 字符串   | Python 对象（字典、列表等） | JSON 字符串  |
| `json.dump()`  | 将 Python 对象转为 JSON 并写入文件 | Python 对象 + 文件对象  | 无（写入文件）   |
| `json.loads()` | 将 JSON 字符串转为 Python 对象   | JSON 字符串          | Python 对象 |
| `json.load()`  | 从文件读取 JSON 并转为 Python 对象 | 文件对象              | Python 对象 |