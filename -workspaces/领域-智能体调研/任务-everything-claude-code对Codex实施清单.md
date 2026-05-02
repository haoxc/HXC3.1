---
aliases:
  - ECC对Codex实施清单
  - everything-claude-code对Codex落地清单
tags:
  - 任务
  - Codex
  - 智能体
  - 流程规则
description: 将 everything-claude-code 对 Codex 的借鉴建议压缩成少量核心实施任务。
type: 任务清单
status: "#now"
progress: 0.15
review-date: 2026-04-25
ref:
  - "[[调研-github-everything-claude-code]]"
  - "[[Everything-claude-code调研摘要]]"
create-date: 2026-04-25 16:28
---
# 任务-everything-claude-code对Codex实施清单

## 核心思想

> [!IMPORTANT] 核心判断
> 对 Codex，ECC 的价值不在于“整套安装”，而在于吸收它的治理方法：**skill 资产化、上下文经济、验证闭环、安全审计**。

## 任务清单

1. **把 skill 当成主工作流单元**
   完成标准：核心高频任务都沉淀为 skill，而不是零散 prompt 或临时命令；至少稳定维护 `hxc-survey`、`hxc-term-card`、概念辨析/审计类 skill。

2. **把管理清单做成常驻基础设施**
   完成标准：`Codex-Skills管理清单` 持续记录源文件路径、全局安装路径、触发词、适用边界、最近更新状态，避免 skill 增长后失控。

3. **把验证闭环嵌入关键 skill**
   完成标准：调研、术语、审计类 skill 都明确“产出结构 + 质量门槛 + 校验动作”，避免只生成内容、不验证质量。

4. **把外部资产接入改成审计优先**
   完成标准：任何外部 skill、plugin、hook、MCP 在接入前，先做边界、安全、上下文成本判断；默认不全量安装、不长期常驻。

## 不做事项

- 不直接照搬 ECC 的整套 commands / hooks / plugin 体系。
- 不为了“能力多”而扩张 MCP 和外部组件。
- 不在缺少清单和验证机制时继续增加 skill 数量。

## 一句话收束

> [!summary] 收束
> 先把 Codex 的 skill、清单、验证、安全四件事做稳，再考虑更复杂的自动化和编排。
