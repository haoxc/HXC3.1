---
aliases:
  - ai/智能体/开发框架/执行网关/openclaw(agent-openclaw)
tags:
  - ai/智能体/开发框架
  - 自动化框架/浏览器
description:
type:
ref-url:
Positioning:
create-date: 2026-02-08
---
## 1. 什么是 OpenClaw？

**OpenClaw** 是一个开源的自动化框架，旨在将大语言模型（LLM）与浏览器环境（如 Chrome）深度连接。它通常作为 **MCP (Model Context Protocol) Server** 运行，允许像 Claude Desktop 或 Dify 这样的客户端通过标准化协议直接控制网页。

- **核心定位**：网页操作的“协议翻译官”。
- **技术特色**：比原生的 DevTools Server 更强调**任务闭环**，支持复杂的 DOM 解析和视觉辅助定位。

---

## 2. 部署配置步骤 (实践指南)

### A. 环境准备

1. **安装 Node.js**（建议 v20 或更高版本）。
2. **启动 Chrome 调试模式**：

    ```PowerShell
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
    ```

### B. 获取并运行 OpenClaw
在终端中，你可以直接通过 `npx` 运行或从 GitHub 克隆：
```Bash
# 通过 npx 运行（推荐）
npx openclaw
```

_注：启动后，它会监听本地端口并等待 MCP 客户端的连接。_
### C. Dify 接入配置
1. 在 Dify 中选择 `工具 > 添加工具 > MCP`。
2. **连接模式**：由于 Dify 通常运行在 Docker 中，建议使用 **SSE (Server-Sent Events)** 模式。
3. **URL 配置**：
    - **Endpoint**: `http://host.docker.internal:端口`（端口通常由 OpenClaw 启动时指定，默认为 3000 或由配置决定）。
---

## 3. OpenClaw vs. 原生 DevTools MCP

| **维度**   | **原生 DevTools Server** | **OpenClaw**           |
| -------- | ---------------------- | ---------------------- |
| **易用性**  | 偏向底层指令（点击、移动）          | **偏向任务描述（搜索、提取）**      |
| **稳定性**  | 极高，但需要模型处理大量 DOM       | **更高，内置了 DOM 压缩和清理逻辑** |
| **多模态**  | 基础截图支持                 | **增强的视觉识别与反馈**         |
| **适用场景** | 开发者调试、底层控制             | **业务流自动化、复杂数据采集**      |

---
## 4. 落地建议

- **状态感知**：OpenClaw 提供了更好的“等待”机制。在 Dify 工作流中，你可以直接调用它的“Wait for Element”指令，有效降低任务失败率。

---

> [!ABSTRACT] 一句话总结
>
> **OpenClaw 是一个针对 Agent 优化的 MCP 增强版浏览器服务器，它通过精简 DOM 噪声和强化任务指令，让 Dify 等平台能够以更低的 Token 成本实现更稳健的网页操纵。**
