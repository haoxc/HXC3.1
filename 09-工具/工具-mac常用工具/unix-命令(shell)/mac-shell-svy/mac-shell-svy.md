---
aliases:
  - mac/shell svy
tags:
description:
type:
ref-url:
---
## 内容
-  *打开*
	- open...
- *程序*
	- code...
- 文件
	- [[shell-删除文件夹]]
- [[终端常用快捷键]]
- **环境**
	- env...
- 端口
	- sudo lsof -i :7890
- **多 CLI 监控**
	- 场景：iTerm2 同时打开多个 CLI/Agent/构建任务时，减少来回切窗口轮询状态。
	- 落地组合：
		- iTerm2：负责窗口、Tab、分屏。
		- tmux：负责会话保持、分屏工作台、任务结束后保留现场。
		- `~/cli-monitor/logs/`：集中存放任务日志。
		- `~/cli-monitor/state/`：集中存放任务状态。
		- macOS 通知：任务完成/失败时主动提醒。
	- 已配置命令：
		- `monrun <任务名> <命令>`：运行任务、写日志、记录状态、完成/失败通知。
		- `monstatus` / `ms`：查看所有监控任务当前状态。
		- `monview` / `mvw`：持续刷新状态面板。
		- `monlog` / `mlog`：追踪所有任务日志。
		- `monmux` / `mmux`：一键进入 tmux 监控工作台。
	- 常用示例：
```bash
monrun build npm run build
monrun test npm test
monrun sync git pull

ms      # 查看当前状态
mvw     # 打开持续刷新监控面板
mlog    # 查看全部日志流
mmux    # 进入 tmux 监控工作台
```
	- 配置位置：
		- 脚本目录：`~/.local/bin/`
		- 日志目录：`~/cli-monitor/logs/`
		- 状态目录：`~/cli-monitor/state/`
		- shell 入口：`~/.zshrc`
		- tmux 配置：`~/.tmux.conf`
