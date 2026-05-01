---
aliases:
  - Hermes Auxiliary Model Pitfalls
  - hermes辅助模型
  - hermes/配置/辅助模型配置(FZMX, AMC)
tags: [Hermes, mac-工具, AI工具, 踩坑]
description: Hermes auxiliary 模型配置的 5 个踩坑点：端点一致性、auto provider 不确定性、空 model 回退、重启生效和 delegation 混淆。
type: note
create-date: 2026-05-01
---

# Hermes auxiliary 模型配置踩坑

## 背景

Hermes 有 8 个辅助模型槽位（主模型 `deepseek-v4-pro-openai` 之外）：

| 槽位                 | 用途                            |
| ------------------ | ----------------------------- |
| `vision`           | 图片分析                          |
| `web_extract`      | 网页提取                          |
| `compression`      | 上下文压缩                         |
| `session_search`   | 历史会话搜索                        |
| `title_generation` | 会话标题生成                        |
| `skills_hub`       | Skills 市场搜索                   |
| `approval`         | 智能审批（`approvals.mode: smart`） |
| `mcp`              | MCP 交互                        |

本机当前 5 个已显式设为 `deepseek-v4-flash`（vision / web_extract / compression / session_search / title_generation），其余 3 个留空。

---

## 踩坑 1：端点不一致导致静默失败

**现象**：主模型正常工作，但 vision 看图、compression 压缩上下文、session_search 搜索都无响应，不报错。

**原因**：辅助模型的 `provider: auto` + `base_url: ''` 走的是默认路由。当主模型用 `custom` provider（`localhost:4000/v1`）时，辅助模型也必须在**同一个 LiteLLM 端点**上注册。

**验证**：

```bash
# 检查 LiteLLM 端点是否有 deepseek-v4-flash
curl -s http://localhost:4000/v1/models \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" | jq '.data[].id' | grep flash
```

若无输出，说明 `deepseek-v4-flash` 未在 LiteLLM 中配置，辅助任务会全部静默失败。

**修复**：在 LiteLLM 中添加对应模型别名，或改用已注册的模型名。

---

## 踩坑 2：provider: auto 的不确定性

**现象**：某些辅助任务偶尔成功、偶尔失败。

**原因**：`provider: auto` 让 Hermes 自动选择后端。如果系统有多个可用 provider（OpenRouter 的 key 也配了），`auto` 可能路由到不同 provider，行为不稳定。

**修复**：为每个辅助槽位显式指定 provider：

```bash
hermes config set auxiliary.vision.provider custom
hermes config set auxiliary.vision.model deepseek-v4-flash
```

三个字段缺一不可：`provider` + `model` + `base_url`（如果是 custom 端点）。

---

## 踩坑 3：model 留空时的回退逻辑

**现象**：`skills_hub` / `approval` / `mcp` 三个槽位 model 为空，但某些场景能工作。

**原因**：model 为空 ≠ 功能禁用。Hermes 会尝试：
1. 用主模型处理（消耗主模型上下文和 token）
2. 或 fallback 到任何可用的 provider

**结论**：不用的辅助槽位也建议显式设置，避免无意间用主模型执行轻量任务。

---

## 踩坑 4：配置后不重启不生效

`hermes config set` 写入 `config.yaml` 后，**正在运行的 Hermes 会话不会自动重读**。需要：

- CLI：退出后重新 `hermes`
- Gateway：`/restart`

验证方法：新会话发一张图，看 `auxiliary.vision` 是否被触发。

---

## 踩坑 5：auxiliary 和 delegation 模型混淆

| | auxiliary | delegation |
|---|---|---|
| 用途 | 后台工具型子任务 | 委派独立子 agent |
| 模型需求 | 轻量、快、便宜 | 需要一定推理能力 |
| 配置位置 | `auxiliary.{task}.model` | `delegation.model` |
| 空 model 行为 | 回退到主模型或 auto | 继承主模型配置 |

**常见错误**：以为设了 `auxiliary.compression.model` 就能优化 delegate_task 的上下文——不，delegate_task 走的是 `delegation` 配置，和 `auxiliary.compression` 无关。

---

## 本机当前配置（2026-05-01）

```yaml
# ~/.hermes/config.yaml 第 130-188 行
auxiliary:
  vision.model:          deepseek-v4-flash
  web_extract.model:     deepseek-v4-flash
  compression.model:     deepseek-v4-flash
  session_search.model:  deepseek-v4-flash
  title_generation.model: deepseek-v4-flash
  skills_hub.model:      ''          # 未配置
  approval.model:        ''          # 未配置
  mcp.model:             ''          # 未配置
```

全部 `provider: auto`，`base_url: ''`，依赖 LiteLLM 端点提供 `deepseek-v4-flash`。

---

## 相关

- [[hermes-模型配置]]
- [[Hermes-LiteLLM-DeepSeek-Docker-Postgres配置笔记]]
