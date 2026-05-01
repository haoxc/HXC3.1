---
tags:
  - mac-工具
  - AI工具
  - Agent
description: Hermes Agent 4 层可交互架构图：接入层 → 核心层 → 模型层 → 能力层。
type: note
create-date: 2026-04-30
---
[[hermes|Hermes 工具入口]]

## 架构概览

4 层架构，20+ 平台接入，20+ 模型提供商。

- **接入层** — CLI、Telegram、Discord、Slack、Webhook、API Server
- **核心层** — 会话循环、上下文压缩、模型路由、凭证池、Profiles
- **模型层** — OpenRouter、Anthropic、OpenAI、DeepSeek、Google、本地模型
- **能力层** — Tools（20+ 工具集）、Skills、Memory、Sessions、Cron、MCP、Subagents、Checkpoints

- ![[Hermes-典型应用场景逻辑架构图.svg|700]]

## 交互

- 拖拽平移 / 滚轮缩放 / 悬停高亮 / 点击显示详情
- 基于 LeaferJS 2.1.0 Canvas 引擎
