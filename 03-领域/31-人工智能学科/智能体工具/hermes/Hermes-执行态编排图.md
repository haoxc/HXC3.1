---
title: Hermes 执行态编排图
aliases:
  - Hermes 执行态编排
  - Hermes Runtime Orchestration
  - Hermes 运行时编排图
tags:
  - mac-工具
  - AI工具
  - Hermes
  - 工作流
created: 2026-04-29
description: 用一张 SVG 图说明 Hermes 在运行时如何从入口事件进入 Gateway、Cron 或 CLI，会话如何加载上下文和 skill，并调度工具、模型与外部执行器。
diagram_type: runtime-orchestration
diagram_format: svg
create-date: 2026-04-29
type: note
---
# Hermes 执行态编排图

![[Hermes-执行态编排图.svg]]

## 阅读口径

- 入口事件：来自 CLI/TUI、Gateway 消息、Cron 到期任务、Webhook、外部系统或人工触发。
- 调度入口：CLI/TUI Runtime 负责交互会话，Gateway Daemon 负责消息平台与后台调度，Cron Scheduler 负责定时任务。
- 会话装配：Hermes 创建 fresh 或 resumed AIAgent session，并装入 prompt、上下文、memory、skill、模型配置、工具清单和权限边界。
- 决策执行：Planner 先识别意图，再选择 skill、工具、模型和外部执行器。
- 结果交付：执行结果回到消息通道、文件、日志、状态库或外部系统。

> [!summary]
> 执行态编排关注“任务实际如何跑起来”：入口负责触发，Gateway/Cron 负责调度，AIAgent Session 负责装配上下文与 skill，Planner 负责路由，工具、模型和外部 agent 负责落地。
