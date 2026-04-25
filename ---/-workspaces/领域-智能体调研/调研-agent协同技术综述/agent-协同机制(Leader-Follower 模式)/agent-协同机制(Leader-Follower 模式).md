---
aliases:
  - Leader-Follower 模式
  - 主从协同
  - 层级协同
tags: [调研, agent, 协同机制]
description: 面向知识工作与多智能体编排的 Leader-Follower 协同机制技术调研。
type: 调研报告
ref-url:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html
  - https://openai.github.io/openai-agents-js/guides/handoffs/
  - https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff
create-date: 2026-04-25 17:10
hxc-ref: hxc-survey
---

# agent-协同机制(Leader-Follower 模式)

## 调研摘要

> [!abstract] 调研摘要
> Leader-Follower 模式可以理解为一种 **层级式协同机制**：由一个上层 agent 负责理解任务、分配工作、收敛结果，再由多个下层 agent 承担具体执行。它不是“多 agent 同时工作”的泛称，而是一种带有明确控制中心的协同结构。
>
> 它的价值不在于把 agent 数量堆多，而在于把 **任务分解、上下文分发、质量收口** 集中到同一个领导节点上。这样做通常能提升可控性、可观察性和角色边界清晰度。
>
> 从本项目视角看，最值得借鉴的不是做一个复杂多智能体 runtime，而是先把 `leader 负责分解/校验，follower 负责执行` 这条职责边界固化成可复用 workflow。

## 调研结论

> [!IMPORTANT] 调研结论
> - Leader-Follower 模式的核心价值不在于“多人协作感”，而在于把协同系统的控制权集中到 leader。
> - 它更像一种 **层级调度结构**，不是去中心化 handoff 网络，也不是自由群聊式多 agent 讨论。
> - 对知识工作和工程自动化而言，这种模式最适合承担 `任务拆解 -> 角色分派 -> 结果汇总 -> 质量把关`。
> - 对本项目而言，启发不是先做复杂 supervisor runtime，而是先把 leader 的判断职责写成 skill/workflow，把 follower 收束成可验证执行单元。
>
> **结论依据**：以上判断基于 Anthropic 对 orchestrator-workers 的工作流定义、LangGraph Supervisor 对层级多 agent 的官方说明、OpenAI Agents SDK 对 handoffs 与 agent-as-tools 的边界说明，以及 Microsoft Agent Framework 对 handoff / workflow 的控制流定义。分析维度包括：控制权归属、任务分解方式、上下文流动、可观察性、工程实现成本。

## 课题判断

- **课题类型**：协同机制调研
- **调研目标**：判断 Leader-Follower 是否适合作为本项目的 agent 协同默认范式
- **核心判断**：适合作为默认协同骨架，但只适合承担“集中分解与集中收口”的任务，不适合强互动、强对等协商、强自治探索场景

## 核心定位

Leader-Follower 模式本质上是一种 **单中心、多执行单元** 的协同机制。

leader 通常负责：

- 理解目标；
- 判断该拆成哪些子任务；
- 决定由哪个 follower 执行；
- 汇总 follower 结果；
- 在必要时做二次分派或质量校验。

follower 通常负责：

- 执行明确子任务；
- 在限定上下文内产出局部结果；
- 把结果返回给 leader，而不是自行接管整个任务流程。

这意味着它最接近 Anthropic 所说的 `orchestrator-workers`，也接近 LangGraph Supervisor 的“central supervisor controls communication flow and task delegation”结构，而不是 mesh 式 handoff 网络。[Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [LangGraph Supervisor](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)

## 核心思想

Leader-Follower 模式的核心不是“角色多”，而是下面四层递进逻辑：

1. **先集中判断，再分散执行**  
   先由 leader 统一理解任务和拆解方式，避免 follower 各自带着不同口径启动。

2. **上下文按需下发，而不是全量共享**  
   follower 只拿到完成当前子任务所需的信息，这能降低上下文污染和角色漂移。

3. **结果统一回收到 leader**  
   这样最终交付标准和判断口径不会散落在多个 agent 身上。

4. **质量门槛在 leader 端收口**  
   follower 可以很强，但“是否通过、是否继续、是否重做”最好由 leader 统一决定。

Anthropic 官方把相近模式概括为 `orchestrator-workers workflow`：中央 LLM 动态拆解任务、委派给 worker、再综合结果。LangGraph Supervisor 则把这种结构实现成层级系统，由 central supervisor 控制 communication flow 和 task delegation。[Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [LangGraph Supervisor](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)

## 技术框架 / 分析框架

一个可落地的 Leader-Follower 技术框架，通常包含 5 个层次：

1. **任务入口层**  
   接收用户目标，判断是否需要拆解。

2. **leader 决策层**  
   负责任务拆解、角色选择、优先级安排、结果收口。

3. **follower 执行层**  
   负责在限定上下文中执行局部任务，如调研、编码、审计、结构化整理。

4. **状态与上下文层**  
   记录任务状态、消息历史、局部结果、中间决策。没有这层时，leader-follower 很容易退化成“多 prompt 串联”。

5. **验证与治理层**  
   负责质量门槛、异常回退、人工审批、日志与评估。

如果只做前 3 层，这是一种轻量协同 workflow；如果把后 2 层补齐，它才接近生产级协同框架。

## 判断-证据链

| 判断 | 依据 | 含义 |
| --- | --- | --- |
| Leader-Follower 属于层级式协同 | LangGraph Supervisor 明确说明由 central supervisor 控制 communication flow 和 task delegation | 该模式默认存在中心控制点 |
| 它更接近 orchestrator-workers，而不是并行化 | Anthropic 将 orchestrator-workers 定义为中央 LLM 动态拆解并综合 worker 结果 | 重点在动态分解与统一收口 |
| 它不同于 handoff mesh | Microsoft handoff 文档说明 handoff 中控制权可以在 agent 间转移；OpenAI 说明 handoff 后 specialist owns the conversation | Leader-Follower 默认主控不下放到 follower 长期接管 |
| 它需要显式状态/治理层才能稳定工程化 | Microsoft Workflow 文档强调 graph、executors、edges、checkpointing、events | 只靠角色提示词很难稳定支持复杂协同 |

## 同类机制对比

| 对象 | 本质 | 适合解决什么 | 不适合什么 |
| --- | --- | --- | --- |
| Leader-Follower | 单中心层级协同 | 任务拆解明确、需要统一口径和质量收口的工作 | 强对等讨论、强自治探索 |
| Routing | 入口分流机制 | 先把任务分给不同路径 | 执行过程中的持续协调 |
| Handoffs | 控制权移交机制 | 让更合适的 specialist 接管后续对话 | 需要持续集中统筹的任务 |
| Group Chat / Peer-to-Peer | 多主体共同讨论 | 需要多视角碰撞或协商 | 高一致性、高治理要求的生产流程 |

## 可借鉴价值

对本项目最有价值的不是“构建一个多 agent 平台”，而是借鉴这套职责分离方式：

- leader 负责 `分解 / 路由 / 质量门槛 / 汇总`
- follower 负责 `稳定执行`
- 验证层负责 `通过 / 退回 / 复审`

这和你现在已经在做的 `skill + workflow + validator` 很契合。  
换句话说，Leader-Follower 对本项目的最佳落点不是“再造一个 runtime”，而是把现有技能链明确分成：

- **Leader skill**：决定任务怎么拆、产物挂到哪里、是否需要摘要和 MOC
- **Follower skill**：完成具体产物，如术语卡、调研报告、审计报告
- **Validator**：检查 bundle 是否完整

## 使用边界与误用风险

> [!WARNING] 常见误区
> 不要把 Leader-Follower 理解成“任何多 agent 协作都能套一个 leader”。如果任务本身高度开放、需要多轮协商，硬上 leader 往往会把真实问题压扁成单向派单，反而降低系统质量。

主要风险有 4 个：

1. **leader 成为瓶颈**  
   所有判断都集中在 leader，吞吐量和质量都会被 leader 上限锁死。

2. **follower 退化成被动工具**  
   如果 leader 拆解过细，follower 会失去专业判断空间，最终只是“带 prompt 的工具调用”。

3. **状态漂移集中爆发**  
   一旦 leader 的任务状态管理不稳，错误会向所有 follower 扩散。

4. **错误归因困难**  
   如果没有事件日志和中间状态记录，最后只会看到“结果不对”，很难判断是 leader 拆错、follower 执行错，还是校验漏掉了。

## 对本项目的建议

1. 先把 Leader-Follower 作为 **默认工作流口径**，不要先做 runtime。  
   也就是先明确：谁是 leader，谁是 follower，什么算交接，什么算完成。

2. leader 先承担三件事：  
   `任务分解`、`产物落点决策`、`validator 触发`

3. follower 只做高频稳定单元：  
   例如 `hxc-survey`、`hxc-term-card`、后续的 `quality-review`

4. 把真正的 runtime 能力延后到出现明确需求时再补：  
   如状态图、checkpoint、并发调度、人工审批、trace

这条路径的好处是：先把协同机制固化成 **治理规则**，而不是先上复杂基础设施。

## 图表建议

- **图表类型**：层级协同结构图
- **适用原因**：Leader-Follower 的理解重点是控制权、上下文流和结果回流，不是时间线本身
- **图中建议表达的关键维度**：
  - leader 的职责
  - follower 的职责
  - 上下文下发路径
  - 结果回流路径
  - validator / review gate 所在位置

## 来源

- [Anthropic - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [LangGraph Supervisor Reference](https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html)
- [OpenAI Agents SDK - Handoffs](https://openai.github.io/openai-agents-js/guides/handoffs/)
- [OpenAI Agents SDK - Agents](https://openai.github.io/openai-agents-js/guides/agents/)
- [Microsoft Agent Framework - Handoff orchestration](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff)
- [Microsoft Agent Framework - Workflows](https://learn.microsoft.com/en-us/agent-framework/workflows/)

## 关联摘要

- [[Leader-Follower模式调研摘要]]

> [!summary] 一句话总结
> Leader-Follower 模式的本质是把协同系统的控制权集中到 leader，用明确的任务分解、上下文分发和质量收口来换取稳定协同。 
