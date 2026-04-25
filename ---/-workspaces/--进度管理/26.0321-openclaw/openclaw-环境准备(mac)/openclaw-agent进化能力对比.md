---
aliases:
tags:
  - agent/能力/self-improving
description:
type:
ref-url:
---
## 内容

## 真正支持 Agent 自进化的框架
**这类框架与 OpenClaw 最接近——Agent 可以改写自身的行为、记忆或技能。**
### 1. OpenClaw 多 Agent 编排系统（社区衍生）

GitHub 上有一个基于 OpenClaw 的三省六部制多 Agent 编排系统，9 个专职 Agent 协作，带实时看板、模型配置和完整审计链，已达 10,100 Stars。 这是目前最接近 OpenClaw 原生进化思路的社区扩展。

### 2. Self-Improving Agent Framework（无名框架）

GitHub 上有一个标签为 `self-improving`、`agent-skills`、`self-improving-ai` 的框架，专门面向 outcome-driven 的 Agent 开发，Agent 可以通过 AI evaluation 自我改进，支持 human-in-the-loop 和 Claude Code 集成，约 9,700 Stars。

### 3. NVIDIA OpenShell

NVIDIA Agent Toolkit 包含 OpenShell 开源运行时，专门用于构建自进化 Agent，内置安全和隔离机制，与 LangChain 深度集成，支持企业级策略守护。

---

## 多 Agent 编排框架（接近但不完全等同）

### 4. CrewAI
CrewAI 编排角色扮演 Agent 协作完成任务，44,300 Stars，月下载 520 万次，2026 年 1 月新增流式工具调用事件。 角色是静态定义的，Agent 不会自我修改，但协作机制成熟。

### 5. Microsoft AutoGen → 已并入 Microsoft Agent Framework

2025 年 10 月 Microsoft 将 AutoGen 与 Semantic Kernel 合并为统一的 Microsoft Agent Framework，AutoGen 本身进入维护模式，只接受 bug 修复。

### 6. LangGraph

LangGraph 是有状态的图结构多 Actor 框架，支持持久记忆和精细流程控制，是构建自定义 Agent 编排的坚实底座。 帮 Klarna 把客服解决时间缩短了 80%。

### 7. Google ADK

Google Agent Dev Kit 于 2025 年 4 月发布，17,800 Stars，支持层级式 Agent 组合和自定义工具，深度整合 Gemini 和 Vertex AI。

---

## 与 OpenClaw 的关键能力对比

|能力|OpenClaw|CrewAI|LangGraph|OpenShell|Self-Improving|
|---|---|---|---|---|---|
|SOUL.md 人格持久化|✅|❌|❌|❌|部分|
|MEMORY.md 跨会话记忆|✅|❌|✅|✅|✅|
|Skills 动态注入|✅|❌|❌|✅|✅|
|Agent 自我修改行为|✅|❌|❌|✅|✅|
|消息平台接入|✅|❌|❌|❌|❌|
|Heartbeat 主动触发|✅|❌|部分|❌|❌|
|模型无关|✅|✅|✅|✅|✅|

---

**结论**：目前开源生态里，在"消息平台接入 + 持久人格 + Skills 进化"这个组合上，OpenClaw 依然是最完整的实现。纯进化能力最强的是那个 outcome-driven 的 Self-Improving Agent 框架，但它没有 OpenClaw 的消息通道层。两者结合是目前最接近"真正自进化个人 Agent"的方案。