---
aliases:
  - handoffs
  - 任务交接
tags:
  - 术语
  - agent
description: OpenAI Agents SDK 中 handoff 机制的术语定义与边界辨析。
type: 术语定义
ref-url:
  - https://openai.github.io/openai-agents-js/guides/handoffs/
  - https://openai.github.io/openai-agents-js/guides/guardrails/
create-date: 2026-04-25 16:31
---

# 术语解析：任务交接 (Handoffs)

> [!IMPORTANT] 快速理解
> 在 OpenAI Agents SDK 里，任务交接 (Handoffs) 的本质不是“多 agent 一起聊天”，而是把当前任务控制权有条件地移交给更合适的下游 agent。

## 1. 概念界定 (Concept Definition)

任务交接 (Handoffs) 是一种 **agent 编排机制**：当前 agent 在运行过程中判断“这段任务更适合由另一个 agent 处理”，于是把后续处理权转给目标 agent。

它解决的问题不是“怎么多建几个 agent”，而是“当任务跨越角色边界时，如何把工作段落交给更合适的执行者”。这背后的核心逻辑是：**角色分工先于能力堆叠**。如果一个 agent 既负责统筹、又负责执行、又负责审查，最终往往会出现上下文过载、判断标准漂移、产物风格不稳定的问题。

在 OpenAI Agents SDK 的语境里，handoff 不是普通文本提示词技巧，而是框架层承认的一种控制流。官方文档把它定义为 agent orchestration 的一部分，用来把工作从一个 agent 委派到另一个 agent；它强调的是“交接链路”和“责任切换”，不是简单地让模型顺手调用另一个能力。[OpenAI Agents SDK Handoffs](https://openai.github.io/openai-agents-js/guides/handoffs/)

对理解多智能体系统而言，handoff 最重要的启发是：**agent 协同首先是任务边界设计问题，其次才是提示词和工具问题**。

## 2. 替代范式 (Alternative Paradigms)

- `agent as tool`: 适合把另一个 agent 当成局部能力模块调用。重点是“被调用者提供一个能力”，而不是“接管后续任务流程”。
- `router / routing`: 适合在入口阶段做分流。重点是“先决定该走哪条路径”，而不是在执行过程中动态切换责任主体。
- `workflow orchestration`: 适合把多步骤流程固定成显式流程图或状态机。重点是“流程可控”，比 handoff 更强约束，但也更重。
- `delegate / delegation`: 是更一般的委派概念。handoff 可以看作 delegation 在 agent runtime 中的具体实现形态之一。

如果你想表达“一个 agent 把后续任务正式移交给另一个 agent”，`handoff` 比 `tool call` 更准确；如果你想表达“让另一个 agent 提供一次局部能力”，那更适合用 `agent as tool`。

## 3. 边界辨析 (Boundary Analysis)

| 维度   | 任务交接 (Handoffs)       | agent as tool  | router / routing |
| ---- | --------------------- | -------------- | ---------------- |
| 核心目的 | 转移任务控制权               | 借用局部能力         | 决定入口分流           |
| 角色关系 | 上下游角色切换               | 主从式能力调用        | 路由器决定路径          |
| 发生时机 | 执行过程中                 | 某一步需要能力时       | 任务开始或关键分叉点       |
| 产物含义 | 后续责任主体变了              | 当前 agent 仍是主控  | 任务被分配到某条流程       |
| 常见误解 | 误以为只是“再叫一个 agent 来帮忙” | 误以为等同于 handoff | 误以为可以替代执行期交接     |

最常见的认知误区是把 handoff 理解成“多智能体自动合作”的宽泛说法。这个理解太松。更准确的口径是：**handoff 是一种带有角色切换含义的任务移交机制**。

另一个边界点是 guardrails。guardrails 负责检查输入、输出或工具调用边界，失败时会触发 tripwire 并中止流程；它解决的是“能不能继续”，不是“应该由谁接手”。所以 handoff 管的是 **任务归属**，guardrail 管的是 **流程约束**。[OpenAI Agents SDK Guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/)

> [!IMPORTANT] 实践指南
>
> - 当你要设计多 agent 协同时，先问“哪一步应该换角色”，再决定要不要用 handoff。
> - 如果目标只是复用另一个 agent 的局部能力，不要滥用 handoff，优先考虑 `agent as tool`。
> - 如果流程必须可追踪、可回滚、可治理，单靠 handoff 不够，通常还要补显式 workflow 或状态管理。
> - 一个好比喻是“handoff 像接力赛交棒”：重点不在于场上有多少跑者，而在于谁在什么位置接棒、接棒后跑哪一段。
> - 例句：这个系统不是让所有 agent 同时参与，而是由总控 agent 在识别到专业任务后，把分析段 handoff 给对应专家 agent。
> - 不要在只是“补一个工具能力”时使用这个术语，那会把“能力调用”和“责任切换”混在一起。
