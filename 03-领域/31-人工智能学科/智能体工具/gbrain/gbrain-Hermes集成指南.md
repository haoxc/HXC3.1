---
aliases:
  - GBrain Hermes Integration Guide
  - gbrain-Hermes集成
  - gbrain/Hermes集成/集成指南(JZ, GHI)
tags: [AI, AI-Agent, 教程, gbrain, hermes]
description: gbrain 在 Hermes Agent 中的安装、配置与使用流程
type: note
create-date: 2026-05-01
---

# gbrain-Hermes集成指南

**一句话定义**：gbrain 作为 Hermes 的外挂记忆脑，通过技能注册 + MCP 工具连接集成，让 Hermes 拥有跨会话的知识图谱记忆。

## 集成架构

```
Hermes Agent
├── skills/                   ← gbrain 29 个技能（signal-detector, brain-ops, query...）
├── mcp_servers:              ← gbrain MCP 服务（30+ 工具）
│   └── gbrain serve
└── ~/brain/                  ← 脑仓库（Markdown 文件，独立于 ~/gbrain 工具仓库）
```

三层集成：技能层（每次交互自动触发）→ MCP 工具层（显式调用）→ Minions 作业队列（后台批量任务）。

## 安装

### Step 1: 前置依赖

```bash
# 安装 Bun（gbrain 运行时）
curl -fsSL https://bun.sh/install | bash
export PATH="$HOME/.bun/bin:$PATH"
```

```bash
# 克隆 + 安装
git clone https://github.com/garrytan/gbrain.git ~/gbrain && cd ~/gbrain
bun install && bun link
```

验证：`gbrain --version` 输出版本号。

> 禁止 `bun install -g github:garrytan/gbrain` —— Bun 全局安装会跳过 postinstall hook 导致 schema 迁移失败。见 [issue #218](https://github.com/garrytan/gbrain/issues/218)。

### Step 2: API 密钥

```bash
export OPENAI_API_KEY=sk-...      # 必需，向量搜索
export ANTHROPIC_API_KEY=sk-ant-...  # 可选，提升搜索质量
```

写入 shell profile 或 `~/gbrain/.env`。

### Step 3: 初始化脑

```bash
gbrain init                     # 创建 PGLite 数据库（无需独立服务）
gbrain doctor --json            # 验证所有检查通过
```

### Step 4: 创建脑仓库

```bash
mkdir -p ~/brain && cd ~/brain && git init
```

按 MECE 目录结构组织：`people/` `companies/` `concepts/` 等。详细 schema 见 `~/gbrain/docs/GBRAIN_RECOMMENDED_SCHEMA.md`。

### Step 5: 导入并索引

```bash
gbrain import ~/brain/ --no-embed   # 导入 Markdown
gbrain embed --stale                # 生成向量
gbrain query "关键主题是什么？"      # 验证搜索
```

### Step 6: 构建知识图谱

```bash
# 预览
gbrain extract links --source db --dry-run | head -20

# 执行
gbrain extract links --source db
gbrain extract timeline --source db

# 验证
gbrain stats    # links > 0
```

空脑跳过此步 —— 后续 auto-link 自动填充。

## Hermes 集成

### 技能注册

gbrain 安装脚本通过 `--host hermes` 将 29 个技能写入 `~/.hermes/skills/gbrain/`。若手动安装，从 `~/gbrain/skills/` 复制或链接。

核心技能（必须立即启用）：

| 技能 | 文件 | 触发 | 作用 |
|------|------|------|------|
| signal-detector | `skills/signal-detector/SKILL.md` | 每条消息 | 并行捕获想法和实体，脑自动成长 |
| brain-ops | `skills/brain-ops/SKILL.md` | 每次回复 | 先查脑再回复，读写-充实循环 |
| query | `skills/query/SKILL.md` | 显式调用 | 三层混合搜索（关键词+向量+图谱） |
| conventions | `skills/conventions/quality.md` | 全局 | 引用格式、反链铁律、来源归属 |

技能分发器：`~/gbrain/skills/RESOLVER.md` —— 读此文件了解所有技能的路由规则。

### MCP 工具连接

在 Hermes 的 MCP 配置中注册 gbrain 服务：

```yaml
mcp_servers:
  gbrain:
    command: gbrain
    args: ["serve"]
```

注册后 Hermes 可直接调用 30+ gbrain MCP 工具：
- 查询脑（query）
- 写入页（put_page）
- 提取实体（extract）
- 图遍历（graph_query）

### cron 定时任务

| 频率 | 命令 | 作用 |
|------|------|------|
| 每 15 分钟 | `gbrain sync --repo ~/brain && gbrain embed --stale` | 实时同步 |
| 每日 | `gbrain check-update --json` | 版本检查 |
| 夜间 | 梦想循环（8 阶段） | 实体扫描、引用修复、记忆整合、跨会话模式检测 |
| 每周 | `gbrain doctor --json && gbrain embed --stale` | 健康检查 |

梦想循环是脑复合增长的核心，不可跳过。详细协议见 `~/gbrain/docs/guides/cron-schedule.md`。

## 工作流

### 交互循环

```
信号到达
 → signal-detector 捕获想法和实体（并行）
 → brain-ops 查询脑（脑优先）
 → 回复 + 脑上下文
 → 写入脑页（新信息 + 引用）
 → 自动提取类型化关系（零 LLM 调用）
 → 同步索引
```

### 确定性工作分离

| 工作类型 | → 路由 | Token 成本 | 耗时 |
|----------|--------|-----------|------|
| 确定性（同输入→同输出） | Minions 作业队列 | $0.00 | ~753ms |
| 需判断（评估/决策） | Hermes 子 Agent | ~$0.03/次 | >10s |

## 升级

```bash
cd ~/gbrain && git pull origin master && bun install
gbrain init                           # schema 迁移（幂等）
gbrain post-upgrade                   # 版本迁移说明
```

读取 `~/gbrain/skills/migrations/v<NEW_VERSION>.md` 执行回填或验证步骤。

## 验证

`~/gbrain/docs/GBRAIN_VERIFY.md` 含 7 项检查。最关键的是检查 #4（实时同步实际工作）。

## 相关

- [[gbrain 介绍]]
- [[gstack 介绍]]
- [[hermes-agent]]
