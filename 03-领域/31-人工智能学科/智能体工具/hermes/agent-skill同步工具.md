---
aliases:
  - Agent Skill Sync Tool
  - 跨端skill同步
  - hermes/配置/skill同步工具(SST, ASST)
tags: [hermes, codex, claude-code, 工具]
description: agent-skill 同步工具：从 Vault 核心规范生成三端（Hermes/Codex/Claude Code）SKILL.md
type: note
create-date: 2026-05-01
---

# agent-skill同步工具

**一句话定义**：以 Vault 中 `99-设置/agent-skills/<skill>/core.md` 为核心规范，通过 `manifest.yaml` 配置各端差异，自动生成三端 SKILL.md。

## 目录结构

```
99-设置/agent-skills/
├── sync-agent-skills.py     # 同步脚本
└── <skill-name>/
    ├── core.md              # 不变知识（命名/路由/质量审查/陷阱）含 {{RUNTIME_PREPEND}} / {{RUNTIME_APPEND}} 占位
    ├── manifest.yaml        # 运行时配置：路径、frontmatter、prepend/append 块
    ├── hermes/SKILL.md      # 生成副本（追踪用）
    ├── codex/SKILL.md       # 生成副本
    └── claude-code/SKILL.md # 占位（待启用）
```

## 运行

```bash
# 同步单个 skill
python3 99-设置/agent-skills/sync-agent-skills.py --skill note-crafter

# 同步全部
python3 99-设置/agent-skills/sync-agent-skills.py

# 仅同步某一端
python3 99-设置/agent-skills/sync-agent-skills.py --skill note-crafter --runtime codex

# 预览（不写入）
python3 99-设置/agent-skills/sync-agent-skills.py --skill note-crafter --dry

# 列出所有管理的 skill
python3 99-设置/agent-skills/sync-agent-skills.py --list
```

## 工作原理

| 阶段 | 操作 |
|------|------|
| 1 读取 | 加载 `core.md`（不变知识） + `manifest.yaml`（端差异） |
| 2 组装 | frontmatter（端特定字段） + prepend（执行策略/路由表） + core（共享规范） + append（运维脚本/参考） |
| 3 写入 | 写入运行时路径 + 本地副本（`<端>/SKILL.md`） |
| 4 记录 | `manifest.yaml` 更新 `last_sync` 时间戳 |

`{{RUNTIME_PREPEND}}` 和 `{{RUNTIME_APPEND}}` 是 core.md 中的占位符，由 sync 脚本替换为 manifest 中对应运行时的 prepend/append 内容。

## 端差异

| 维度 | Hermes | Codex |
|------|--------|-------|
| 路径 | `~/.hermes/skills/<category>/<name>/` | `~/.codex/skills/<name>/` |
| frontmatter | 含 `triggers` / `related_skills` | 仅 `name` / `description` |
| 执行策略 | 4-window（skill_view → execute_code → write_file → execute_code） | 4-window（简化版） |
| 运维脚本 | 完整 bash/python 命令 | 简化版 |
| 语言 | 中文 | 英文 |

Claude Code 端当前 `enabled: false`，待实际使用时启用。

## 已管理技能

| 技能 | 端 | 状态 |
|------|----|------|
| note-crafter | hermes, codex | ✓ 已同步（2026-05-01） |
| pjx-common-auditor | hermes, codex | 待迁移 |

## 新 skill 接入流程

1. 从 authoritative 端提取 `core.md`
2. 识别不变知识（命名/规则/流程）与端差异（工具名/执行策略/运维）
3. 写 `manifest.yaml`（prepend/append 各端差异块）
4. 运行 `sync-agent-skills.py --skill <name> --dry` 预览
5. 确认无误后正式同步

## 相关

- [[Hermes-Claude-Code-Codex-Skill维护课题]]
- [[Hermes Skill 内容地图]]
- [[99-设置/vault-rules.yaml]]
