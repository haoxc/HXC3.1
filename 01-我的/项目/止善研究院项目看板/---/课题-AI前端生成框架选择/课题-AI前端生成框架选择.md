---
aliases:
tags:
  - ai/课题/工具链/前端框架
type: note
description: -  Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2模板引擎。Flask使用BSD授权。 Fla
create-date: 2026-04-29
---
## 前端框架备选
-  Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2模板引擎。Flask使用BSD授权。 Flask被称为“微框架”，因为它使用简单的核心，用扩展增加其他功能。Flask没有默认使用的数据库、表单验证工具。(同步框架)

### 性能比较

| 框架          | 类型            | 吞吐量 (RPS)        | 平均延迟      | 优势场景                        |
| ----------- | ------------- | ---------------- | --------- | --------------------------- |
| **Flask**   | 同步 ([[WSGI, ASGI]]) | ≈ 1,000 - 3,000  | ~7.7 ms   | 简单原型、内部管理后台、传统单体应用          |
| **FastAPI** | 异步 (ASGI)     | ≈ 9,000 - 20,000 | ~11-21 ms | 高并发 API、机器学习模型部署、WebSockets |
| **Quart**   | 异步 (ASGI)     | ≈ 9,000          | -         | 需要 Flask 语法但想用异步的场景         |
| **Django**  | 同步/异步混血       | ≈ 950 - 3,000    | ~8.8 ms   | 大型全功能 Web 应用                |
