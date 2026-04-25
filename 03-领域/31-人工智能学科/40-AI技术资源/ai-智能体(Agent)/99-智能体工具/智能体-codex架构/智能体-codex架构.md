---
aliases: []
tags: []
description:
type:
ref-url:
create-date: 2026-04-09 22:59
---
Codex 架构可以总结为四个功能维度，共同构成 Gemini 在 IDE 中的运行逻辑：
## 1. 规范与指令层 (Governance)

这定义了 Gemini 的“人设”和“语言风格”，是所有对话的基础。

- **Instructions (全局指令)**：设置 AI 的底层行为准则，例如使用中文和代码规范。
- **Prompts (提示词库)**：预设高频对话模板，方便调用，避免重复输入复杂需求。

## 2. 执行与自动化层 (Execution)

赋予 AI “手脚”，让它能够主动完成任务，而不只是聊天。

- **Agents (智能体)**：具备特定专业身份的 AI 单元，例如“重构专家”，拥有独立思考和处理任务的能力。
- **Skills (技能)**：封装好的多步骤自动化工作流，例如写代码、跑测试和修复错误，是 Agent 调用的具体“招式”。

## 3. 数据与上下文层 (Context)

让 AI 拥有“眼睛”和“记忆”，能`感知`项目全局。
- **[[MCP Servers (上下文协议)]]**：通过 Model Context Protocol 连接外部数据，例如 GitHub、数据库和本地文档，消除信息差。
- **Plugins (插件)**：扩展工具箱，让 AI 能查询文档或操作特定的外部服务。

## 4. 触发与集成层 (Integration)

将 AI 无缝嵌入开发生命周期。

- Hooks (钩子)：基于事件的自动触发机制，例如保存代码时或提交 Git 前，自动触发 AI 审计或生成注释。

---

>[!important] 总结：
Codex 架构通过 Instructions 制定规范，通过 MCP 获取感知，用 Skills 赋能，最终以 Agents 的形式完成自动化任务。建议是先优化 Instructions（解决语言偏好），或增加一个 MCP Server 来连接本地数据。
