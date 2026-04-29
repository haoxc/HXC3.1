---
aliases: [Claude Code常用命令, Claude Code Slash Commands, Claude Code指令速查]
tags: [ai/智能体/工具/claude, Claude-Code]
description: Claude Code 内置斜杠命令分类速查与键盘快捷键一览
type: 工具参考
create-date: 2026-04-28 20:30
---

# Claude Code 常用命令

## 概述

Claude Code CLI 内置了 70+ 个以 `/` 开头的斜杠命令，覆盖会话管理、项目配置、代码审查、工具集成、系统诊断等场景。所有命令在聊天输入框输入 `/` 即可触发自动补全。

## 斜杠命令速查

### 会话管理

| 命令                            | 说明                            |
| ----------------------------- | ----------------------------- |
| `/clear`                      | 清空会话，重新开始（别名：`/reset`、`/new`） |
| `/compact [指令]`               | 压缩会话上下文以释放 token              |
| `/context`                    | 可视化当前上下文窗口使用情况                |
| `/cost` / `/usage` / `/stats` | 查看 token 消耗与费用估算              |
| `/branch [名称]`                | 从当前会话分支出一个新会话（别名：`/fork`）     |
| `/resume [会话]`                | 恢复之前的会话（别名：`/continue`）       |
| `/rename [名称]`                | 重命名当前会话                       |
| `/rewind`                     | 回退到之前的检查点（别名：`/undo`）         |
| `/recap`                      | 生成当前会话的一句话摘要                  |
| `/export [文件名]`               | 导出当前会话为纯文本                    |
| `/copy [N]`                   | 复制最近一次回复到剪贴板                  |
| `/plan [描述]`                  | 进入计划模式                        |
| `/btw <问题>`                   | 旁路提问，不写入会话上下文                 |
| `/loop [间隔] [提示词]`            | 定时重复执行指令                      |
| `/schedule [描述]`              | 创建/管理定时远程任务                   |
| `/tasks`                      | 查看后台任务列表（别名：`/bashes`）        |
| `/exit`                       | 退出 CLI（别名：`/quit`）            |
| `/desktop`                    | 切换到桌面版 App（别名：`/app`）         |
| `/teleport`                   | 从 Web 端拉取会话到终端（别名：`/tp`）      |
| `/color [颜色]`                 | 设置提示栏颜色                       |
| `/fast [on\|off]`             | 切换快速模式                        |
| `/focus`                      | 切换专注视图（仅全屏模式）                 |
| `/add-dir <路径>`               | 添加额外的工作目录                     |

### 项目配置

| 命令 | 说明 |
|------|------|
| `/init` | 为项目生成 `CLAUDE.md` 指引文件 |
| `/config` / `/settings` | 打开设置面板（主题、模型、输出风格等） |
| `/model [模型]` | 选择或切换模型 |
| `/effort [low\|medium\|high\|xhigh\|max\|auto]` | 设置模型思考深度 |
| `/permissions` | 管理工具调用的允许/询问/拒绝规则 |
| `/fewer-permission-prompts` | 扫描历史记录，减少权限弹窗 |
| `/hooks` | 查看/管理 hook 配置 |
| `/memory` | 编辑 CLAUDE.md 记忆文件 |
| `/agents` | 管理子代理配置 |
| `/keybindings` | 自定义键盘快捷键 |
| `/theme` | 切换颜色主题 |
| `/statusline` | 配置终端状态栏 |
| `/terminal-setup` | 终端按键行为配置 |
| `/tui [default\|fullscreen]` | 设置终端 UI 渲染模式 |
| `/sandbox` | 切换沙箱模式 |

### 代码审查与质量

| 命令 | 说明 |
|------|------|
| `/review [PR]` | 审查 Pull Request |
| `/ultrareview [PR]` | 云沙箱多代理深度代码审查 |
| `/security-review` | 分析当前分支变更的安全漏洞 |
| `/diff` | 交互式 diff 查看器 |
| `/simplify [焦点]` | 审查代码的复用性、质量和效率 |
| `/autofix-pr [提示]` | 自动监控 PR 并在 CI 失败时推送修复 |
| `/batch <指令>` | 大规模并行变更（5-30 个隔离代理） |

### 工具集成

| 命令 | 说明 |
|------|------|
| `/ide` | 管理 IDE 集成状态 |
| `/mcp` | 管理 MCP 服务器连接 |
| `/plugin` | 管理插件 |
| `/reload-plugins` | 热重载所有插件 |
| `/install-github-app` | 安装 GitHub App 授权 |
| `/install-slack-app` | 安装 Slack App |
| `/remote-control` | 启用远程控制（别名：`/rc`） |
| `/web-setup` | 关联 GitHub 账号到 Web 版 |
| `/voice [hold\|tap\|off]` | 切换语音输入 |
| `/claude-api` | 加载 Claude API 参考和 Managed Agents 参考 |
| `/setup-bedrock` | 配置 Amazon Bedrock 鉴权 |
| `/setup-vertex` | 配置 Google Vertex AI 鉴权 |

### 系统与帮助

| 命令 | 说明 |
|------|------|
| `/help` | 显示帮助信息 |
| `/doctor` | 诊断系统健康状态（按 `f` 自动修复） |
| `/status` | 查看版本、模型、账号和连接状态 |
| `/login` | 登录 Anthropic 账号 |
| `/logout` | 退出登录 |
| `/upgrade` | 升级到更高付费计划 |
| `/feedback [报告]` | 提交反馈（别名：`/bug`） |
| `/release-notes` | 查看更新日志 |
| `/debug [描述]` | 启用调试日志 |
| `/insights` | 生成 Claude Code 使用分析报告 |
| `/skills` | 列出可用技能（按 `t` 按 token 数排序） |
| `/powerup` | 交互式功能教程 |

## 自定义技能（本 Vault）

| 命令 | 说明 |
|------|------|
| `/checkpoint` | 创建 git 检查点存档 |
| `/note-crafter` | 按规范创建知识笔记 |
| `/pjx-common-auditor` | 项目结构审计与规约设计 |

## 键盘快捷键

### 全局

| 快捷键 | 操作 |
|--------|------|
| `Ctrl+C` | 中断当前操作（不可修改） |
| `Ctrl+D` | 退出 Claude Code（不可修改） |
| `Ctrl+T` | 切换任务列表显示 |
| `Ctrl+O` | 切换详细记录视图 |
| `Ctrl+R` | 搜索命令历史 |
| `↑ / ↓` | 上一条 / 下一条历史 |

### 输入框

| 快捷键 | 操作 |
|--------|------|
| `Enter` | 提交消息 |
| `Escape` | 取消当前输入 |
| `Ctrl+J` | 插入换行 |
| `Ctrl+L` | 清空输入并重绘屏幕 |
| `Ctrl+S` | 暂存当前输入 |
| `Ctrl+G` / `Ctrl+X Ctrl+E` | 外部编辑器打开 |
| `Ctrl+V` | 粘贴图片 |
| `Ctrl+Z` / `Ctrl+Shift+-` | 撤销 |
| `Shift+Tab` | 切换权限模式 |
| `Meta+P` (Cmd+P / Alt+P) | 打开模型选择器 |
| `Meta+O` (Cmd+O / Alt+O) | 切换快速模式 |
| `Meta+T` (Cmd+T / Alt+T) | 切换扩展思考 |

### 确认对话框

| 快捷键 | 操作 |
|--------|------|
| `Y` / `Enter` | 确认 |
| `N` / `Escape` | 拒绝 |
| `↑ / ↓` | 上/下选项 |
| `Tab` | 下一字段 |
| `Space` | 切换选中 |

### Diff 查看器

| 快捷键 | 操作 |
|--------|------|
| `Escape` | 关闭 |
| `← / →` | 上一个 / 下一个 diff |
| `↑ / ↓` | 上一个 / 下一个文件 |
| `Enter` | 查看详情 |

## 相关链接

- [[claude-code-使用备忘录]] — 多链路多模型使用策略
- [[claude-code-上下文切换]] — 会话上下文管理
- [[claude-code-checkpoint]] — 检查点机制
- [[claude-学习路径]] — 系统学习规划
- [[claude-app-claude-code-分层工作流]] — 分层工作流设计
