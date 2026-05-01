---
aliases:
  - GBrain Usage Guide
  - gbrain使用手册
  - gbrain/操作/使用指南(SYZN, GUG)
tags: [AI, AI-Agent, 教程, gbrain]
description: gbrain 日常使用：搜索、写入、图谱查询、维护操作
type: note
create-date: 2026-05-01
---

# gbrain-使用指南

**一句话**：gbrain = PGLite + pgvector + 知识图谱，把 Obsidian Vault 变成可语义搜索、实体查询的 AI 记忆系统。

## 架构

```
Hermes → MCP (gbrain serve) → brain.pglite
         ↑ stdio transport      ├─ pages (markdown 全文)
                                ├─ chunks (分段 + embedding)
                                └─ entities + edges (知识图谱)
```

三层交互：
- **MCP 工具**（日常主力）— Hermes 直接调用 `brain_*` 系列工具
- **CLI 命令**（维护/诊断）— `gbrain <command>`
- **触发词**（快捷入口）— "查脑"、"脑状态" 等关键词路由到 gbrain skill

## MCP 工具清单

### 读取

| 工具 | 用途 | 参数 |
|------|------|------|
| `brain_search` | 混合搜索（关键词 + 语义向量） | `query`, `max_results` |
| `brain_read` | 读取完整页面 | `page_id` 或 `path` |
| `brain_query` | 知识图谱实体查询 | `entity` |
| `brain_list` | 列出所有页面 | `filter`, `limit` |
| `brain_links` | 页面进出链接 | `page_id` |
| `brain_status` | 脑状态总览 | — |

### 写入

| 工具 | 用途 | 参数 |
|------|------|------|
| `brain_write` | 创建/更新页面 | `path`, `content`, `frontmatter` |
| `brain_delete` | 删除页面 | `page_id` 或 `path` |
| `brain_enrich` | 自动丰富实体信息 | `entity` |

### 维护

| 工具 | 用途 | 参数 |
|------|------|------|
| `brain_doctor` | 健康检查 + 自动修复 | — |
| `brain_embed` | 生成/刷新 embedding | `--stale` |
| `brain_extract` | 提取实体与关系 | — |
| `brain_sync` | 从文件系统重新同步 | `--skip-failed` |

## CLI 命令

```
# 状态
gbrain status          # 页数/块数/健康分
gbrain doctor          # 健康检查 + 修复建议

# 导入
gbrain import ~/Vault   # 导入 Obsidian Vault
gbrain sync             # 增量同步变更

# Embedding（需要 OPENAI_API_KEY）
gbrain embed --stale    # 为无 embedding 的 chunk 生成向量

# 实体提取（需要 ANTHROPIC_API_KEY）
gbrain extract links    # 提取 wikilink 关系
gbrain extract entities # 提取实体 + 关系（人物/概念/组织）

# 搜索（CLI 直搜，不经过 MCP）
gbrain search "向量检索"  # 混合搜索

# 脑分
gbrain score            # 脑健康评分（0-100）
```

## 使用场景

### 场景 1：查找存量知识

```
# Hermes 对话中
"查脑：transformer 自注意力机制"
→ brain_search(query="transformer 自注意力", max_results=5)
→ 返回相关页面 + chunk 片段
→ 如需要全文：brain_read(path="03-领域/...")
```

### 场景 2：探索实体关系

```
"查脑：OpenAI 和 Anthropic 的关系"
→ brain_query(entity="OpenAI")
→ 返回实体卡片 + 关联节点
```

### 场景 3：写入记忆

```
"记一下：gbrain embed 超时需先停 MCP"
# Hermes 调用 brain_write → 写入脑数据库 + 可选同步到 Vault
```

### 场景 4：健康巡检

```
"脑状态"
→ brain_status → 页数/块数/实体数/健康分
→ brain_doctor → 问题清单 + 修复建议
```

## 前置条件

| 功能 | 需要的 Key | 不配的影响 |
|------|-----------|-----------|
| 关键词搜索 | 无 | — |
| 语义搜索 | `OPENAI_API_KEY` | 只能关键词匹配，语义召回不可用 |
| 实体提取 | `ANTHROPIC_API_KEY` | 知识图谱为空，`brain_query` 无结果 |
| 实体丰富 | `TAVILY_API_KEY`（可选） | `brain_enrich` 不可用 |

当前环境通过 LiteLLM proxy (`localhost:4000`) 路由，需同时设 `*_BASE_URL`：

```bash
export OPENAI_API_KEY="$LITELLM_MASTER_KEY"
export OPENAI_BASE_URL="http://localhost:4000/v1"
export ANTHROPIC_API_KEY="$LITELLM_MASTER_KEY"
export ANTHROPIC_BASE_URL="http://localhost:4000"
```

## 常见问题

| 症状 | 原因 | 解决 |
|------|------|------|
| `brain_search` 无语义结果 | embedding 未生成 | `gbrain embed --stale` |
| `brain_query` 返回空 | 实体未提取 | `gbrain extract entities` |
| embed 报 `PGLite lock timeout` | MCP server 占着库 | `pkill gbrain serve` → embed → 重启 Hermes |
| sync 有 slug 错误 | 文件名含特殊字符 | `gbrain sync --skip-failed` |
| MCP 工具不可用 | gbrain serve 挂了 | 检查 `config.yaml` 中 `mcp_servers.gbrain.enabled` |
| 脑分低 | 缺 embedding / 实体 / 链接 | 跑完 embed + extract links + extract entities |

## 脑分计算公式

脑分 = embedding 覆盖率 × 30% + 实体提取完整性 × 30% + 链接提取 × 20% + 页面活跃率 × 20%

- 仅导入（无 key）：~10/100
- 导入 + embedding：~40/100
- 全量（embedding + entities + links）：~90+/100

## 相关

- [[gbrain-Hermes集成指南]] — 安装配置
- [[gbrain 介绍]] — 概念与设计理念
- [[gbrain]] — MOC 索引
