---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-04-29
---
## 内容
这两个概念是 Python Web 开发的两大基石，决定了框架处理请求的底层逻辑和并发上限。
简单来说：WSGI 是“排队办业务”，ASGI 是“取号等通知”。
## 1. WSGI (Web Server Gateway Interface)
- 诞生背景：2003 年发布，旨在标准化 Python Web 框架（如 Flask, Django）与 Web 服务器（如 Gunicorn, uWSGI）之间的通信。
- 工作模式：同步 (Synchronous)。
    - 一个工作进程/线程在同一时间只能处理一个请求。
    - 如果请求涉及数据库查询或调用第三方 API，该线程会阻塞（卡住）等待返回。
- 局限性：无法原生处理长时间连接，如 WebSocket、服务器推送 (SSE) 或高并发的 I/O 密集型任务。
- 代表框架：Flask, Django (传统模式), Bottle。

## 2. ASGI (Asynchronous Server Gateway Interface)
- 诞生背景：WSGI 的精神继承者，为了支持现代 Web 的异步 (Async) 需求。
- 工作模式：异步 (Asynchronous)。
    - 基于 `async/await`。当请求在等待 I/O 时，服务器可以挂起该任务，转而处理其他请求。
    - 单进程即可处理成千上万的并发连接。
- 核心优势：原生支持 WebSocket、HTTP/2，非常适合实时聊天、高频 API 和长连接场景。
- 代表框架：FastAPI, Starlette, Sanic, Django (3.0+ 异步部分)。

---

## 3. 直观对比总结

|特性|WSGI|ASGI|
|---|---|---|
|并发模型|同步 / 阻塞|异步 / 非阻塞|
|通信协议|仅限 HTTP|HTTP, WebSocket, HTTP/2|
|性能|适合 CPU 密集或低并发|适合 I/O 密集或高并发|
|服务器|Gunicorn, uWSGI, Mod_wsgi|Uvicorn, Daphne, Hypercorn|
|代码风格|简单直观的命令式代码|需要掌握 `async/await` 语法|

## 4. 我该选哪种？
- 选 WSGI (Flask/Django)：如果你的应用是传统的 CRUD（增删改查），并发量不是天文数字，且你更追求开发的简单性和庞大的第三方插件生态。
- 选 ASGI (FastAPI/Quart)：如果你需要处理实时通讯（WebSocket）、大量并发请求，或者希望在机器学习模型推理等 I/O 密集场景中榨干服务器性能。
 