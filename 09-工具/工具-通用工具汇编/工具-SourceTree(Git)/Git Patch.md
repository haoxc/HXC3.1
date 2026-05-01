---
aliases: [patch, 补丁, Git patch, diff patch]
tags: [git, version-control, 工具]
description: 快速理解 Git Patch 的含义、适用场景与常用操作
type: 概念定义
create-date: 2026-04-29 23:29
---

## 一句话定义

Git Patch 是把一组代码差异保存成可传递、可审查、可重新应用的文本补丁，用来在不直接推送分支的情况下交换变更。

## 最小理解图

```text
工作区/提交中的差异
  ↓
diff 文本化
  ↓
.patch 文件或邮件
  ↓
git apply / git am 重新应用
```

## 判断标准

1. 内容核心是“差异”，不是完整项目副本。
2. 可以被审查、归档、发送给他人，或在另一个仓库/分支上应用。
3. 通常用于小范围变更、离线协作、代码评审前交换、无法直接 push 的场景。

## 和相近概念的区别

| 对象 | 区别 |
| --- | --- |
| `diff` | `diff` 是差异文本本身；`patch` 是可保存、传递、应用的差异载体。 |
| commit | commit 是仓库历史中的正式记录；patch 可以来自未提交变更，也可以从 commit 导出。 |
| pull request | PR 是平台化评审流程；patch 是轻量文件级交换，不依赖 GitHub/GitLab。 |
| stash | stash 是本地临时搁置；patch 更适合跨机器、跨人、跨仓库传递。 |

## 常用操作

生成当前未提交变更：

```bash
git diff > change.patch
```

生成某个提交的补丁：

```bash
git format-patch -1 <commit>
```

应用普通补丁：

```bash
git apply change.patch
```

应用 `format-patch` 生成的邮件式补丁，并保留作者与提交信息：

```bash
git am 0001-some-change.patch
```

检查补丁能否应用：

```bash
git apply --check change.patch
```

## 典型例子

- 在受限网络中，不能直接 push 到远端，只能把变更导出为 patch 给同事应用。
- 想把某个小修复迁移到另一个仓库，但暂时不想引入整个分支历史。
- 做代码评审前，先把候选变更以文本差异形式发给别人快速查看。

## 常见误区

- patch 不是备份。它只保存差异，依赖目标仓库已有相近的上下文。
- `git apply` 不会自动生成 commit；应用后仍需要检查、测试、提交。
- 补丁越大，冲突概率越高。大范围改动更适合分支或 PR。

## 相关链接

- [[工具-SourceTree(Git)]]

## 压缩记忆

> patch 是“可搬运的差异”：比口头说明精确，比分支轻，但不替代正式提交和评审流程。
