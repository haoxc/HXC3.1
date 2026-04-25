### 配置本地MCP   #智能体/实践/MCP/配置LocalMCP
- [超实用！Dify快速接入本地MCP服务-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2530658)
> - 在Docker中安装 Nodejs   [[安装nodejs(docker)]]
## 1. 架构逻辑：协议驱动 (Protocol Driven)
在这种架构下，Dify 不再是发送“网页指令”，而是直接调用 Chrome 的 **开发者工具协议 (CDP)**。
> **Dify (MCP Client)** ←[`MCP 协议`]→ **Chrome MCP Server (中转)** ←[`CDP 协议`]→ **你的 Chrome 浏览器**

---
# Windows 环境：Dify + MCP + Chrome 落地手册

## 操作步骤 (实践指南)

### 第一步：Chrome 宿主机环境配置
1. **彻底关闭**当前所有运行中的 Chrome 浏览器（检查后台任务管理器）。
2. **创建快捷方式/命令行启动**：
    - 按 `Win + R`，输入 `cmd`。
    - 输入并运行以下命令（路径根据你的实际安装位置调整）：

        ```powershell
        "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_mcp"
        ```
        
    - **验证**：在浏览器访问 `http://localhost:9222`，看到包含 JSON 信息的页面即代表成功。

### 第二步：部署 MCP Server

1. **安装 Node.js**（推荐 v18+）。
2. 全局启动工具：

    在 Windows 终端运行：

    Bash

    ```
    npx -y @modelcontextprotocol/server-chrome-devtools
    ```

    _该命令会自动拉取最新版 MCP Server 并建立 stdio 通信。_

### 第三步：Dify 平台侧集成

1. **定位工具菜单**：进入 Dify 仪表盘 -> `工具 (Tools)` -> `添加工具` -> `MCP`。
2. **参数填写**：
    
    - **名称**：`ChromeAutomation`
    - **模式**：选择 `SSE`（如果你在 Docker 内部），或者 `stdio`（如果你直接在 Windows 跑 Dify 源码）。
    - **Endpoint**：若使用 Docker 部署，地址填写 `http://host.docker.internal:端口`。
        
3. **发布与测试**：
    
    - 在 Dify 应用的 `设置 -> 工具` 中添加刚才创建的 `ChromeAutomation`。
    - 尝试发送指令：“打开百度并搜索‘2026 AI 趋势’”。

## 3. 关键故障排查

|**现象**|**原因**|**解决方法**|
|---|---|---|
|**Connection Refused**|9222 端口未开放|检查 Chrome 启动参数，确保没有残留进程占用端口。|
|**Dify 找不到 Host**|Docker 网络隔离|确保使用的是 `host.docker.internal` 而非 `localhost`。|
|**权限报错**|MCP Server 未授权|在 Dify 权限弹窗中勾选所有工具项。|

---

> [!ABSTRACT] 一句话总结
>
> 通过开启 Chrome 远程调试端口并利用 MCP Server 作为协议转换网关，可以将 Windows 宿主机的浏览器能力直接透传给 Dify 容器，构建起高性能的自动化工作流。

---

下一步动作：

是否需要我为你提供一个 Dify 自动化工作流 (Workflow) 模板，直接包含“搜索-提取-总结”的完整逻辑节点？