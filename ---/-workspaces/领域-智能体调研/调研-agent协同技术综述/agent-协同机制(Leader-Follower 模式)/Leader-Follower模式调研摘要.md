---
aliases: [Leader-Follower 模式摘要, 主从协同摘要]
tags: [调研, 摘要, agent]
description: Leader-Follower 协同机制的快速理解摘要。
type: 调研摘要
ref-url:
  - https://www.anthropic.com/engineering/building-effective-agents
  - https://langchain-ai.github.io/langgraphjs/reference/modules/langgraph-supervisor.html
  - https://openai.github.io/openai-agents-js/guides/handoffs/
create-date: 2026-04-25 17:10
hxc-ref: hxc-survey
---

# Leader-Follower模式调研摘要

## 摘要判断

> [!abstract] 调研摘要
> Leader-Follower 模式可以理解为一种层级式 agent 协同机制：由 leader 统一理解任务、拆解子任务、分派给 follower，并在末端统一收口结果。
>
> 它的价值不在于多 agent 数量，而在于让控制权、质量标准和任务边界集中在 leader 端。这样更适合需要稳定执行口径和明确责任链的知识工作。
>
> 对本项目而言，最值得借鉴的不是做一个复杂 supervisor runtime，而是先把 `leader 做分解与校验，follower 做稳定执行` 固化成 workflow。

## 本质定位

Leader-Follower 不是自由群聊，也不是去中心化 handoff 网络。它更接近 Anthropic 的 `orchestrator-workers` 和 LangGraph 的 `supervisor` 结构：**一个中心负责决策，多个执行单元负责落实**。

## 适合借鉴什么

- 任务分解与路由权集中
- follower 只拿局部上下文
- 结果统一回收
- 质量门槛集中收口

## 不宜过度理解

- 不要把它理解成“任何多 agent 协作都该有一个 leader”
- 不要把它等同于 handoff；handoff 更强调`控制权转移`
- 不要忽略状态管理和验证层，否则它只会退化成多段 prompt 串联

## 关联报告

- [[agent-协同机制(Leader-Follower 模式)]]

> [!summary] 一句话总结
> Leader-Follower 的核心不是“多 agent”，而是“谁拥有控制权，以及如何把分解、执行和收口稳定地串起来”。
