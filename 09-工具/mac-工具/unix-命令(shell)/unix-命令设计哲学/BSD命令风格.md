---
aliases:
  - mac/shell/命令/命名风格/BSD风格, POSIX/GUN风格(command bsd style)
tags:
  - 命令/风格
description:
type:
ref-url:
create-date: 2026-02-06
---
## 内容
在 Unix 和类 Unix 系统中，处理命令行选项有两种主要的风格：
1. **BSD 风格**：起源于伯克利软件发行版（Berkeley Software Distribution）。在这种风格中，某些命令（尤其是 `ps`）允许用户将多个单字母选项组合在一起，并且**不需要**在前面加上连字符。因此，`ps aux` 是 `a`、`u` 和 `x` 三个选项的组合。
2. **POSIX/GNU 风格**：这是现代 Linux 系统和 POSIX 标准更推荐的风格。在这种风格中，每个选项前都需要一个连字符。例如，BSD 风格的 `ps aux` 对应于 POSIX 风格的 `ps -aux` 或 `ps -a -u -x`。