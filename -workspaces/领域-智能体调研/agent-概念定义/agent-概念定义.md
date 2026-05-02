---
aliases: []
tags: [AI-Agent, 概念定义]
description: 快速理解智能体 Agent 的核心概念、边界与常见架构图
type: 概念定义
ref-url:
  - https://www.anthropic.com/research/building-effective-agents/
  - https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components
  - https://www.ibm.com/think/topics/ai-agents
create-date: 2026-04-25 12:31
---
## 一句话定义
智能体（AI Agent）是：**以目标为牵引，能自主规划步骤、调用工具、观察结果并迭代行动的 AI 执行系统**。
更短地说：
> **大模型负责“想”，智能体负责“围绕目标持续做”。**
## 最小理解图

```text
目标
 ↓
理解 / 规划
 ↓
调用工具 / 执行动作
 ↓
观察环境反馈
 ↓
修正计划并继续
```

智能体的关键不是“会聊天”，而是有一个持续循环：

```text
Plan → Act → Observe → Reflect → Plan ...
```

## 判断标准
一个系统越符合下面 4 点，越接近智能体：
1. **有目标**：不是只回答一句话，而是围绕任务推进。
2. **能规划**：能拆分步骤，决定下一步做什么。
3. **能行动**：能调用工具，例如搜索、读写文件、运行代码、操作浏览器、调用 API。
4. **能反馈修正**：看到执行结果后，会调整策略，而不是一次性输出后结束。
## 和普通大模型的区别

| 对象  | 核心能力         | 典型形态                 |
| --- | ------------ | -------------------- |
| 大模型 | 生成、理解、推理     | 回答问题、写文本、解释代码        |
| 工作流 | 按固定流程调用模型和工具 | 固定步骤的自动化流程           |
| 智能体 | 动态决定步骤并持续执行  | 编程智能体、浏览器智能体、数据分析智能体 |

边界判断：

- **只输出答案**：更像大模型应用。
- **按固定节点执行**：更像工作流。
- **根据环境反馈自己决定下一步**：更像智能体。

## 核心组件

```text
模型：理解、推理、决策
工具：搜索、代码、浏览器、API、文件系统
记忆：保存上下文、偏好、历史状态
运行时：负责执行、权限、状态、日志、回滚
反馈机制：观察结果、评估进展、修正计划
```

## 典型例子

- **编程智能体**：读代码、改文件、运行测试、根据报错继续修复。
- **浏览器智能体**：打开网页、点击、填写表单、读取页面状态。
- **数据分析智能体**：读取数据、写分析代码、生成图表、解释结果。
- **企业流程智能体**：连接多个系统，自动完成审批、查询、同步、报告。

## 常见误区

- 智能体不等于聊天机器人。聊天只是交互方式，不是智能体本身。
- 智能体不等于工具调用。单次调用工具还不够，关键是能否形成目标驱动的行动闭环。
- 智能体不一定完全自主。很多可靠系统会保留人工确认、权限控制和停止条件。
- 智能体能力强不代表一定适合使用。开放任务适合智能体；固定任务通常用工作流更稳。

## 概念图链接

- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents/)  
  推荐看其中的 **Augmented LLM**、**Workflows**、**Autonomous agent** 图。适合理解“工作流 vs 智能体”的边界。 
	- [[agent-anthropic-Building effective agents(bk)]]
	- [[agent-anthropic-Building effective agents观点]]

- [Google Cloud: Agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)  
  推荐看 **architecture components of an agentic system** 图。适合理解智能体系统由模型、工具、记忆、运行时、前端等组件组成。 [[agent-google智能体框架(bk图)]]

- [Google Cloud: Single-agent AI system](https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run)  
  推荐看单智能体参考架构图。适合理解一个智能体如何连接用户、模型、工具和运行环境。

- [Google Cloud: Multi-agent AI system](https://docs.cloud.google.com/architecture/multiagent-ai-system)  
  推荐看多智能体架构图。适合理解多个专门智能体如何协作。

- [IBM: What are AI agents?](https://www.ibm.com/think/topics/ai-agents)  
  适合快速补充企业视角定义：智能体是能使用工具自主完成任务的系统。

## 压缩记忆

> **智能体 = 大模型 + 工具 + 记忆 + 反馈闭环 + 目标驱动的自主行动。**
