---
title: hermes应用-obsidian协同-落地操作笔记
aliases:
  - Hermes Obsidian 协同落地操作
  - Hermes 窗口落地 Obsidian 协同
  - ob协同落地操作笔记
tags:
  - mac-工具
  - AI工具
  - Hermes
  - Obsidian
  - 操作指南
description: 记录在 Hermes 窗口中落地 Obsidian 协同的具体操作步骤，包括启动模型、Vault 路径配置、obsidian skill 验证、项目专用 skill 创建、只读巡检和 cron 任务。
type: 操作指南
create-date: 2026-04-29
ref-url:
---

# hermes应用-obsidian协同-落地操作笔记

## 一句话结论

在 Hermes 窗口中落地 Obsidian 协同，不要从“自动改 Vault”开始，而应先完成一个最小闭环：Hermes 能读当前 Vault、能搜索当前 Vault、能按项目规则只读巡检、能定时输出报告。低风险修复可以后续开放，高风险修改仍交给 Codex 或人工确认。

## 前提判断

当前 Vault 路径：

```text
/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)
```

当前关键约束：

- Hermes 内置 `obsidian` skill 已可用。
- `obsidian` skill 只负责文件访问，不负责当前 Vault 的 MOC/frontmatter 规则。
- 当前已新增 `deepseek-v4-pro-openai`，Hermes 工具调用优先用该别名；原 `deepseek-v4-pro` 仍保留给 Claude Code 的 Anthropic-compatible 链路。
- 所有批量修改前必须先输出计划和影响清单。

## 第一步：用工具兼容模型启动 Hermes

推荐启动方式：

```bash
hermes --tui -m deepseek-v4-pro-openai --provider custom --skills obsidian
```

如果已经在 Hermes 窗口中，先输入：

```text
/model
```

然后切到：

```text
deepseek-v4-pro-openai
```

判断标准：

```text
能加载 skill、能调用工具、不会因为 tool schema 报错。
```

## 第二步：配置当前 Vault 路径

如果 Hermes 还没有指向当前 Vault，在终端执行：

```bash
echo 'OBSIDIAN_VAULT_PATH="/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"' >> ~/.hermes/.env
```

然后重启 Hermes。

> [!warning]
> Vault 路径包含括号，命令和 env 中必须使用引号。

## 第三步：验证 Hermes 能读取当前 Vault

在 Hermes 窗口输入：

```text
/obsidian 读取 09-工具/mac-工具/hermes/hermes应用-obsidian协同.md
```

预期结果：

```text
Hermes 能输出该笔记内容或摘要。
```

如果读不到：

- 检查 `~/.hermes/.env` 是否有 `OBSIDIAN_VAULT_PATH`。
- 检查路径是否完整包含 `(Apple)`。
- 退出并重新启动 Hermes。
- 确认没有读到默认路径 `~/Documents/Obsidian Vault`。

## 第四步：验证搜索能力

在 Hermes 窗口输入：

```text
/obsidian 搜索 Hermes Obsidian 协同
```

或：

```text
/obsidian 搜索 DeepSeek V4 Pro
```

预期结果：

```text
搜索结果来自当前 Vault，而不是其他 Obsidian 目录。
```

## 第五步：创建项目专用 Vault skill

在 Hermes 窗口输入：

```text
请创建一个 Hermes skill，名称为 hxc-obsidian-vault。

用途：维护当前 Obsidian Vault 的笔记规范。

规则：
- 当前 Vault 路径是 /Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)
- 创建笔记前必须先判断 MOC 归属
- 新笔记必须有 frontmatter：tags、description、type、create-date
- 不创建孤立笔记
- SVG 图表必须有同名 Markdown 说明页
- MOC 页面只做导航，不写长篇正文
- 批量移动、重命名、删除前必须先输出计划和影响清单
- 默认禁止修改 .obsidian/、删除附件、写入 secrets

创建后告诉我 skill 路径，并给一个验证用例。
```

预期产物：

```text
~/.hermes/skills/.../hxc-obsidian-vault/SKILL.md
```

判断标准：

- skill 名称清晰。
- frontmatter 有 `name` 和 `description`。
- 正文包含当前 Vault 的 MOC、frontmatter、图表说明页、安全边界规则。
- 给出一个只读验证用例。

## 第六步：手动执行一次只读巡检

在 Hermes 窗口输入：

```text
使用 obsidian 和 hxc-obsidian-vault，检查 09-工具/mac-工具/hermes/ 目录：
- 是否有未挂到 hermes.md 的笔记
- 是否有 frontmatter 不完整的笔记
- 是否有 SVG 文件没有同名说明页
- 是否有疑似重复主题

只输出巡检报告，不修改文件。
```

预期输出：

```text
问题清单 + 文件路径 + 建议动作。
```

不应出现：

```text
直接移动文件
直接删除文件
直接批量改 frontmatter
直接改 .obsidian/
```

## 第七步：创建每日 cron 巡检

在 Hermes 窗口输入：

```text
/cron add "every 1d" "使用 obsidian 和 hxc-obsidian-vault，检查 09-工具/mac-工具/hermes/ 下的 Markdown 和 SVG 文件：列出未挂 MOC、frontmatter 不完整、SVG 没有同名说明页、疑似重复主题的问题。只输出报告，不修改文件。" --skill obsidian --skill hxc-obsidian-vault
```

查看任务：

```text
/cron list
```

手动触发：

```text
/cron run <job_id>
```

如果需要在终端中管理：

```bash
hermes cron list
hermes cron run <job_id>
hermes cron tick
```

## 第八步：逐步开放低风险修复

第一阶段只读。

第二阶段可允许低风险自动修复：

- 补 MOC 链接。
- 创建 SVG 同名说明页。
- 给新笔记补基础 frontmatter。

仍需人工确认：

- 批量移动。
- 批量重命名。
- 合并重复笔记。
- 删除文件。
- 改 `.obsidian/` 配置。

## 第九步：与 Codex 分工

Hermes 发现问题后，不一定亲自修。

推荐分工：

| 问题 | 推荐执行者 |
| --- | --- |
| 只读巡检、定时报告 | Hermes |
| 补 MOC、创建说明页 | Hermes 或 Codex |
| 精细修改 Vault 文件 | Codex |
| 大规模目录调整 | Codex，且先出计划 |
| 代码仓库相关任务 | Claude Code |

落地原则：

```text
Hermes 负责让任务按时发生。
Codex 负责把文件改准确。
Claude Code 负责代码仓库。
```

## 常见问题

### `/obsidian` 读不到当前 Vault

检查：

```bash
grep OBSIDIAN_VAULT_PATH ~/.hermes/.env
```

如果没有，补：

```bash
echo 'OBSIDIAN_VAULT_PATH="/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"' >> ~/.hermes/.env
```

然后重启 Hermes。

### 工具调用报错

如果使用 `deepseek-v4-pro` 报工具 schema 相关错误，切到：

```text
deepseek-v4-pro-openai
```

原因：

```text
deepseek-v4-pro 是 Anthropic-compatible 别名，保留给 Claude Code。
deepseek-v4-pro-openai 是 OpenAI-compatible 别名，给 Hermes 工具调用使用。
```

### Cron 执行结果不符合预期

检查：

```text
/cron list
/cron status
```

并确认 cron prompt 是自包含的。不要写：

```text
检查那个目录。
```

要写：

```text
检查 09-工具/mac-工具/hermes/ 下的 Markdown 和 SVG 文件，列出未挂 MOC、frontmatter 不完整、SVG 没有同名说明页、疑似重复主题的问题。只输出报告，不修改文件。
```

## 最小落地检查清单

- [ ] Hermes 用 `deepseek-v4-pro-openai` 或其他工具兼容模型启动。
- [ ] `OBSIDIAN_VAULT_PATH` 指向当前 Vault。
- [ ] `/obsidian 读取 ...` 能读到当前 Vault 笔记。
- [ ] `/obsidian 搜索 ...` 能搜到当前 Vault 内容。
- [ ] `hxc-obsidian-vault` skill 已创建。
- [ ] 手动只读巡检能输出报告。
- [ ] cron 巡检任务已创建。
- [ ] 高风险修改仍需人工确认。

## 相关链接

- [[hermes应用-obsidian协同]]
- [[hermes应用-obsidian协同-hermes什么时候必要]]
- [[Hermes-执行态编排图]]
- [[Hermes-Claude-Code-Codex-Skill维护课题]]
- [[03-领域/31-人工智能学科/智能体工具/hermes/hermes]]

> [!summary]
> Hermes 窗口里的 Obsidian 协同落地顺序是：先用 `deepseek-v4-pro-openai` 启动，再验证当前 Vault 读写，再创建项目专用 `hxc-obsidian-vault` skill，随后手动跑只读巡检，最后再创建 cron 定时任务。先让 Hermes 稳定发现问题，再逐步开放低风险自动修复。
