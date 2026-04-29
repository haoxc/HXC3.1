---
aliases:
  - Claude Code Effort
  - Claude Code推理强度
  - Claude Code思考强度
  - effort
  - effortLevel
tags: [概念定义, ai/智能体/工具/claude, Claude-Code]
description: 快速理解 Claude Code effort level、extended thinking 与 thinking summary 的区别和用法
type: 学习笔记
ref-url:
  - https://code.claude.com/docs/en/model-config
  - https://code.claude.com/docs/en/settings
  - https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
create-date: 2026-04-28 00:00
---

# Claude Code Effort

## 一句话定义

**推理强度(Effort Level)** 是 Claude Code 控制模型自适应思考深度的设置：低 effort 更快、更省 token，高 effort 更适合复杂推理、代码架构、长任务和高风险修改。

## 最小理解图

```text
任务复杂度
   ↓
effort level: low / medium / high / xhigh / max
   ↓
模型决定每一步要不要多思考、思考多少
   ↓
输出质量、速度、token 消耗之间取舍
```

## 支持级别

| 模型 | 支持的 effort level |
| --- | --- |
| Opus 4.7 | `low`、`medium`、`high`、`xhigh`、`max` |
| Opus 4.6 / Sonnet 4.6 | `low`、`medium`、`high`、`max` |

如果当前模型不支持你设置的级别，Claude Code 会退到该模型支持的、最接近且不高于目标的级别。例如：在 Opus 4.6 上设置 `xhigh`，实际会按 `high` 运行。

## 什么时候用哪个

| 级别 | 适合场景 |
| --- | --- |
| `low` | 很短、很明确、对智能要求不高、追求速度的任务 |
| `medium` | 成本敏感、可以接受推理能力略降的普通任务 |
| `high` | 需要较稳判断的编码、审计、设计任务 |
| `xhigh` | 大多数复杂 coding / agentic 任务的推荐高质量档位，尤其适合 Opus 4.7 |
| `max` | 极复杂、很高风险、需要深度推理的任务；可能收益递减，也容易过度思考 |

实用口径：

```text
日常简单任务：medium / high
复杂代码与结构设计：xhigh
非常关键的架构、审计、迁移：max 或 ultrathink
```

## 设置方式

会话内设置：

```text
/effort xhigh
/effort high
/effort auto
```

打开交互选择器：

```text
/effort
```

启动时设置：

```bash
claude --effort xhigh
```

环境变量：

```bash
export CLAUDE_CODE_EFFORT_LEVEL=xhigh
```

配置文件：

```json
{
  "effortLevel": "xhigh"
}
```

可写入：

```text
~/.claude/settings.json
.claude/settings.local.json
```

优先级简化理解：

```text
CLAUDE_CODE_EFFORT_LEVEL
> 已配置的 effortLevel
> 当前模型默认值
```

Skill 或 subagent 也可以在 frontmatter 里写：

```yaml
---
effort: high
---
```

## `ultrathink` 和 `/effort` 的区别

| 用法 | 作用 |
| --- | --- |
| `/effort xhigh` | 改变当前会话的 effort setting |
| `claude --effort xhigh` | 启动本次会话时指定 effort |
| `effortLevel` | 持久化默认 effort |
| `ultrathink` | 本轮提示词里要求更深思考，不改变 API 层面的 effort level |

示例：

```text
ultrathink 这个项目结构迁移方案的风险、替代路径和回滚策略
```

`ultrathink` 适合一次性深思考；`/effort` 适合把后续一段会话都切到更高或更低推理强度。

## 和显示思考内容的关系

Effort 控制的是“模型是否更愿意思考、思考多少”，不是“是否显示完整思考过程”。

如果你想在 Claude Code 里看到 extended thinking 的摘要，可以设置：

```json
{
  "alwaysThinkingEnabled": true,
  "showThinkingSummaries": true
}
```

区别：

| 设置 | 含义 |
| --- | --- |
| `effortLevel` | 控制推理强度 |
| `alwaysThinkingEnabled` | 默认启用 extended thinking |
| `showThinkingSummaries` | 在交互会话中显示 extended thinking 摘要 |
| `showTurnDuration` | 显示每轮耗时，不等于显示思考 |

注意：`showThinkingSummaries` 显示的是摘要，不是完整原始内部思考。关闭显示也不会减少模型思考花费；要减少花费应降低 effort 或关闭 thinking。

## 典型例子

复杂结构设计前：

```text
/effort xhigh
先不要改文件。请先判断目录结构问题、关键假设、风险和迁移路径。
```

一次性深度审计：

```text
ultrathink 审计这个课程资料库的目录边界、MOC负载和学习材料泄漏风险
```

简单任务后恢复默认：

```text
/effort auto
```

## 常见误区

1. **以为 effort 越高越好。**  
   不一定。`max` 可能收益递减，也可能让简单问题变慢、变啰嗦。

2. **以为 `ultrathink` 等于 `/effort max`。**  
   不等。`ultrathink` 是提示词内的一次性深思考指令，不改变会话 effort setting。

3. **以为显示 thinking summary 等于显示完整思维链。**  
   不等。Claude Code 显示的是 extended thinking 摘要，完整内部思考不会作为普通答案直接展示。

4. **以为关闭 summary 就能省 token。**  
   不对。summary 显示开关只影响你看到什么；要减少思考消耗，应调低 effort。

## 压缩记忆

> Effort 是 Claude Code 的“推理强度旋钮”：`/effort` 管持续设置，`ultrathink` 管本轮深思考，`showThinkingSummaries` 只管是否显示思考摘要。复杂任务用 `xhigh`，关键任务临时用 `max` 或 `ultrathink`，简单任务不要过度拉高。
