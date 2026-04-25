---
aliases:
  - agency-agents核心思想
tags:
  - 调研
  - 智能体
  - agent
description: 基于 agency-agents 仓库的快速理解型调研，判断其核心价值、可借鉴方法与使用边界。
type: 调研报告
ref-url:
  - https://raw.githubusercontent.com/msitarzewski/agency-agents/main/README.md
  - https://raw.githubusercontent.com/msitarzewski/agency-agents/main/specialized/agents-orchestrator.md
  - https://raw.githubusercontent.com/msitarzewski/agency-agents/main/testing/testing-reality-checker.md
  - https://docs.claude.com/en/docs/claude-code/subagents
  - https://openai.github.io/openai-agents-js/guides/handoffs/
  - https://openai.github.io/openai-agents-js/guides/guardrails/
create-date: 2026-04-25 14:40
hxc-ref: template
---

# 调研-agency-agents核心思想-v2_0425

## 摘要入口

- [[Agency-agents调研报告(google版)|Agency-agents调研摘要]]

## 调研结论

> [!IMPORTANT] 调研结论
> 
> - `agency-agents` 的核心价值不在于"实现多智能体系统"，而在于把专业角色沉淀成可复制的 **智能体角色卡 (Agent Role Card)**。
>     
> - 它更像一个"AI 专家岗位说明书库"，不是完整的智能体运行时框架。真正值得学习的是：**把专家经验写成可调用、可交付、可验证的 agent 指令资产**。
>     
> - 对本项目而言，它的启发不是照搬几十个 agent，而是提炼一种建模方法： **角色定位 → 任务边界 → 工作流程 → 交付标准 → 质量门槛 → 触发方式**
>     
> 
> **结论依据**：以上判断基于对 README、Agents Orchestrator、Reality Checker 三个核心文件的精读，以及与 Claude Code subagents 官方文档、OpenAI Agents SDK（handoffs / guardrails）的横向对比。分析维度包括：角色设计方式、工作流编排逻辑、质量保障机制、运行时能力边界。

---

## 课题判断

- **课题类型**：技术实践 / agent 指令资产库
- **调研目标**：快速判断 `agency-agents` 对本地 Codex skill、Claude subagent、知识工作流建设有什么可借鉴价值
- **核心判断**：它不是"更聪明的模型"，而是"把工作经验结构化成可复用角色"

---

## 核心定位

`agency-agents` 把 agent 理解为一种 **专业角色封装 (Specialized Role Packaging)**。

仓库里的 agent 文件通常包含：

- `name / description`：说明这个 agent 是谁、何时使用；
- `Identity & Memory`：定义角色身份、性格、经验模式；
- `Core Mission`：限定核心职责；
- `Workflow Process`：给出执行步骤；
- `Critical Rules`：设置不可突破的约束；
- `Success Metrics`：定义什么算完成得好；
- `Communication Style`：约束输出语气和表达方式。

这说明它关注的不是底层调度算法，而是 **专家工作模式的文本工程化 (Textual Operationalization of Expertise)**。

---

## 核心思想

三条核心思想之间有内在递进关系，依次回答三个问题：

```
agent 是谁？（角色定义）
  → agent 怎么做事？（流程内置）
  → agent 做完了算什么？（质量门槛）
```

理解这个递进关系，比单独理解任何一条都更重要。

### 1. Agent 不是"万能助手"，而是"岗位角色"

普通提示词常见问题是边界模糊：让模型"帮我做设计""帮我写代码"，模型会自由发挥。 `agency-agents` 的做法是把角色收窄：

|维度|普通提示词|agency-agents|
|---|---|---|
|角色|临时设定|稳定岗位|
|能力|泛化描述|专业分工|
|过程|用户临时指挥|内置流程|
|交付|看模型发挥|有交付标准|
|质量|事后评价|过程内置质量门槛|

> [!WARNING] 常见误区
> 不要把 agent 当成“临时人格设定”。对知识工作流而言，真正关键的是角色边界是否稳定；一旦角色不稳定，产物风格、分析深度和判断标准都会漂移。

### 2. 好 agent 的重点是"流程"，不是"人格"

仓库里有不少人格化表达，但可复用价值主要来自流程结构，而不是语气包装。

例如 `Agents Orchestrator` 的关键不是"像指挥家"，而是它定义了一个开发流水线：

```text
需求规格
  -> 项目管理拆任务
  -> 架构/UX 建基础01-
  -> 开发 agent 执行
  -> QA agent 验证
  -> 失败则回到开发
  -> 全部通过后做集成验收
```

这接近 OpenAI Agents SDK 中的 **handoff** 思路：不同 agent 负责不同任务段，由上游 agent 将任务交给更合适的下游专家。但 `agency-agents` 主要停留在指令资产层，未提供严格的运行时状态机。

### 3. 质量门槛是 agent 可用性的分水岭

`Reality Checker` 这类 agent 的价值在于反制"过早宣布完成"。它要求证据、截图、实际检查和保守判断。

这一点比"多几个角色"更重要。没有质量门槛的多 agent 系统，容易变成多个模型互相附和；有质量门槛后，agent 才能形成闭环：

```text
执行 -> 证据 -> 验证 -> 反馈 -> 修正
```

这和 OpenAI Agents SDK 的 **guardrails** 思路相近：在输入、输出或工具调用边界上设置检查机制，减少错误进入下一阶段。

---

## 技术框架

从工程形态看，`agency-agents` 可拆成三层：

|层级|作用|对应内容|
|---|---|---|
|角色层|定义 agent 是谁|name、description、identity、personality|
|流程层|定义 agent 怎么做事|workflow、critical rules、decision logic|
|质量层|定义什么算合格|success metrics、QA loop、evidence requirements|

它缺少的是第四层：**运行时层 (Runtime Layer)**。也就是 agent 如何被调度、如何共享状态、如何隔离上下文、如何记录过程、如何自动评估。

**这个缺口在什么时候会触发问题？**

只要任务是单次、单人、线性执行，缺运行时层没有明显障碍。一旦涉及以下场景，缺口就会暴露：

- **多任务并发**：两个 agent 同时修改同一个资产，没有状态锁机制；
- **中间结果共享**：上游 agent 的输出需要传递给下游，无结构化传递协议时只能靠复制粘贴；
- **失败重试**：某个环节出错，没有追溯点，整个流程需要从头手动介入。

因此，`agency-agents` 的定位是"角色与流程设计参考"，不是完整智能体系统，不适合直接当成可运行框架部署。

---

## 可借鉴价值

对本地 Codex skill / Claude subagent 建设，最值得借鉴的是四点：

1. **触发条件写清楚**：什么时候该用这个 agent，什么时候不该用。
2. **交付物写具体**：不要只写"提供建议"，要写"产出什么文件、表格、检查项或报告"。
3. **流程写成闭环**：任务不是"回答完"，而是"检查、验证、修正、落文件"。
4. **质量标准前置**：在 skill 或 agent 中提前定义什么是低质量输出，避免每次靠人工纠偏。

这与 Claude Code subagents 的官方定位也一致：subagent 是有独立任务目的、独立上下文和专门系统提示的任务型助手；它的价值来自任务边界和上下文隔离，而不是名称本身。

---

## 使用边界

不要把 `agency-agents` 理解为：

- 自动协作平台；
- 可直接部署的 agent runtime；
- 完整的多智能体编排框架；
- 能替代项目管理、测试、审计的工具系统。

它更适合用于：

- 设计 Codex skill；
- 设计 Claude subagent；
- 梳理团队中的 AI 工作角色；
- 把专家经验写成可复用提示词资产；
- 为某类任务建立输出标准和质量门槛。

如果要落地成真正的智能体系统，还需要补：

- 状态管理；
- 任务队列；
- 上下文传递；
- 工具权限；
- 日志与审计；
- 自动评估；
- 失败重试策略。

---

## 对本项目的建议

本项目不建议照搬 `agency-agents` 的大量角色。更稳的做法是按本地知识工作流拆 5 类核心 agent / skill：

|优先级|本地角色|解决的问题|关键产物|
|---|---|---|---|
|⭐⭐⭐ 优先|术语卡片创建|快速理解概念，降低理解门槛|术语卡片 + MOC 链接|
|⭐⭐⭐ 优先|质量复核|防止空洞、跑偏、未落地|检查清单 + 修正建议|
|⭐⭐ 次优先|课题综述调研|快速判断技术方向|调研报告 + 决策要点|
|⭐⭐ 次优先|文档共创|把材料变成交付文档|方案、PRD、申报书|
|⭐ 后续|目录结构审计|判断知识库结构是否合理|审计报告 + 整改清单|

**优先级判断逻辑**：

- "术语卡片创建"和"质量复核"频率最高、产物格式最稳定，是知识工作的基础设施，优先建设投入产出比最高。
- "课题综述调研"和"文档共创"场景略复杂，建议在前两者成熟后再建。
- "目录结构审计"需求偶发，暂缓，等知识库规模到达一定量级后再建。

判断标准只有一条：**只有当某类任务会反复出现、产物格式稳定、质量标准可描述时，才值得做成 skill 或 agent。**

---

## 图表建议

- **图表类型**：分层架构图
- **适用原因**：`agency-agents` 的本质是"角色层 → 流程层 → 质量层 → 缺失的运行时层"，用分层图比流程图更能看清它的能力边界。
- **图中建议表达的 4 个关键维度**：角色定义、工作流程、质量门槛、运行时缺口。

---

## 来源

- [msitarzewski/agency-agents GitHub 仓库](https://github.com/msitarzewski/agency-agents)
- [README：The Agency](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/README.md)
- [Agents Orchestrator](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/specialized/agents-orchestrator.md)
- [Reality Checker](https://raw.githubusercontent.com/msitarzewski/agency-agents/main/testing/testing-reality-checker.md)
- [Claude Code Subagents 文档](https://docs.claude.com/en/docs/claude-code/subagents)
- [OpenAI Agents SDK Handoffs](https://openai.github.io/openai-agents-js/guides/handoffs/)
- [OpenAI Agents SDK Guardrails](https://openai.github.io/openai-agents-js/guides/guardrails/)

> [!summary] 一句话总结 
> `agency-agents` 的核心不是"多智能体自动运行"，而是把专家角色、工作流程和质量门槛沉淀成可复用的 agent 指令资产；对本项目最直接的价值是建立"术语卡片创建"和"质量复核"两个高频 skill。
