---
aliases: [Hermes CLI指令, 常用命令, hermes命令速查]
tags: [mac-工具, AI工具, Agent, Hermes]
description: Hermes CLI 常用命令速查：配置、模型、Profile、技能、任务管理。
type: note
create-date: 2026-05-02
---

# Hermes 常用指令速查

## 启动与配置

| 命令 | 说明 |
|------|------|
| `hermes` | 启动默认会话（CLI 交互） |
| `hermes -p vault-only` | 以 vault-only profile 启动 |
| `hermes config list` | 列出所有配置项 |
| `hermes config get <key>` | 查看单个配置值 |
| `hermes config set <key> <value>` | 设置配置值 |
| `hermes config edit` | 编辑器打开 config.yaml |

## 模型与 Provider

| 命令 | 说明 |
|------|------|
| `hermes models list` | 列出已配置的模型 |
| `hermes models providers` | 列出已配置的 provider |
| `hermes --model <model>` | 启动时指定模型 |
| `hermes --provider <provider>` | 启动时指定 provider |

## Profile 管理

| 命令 | 说明 |
|------|------|
| `hermes profile list` | 列出所有 profile |
| `hermes -p <name>` | 以指定 profile 启动 |

Profile 定义在 `~/.hermes/profiles/<name>/`。Profile 可限定工具集、模型、技能范围，减少无关 token 开销。

详见 [[hermes-profile使用指南]]。

## 技能管理

| 命令 | 说明 |
|------|------|
| `hermes skills list` | 列出可用技能 |
| `hermes skills view <name>` | 查看技能内容 |
| `hermes skills reload` | 热重载技能 |

Agent 端通过 `skill_view(name)` 和 `skill_manage(action, ...)` 操作技能。

详见 [[Hermes Skill 内容地图]]。

## 会话管理

| 命令 | 说明 |
|------|------|
| `hermes` | 新会话 |
| `hermes --continue` | 恢复最近会话 |
| `hermes sessions list` | 列出历史会话 |
| `/clear` | 清空上下文（会话内指令） |
| `/new` | 新建会话（会话内指令） |

## 后台任务

| 命令 | 说明 |
|------|------|
| `/background <task>` | 投递后台任务 |
| `/btw` | 查看后台任务队列 |
| `cronjob(action="create", ...)` | 创建定时任务 |

详见 [[Hermes-后台进程管理]]、[[Hermes-定时任务]]。

## 常用代理配置

### 直接使用

```
# 交互模式
hermes

# 单次命令
hermes -c "列出当前目录" 
```

### Claude Code 委派

```
hermes -p vault-only  # 知识管理
claude -p "实现 foo 功能"  # 代码工程
```

Agent 分工：Hermes = 知识管理 + 任务路由；Claude Code = 代码工程。

详见 [[Hermes-介绍]]、[[Hermes-Claude-Code-CLI协同方案]]。

## 配置文件位置

| 文件 | 路径 |
|------|------|
| 主配置 | `~/.hermes/config.yaml` |
| Profile | `~/.hermes/profiles/<name>/` |
| 技能 | `~/.hermes/skills/` |
| 会话历史 | `~/.hermes/sessions/` |
| 计划文件 | `~/.hermes/plans/` |

## 故障排查速查

| 问题 | 排查命令 |
|------|----------|
| 技能未生效 | `hermes skills reload` |
| 模型连接失败 | `hermes config get models` + 检查 API key |
| 配置语法错误 | `hermes config edit` 检查 YAML 缩进 |
| Profile 工具缺失 | 检查 `~/.hermes/profiles/<name>/config.yaml` 中 `enabled_toolsets` |
