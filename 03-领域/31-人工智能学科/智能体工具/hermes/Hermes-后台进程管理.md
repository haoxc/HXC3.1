---
aliases: [后台进程管理, Hermes进程管理, background任务]
tags: [mac-工具, AI工具, Agent, Hermes]
description: Hermes terminal 后台进程的启动、监控、等待与终止操作指南。
type: note
create-date: 2026-05-02
---

# Hermes 后台进程管理

## 一句话

`terminal(background=true)` 将耗时命令投递到后台，通过 `process` 工具管理生命周期。适用于构建、测试套件、长时间脚本等需要异步执行的场景。

## 两种后台模式

| 模式 | 适用场景 | 参数 |
|------|----------|------|
| 长期服务 | 服务器、watcher，永不退出 | `background=true` |
| 一次性任务 | 测试、构建、批量处理，有明确结束 | `background=true, notify_on_complete=true` |

> 短期命令用前台 + timeout 即可，不需要 background。

## 启动

```
terminal(command="npm test", background=true, notify_on_complete=true)
```

返回 `session_id`，后续所有 process 操作都以此 ID 定位。

## 生命周期管理

| 操作 | process action | 说明 |
|------|----------------|------|
| 查看所有进程 | `list` | 列出所有活跃后台进程 |
| 查看进度 | `poll(session_id)` | 获取最新输出 + 状态 |
| 查看完整日志 | `log(session_id)` | 分页查看全部输出 |
| 阻塞等待 | `wait(session_id, timeout=N)` | 阻塞直到完成或超时 |
| 终止 | `kill(session_id)` | 终止进程 |
| 发送输入 | `write(session_id, data)` | 写入 stdin（不含换行） |
| 发送输入+回车 | `submit(session_id, data)` | 写入 stdin + Enter |
| 关闭 stdin | `close(session_id)` | 发送 EOF |

## 典型工作流

### 异步构建 + 继续工作

```
# 1. 启动构建
terminal("cargo build --release", background=true, notify_on_complete=true)
# → session_id: "abc123"

# 2. 继续做其他事...

# 3. 系统自动通知构建完成
```

### 监控进度

```
process(action="poll", session_id="abc123")
# 返回最新输出 + 运行/完成/失败状态
```

### 等待完成

```
process(action="wait", session_id="abc123", timeout=600)
# 阻塞 600 秒，完成后返回完整输出
```

## 限制

| 限制 | 值 |
|------|-----|
| foreground timeout 上限 | 600 秒 |
| 超过 600 秒的任务 | 必须用 background=true |
| PTY 模式 | 仅 local/SSH backend 支持 |

## 与 cronjob 的区别

| | 后台进程 | 定时任务 |
|------|----------|----------|
| 触发方式 | 即时 | 计划（cron/crontab） |
| 生命周期 | 当前会话 | 跨会话独立运行 |
| 使用工具 | `terminal` + `process` | `cronjob` |
| 适用 | 单次异步执行 | 周期性自动化 |

定时任务详见 [[Hermes-定时任务]]。

## 注意事项

- 不要在前台命令中使用 `nohup`/`disown`/`setsid`/`&` —— 用 `background=true` 替代，Hermes 才能追踪生命周期。
- `notify_on_complete` 和 `watch_patterns` 互斥，选一个设置。
- 后台进程数量无硬限制，但建议不超过 5 个并发以避免混乱。
