---
title: Hermes 典型应用场景逻辑架构图
aliases:
  - Hermes 应用场景架构图
  - Hermes 逻辑架构图
  - Hermes 场景架构
tags:
  - mac-工具
  - AI工具
  - Hermes
  - 工作流
created: 2026-04-29
description: 用一张 SVG 图说明 Hermes 在入口触发、核心编排、典型应用场景、底层执行资源与模型服务之间的逻辑关系。
diagram_type: logical-architecture
diagram_format: svg
create-date: 2026-04-29
type: note
---
# Hermes 典型应用场景逻辑架构图

![[Hermes-典型应用场景逻辑架构图.svg]]

## 阅读口径

- 入口与触发场景：说明 Hermes 可以从 CLI/TUI、Gateway、Cron、Webhook 等入口被触发。
- Hermes Agent 核心编排层：说明 Hermes 的核心价值在于上下文、skills、tools、memory、delegation 的统一调度。
- 典型应用场景层：聚焦知识库管家、代码协同调度、调研资料处理、自动化巡检、多模型路由。
- 底层执行资源与模型服务：说明 Hermes 不是独立完成一切，而是调度 Vault、Claude Code CLI、Shell/Browser/API、LiteLLM 与模型服务。

> [!summary]
> Hermes 更适合做长期上下文、调度和自动化的 Agent 工作台；Claude Code 更适合具体代码执行；LiteLLM 负责模型代理；Docker Postgres 支撑 LiteLLM 状态数据。
