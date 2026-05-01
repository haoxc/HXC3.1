---
aliases: [GBrain, gbrain脑系统, "AI/Agent平台/gbrain(GB, GBRAIN)"]
tags: [AI, AI-Agent, 术语]
description: Garry Tan 构建的 AI Agent 记忆脑系统——自连线知识图谱、混合搜索、29个技能、Minions 任务队列，安装 30 分钟运行 17,888 页知识库
type: note
create-date: 2026-05-01
---

# gbrain 介绍

**一句话定义**：gbrain 是 Y Combinator 总裁 Garry Tan 为他的 AI Agent（OpenClaw/Hermes）构建的记忆脑系统——自连线知识图谱 + 混合搜索 + 实体提取 + 定时维护，让 Agent 在每次交互后变聪明一点。

| 维度    | 数据                                                    |
| ----- | ----------------------------------------------------- |
| 仓库    | [garrytan/gbrain](https://github.com/garrytan/gbrain) |
| Stars | 12,540（2026-05-01）                                    |
| 语言    | TypeScript                                            |
| 许可    | MIT                                                   |
| 创建    | 2026-04-05，12 天构建完成                                   |
| 生产规模  | 17,888 页、4,383 人、723 家公司、21 个 cron 任务                 |
| 数据库   | PGLite（Postgres in WASM），2 秒就绪，无需独立服务                 |

## 核心理念

AI Agent 聪明但健忘。gbrain 给它一个脑。

每次交互循环：信号到达 → 信号检测器捕获想法和实体 → 脑优先查询 → 回复加全上下文 → 写入脑页（新信息 + 引用）→ 自动提取类型化关系（零 LLM 调用）→ 同步索引。

**关键设计决策**：实体提取和关系连线在每次写入时由确定性规则完成，不消耗 LLM token。类型化链接包括 `attended`、`works_at`、`invested_in`、`founded`、`advises`。

## 搜索能力

三层混合搜索：关键词 + 向量 + 图谱。基准测试结果（240 页 Opus 语料）：

| 指标 | gbrain | 无图谱变体 | 差距 |
|------|--------|-----------|------|
| P@5 | 49.1% | 17.7% | **+31.4** |
| R@5 | 97.9% | — | — |

差距来自图谱层 + v0.12 提取质量。完整评分卡：[gbrain-evals](https://github.com/garrytan/gbrain-evals)。

## 安装方式

**推荐：通过 AI Agent 安装**（~30 分钟）。将以下指令粘贴给 Agent：

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

支持宿主平台：OpenClaw（一键部署 Render）、Hermes Agent（一键部署 Railway）。

**独立 CLI**（无需 Agent）：

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain && bun install && bun link
gbrain init
gbrain import ~/notes/
gbrain query "what themes show up across my notes?"
```

**MCP 服务**：暴露 30+ 工具，零配置注册到 Claude Code / Cursor / Windsurf。

```json
{ "mcpServers": { "gbrain": { "command": "gbrain", "args": ["serve"] } } }
```

## 29 个技能

技能按功能组分为五类。技能通过 `RESOLVER.md` 路由分发——Agent 读技能、执行技能，智能活在技能文件而非运行时。

### 始终在线

| 技能 | 功能 |
|------|------|
| signal-detector | 每条消息触发，并行捕获原始想法和实体提及，脑在自动驾驶中复合成长 |
| brain-ops | 任何外部 API 调用前先查脑，读写-充实循环让每次回复更聪明 |

### 内容摄入

| 技能 | 功能 |
|------|------|
| ingest | 薄路由：检测输入类型，分派到对应摄入技能 |
| idea-ingest | 链接、文章、推文 → 脑页 + 分析 + 作者页面 + 交叉链接 |
| media-ingest | 视频、音频、PDF、书籍、截图、GitHub 仓库 → 转录 + 实体提取 |
| meeting-ingestion | 会议转录 → 脑页，参会者充实，公司时间线条目 |

### 脑操作

| 技能 | 功能 |
|------|------|
| enrich | 分层充实（Tier 1/2/3），创建/更新人员页和公司页 |
| query | 三层搜索 + 综合 + 引用。查不到就说"没有"，不编造 |
| maintain | 定期健康检查：过期页、孤立页、死链接、引用审计、反链执行、标签一致性。v0.23 增加梦想循环的合成+模式阶段 |
| citation-fixer | 扫描缺失或格式错误的引用，修正为标准格式 |
| repo-architecture | 新脑文件归档决策协议：主主题决定目录，不按格式 |
| publish | 将脑页分享为密码保护的 HTML，零 LLM 调用 |
| data-research | 结构化数据研究，YAML 配方参数化 |

### 运维

| 技能 | 功能 |
|------|------|
| daily-task-manager | 任务生命周期 + P0-P3 优先级，存储为可搜索脑页 |
| daily-task-prep | 晨间准备：日历前瞻 + 每参会者脑上下文 + 开放线程 + 任务审查 |
| cron-scheduler | 调度错峰（5 分钟偏移）、静默时段（时区感知）、幂等性 |
| cross-modal-review | 第二模型质量把关，拒答路由 |
| skill-creator | 按一致性标准创建新技能，与现有技能做 MECE 检查 |
| skillify | "skillify it!" 元技能：10 步循环将失败转化为持久技能 |
| minion-orchestrator | 后台工作：Shell 作业和 LLM 子代理，父子 DAG，跨重启持久 |

### 身份与设置

| 技能         | 功能                                                           |
| ---------- | ------------------------------------------------------------ |
| soul-audit | 6 阶段访谈生成 SOUL.md + USER.md + ACCESS_POLICY.md + HEARTBEAT.md |
| setup      | 自动配置 PGLite 或 Supabase，首次导入，GStack 检测                        |
| migrate    | 通用迁移：Obsidian、Notion、Logseq、Markdown、CSV、JSON、Roam           |
| briefing   | 每日简报：会议上下文、活跃交易、引用追踪                                         |

> 跨领域约定在 `skills/conventions/`：quality.md（引用、反链、显著性门槛）、brain-first.md（5 步查询再调用外部 API）、model-routing.md（哪个模型用于哪个任务）、test-before-bulk.md（批量前试 3-5 个）。

## Minions：持久化作业队列

内建于脑的 Postgres 原生作业队列。每个长时间 Agent 任务变成可存活于网关重启的作业。

**路由规则**：确定性工作（同输入→同步骤→同输出）→ Minions；需要判断（评估或决策）→ 子 Agent。

生产对比（拉取一个月社交帖子摄入脑）：

| 维度       | Minions   | sessions_spawn  |
| -------- | --------- | --------------- |
| 耗时       | **753ms** | >10,000ms（网关超时） |
| Token 成本 | **$0.00** | ~$0.03/次        |
| 成功率      | **100%**  | 0%（无法生成）        |
|          |           |                 |

## 与 Hermes 的关系

gbrain 明确支持 Hermes Agent 作为宿主平台。多个社区仓库组合两者：

- `LucidPaths/hermes-control-plane`：Hermes + gbrain + 自进化 + browser-use
- `kongaharsha/hermes_stack`：Hermes + gbrain + 技能库
- gbrain 安装脚本通过 `--host hermes` 将技能安装到 Hermes 技能目录

## 相关笔记

- [[gstack 介绍]] — Garry Tan 的另一项目，AI Agent 工程平台
- [[COG-second-brain]] — 受 gstack 和 gbrain 启发的自进化第二脑系统（382⭐）
