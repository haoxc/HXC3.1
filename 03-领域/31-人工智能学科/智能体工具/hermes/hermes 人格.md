---
aliases:
  - Hermes Agent Personality
  - hermes人设
  - hermes/配置/人格设计(RGSJ, HPD)
tags: [hermes, AI-Agent, 参考]
description: Hermes Agent 的默认人格设计、核心特质、通信风格及定制方式
type: note
create-date: 2026-05-01
---

# Hermes 人格

**一句话定义**：Hermes 的人格由 system prompt 注入的身份声明和行为指令决定，核心是「直接、渊博、有用」——优先真正帮到用户而非多说话。

## 默认人格

| 维度  | 设定                            |
| --- | ----------------------------- |
| 身份  | 由 Nous Research 创建的智能 AI 助手   |
| 定位  | 通用助手，覆盖问答、编码、分析、创意、工具执行       |
| 语气  | 清晰、直接，不确定时明确表示，优先有用而非 verbose |
|     |                               |

### 核心特质

| 特质   | 表现          | 反例          |
| ---- | ----------- | ----------- |
| 直接   | 简洁完成任务，不多铺垫 | 过度解释或寒暄     |
| 渊博   | 覆盖广泛知识域     | 对陌生领域编造答案   |
| 诚实   | 不确定时承认      | 编造或回避       |
| 有用优先 | 强调行动而非言辞    | 说「我理解了」但不做事 |

## 人格注入机制

```
config.yaml → system prompt 拼装 → 模型推理
```

人格由两部分拼接而成：

| 层级    | 来源                    | 内容             |
| ----- | --------------------- | -------------- |
| 基础人格  | 系统 prompt 模板          | 身份声明 + 通用行为指令  |
| 领域知识  | Skills 加载             | 任务特定流程、陷阱、插件规则 |
| 用户偏好  | Memory 注入             | 用户画像 + 持久化偏好   |
| 项目上下文 | CLAUDE.md / AGENTS.md | 项目级规范          |

> 在「Hermes 人格」之上叠加 skills 和 memory，类似「角色」+「装备」+「记忆」三层模型。

## 人格定制

### Profile 系统

`~/.hermes/profiles/` 下定义多个 profile，切换人格参数：

```yaml
# ~/.hermes/profiles/vault-only/config.yaml
system_prompt_appendix: |
  你是 HXC Vault 管理专家，只做笔记操作。
  语气冷静精确，不废话。
```

| 定制维度 | 方法 |
|----------|------|
| 语气/风格 | `system_prompt_appendix` 追加指令 |
| 工具范围 | `enabled_toolsets` 限制 |
| 模型选择 | `model` 字段指定 provider/model |
| 领域知识 | 关联 skills |

### 实际效果对比

| 场景 | 默认人格 | vault-only profile |
|------|---------|-------------------|
| 创建笔记 | 解释流程再动手 | 直接查索引→写文件 |
| 错误处理 | 先分析可能原因 | 直接读取日志定位 |

## 通信风格详细规范

以下规则来自默认 system prompt：

| 规则 | 含义 |
|------|------|
| 回述确认意图 | 执行前用英文描述目标 + 关键字，等确认再动手 |
| 加载 skill 再干活 | 即使觉得会做，skill 里有约定俗成的工作流和陷阱 |
| Skills 优先于通用方法 | skill 编码了用户偏好和工作流，必须遵从而非绕过 |
| 保存记忆 | 用户偏好、环境事实、工具怪癖→memory；任务进度→不保存 |
| 复杂任务后 offer skill | 5+ 工具调用或克服过错误的任务→提炼成可复用 skill |

## 人格 vs 用户偏好

| | Hermes 人格 | 用户偏好（Memory） |
|------|------------|-------------------|
| 谁定义 | Nous Research + 用户 config | 用户行为中提取 |
| 稳定性 | 高（版本级变更） | 动态（持续追加） |
| 作用域 | 所有会话 | 跨会话持久 |
| 举例 | 「直接、有用」 | 「沟通极其简洁，单字指令」 |

## 相关

- [[03-领域/31-人工智能学科/智能体工具/hermes/Hermes-Claude-Code-CLI协同方案|Hermes-Claude-Code-CLI协同方案]]
- 人格定制详见 `hermes config` 和 profiles 系统
