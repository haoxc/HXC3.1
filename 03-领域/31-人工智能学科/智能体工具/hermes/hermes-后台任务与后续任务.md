---
aliases: [Hermes后台任务, Hermes后续任务, Hermes不打断当前任务]
tags: [mac-工具, AI工具, Agent, Hermes]
description: Hermes 中不打扰当前任务时添加后续任务、旁路问题、后台任务和定时任务的使用方法。
type: note
ref-url: https://github.com/nesquena/hermes-webui
create-date: 2026-05-01
---

# hermes-后台任务与后续任务

## 概述

在 Hermes WebUI 中，不打扰当前任务有四种方式：排队后续任务、旁路提问、后台并行任务、定时任务。选择标准是：是否需要当前上下文、是否需要进入历史、是否要立即并行执行、是否要周期运行。

## 选择表

| 需求 | 用法 | 是否打断当前任务 | 是否进入主历史 | 适合场景 |
| --- | --- | --- | --- | --- |
| 同一任务的补充要求 | `Queue follow-up` | 否 | 是 | 当前任务结束后继续执行 |
| 临时问一句 | `/btw <question>` | 否 | 否 | 旁路问题、快速确认 |
| 并行跑一个任务 | `/background <prompt>` | 否 | 结果回贴 | 只读检查、调研、摘要 |
| 以后或周期执行 | `Tasks / Scheduled jobs` | 否 | 保存到任务运行记录 | 定期巡检、每日汇总 |

## 核心操作

### 1. 后续任务：Queue follow-up

适合在当前任务运行中追加同一上下文的要求。

操作：

1. 打开 Hermes WebUI 设置。
2. 找到 `Busy input mode`。
3. 选择 `Queue follow-up`。
4. 当前任务运行时继续发消息。

效果：消息不会中断当前 turn，会排队到当前任务结束后执行。

### 2. 旁路问题：/btw

适合问不想污染主历史的小问题。

```text
/btw Hermes 的 workspace 和 CLI cwd 有什么区别？
```

效果：Hermes 会临时回答这个问题，不把它作为主任务历史的一部分。

### 3. 后台任务：/background

适合并行执行一个相对独立的任务。

```text
/background 检查当前 Vault 的 MOC 断链，先只输出清单，不修改文件
```

效果：Hermes 创建隐藏 session，在后台并行执行。完成后结果会回贴到当前会话，显示为 Background result。

建议写法：

```text
/background 只读检查：扫描 09-工具/mac-工具/hermes 下的笔记，列出 Frontmatter 缺失项，不修改文件
```

如果后台任务可能改文件，应明确写：

```text
只读，不修改文件；先输出建议清单，等待我确认。
```

### 4. 定时任务：Tasks / Scheduled jobs

适合以后执行或周期执行。

操作：

1. 打开 `Tasks` 或 `Scheduled jobs`。
2. 新建任务。
3. 填写 `Name`、`Schedule`、`Prompt`、`Deliver output`。
4. 保存后可手动 `Run now`，也可等待计划触发。

示例 schedule：

```text
every 1h
```

```text
0 9 * * *
```

示例 prompt：

```text
每天检查当前 Vault 的 MOC 断链和新增无 Frontmatter 笔记，只输出报告，不修改文件。
```

## 判断标准

| 判断问题 | 推荐方式 |
| --- | --- |
| 这件事依赖当前任务结果吗？ | 用 `Queue follow-up` |
| 只是问一句解释，不想进入历史吗？ | 用 `/btw` |
| 可以独立跑，且希望现在并行执行吗？ | 用 `/background` |
| 不是现在跑，或需要周期运行吗？ | 用 `Tasks / Scheduled jobs` |
| 会修改同一批文件吗？ | 不建议并行；先排队或只读 |

## 常见风险

### 并行写入冲突

如果当前任务和后台任务都会编辑同一批文件，可能产生覆盖或逻辑冲突。后台任务默认建议写成只读。

### 上下文污染

不相关的小问题不要直接发到主会话，优先用 `/btw`。

### 长任务误用队列

如果后续任务很长且与当前任务关系不大，不要排队在主 session 后面，优先用 `/background` 或新会话。

## 压缩记忆

> 同一任务补充用 Queue follow-up；旁路小问用 `/btw`；独立并行用 `/background`；以后或周期执行用 Tasks。可能改文件时，后台任务先写“只读，不修改文件”。
