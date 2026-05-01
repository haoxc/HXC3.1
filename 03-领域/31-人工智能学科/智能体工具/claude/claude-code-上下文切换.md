---
aliases: [Claude Code上下文切换, Claude Code会话上下文管理]
tags: [ai/智能体/工具/claude, Claude-Code]
description: Claude Code 会话内上下文切换、压缩、恢复与项目切换的使用备忘
type: 学习笔记
ref-url:
  - https://code.claude.com/docs/en/commands
  - https://code.claude.com/docs/en/checkpointing
  - https://code.claude.com/docs/en/memory
create-date: 2026-04-28 00:00
---

# Claude Code 上下文切换

> [!summary]
> Claude Code 可以在会话中调整一部分上下文，例如清空、压缩、恢复历史会话、创建会话分支、回到检查点、增加可访问目录。但“真正切换主项目上下文”通常还是退出后进入新目录重新启动更干净。

## 核心理解

Claude Code 的上下文不只是聊天记录，至少包括几层：

| 上下文层     | 含义                                                           | 常见切换方式                                          |
| -------- | ------------------------------------------------------------ | ----------------------------------------------- |
| 对话上下文    | 当前会话里的历史消息、任务状态、Claude 已经推理过的信息                              | `/clear`、`/compact`、`/resume`                   |
| 会话上下文    | 某一次 Claude Code 会话本身，包括 session id 和历史记录                     | `/resume`、`claude --resume`、`claude --continue` |
| 检查点上下文   | 当前会话内某个历史时刻的代码与对话状态                                           | `/rewind`、`/checkpoint`、`/undo`                 |
| 工作目录上下文  | Claude Code 启动时所在的项目目录                                       | 退出后 `cd /path/to/project && claude`             |
| 文件访问上下文  | Claude 当前有权限读取或修改的目录                                         | `/add-dir <path>`、`claude --add-dir <path>`     |
| 项目记忆上下文  | `CLAUDE.md`、`.claude/CLAUDE.md`、`.claude/rules/`、auto memory | `/memory`、编辑项目规则文件                              |
| 模型与输出上下文 | 当前使用的模型、输出风格、权限模式等                                           | `/model`、`/output-style`、`/permissions`         |

关键区别：

```text
会话内切换上下文
= 调整当前会话能保留什么、忘掉什么、访问哪里、恢复哪段历史

切换主项目上下文
= 换一个 cwd / project_dir，通常需要重新启动 Claude Code
```

## 会话中常用命令

| 命令                  | 作用             | 适合场景                |
| ------------------- | -------------- | ------------------- |
| `/clear`            | 清空当前对话历史，开始新对话 | 换任务、上下文已经混乱         |
| `/compact`          | 压缩已有对话，保留摘要    | 当前任务没结束，但上下文太长      |
| `/compact <指令>`     | 按指定重点压缩上下文     | 只保留某个 bug、某组文件、某个方案 |
| `/resume`           | 打开历史会话选择器      | 回到之前某个任务            |
| `/resume <session>` | 恢复指定会话         | 已知道会话 ID 或名称        |
| `/branch [name]`    | 从当前点创建会话分支     | 尝试另一个方案，同时保留原路径     |
| `/rewind`           | 回到当前会话的某个检查点   | 后悔某一步、回退代码或对话状态     |
| `/add-dir <path>`   | 增加当前会话可访问目录    | 临时查看或修改另一个目录        |
| `/memory`           | 查看或编辑记忆文件      | 调整长期项目规则、个人偏好       |

## 什么时候用哪个

| 需求                          | 推荐操作                                           |
| --------------------------- | ---------------------------------------------- |
| 当前任务结束，准备换一个问题              | `/clear`                                       |
| 当前任务还没结束，但上下文太满             | `/compact 只保留当前任务、已改文件、待验证事项`                  |
| 想回到昨天或之前的某次 Claude Code 任务  | `/resume` 或 `claude --resume`                  |
| 想从当前方案分叉，试另一个解法             | `/branch 新方案名称`                                |
| 想撤回当前会话中的某一步                  | `/rewind`                                      |
| 想只回退对话、只回退代码，或二者都回退          | `/rewind` 后选择对应恢复方式                            |
| 想让当前会话临时访问另一个目录             | `/add-dir ../other-project`                    |
| 想真正切到另一个项目                  | `exit` 后 `cd /path/to/other-project && claude` |
| 想修改 Claude Code 每次都应遵守的项目规则 | `/memory` 或编辑 `CLAUDE.md`                      |

## 概念补充：Checkpoint

**检查点(Checkpoint)** 是 Claude Code 在当前会话中自动记录的可恢复状态点，用来把对话、代码或二者一起回到之前某个时间位置。

最小理解：
```text
用户提示词 / Claude 编辑动作
        ↓
自动生成 checkpoint
        ↓
/rewind 选择某个 checkpoint
        ↓
恢复代码、恢复对话，或压缩该点之后的上下文
```

判断一个东西是不是 checkpoint，看三点：
1. 它属于某个 Claude Code session 内部，而不是独立项目或 Git 分支。
2. 它可以被 `/rewind` 选中，用来恢复代码、恢复对话，或二者都恢复。
3. 它主要追踪 Claude Code 文件编辑工具产生的改动，不完整追踪 shell 命令或外部手动改动。

容易混淆：

| 容易混淆对象      | 区别                                                     |
| ----------- | ------------------------------------------------------ |
| `/rewind`   | `/rewind` 是操作入口；checkpoint 是被选择和恢复的历史状态点。              |
| Session     | session 是整条会话任务线；checkpoint 是这条任务线里的某个恢复点。             |
| Branch/Fork | branch 是从当前会话派生一条新会话；checkpoint 是在当前会话内回到旧状态。          |
| Git commit  | Git commit 是长期版本历史；checkpoint 是 Claude Code 的会话级临时恢复点。 |

典型例子：

```text
你让 Claude Code 重构一个模块。
Claude 修改了 5 个文件。
发现方向不对。
用 /rewind 选中重构前的 checkpoint。
选择只恢复代码，或代码和对话一起恢复。
```

## 关于 `/rewind` 的边界

`/rewind` 是当前会话内的回溯命令，用来回到某个 checkpoint。它也可以通过 `Esc` + `Esc` 打开，官方别名包括 `/checkpoint`、`/undo`。

进入 `/rewind` 后，通常可以按历史提示词或检查点选择一个时间位置，再决定恢复范围：

| 恢复方式 | 含义 |
| --- | --- |
| Restore code and conversation | 代码和对话都回到该检查点 |
| Restore conversation | 只回退对话，保留当前代码 |
| Restore code | 只回退代码，保留当前对话 |
| Summarize from here | 从该点之后压缩成摘要，释放上下文空间 |

它和其他命令的区别：

```text
/rewind = 回到当前会话里的某个 checkpoint
/resume = 找回另一个历史 session
/branch = 从当前会话分叉出一个新 session
/clear = 清空当前对话上下文
```

注意边界：

```text
/rewind 是会话级后悔药
Git 是长期版本管理
```

`/rewind` 适合撤回 Claude Code 在当前会话中推进过的一段工作，但不应该替代 Git。尤其是通过 shell 命令造成的文件变化，例如 `rm`、`mv`、`cp`、`sed -i`，不一定能被 checkpoint 系统完整追踪。

## 关于 `/add-dir` 的边界

`/add-dir` 的作用更接近“增加文件访问范围”，不是完整切换项目。

它能解决：

```text
当前项目需要参考 shared-lib
当前任务需要读取另一个目录的配置
当前会话要跨目录修改少量文件
```

但它不等于：

```text
切换当前 cwd
切换主 project_dir
自动加载新增目录下的全部 .claude 配置
自动变成另一个项目的完整上下文
```

如果目标是进入另一个项目长期工作，更稳的方式是：

```bash
exit
cd /path/to/other-project
claude
```

## 命令示例

继续当前目录最近一次会话：

```bash
claude --continue
```

打开历史会话选择器：

```bash
claude --resume
```

恢复指定会话：

```bash
claude --resume <session-id>
```

启动时增加额外目录：

```bash
claude --add-dir ../shared-lib ../docs
```

会话中增加额外目录：

```text
/add-dir ../shared-lib
```

按任务重点压缩当前上下文：

```text
/compact 只保留当前 bug、关键假设、已修改文件、未完成验证
```

回到当前会话的某个检查点：

```text
/rewind
```

## 实践建议

1. 轻量换话题：用 `/clear`，避免旧任务污染新任务。
2. 长任务继续推进：用 `/compact`，不要过早丢掉上下文。
3. 需要试验方案：用 `/branch`，比在同一条会话里来回反悔更清楚。
4. 单步或阶段性后悔：用 `/rewind`，明确选择只回退对话、只回退代码，还是二者都回退。
5. 跨目录参考：用 `/add-dir`，但要明确它只是扩展访问范围。
6. 跨项目长期工作：退出后在新项目目录重新启动 Claude Code。
7. 固化长期规则：写进 `CLAUDE.md` 或 `.claude/rules/`，不要依赖某一次聊天记录。

## 压缩记忆

> Claude Code 会话中可以切换“对话、历史会话、分支、检查点和可访问目录”。`/rewind` 用来回到当前会话的 checkpoint，`/resume` 用来恢复历史 session，`/branch` 用来分叉新 session。真正换项目，退出后进入新目录重新启动最清晰。
