---
aliases:
  - abbr://智能体/实践/构建本地智能体(dify, agent-action(builidng Win-LLMs)
title: 构建本地智能体(Win-LLMs)
domain:
created: 2026-01-03 12:24
tags:
  - 智能体/实践/构建本地智能体_dify
ref-url: https://zhuanlan.zhihu.com/p/25771359587
type: note
description: > **Agent = LLM (大脑) + Planning (规划) + Memory (记忆) + Tool Use (工具使用)**
create-date: 2026-01-09
---
## 内容
## 架构决策

### 构建思想
> **Agent = LLM (大脑) + Planning (规划) + Memory (记忆) + Tool Use (工具使用)**
### 构建策略
- **先 Workflow，后 Agent**：如果能通过固定的 Prompt 链解决，就不要引入复杂的自主决策，因为确定性是商业应用的首要追求。
- **人机协同 (Human-in-the-loop)**：在关键节点设置人工审核，这是目前最稳妥的架构。
- **解耦思考与执行**：让昂贵的模型（如 GPT-4o）负责规划，便宜的模型（如 GPT-4o-mini）负责简单执行。
---
## Agent构建
### 1. 为什么这是 Windows 上的最佳架构？
- **可视化 (Dify)**：提供类似工作流画布的界面，拖拽即可完成 RAG（知识库）和 Agent 逻辑。
- **高性能 (WSL2)**：在 Windows 上获得原生的 Linux 环境，解决 Docker 运行的兼容性与速度问题。
- **模型自由 (Ollama)**：一键运行本地模型（如 DeepSeek-V3, Llama 3.1），数据不出本地，零成本。

### 2. 准备工作：环境搭建 (环境搭建)

### 第一步：开启 WSL2 与安装 Docker
1. **开启 WSL2**：打开 PowerShell (管理员)，运行 `wsl --install`。重启电脑。
2. **安装 Docker Desktop**：
    - 下载并安装 [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)。
    - 在设置中确保勾选 **"Use the WSL 2 based engine"**。
        - ![[87f81ca639b67081737bcef1b4c4ab9b_MD5.jpg]]
3. **安装 Ollama**：
    - 去 [Ollama 官网](https://ollama.com/) 下载 Windows 版并运行。
    - 在终端运行测试：`ollama run deepseek-v3`。
### 3. 部署可视化平台 (Dify)

Dify 是目前本地可视化最强的平台，建议通过 Docker 一键部署：
```PowerShell
# 1. 克隆代码仓库
git clone https://github.com/langgenius/dify.git
cd dify/docker

# 2. 准备配置文件
copy .env.example .env

# 3. 启动 Dify
docker compose up -d
```
- **访问地址**：浏览器打开 `http://localhost`，首次进入需设置管理员账号。

### 4. 架构联动：将本地模型接入 Dify
1. **获取本机局域网 IP**：在 PowerShell 输入 `ipconfig`，找到 `IPv4 地址`（通常是 `192.168.x.x`）。
2. **配置 Ollama 允许远程访问**：
    - 在 Windows 环境变量中添加：变量名 `OLLAMA_HOST`，变量值 `0.0.0.0`。
    - 重启 Ollama 软件。
3. **在 Dify 中添加模型**：
    - 进入 Dify 设置 -> 模型供应商 -> 选择 **Ollama**。
    - **模型名称**：`deepseek-v3`（需与你本地 pull 的名称一致）。
    - **基础 URL**：`http://你的局域网IP:11434` (不要写 localhost，Docker 容器访问不到宿主机的 localhost)。
4. 安装 Neo4j
```
docker run -itd --name neo4j -p 7474:7474 -p 7687:7687 -v $HOME/neo4j/data:data neo4j
```
- 命令运行完成后，打开浏览器，访问`http://localhost:7474`，如果看到Neo4j的登录页面，说明安装成功。

## 配置模型
在 Dify 的“模型供应商”里选择 `Ollama`，按你文档配置：
- LLM 模型
- Embedding 模型
- Rerank 模型
- 基础 URL：http://<服务器IP>:11434

## 配置MCP

[[配置本地MCP]]
