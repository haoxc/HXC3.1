---
title: hermes应用-obsidian协同
aliases:
  - Hermes Obsidian 协同
  - Hermes 应用 Obsidian 协同
  - Hermes 与 Obsidian Vault 协同
tags:
  - mac-工具
  - AI工具
  - Hermes
  - Obsidian
  - 知识管理
description: 规划 Hermes 与当前 Obsidian Vault 的协同方式，包括架构定位、最小配置、典型应用场景、项目专用 skill、Cron 自动化和安全边界。
type: 应用规划
create-date: 2026-04-29
ref-url:
  - https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian
  - https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd
  - https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/
---

# hermes应用-obsidian协同

## 一句话结论

Obsidian 负责“人读、人改、知识结构可视化”；Hermes 负责“自动读写、整理、巡检、调度、把任务变成笔记资产”。二者协同的关键不是让 Hermes 替代 Obsidian，而是让 Hermes 成为当前 Vault 的自动化整理员和任务调度员。

当前 Vault 路径：

```text
/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)
```

## 协同架构

| 层                     | 角色        | 做什么                                  |
| --------------------- | --------- | ------------------------------------ |
| Obsidian              | 知识前端      | 阅读、编辑、双链、MOC、图谱、人工判断                 |
| Hermes                | Agent 编排层 | 定时整理、批量创建笔记、巡检链接、调用 skill            |
| Hermes Obsidian skill | 文件操作层     | 读、搜、创建 Markdown 笔记                   |
| 项目专用 Vault skill      | 规则适配层     | 当前 Vault 的 MOC、frontmatter、命名、目录归属规则 |
| Codex / Claude Code   | 执行代理      | 复杂文件修改、代码仓库任务、批量重构                   |
| Git                   | 安全层       | diff、版本回退、同步备份                       |

最小理解：

```text
Hermes 负责调度
Obsidian skill 负责文件访问
项目专用 Vault skill 负责“怎么写才符合当前 Vault”
Codex / Claude Code 负责复杂执行
Git 负责兜底和回退
```

## 最小配置

Hermes 官方内置 `obsidian` skill，可通过环境变量指定 Vault。

建议写入：

```text
~/.hermes/.env
```

内容：

```bash
OBSIDIAN_VAULT_PATH="/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"
```

验证命令：

```bash
hermes chat --toolsets skills -q "/obsidian 搜索 hermes 相关笔记"
```

或在 Hermes 交互界面中测试：

```text
/obsidian 搜索 hermes 相关笔记
/obsidian 读取 09-工具/mac-工具/hermes/hermes.md
/obsidian 创建一篇关于 xxx 的笔记
```

> [!warning]
> Vault 路径包含括号，命令中必须加引号。不要把 API key、token、账号密码写进 Vault 笔记。

## 为什么不只用通用 Obsidian skill

Hermes 的通用 `obsidian` skill 解决的是文件访问问题：

- 读笔记。
- 搜索笔记。
- 创建笔记。
- 使用 `[[wikilinks]]`。

但当前 Vault 有自己的知识库规范：

- MOC 页面。
- frontmatter 字段。
- 目录分层。
- 专题笔记。
- 术语卡。
- 图表说明页。
- 中文命名习惯。
- 不同目录的归属规则。

因此通用 `obsidian` skill 只能作为底层访问能力。真正要做到“写得像这个 Vault 的笔记”，还需要项目专用 skill。

建议新增：

```text
hxc-obsidian-vault
```

职责：

- 识别当前 Vault 的笔记类型。
- 判断笔记应该归属哪个 MOC。
- 套用 frontmatter、命名、链接和图表说明页规则。
- 避免创建孤立笔记。
- 批量修改前先输出计划。

## 典型应用场景

### 1. 每日自动巡检

Hermes Cron 每天或每周检查当前 Vault 的局部质量。

可检查：

- 是否有未挂 MOC 的新笔记。
- `09-工具/mac-工具/hermes/` 是否有孤立文件。
- 是否有重复主题或近似文件名。
- 图表 SVG 是否有同名说明页。
- frontmatter 是否缺少 `tags`、`description`、`type`、`create-date`。

示例任务：

```text
每天 09:00 检查 09-工具/mac-工具/hermes/ 下新增或修改的 Markdown，列出未挂 MOC、frontmatter 不完整、SVG 无说明页的问题，只输出报告，不直接修改。
```

### 2. 快速捕获

通过 Hermes Gateway 或 CLI 把临时想法写入指定入口。

可写入：

- daily note 的 `## 新建`。
- 指定 inbox。
- 某个课题的待整理区。

示例：

```text
把这句话作为新建笔记线索写入今天 daily note 的 ## 新建：Hermes 如何做 Obsidian 自动巡检。
```

### 3. 课题笔记生成

Hermes 根据主题调用项目专用 skill，生成结构化笔记，并挂到对应 MOC。

适合：

- 工具应用规划。
- 概念辨析。
- 技术方案。
- 调研摘要。
- 工作流说明。

约束：

- 先判断 MOC 位置。
- 再创建笔记。
- 最后更新 MOC。
- 不创建孤立笔记。

### 4. 链接与目录维护

Hermes 可定期检查 Obsidian 链接和目录结构。

可检查：

- `[[wikilink]]` 是否断链。
- MOC 是否漏挂新笔记。
- 文件名是否过泛，例如 `方案.md`、`配置.md`。
- 是否有同主题多文件未合并。
- 是否存在图表文件但无说明页。

处理策略：

```text
默认只输出报告。
用户确认后再批量修改。
```

### 5. 知识库问答

简单检索：

```text
Hermes obsidian skill 搜索文件名和正文。
```

复杂检索：

```text
安装 qmd 或 llm-wiki 类 skill，对 Markdown notes 做本地知识库检索。
```

适合问题：

- “当前 Hermes 相关笔记有哪些？”
- “关于 LiteLLM 的配置笔记在哪里？”
- “哪些笔记提到了 DeepSeek V4 Pro？”
- “最近新增的工具类笔记是否都挂到了 MOC？”

### 6. 图表与说明页维护

Hermes 可以生成 SVG / Excalidraw / Mermaid，并同时创建说明页。

当前已采用的模式：

```text
Hermes-执行态编排图.svg
Hermes-执行态编排图.md
```

维护规则：

- 图表文件不单独裸放。
- 每张图有同名说明页。
- 说明页挂到对应 MOC。
- 图表页解释阅读口径，不塞长篇背景。

## 执行边界

### 默认允许

- 创建新 Markdown 笔记。
- 补充 MOC 链接。
- 新增图表说明页。
- 输出巡检报告。
- 搜索、读取、摘要已有笔记。

### 谨慎执行

- 批量重命名文件。
- 移动目录。
- 修改大量 frontmatter。
- 合并重复笔记。
- 更新大量反向链接。

这些操作应先输出计划和影响清单，再执行。

### 默认禁止

- 删除附件。
- 清空目录。
- 修改 `.obsidian/` 配置。
- 写入 secrets。
- 未经确认批量移动或删除文件。

## 推荐落地步骤

### 第一步：设置 Vault 路径

```bash
OBSIDIAN_VAULT_PATH="/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"
```

写入 `~/.hermes/.env` 后，重启 Hermes 会话。

### 第二步：验证通用 Obsidian skill

```text
/obsidian 搜索 hermes
/obsidian 读取 09-工具/mac-工具/hermes/hermes.md
```

目标：

```text
确认 Hermes 能读到当前 Vault，而不是默认的 ~/Documents/Obsidian Vault。
```

### 第三步：创建项目专用 skill

建议名称：

```text
hxc-obsidian-vault
```

核心内容：

- 当前 Vault 路径。
- MOC 规则。
- frontmatter 规则。
- 文件命名规则。
- SVG 图表说明页规则。
- 批量修改确认规则。

### 第四步：建立巡检任务

先从只读巡检开始：

```text
每周检查 09-工具/mac-工具/hermes/ 的 MOC 链接、frontmatter、SVG 说明页，只输出问题清单，不修改文件。
```

等规则稳定后，再允许 Hermes 执行低风险修复。

### 第五步：接入 Git 兜底

批量修改前必须检查：

```bash
git status --short
```

批量修改后必须查看：

```bash
git diff --stat
git diff
```

必要时再提交。

## 与 Codex 的分工

| 场景 | 优先使用 |
| --- | --- |
| 当前对话中创建笔记、改 MOC | Codex |
| 长期自动巡检、定时任务 | Hermes |
| 手机或消息入口捕获 | Hermes Gateway |
| 大规模文件重构 | Codex 或 Claude Code |
| repo 内代码任务 | Claude Code |
| 知识库规则沉淀 | Codex skill + Hermes skill |

分工原则：

```text
Hermes 负责持续触发和调度；Codex 负责当前工作区内的精细编辑；Claude Code 负责代码仓库。
```

## 相关链接

- [[03-领域/31-人工智能学科/智能体工具/hermes/hermes]]
- [[Hermes-执行态编排图]]
- [[Hermes-典型应用场景逻辑架构图]]
- [[Hermes-Claude-Code-Codex-Skill维护课题]]
- [[hermes-模型配置]]

> [!summary]
> Hermes 与 Obsidian 的最佳协同方式，是把当前 Vault 当成 Markdown 工作区：Hermes 通过 `obsidian` skill 读写文件，通过项目专用 skill 遵守当前 Vault 规则，通过 Cron/Gateway 做自动化与捕获，通过 Git 保证批量修改可审计、可回退。
