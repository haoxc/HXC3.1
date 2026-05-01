---
aliases:
  - Hermes CLI Fuzzy File Reference
  - hermes文件模糊引用
  - hermes/文件操作/文件模糊引用(WJMH, HFFR)
tags:
  - Hermes
  - mac-工具
  - AI工具
description: Hermes CLI 中通过自然语言或 glob 片段模糊引用文件/文件夹的方式，及底层 search_files 机制。
type: note
create-date: 2026-05-01
---

# Hermes CLI 文件模糊引用

## 概述

Hermes CLI 输入框不支持 `@` 实时文件补全（不像 Claude Code 的 `@file`），但 agent 内部通过 `search_files` 工具实现等效的模糊定位。输入自然语言或 glob 片段，agent 自动解析。

## 方式 1：自然语言描述（推荐）

直接描述你要找的文件，agent 内部调用 `search_files` 解析：

```
看一下 auxiliary 模型配置踩坑那篇笔记
找 hermes 目录下所有 profile 相关的笔记
read the note about Hermes profiles
```

**底层**：agent 提取关键词 → `search_files('*auxiliary*profile*', target='files')` → 匹配结果 → `read_file`。

## 方式 2：glob 片段

输入时直接写通配符，agent 透传：

```
read 09-工具/mac-工具/hermes/hermes-aux*
找 *profile*使用*.md
```

## 方式 3：内容搜索定位

不记得文件名，只记得内容：

```
搜包含 "auxiliary.vision.model" 的笔记
grep "provider: auto" 在 config.yaml
```

底层：`search_files(pattern='auxiliary.*vision.*model', target='content')`

## 本质

不是 CLI 输入框帮你补全，而是 agent 收到指令后调用 `search_files` 定位。三个搜索维度：

| 维度 | 工具调用 | 适用场景 |
|------|---------|---------|
| 文件名模糊 | `search_files('*glob*', target='files')` | 知道名字片段 |
| 内容正则 | `search_files('regex', target='content')` | 只记得内容 |
| 路径纠错 | `read_file` 自动提示相似路径 | 路径拼错 |

## 相关

- [[hermes-profile使用指南]]
- [[hermes-模型配置]]
