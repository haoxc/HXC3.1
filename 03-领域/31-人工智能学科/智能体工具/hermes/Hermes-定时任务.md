---
aliases: [cronjob, 定时任务, 计划任务, Hermes调度]
tags: [mac-工具, AI工具, Agent, Hermes]
description: Hermes cronjob 定时任务的创建、管理、调试操作指南。
type: note
create-date: 2026-05-02
---

# Hermes 定时任务

## 一句话

`cronjob` 是 Hermes 内置的跨会话任务调度器：它让 Agent 任务在指定时间自动执行，不依赖当前会话存活。

## 与后台进程的区别

|      | 定时任务             | 后台进程                   |
| ---- | ---------------- | ---------------------- |
| 触发方式 | 计划（cron/crontab） | 即时                     |
| 生命周期 | 跨会话独立运行          | 当前会话                   |
| 使用工具 | `cronjob`        | `terminal` + `process` |
| 适用   | 周期性自动化           | 单次异步执行                 |

后台进程详见 [[Hermes-后台进程管理]]。

## 核心操作

| 操作   | 命令                                      | 说明     |
| ---- | --------------------------------------- | ------ |
| 创建   | `cronjob(action="create", ...)`         | 新建任务   |
| 列出   | `cronjob(action="list")`                | 查看所有任务 |
| 更新   | `cronjob(action="update", job_id, ...)` | 修改已有任务 |
| 暂停   | `cronjob(action="pause", job_id)`       | 暂停调度   |
| 恢复   | `cronjob(action="resume", job_id)`      | 恢复调度   |
| 删除   | `cronjob(action="remove", job_id)`      | 删除任务   |
| 手动运行 | `cronjob(action="run", job_id)`         | 立即执行一次 |

> 删除前必须先用 `list` 确认 job_id，禁止猜测 ID。

## 创建示例

### 一次性任务

```
cronjob(
  action="create",
  prompt="运行 pjx-common-auditor 审计 vault 并生成报告",
  schedule="2026-05-03T09:00:00",
  name="审计报告",
)
```

### 周期任务

```
cronjob(
  action="create",
  prompt="检查 gbrain sync 状态并通知异常",
  schedule="0 9 * * *",       # 每天 9:00
  name="gbrain健康检查",
  repeat=0,                    # 0 = 无限重复
  skills=["gbrain"],           # 加载技能
)
```

### 链式任务

```
cronjob(
  action="create",
  prompt="处理上游数据并生成摘要",
  schedule="every 2h",
  name="数据处理",
  context_from=["job_abc123"], # 注入上游任务输出
)
```

## 调度表达式

| 格式 | 示例 | 含义 |
|------|------|------|
| 相对时间 | `30m`, `every 2h`, `every 1d` | 间隔执行 |
| Cron 表达式 | `0 9 * * *` | 每天 9:00 |
| ISO 时间戳 | `2026-05-03T09:00:00` | 一次性到期 |

## 高级参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `skills` | `string[]` | 加载的技能列表，按顺序加载 |
| `model` | `{provider, model}` | 覆盖默认模型 |
| `script` | `string` | 执行前运行的 Python 脚本路径，stdout 注入为上下文 |
| `context_from` | `string[]` | 注入其他任务的最近完成输出 |
| `enabled_toolsets` | `string[]` | 限制可用工具集（减少 token 开销） |
| `workdir` | `string` | 工作目录（必须是绝对路径，存在） |

### 精简工具集示例

```
enabled_toolsets=["web", "terminal", "file", "skills"]
```

仅加载指定工具集，显著减少输入 token。推断原则：用 `web_search` → `web`，用脚本 → `terminal`，读文件 → `file`，用 delegate → `delegation`。

## 注意事项

- 定时任务运行在**独立会话**中，无当前聊天上下文，prompt 必须**自包含**。
- 任务执行中**不能提问或请求澄清**，所有逻辑必须在 prompt 中预先定义。
- 安全规则：cron 会话**禁止递归创建新的 cron 任务**。
- `workdir` 下的任务**串行执行**（不在并存），保证目录隔离。
- 修改配置/技能后记得用 `update` 同步，否则任务继续使用旧上下文。
