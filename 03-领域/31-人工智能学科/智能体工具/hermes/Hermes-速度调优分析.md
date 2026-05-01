---
aliases: [Hermes速度调优, Hermes执行慢, Hermes性能分析, Hermes CLI慢]
tags: [mac-工具, AI工具, Agent, Hermes, 性能调优]
description: 分析 Hermes CLI/WebUI 执行慢的常见原因，并给出模型、上下文、工具链和配置侧的调优建议。
type: note
ref-url:
create-date: 2026-05-01
---

# Hermes-速度调优分析

## 一句话结论

Hermes 执行慢通常不是单点问题，而是“大模型 + 自定义 endpoint + 重上下文 + 多工具代理链”叠加造成的。日常使用应区分 fast 模型和 pro 模型。

## 当前观察

本机状态显示：

- 当前模型：`deepseek-v4-pro-openai`
- Provider：`Custom endpoint`
- Gateway Service：停止
- Hermes 版本：`v0.11.0`，落后约 25 个提交
- `hermes doctor` 中 DeepSeek API 连通性检查失败，出现 DNS/连接类提示

这些信号说明：慢的主要嫌疑不是 CLI 渲染，而是模型 endpoint、上下文加载和工具链准备。

## 主要原因

### 1. 模型本身慢

`deepseek-v4-pro-openai` 属于偏强推理模型。强模型通常首 token 慢、输出慢、推理链更长。

如果还经过 LiteLLM 或自定义代理，会增加额外网络和转发延迟。

### 2. 上下文加载重

Hermes 启动和执行时会加载：

- `config.yaml`
- `SOUL.md`
- memory
- skills
- AGENTS / rules
- 工具注册表
- 当前 workspace 上下文

当前 Vault 文件量较大，约 2600+ Markdown。上下文和 skill 越多，首轮启动和任务判断越慢。

### 3. 工具调用链长

Hermes 的定位是长期 Agent 编排层。它会先判断工具、记忆、上下文、权限、session 记录和后台任务状态。

这比普通聊天框慢，但换来的是长期任务、可观测性和可恢复性。

### 4. Endpoint 连通性不稳定

如果 custom endpoint 或 DeepSeek 路由不稳定，Hermes 可能出现：

- 连接等待；
- DNS 解析失败；
- 重试；
- fallback 检查；
- 首 token 时间过长。

这类问题会让“简单问题也慢”。

## 快速测速命令

测试纯模型延迟：

```bash
hermes -z "只回复 OK"
```

测试 CLI quiet 模式：

```bash
hermes chat -Q -q "只回复 OK"
```

查看整体状态：

```bash
hermes status
hermes doctor
```

查看版本：

```bash
hermes version
```

## 调优策略

### 1. 拆分 fast / pro 模型

日常任务使用 fast 模型：

- 简单问答；
- 短笔记；
- 命令解释；
- 小范围检查；
- 不需要深推理的整理。

复杂任务再使用 pro 模型：

- 大范围审计；
- 多文件规划；
- 高风险决策；
- 深度推理；
- 复杂代码分析。

| 场景 | 模型策略 |
| --- | --- |
| 日常 CLI | fast model |
| 长文分析 | pro model |
| 后台巡检 | fast model + 只读 |
| 最终审计 | pro model |

### 2. 减少工具和上下文负担

单次简单问题：

```bash
hermes -z "你的问题"
```

安静输出：

```bash
hermes chat -Q -q "你的问题"
```

临时跳过项目规则：

```bash
hermes -z "只回复 OK" --ignore-rules
```

更彻底的隔离：

```bash
hermes -z "只回复 OK" --ignore-user-config --ignore-rules
```

注意：隔离模式会降低 Hermes 对当前项目和个人偏好的理解。

### 3. 使用 TUI 改善体感

```bash
hermes --tui
```

TUI 不一定让模型更快，但能让状态、工具调用、等待过程更清楚，减少“卡住了”的错觉。

### 4. 修 endpoint

如果 `hermes doctor` 显示 DeepSeek/custom endpoint 连通性失败，应优先检查：

- LiteLLM 是否启动；
- endpoint URL 是否正确；
- DNS 或代理是否可用；
- 模型别名是否仍有效；
- 是否有 fallback 重试造成等待。

## 判断标准

| 现象 | 更可能原因 | 处理 |
| --- | --- | --- |
| 启动慢 | config / skills / memory / workspace 加载 | 用 `-z`、`-Q`、`--ignore-rules` 对比 |
| 首 token 慢 | 模型或 endpoint | 换 fast 模型测试 |
| 工具执行慢 | 工具链或文件扫描 | 缩小任务范围 |
| 简单问题也慢 | endpoint / DNS / proxy | 跑 `hermes doctor` |
| 输出很多过程信息 | CLI 模式噪音 | 用 `-Q` 或 `--tui` |

## 推荐配置思路

默认日常配置：

```yaml
model:
  provider: custom
  name: fast-model-alias
agent:
  max_turns: 30
display:
  skin: slate
```

复杂任务临时指定强模型：

```bash
hermes -m deepseek-v4-pro-openai -z "做一次深入审计"
```

## 压缩记忆

> Hermes 慢，多半不是“CLI 显示慢”，而是模型、endpoint、上下文和工具链叠加。日常用 fast，复杂任务用 pro；简单任务用 `-z` 或 `-Q`；连通性异常先跑 `hermes doctor`。
