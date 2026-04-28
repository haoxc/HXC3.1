---
aliases:
  - Claude Code Checkpoint
  - Claude Code检查点
  - checkpoint
  - 检查点
tags: [概念定义, ai/智能体/工具/claude, Claude-Code]
description: 快速理解 Claude Code Checkpoint 的核心含义、边界与使用场景
type: 概念定义
ref-url:
  - https://code.claude.com/docs/en/checkpointing
  - https://code.claude.com/docs/en/commands
create-date: 2026-04-28 00:00
---

# Claude Code Checkpoint

## 一句话定义

**检查点(Checkpoint)** 是 Claude Code 在当前会话中自动记录的可恢复状态点，用来把代码、对话，或二者一起回到之前某个时间位置。

## 最小理解图

```text
用户提示词 / Claude 文件编辑
        ↓
Claude Code 自动生成 checkpoint
        ↓
使用 /rewind 选择某个 checkpoint
        ↓
恢复代码 / 恢复对话 / 二者都恢复 / 从该点后压缩上下文
```

## 判断标准

1. 它属于某个 Claude Code session 内部，而不是独立项目、Git branch 或 Git commit。
2. 它可以被 `/rewind`、`/checkpoint` 或 `/undo` 打开并选择。
3. 它主要记录 Claude Code 文件编辑工具造成的改动，以及对应会话上下文状态。
4. 它适合短期回退和试错，不适合承担长期版本管理。

## 和相近概念的区别

| 概念          | 核心区别                                                              |
| ----------- | ----------------------------------------------------------------- |
| `/rewind`   | `/rewind` 是进入回退菜单的命令；checkpoint 是被选择和恢复的历史状态点。                    |
| Session     | session 是整条会话任务线；checkpoint 是这条任务线里的某个恢复点。                        |
| Branch/Fork | branch 是从当前会话派生一条新会话；checkpoint 是在当前会话内回到旧状态。                     |
| Git commit  | Git commit 是长期版本历史；checkpoint 是 Claude Code 的会话级临时恢复点。            |
| `/compact`  | `/compact` 压缩整段上下文；checkpoint 的 Summarize from here 可以从选定点之后定向压缩。 |

## 核心组件

| 组件           | 作用                                                   |
| ------------ | ---------------------------------------------------- |
| 自动追踪         | Claude Code 会在工作过程中自动捕获状态，通常每次用户提示都会形成新的 checkpoint。 |
| 文件编辑记录       | 追踪 Claude Code 文件编辑工具产生的文件改动。                        |
| 会话状态         | 支持把对话历史回到某个点，或只保留当前代码。                               |
| `/rewind` 菜单 | 用来选择历史提示词或检查点，并决定恢复范围。                               |
| 自动清理         | checkpoint 会随 session 清理周期被清理，默认约 30 天，可配置。          |

## 典型例子

- 让 Claude Code 重构模块后发现方向错误，用 `/rewind` 回到重构前的 checkpoint。
- Claude 改了代码，但当前讨论很有价值，选择只恢复代码，保留对话。
- 对话变得很长，但前半段很重要，选择某个 checkpoint 后 `Summarize from here` 压缩后半段上下文。

## 示例：创建 checkpoint

Claude Code 通常不需要手动创建 checkpoint。每次用户发送提示词时，Claude Code 都会自动生成一个 checkpoint；当 Claude 使用文件编辑工具改文件时，也会记录可回退状态。

所以“创建 checkpoint”的实际做法是：在关键操作前发一个明确的提示词，让它成为可识别的恢复点。

示例：

```text
现在先不要改文件。请确认当前状态可以作为重构前 checkpoint，并简要说明接下来要改哪些文件。
```

Claude 回复后，这条提示词会出现在 `/rewind` 的历史列表里。之后如果重构方向不对，可以：

```text
/rewind
```

然后选择这条提示词附近的 checkpoint，再选择恢复方式：

```text
Restore code and conversation
Restore conversation
Restore code
Summarize from here
```

更实用的写法：

```text
先建立一个可回退点：不要改文件，只记录当前方案边界。接下来我会让你重构 API 层。
```

压缩理解：

```text
创建 checkpoint
= 发送一个清晰的用户提示词
= 让这个提示词成为 /rewind 里容易识别的恢复点
```

## 常见误区

1. **把 checkpoint 当成 Git commit。**  
   不对。checkpoint 是 Claude Code 的会话级恢复点，适合快速撤销；Git commit 才是长期、可协作、可审计的版本历史。

2. **以为 checkpoint 能撤销所有文件变化。**  
   不一定。通过 bash 命令产生的文件变化，例如 `rm`、`mv`、`cp`，通常不能通过 `/rewind` 完整撤销。

3. **以为外部编辑也会被完整追踪。**  
   不一定。手动在编辑器里改文件，或其他并发 Claude Code session 改文件，通常不属于当前 session 的完整 checkpoint 范围。

4. **以为 checkpoint 等于 branch。**  
   不对。checkpoint 是回到过去；branch/fork 是从当前点派生一条新的会话路径。

## 概念图链接

- [Checkpointing - Claude Code Docs](https://code.claude.com/docs/en/checkpointing)  
  推荐看：How checkpoints work、Rewind and summarize、Limitations。它明确说明 checkpoint 如何自动追踪、如何恢复，以及不能替代版本控制。
- [Commands - Claude Code Docs](https://code.claude.com/docs/en/commands)  
  推荐看：`/rewind`、`/branch`、`/resume` 的命令说明。适合把 checkpoint 放回 Claude Code 命令体系中理解。

## 压缩记忆

> Checkpoint 是 Claude Code 的“会话级恢复点”：用 `/rewind` 回到它，用 Git commit 管长期版本。它适合撤回 Claude 的编辑和对话状态，但不能替代 Git，也不保证追踪 bash 或外部改动。
