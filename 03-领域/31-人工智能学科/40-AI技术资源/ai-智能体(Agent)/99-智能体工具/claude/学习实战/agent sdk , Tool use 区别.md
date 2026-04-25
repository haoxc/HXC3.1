---
aliases:
tags:
description:
type:
ref-url:
---
# Tool Use vs Agent SDK 对比

## 一句话区别

> **Tool Use** 是单次调用中的能力扩展；**Agent SDK** 是多次调用间的流程编排。

---

## 工作机制

### Tool Use（单次调用）

```
用户输入
  → Claude 决定调用哪个工具
  → 工具执行（search / code / API …）
  → Claude 整合结果 → 最终回复
  → 输出给用户

└── 全程在一次 API 调用内完成
```

### Agent SDK（多轮编排）

```
用户目标
  → Orchestrator Agent（规划 / 拆解 / 调度）
      ├── 子 Agent A（搜索 / 读取）
      ├── 子 Agent B（代码执行）
      └── 子 Agent C（写入 / 输出）
  → Orchestrator 汇总 / 验证 / 继续迭代
  → 最终输出

└── 跨越多次 LLM 调用，有状态、可中断
```

---

## 对比表

|维度|Tool Use|Agent SDK|
|---|---|---|
|调用次数|单次 LLM 调用内|多次 LLM 调用，跨轮次|
|状态|无持久状态|有持久状态 + 记忆|
|工具/Agent|工具由开发者预先定义|Agent 可动态创建子 Agent|
|执行模式|串行，Claude 主导|可并行，Orchestrator 调度|
|中断/恢复|不支持|支持，可挂起等待外部事件|
|错误处理|单点失败即结束|可重试、回退、切换策略|
|适用场景|单步增强型任务|复杂多步骤自动化任务|
|典型例子|搜索 + 回答、读文件 + 总结|写代码 → 测试 → 修复 → 部署|
|开发复杂度|低，定义工具 schema 即可|高，需设计 Agent 拓扑和状态管理|
|成本|低（单次调用）|高（多次调用叠加）|

---

## 关键边界

**Tool Use 解决**："这次回答需要额外信息或能力" **Agent SDK 解决**："这个任务需要持续运行、跨会话、多步骤协作"

---
## 与 Claude Skills 的关系
```
Claude Skills
  └── 工作在 Tool Use 层
        每次触发 = 一次调用内的知识注入（读取 SKILL.md）

skill-creator 的子 Agent 并行测试
  └── 工作在 Agent SDK 层
        Orchestrator 并行派发多个测试 Agent，汇总结果后迭代
```

Skills 是**知识层**的扩展，Agent SDK 是**执行层**的编排，两者正交，可以组合使用： 一个 Agent SDK 流程中的每个子 Agent，都可以加载自己的 Skills 来获得专业能力。



