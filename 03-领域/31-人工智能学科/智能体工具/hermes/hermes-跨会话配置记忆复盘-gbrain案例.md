---
aliases:
  - "Hermes Cross-Session Config Memory Postmortem"
  - "hermes跨会话配置记忆"
  - "hermes/配置/跨会话记忆机制(KSJY, CSM)"
tags: [AI, AI-Agent, 复盘, hermes]
description: 以 gbrain embedding 模型配置反复调整为例，分析跨会话配置丢失的根因，列出 Hermes 三层防护机制及落地检查清单。
type: note
create-date: 2026-05-02
---

# hermes-跨会话配置记忆复盘-gbrain案例

## 事件

在一个跨多次会话的 gbrain 完整流程跑通任务中，embedding 模型配置被反复调整了 3 轮才稳定，用户明确反馈：「Embedding 不是配置过了吗」。

**时间线**：

| 轮次 | 行为 | 结果 |
|------|------|------|
| 会话 A | 用户指定 Qwen/Qwen3-Embedding-8B，API key 写入 `~/.litellm/.env` | 配置完成 |
| 会话 B（本次） | gbrain sync → embed 失败 | 发现 embedding.ts 硬编码 `text-embedding-3-large`，未读之前配置 |
| 会话 B | 尝试 SiliconFlow `text-embedding-3-large` | 400（模型不存在） |
| 会话 B | 尝试 ohmygpt 代理 | 401 |
| 会话 B | 用户打断：「我配置 embedding 模型是 Qwen/Qwen3-Embedding-8B」 | 回到正确配置 |

**直接成本**：3 次无效尝试 + 1 次用户纠正，约 15 分钟。

---

## 根因分析

按配置丢失的层面分层：

| 层面 | 问题 | 为什么发生 |
|------|------|-----------|
| 代码层 | `gbrain/src/core/embedding.ts` 硬编码 `text-embedding-3-large` | 之前的代码 patch 未持久化（编译后未提交或丢失） |
| 环境变量 | `OPENAI_BASE_URL` 和 `OPENAI_API_KEY` 每次需手动传入 | 未写入 shell profile 或 .env 文件 |
| 记忆层 | embedding 模型选择（Qwen/Qwen3-Embedding-8B）未写入 Hermes memory | 会话 A 结束后该决策仅存于对话历史中 |
| 检索层 | 本次任务开始前未用 `session_search` 搜索「gbrain embedding」 | 跨会话时 AI 不知道之前做过什么 |

**根因链条**：配置分散在三个位置（代码文件 + 环境变量 + 用户记忆），没有一个位置被 Hermes 持久化机制覆盖，导致跨会话后各层都丢失。

---

## Hermes 三层防护机制

### 第 1 层：`session_search` — 跨会话上下文召回

**机制**：每次新会话开始时，若任务涉及之前做过的工作，调用 `session_search` 搜索关键词。

**本次该怎么做**：

```
# 在任务开始前（或刚接手 gbrain 任务时）
session_search(query="gbrain AND embedding AND 模型")
```

**输出**：会返回会话 A 的摘要，包含「用户确认使用 Qwen/Qwen3-Embedding-8B，API key 在 ~/.litellm/.env」。

**触发条件**：任务涉及之前至少两个会话前做过的工作，或用户提到「之前配置过」类表述。

| ✓ 场景 | ✗ 不必要场景 |
|--------|-------------|
| 接手已有进度的工程任务 | 纯粹的新任务，无历史关联 |
| 用户说「上次我们做了...」 | 同一会话内的后续步骤 |
| 配置类任务（模型/API/环境变量） | 一次性查询 |

---

### 第 2 层：`memory` — 持久化配置事实

**机制**：将关键决策写入 memory，每次会话都会注入到系统 prompt。

**本次该怎么做**（会话 A 中应立即执行）：

```
memory(action="add", target="memory", 
  content="gbrain embedding 模型：Qwen/Qwen3-Embedding-8B，走 SiliconFlow API 
  （base URL: https://api.siliconflow.cn/v1，key 在 ~/.litellm/.env 的 SILICONFLOW_API_KEY）。
  维度 1536。不再尝试其他 embedding 模型或 provider。")
```

**此条已写入**（本次会话中）。将来任何会话中涉及 gbrain 时，memory 会直接显示这条配置。

**保存标准**：

| 该保存 | 不该保存 |
|--------|---------|
| 模型选型、API 端点、key 位置 | 中间调试过程、失败尝试 |
| 用户明确的「记住这个结论」 | 一次性命令行参数 |
| 跨会话需要复用的环境事实 | 本次会话内可重新推导的信息 |

---

### 第 3 层：`skill` — 固化完整工作流

**机制**：将复杂流程（包括配置、编译、测试）保存为可复用的 skill，下次直接加载执行。

**适用场景**：

- gbrain 从源码编译到 embedding 验证的完整流程
- 涉及 5+ 次工具调用、有特定环境依赖的操作
- 有已知 pitfalls 需要避免

**本次的 skill 候选**（将 gbrain 完整流程固化为 skill）：

```
skill_manage(action="create", name="gbrain-setup", category="brain-ops",
  content="""... 包含：
  - Postgres + pgvector Docker 配置
  - gbrain 编译（bun build --compile）
  - embedding 模型配置（Qwen/Qwen3-Embedding-8B, SiliconFlow）
  - sync → extract → embed → serve 四步验证
  - 已知 pitfalls：中文 slug 为空、WASM 不可用
  """)
```

---

## 落地检查清单

每次开始一个**跨会话的工程任务**时，执行以下三项：

```
[ ] session_search 搜索任务关键词 → 召回历史上下文
[ ] 读取相关 memory → 确认持久化配置是否存在
[ ] 若流程复杂（5+ 步），检查是否有现成 skill 或考虑新建
```

**反例对照**：

| ✓ | ✗ |
|---|----|
| 任务开始前先 `session_search(gbrain embedding)` | 直接开始 sync，发现 embed 失败后再试各种 provider |
| 用户在会话 A 说「记住这个模型」，立即 `memory(add)` | 依赖对话历史，期待下次会话自然能记住 |
| gbrain 流程跑完后 `skill_manage(create)` | 重复踩坑，每次从零摸索 |

---

## 相关

- [[hermes-模型配置]] — Hermes Agent 自身的模型配置机制
- [[hermes-auxiliary模型配置踩坑]] — 类似的配置反复调整案例
- Hermes memory 工具设计：见 Hermes Agent 系统 prompt
- `~/.litellm/.env` — SiliconFlow API key 实际存储位置
- `~/gbrain/src/core/embedding.ts` — 当前已 patch 为 Qwen/Qwen3-Embedding-8B
