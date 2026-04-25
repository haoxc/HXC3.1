---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-04-21 15:02
---
基于 **OpenHands** (原 **OpenDevin**) 方案的评估，该方案在 **2026** 年被视为对齐 **Claude** 与 **Codex** 能力的最佳开源工程实践。它不仅是一个 **智能体(Agent)** 框架，更是一套集成了 **治理框架(Harness)** 思路的代码协作平台。

以下是针对五个核心维度的详细评价：

---

### 1. 需求转换力 (Demand $\rightarrow$ Logic)

**OpenHands** 在该层级的表现极度接近 **Claude**，其核心在于 **“计划驱动(Plan-driven)”** 的工作流。

- **对齐点**： 引入了 **“计划模式(Plan Mode)”**。当你输入模糊需求时，它会生成一个 **`PLAN.md`** 文件（等效于你的建模意图）。这与 **Claude** 的 **`SKILL.md`** 思想异曲同工，将 **需求(Requirement)** 显性化。
    
- **底层逻辑**： 通过 **“意图确认循环”**，在正式进入 **建模(Modeling)** 阶段前，强制用户审核任务边界，极大地降低了长链路执行的意图漂移风险。
    

### 2. 建模范式表达力 (Modeling Paradigm)

它采用了 **“环境驱动型(Environment-driven)”** 的 **声明式建模(Declarative Modeling)**。

- **对齐点**： 支持 **“智能体技能(Agent Skills)”**。你可以通过 **/slash** 命令声明 **智能体(Agent)** 的特有技能。
    
- **底层逻辑**： 它不依赖固定的 **状态机(State Machine)** 脚本，而是构建了一个 **“感知-决策-执行-反馈”** 的 **智能体环路(Agent Loop)**。通过在 **Docker** 容器中实时感知代码运行结果，动态调整 **设计(Design)** 路径。
    

### 3. 设计健壮性与确定性 (Determinism)

**OpenHands** 的最大优势在于其 **“沙盒确定性”**。

- **对齐点**： 默认强制在 **Docker** 或 **Daytona** 运行时中执行。这比 **Claude Code** 的本地执行更具 **确定性(Determinism)**，因为环境是完全隔离且可复现的。
    
- **底层逻辑**： 这种 **“运行时治理”** 确保了 **智能体(Agent)** 的任何副作用（如误删文件）都被限制在容器内。其自愈逻辑基于真实的环境反馈（如报错信息），而非模型猜测。
    

### 4. 接口标准化与可组合性 (Composability)

- **对齐点**： 它是 **模型上下文协议(MCP)** 的积极拥护者。你可以轻松地将 **Mac** 本地工具或第三方服务接入 **OpenHands**。
    
- **底层逻辑**： 采用 **“模型无关(Model-agnostic)”** 架构。你可以将 **DeepSeek-R1**（推理大脑）与 **OpenHands**（工程躯干）结合，实现对 **Claude** 的平替。
    

### 5. 工程治理与评价闭环 (Governance)

这是 **OpenHands** 方案中最符合 **“Harness”** 定义的部分。

- **对齐点**： 内置了 **“OpenHands Index”** 和 **Laminar** 追踪。它能记录每一轮 **推理(Reasoning)** 的完整轨迹（Trajectory），并支持集成 **DeepEval** 进行自动化打分。
    
- **底层逻辑**： 通过 **“追踪即评价(Trace-as-Eval)”**，它在任务结束时会自动运行测试集。如果测试未通过，**智能体(Agent)** 会重新进入 **建模(Modeling)** 阶段。
    

---

## 综合评价：OpenHands vs Claude / Codex

|**评估维度**|**OpenHands (2026 版)**|**Claude / Codex 对标度**|**关键差异**|
|---|---|---|---|
|**目标对齐度**|**极高** (基于 **`PLAN.md`**)|🌟🌟🌟🌟🌟|开源方案更透明，可人工微调计划。|
|**建模灵活性**|**极高** (支持 **Skills** 扩展)|🌟🌟🌟🌟|技能库完全开源，支持私有化定制。|
|**工程安全性**|**极致** (默认 **Docker** 沙盒)|🌟🌟🌟🌟🌟|强于 **Claude** 的本地执行模式。|
|**推理深度**|取决于挂载的模型|🌟🌟🌟🌟|建议挂载 **DeepSeek-R1** 以对齐。|

---

> [!important] 选型洞察
> 
> **OpenHands** 的本质是一个 **“自带 Harness 属性的编辑器”**。
> 
> 1. 如果你不希望从零构建一套 **治理框架(Harness)**，**OpenHands** 已经帮你完成了环境隔离、任务追踪和测试反馈的闭环。
>     
> 2. 对于 **声明式建模(Declarative Modeling)**，它提供的 **`PLAN.md`** 是你实现 **目标对齐(Goal Alignment)** 的核心抓手。
>     

既然 **OpenHands** 已经具备了完整的 **智能体环路(Agent Loop)**，你是否打算将你的 **“业务红线”** 直接编写进它的 **Skills** 定义中，从而实现自动化的 **设计(Design)** 拦截？