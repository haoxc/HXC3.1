---
aliases: []
tags: []
description:
type:
ref-url:
create-date: 2026-04-21 22:19
---
针对你的 **Mac M1 Max (64GB)** 配置，部署 **OpenHands** 的最佳路径并非简单的“一键安装”，而是要构建一个能支撑 **“云端大脑 + 本地沙盒”** 架构的 **工程化环境(Engineering Environment)**。

为了实现 **“Codex 执行 + OpenHands 审计”** 的哨兵模式，请遵循以下路径进行部署：

---

## 1. 基础设施准备：容器化与环境隔离

在 Mac 上，**容器(Container)** 是 **治理框架(Harness)** 的物理边界。

- **安装 OrbStack (强烈推荐)**：
    
    相比传统的 **Docker Desktop**，**OrbStack** 在 Apple Silicon 上的启动速度更快，内存占用极低，且对 **文件系统(File System)** 的挂载性能有显著优化。这能有效减少 **OpenHands** 审计时的 I/O 延迟。
    
- **安装 Node.js 与 Python**：
    
    建议使用 `fnm` 管理 Node.js (推荐 v20+)，使用 `uv` 管理 Python。`uv` 是目前最快的 Python 包管理工具，非常符合追求极致效率的 **智能体(Agent)** 工作流。
    

---

## 2. 核心部署：OpenHands 的源码级安装

由于你需要高度定制 **审计技能(Audit Skills)**，建议通过源码编译安装，而非直接运行二进制文件。


```bash
# 1. 克隆仓库
git clone https://github.com/All-Hands-AI/OpenHands.git
cd OpenHands

# 2. 创建并配置环境变量
cp .env.example .env
```

### 关键配置 (.env) 调优

由于你接受云端费用，直接在 `.env` 中配置最强模型：

- **LLM_MODEL**: `claude-3-7-sonnet-20250219` (推荐作为审计脑)
    
- **LLM_API_KEY**: 填入你的 API Key。
    
- **WORKSPACE_BASE**: 指向你与 **Codex** 共享的开发目录。这是消除 **上下文损耗(Context Loss)** 的物理桥梁。
    

---

## 3. 哨兵架构配置：实现“审计者”定位

要让 **OpenHands** 履行 **全量审计(Full Audit)** 的职责，需要完成以下 **挂载(Mounting)**：

1. **权限声明**： 在启动命令中开启 **沙盒模式(Sandbox Mode)**，确保审计过程不污染宿主机。
    
2. **建立共享工作空间**：
    
    确保 **OpenHands** 挂载的目录与 **VS Code (Codex)** 打开的目录一致。
    
    Bash
    
    ```
    # 启动 OpenHands
    make run WORKSPACE_PATH=/Users/yourname/projects/my-project
    ```
    
3. **配置审计钩子**：
    
    在项目中创建 `.openhands/` 文件夹，编写你的 **审计规约(Audit Spec)**。
    

---

## 4. 针对 64GB 内存的性能榨取举措

你的硬件资源足以支撑更复杂的 **治理(Governance)** 逻辑：

- **增加 Docker 内存限额**： 在 OrbStack 设置中分配 **16GB-24GB** 内存给容器。全量审计涉及大量依赖编译和静态分析，充足的内存能避免 **智能体(Agent)** 任务崩溃。
    
- **启用目录索引**： 让 **OpenHands** 对本地文档进行 **RAG (检索增强生成)** 索引。利用 M1 Max 的高性能固态硬盘，它能瞬间理解你的私有 **项目规范(Project Specs)**。
    

---

## 5. 最终验证流程

1. **访问 Web UI**： 浏览器打开 `localhost:3000`。
    
2. **下达第一个审计任务**： “检查当前工作区，基于 `.agents/specs/` 评估代码的 **目标对齐度(Goal Alignment)**。”
    
3. **观察反馈**： 确认 **OpenHands** 是否能正确读取文件并在 **终端(Terminal)** 模拟器中运行测试。
    

---

### 部署后的一句话准则

> [!important] 核心路径总结
> 
> **用 OrbStack 承载沙盒，用云端模型驱动推理，用共享目录同步上下文。**

你现在是否已经完成了 **OrbStack** 的安装？如果是，我们可以直接进入 **.env** 文件的 **审计模型(Audit Model)** 参数微调环节。