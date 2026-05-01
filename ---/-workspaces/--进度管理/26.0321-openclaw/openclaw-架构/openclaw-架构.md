---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-03-21
---
## 内容
![[openclaw_architecture.svg|542]]
五层架构从上到下：
**接入层** — 六大消息平台通过 Channel Adapter 统一规范化为标准消息格式 [Techzine Global](https://www.techzine.eu/news/devops/139777/anthropic-builds-openclaw-rival-claude-code-channels/)，CLI 和 Web UI 作为 WebSocket 客户端直连。
**网关层** — Gateway 是单一 WebSocket 服务（127.0.0.1:18789），系统唯一控制平面 [Wikipedia](https://en.wikipedia.org/wiki/OpenClaw)，内含 Session Router（多 Agent 路由）、Lane Queue（串行执行防竞态）、Access Control（设备配对认证）。
**执行层** — Agent Loop 的完整生命周期：Context 组装 → LLM 推理 → Tool 执行 → 流式回复 → 持久化，通过 ReAct 循环反复迭代直到任务完成。 [Openclaw](https://openclaw.ai/)
**智能层** — Skills 按需注入（不是一次性全量注入），Canvas 作为独立进程运行在 18793 端口，提供隔离性 [Wikipedia](https://en.wikipedia.org/wiki/OpenClaw)，Heartbeat 实现无需用户触发的主动行为。
**存储层** — 全部文件化：SOUL.md 定义人格，MEMORY.md 跨会话记忆，JSONL 逐行审计，完全透明可检查