---
aliases:
  - 交互/命令行界面(Command Line Interface, CLI)
tags:
description:
type:
ref-url:
---
## 内容
CLI 是 ==Command Line Interface（命令行界面）的缩写==。

它是一种通过输入文本命令来与计算机程序或操作系统进行交互的方式，与我们常用的鼠标点击图标（GUI，图形用户界面）相对。 [2, 3]

## 1. 核心概念
- **交互方式**：用户在终端（Terminal）或控制台（Console）中通过键盘输入特定的指令，程序根据输入执行操作并以文本形式返回结果。
- **常见称呼**：命令行、cmd、控制台、Shell 或终端。

## 2. 为什么开发者喜欢使用 CLI？

- **高效简洁**：对于熟练用户，输入一行命令往往比在多个窗口间点击鼠标更快。
- **自动化与脚本化**：CLI 命令可以轻松组合成脚本（如.sh 或.bat 文件），实现批量处理和自动化运维。
- **资源占用低**：相比图形界面，CLI 消耗的系统资源极少，非常适合远程服务器管理。

## 3. 常见的 CLI 实例

- 操作系统自带：Windows 的 [Command Prompt](https://zhuanlan.zhihu.com/p/1973806836378530946) (cmd) 和 PowerShell，以及 Linux/macOS 的 Bash 或 Zsh。
- 开发工具：
    - Git CLI：用于版本控制。
    - Vue CLI / React CLI：用于快速搭建前端项目框架。
    - GitHub CLI：在终端管理 GitHub 的仓库和 Issue。
- 云平台管理：如 [AWS CLI](https://aws.amazon.com/cn/cli/)、Azure CLI 和 [阿里云 CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)，用于远程管理云端服务器和资源。 [2, 4, 7, 8, 9, 10, 11, 12]

## 4. 优势
- **确定性的反馈循环 (Predictable Feedback Loop)**: 智能体工作时遵循“`规划-执行-观察`”的循环。CLI 提供的文本输出（如成功提示、错误代码、退出状态）是**结构化且确定**的
 - **组合和编排能力**: CLI 遵循 Unix 哲学：“做一件事并把它做好”。通过“管道（Pipe）”，智能体可以将多个工具连接起来