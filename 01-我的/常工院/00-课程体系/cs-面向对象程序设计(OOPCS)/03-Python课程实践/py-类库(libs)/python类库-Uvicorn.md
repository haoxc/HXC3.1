---
aliases:
  - web服务器
type: note
tags: [工具]
description: Uvicorn 是 Python 高性能**异步 ASGI 服务器**，专门用于运行 FastAPI、Starlette 等异步 Web 框架，是数媒生搭建素材
create-date: 2026-04-29
---
# Uvicorn 完全解析（FastAPI 配套服务器，数媒场景适配）
Uvicorn 是 Python 高性能**异步 ASGI 服务器**，专门用于运行 FastAPI、Starlette 等异步 Web 框架，是数媒生搭建素材管理 API、设计工具后端的核心工具。核心优势：轻量、异步高并发、热重载（开发超方便）。

## 一、核心认知：Uvicorn 是什么？
| 维度      | 说明                                               |
| ------- | ------------------------------------------------ |
| 定位      | FastAPI 官方推荐的`运行服务器`（FastAPI 是框架，Uvicorn 是“发动机”） |
| 核心特性    | 异步处理（适合数媒文件上传/素材解析）、热重载（改代码不用重启）、跨平台             |
| 对比传统服务器 | 比 Flask/Django 自带的 WSGI 服务器快，支持并发处理多素材上传/查询      |
|         |                                                  |

## 二、基础操作：安装 + 核心命令
### 1. 安装（复用 pip 语法）
```bash
# 单独安装
pip install uvicorn
# 安装完整版（含加速依赖，推荐数媒场景）
pip install uvicorn[standard]
```

### 2. 核心运行命令（结合数媒素材 API 示例）
假设你的 FastAPI 代码文件是 `main.py`（含 `app = FastAPI()`），核心命令如下：

| 场景               | 命令                                                                 | 数媒场景说明                     |
|--------------------|----------------------------------------------------------------------|----------------------------------|
| 本地开发（热重载） | `uvicorn main:app --host 127.0.0.1 --port 8000 --reload`             | 改代码自动重启，调试素材 API 超方便 |
| 局域网访问         | `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`               | 团队成员可访问你的素材 API       |
| 生产环境（多进程） | `uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4`            | 处理多用户并发上传素材           |

#### 命令参数解析（数媒生常用）
| 参数         | 作用                                                                 |
|--------------|----------------------------------------------------------------------|
| `main:app`   | 指定运行的应用：`main` = 文件名，`app` = 文件内的 FastAPI 实例名       |
| `--host`     | 绑定 IP：`127.0.0.1` 仅本地访问，`0.0.0.0` 局域网/外网可访问          |
| `--port`     | 端口号（默认 8000），冲突时改 `--port 8001`                          |
| `--reload`   | 热重载（开发专用），修改代码自动重启服务器                           |
| `--workers`  | 进程数（生产环境用），建议设为 CPU 核心数（如 `--workers 4`）         |

## 三、数媒场景实战：两种运行方式
### 方式 1：命令行运行（推荐开发/部署）
```bash
# 运行数媒素材管理 API（热重载 + 局域网访问）
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
运行后输出示例（成功标志）：
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
INFO:     Started server process [12347]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
此时可访问：
- API 文档：http://127.0.0.1:8000/docs
- 素材接口：http://127.0.0.1:8000/materials/

### 方式 2：代码内运行（一体化，适合打包）
把 Uvicorn 运行逻辑写进 `main.py`，双击即可运行（数媒生不用记命令）：
```python
# main.py（完整数媒素材 API + 内置 Uvicorn 运行）
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="数媒素材管理 API")

# 素材接口示例
@app.get("/materials/")
def get_materials():
    return {"data": ["海报.png", "背景音乐.mp3", "宣传视频.mp4"]}

# 内置运行逻辑
if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # 应用路径
        host="0.0.0.0",
        port=8000,
        reload=True  # 开发模式开启热重载
    )
```
运行方式：直接执行 `python main.py`，效果和命令行一致。

## 四、数媒场景避坑指南
### 1. 端口被占用（最常见）
- 报错：`OSError: [Errno 48] Address already in use`
- 解决：换端口（如 `--port 8001`），或杀掉占用端口的进程：
  ```bash
  # Windows 查找并杀掉占用 8000 端口的进程
  netstat -ano | findstr :8000  # 找到 PID（如 1234）
  taskkill /F /PID 1234         # 杀掉进程
  ```

### 2. 热重载（--reload）不生效
- 原因：修改的文件不在当前目录，或用了绝对导入
- 解决：确保运行命令的目录是 `main.py` 所在目录，或指定 `--reload-dir ./`（监控当前目录）。

### 3. 局域网访问不了
- 原因：`host` 设为 `127.0.0.1`，或防火墙拦截
- 解决：
  1. 命令用 `--host 0.0.0.0`；
  2. 关闭 Windows 防火墙（或放行 8000 端口）；
  3. 用本机局域网 IP 访问（如 `http://192.168.1.100:8000`）。

### 4. 文件上传时报错（数媒专属）
- 原因：上传目录无权限，或文件过大
- 解决：
  1. 提前创建 `uploads` 文件夹，并确保有读写权限；
  2. 增加 FastAPI 最大文件限制：
     ```python
     from fastapi import FastAPI, UploadFile, File
     from fastapi.middleware.cors import CORSMiddleware

     app = FastAPI()
     # 允许大文件上传（100MB）
     app.add_middleware(
         CORSMiddleware,
         allow_origins=["*"],
         allow_methods=["*"],
         allow_headers=["*"],
     )
     # 上传接口设置最大尺寸
     @app.post("/upload")
     async def upload(file: UploadFile = File(..., max_length=100*1024*1024)):
         pass
     ```

## 五、进阶：Uvicorn + 配置文件（生产环境）
数媒项目部署时，可创建 `uvicorn_config.py` 统一管理配置，避免记复杂命令：
```python
# uvicorn_config.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,  # 4进程处理并发
        log_level="info",  # 日志级别
        access_log=True,  # 记录访问日志（便于排查素材上传问题）
        limit_concurrency=100,  # 最大并发数（防止服务器过载）
        limit_max_requests=1000,  # 每个进程最大处理请求数
    )
```
运行：`python uvicorn_config.py`。

## 六、数媒场景总结
Uvicorn 是 FastAPI 的“最佳搭档”，数媒生只需掌握 3 个核心操作：
1. 本地开发：`uvicorn main:app --reload`；
2. 团队调试：`uvicorn main:app --host 0.0.0.0 --reload`；
3. 简单部署：`uvicorn main:app --host 0.0.0.0 --workers 4`。

结合之前的 FastAPI 素材 API，可快速搭建：
- 素材上传/解析接口（自动识别图片分辨率、音频时长）；
- 团队素材库查询接口；
- 设计工具的后端服务（如批量处理素材）。

如果需要整合 Uvicorn + FastAPI + 之前的 `Material` 类（自动解析上传素材的分辨率/时长），我可以补充完整的可运行代码。