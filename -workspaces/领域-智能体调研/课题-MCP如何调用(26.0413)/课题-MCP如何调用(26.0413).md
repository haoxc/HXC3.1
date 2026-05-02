---
aliases: []
tags: []
description:
type:
ref-url:
create-date: 2026-04-13 17:13
---
调用 **MCP (Model Context Protocol)** 服务器并非像传统 API 那样通过编写复杂的 HTTP 请求完成，而是通过 **工具调用 (Tool Calling)** 的机制实现。

在 **Codex App** 或类似的 AI Agent 环境中，调用过程通常分为以下三个层面：

---

### 1. 交互层：通过提示词 (Prompt) 显式指令

当你完成配置并重启应用后，Agent 的“大脑”已经感知到了这些新技能。你只需在对话中直接下达任务。

- **自然语言触发：** 你不需要记住复杂的函数名，直接描述目标。
    
    - _示例：_ “使用 `filesystem` 工具读取当前目录下的 `README.md`。”
        
    - _示例：_ “调用 `puppeteer` 访问 `localhost:3000` 并截图。”
        
- **专家技巧：** 如果 Agent 犹豫不决，可以显式指定工具。
    
    > “请调用 **工具 (Tools)** 中的 `write_file` 方法，将这段代码保存到 `app.py`。”
    

### 2. 逻辑层：工具调用机制 (Tool Calling Mechanism)

当你发出指令后，系统内部会经历以下**编排 (Orchestration)** 过程：

1. **意图识别 (Intent Recognition)：** 模型判断你的需求需要外部工具支持。
    
2. **模式匹配 (Schema Matching)：** 模型查找已挂载 MCP 服务器的 **工具模式 (Tool Schema)**，确认参数（如 `path`, `content`）。
    
3. **协议传输 (Transport)：** 客户端（Host）通过 **标准输入输出 (STDIO)** 或 **JSON-RPC** 向 MCP 服务器发送请求。
    
4. **执行与回传：** 服务器完成操作（如写入硬盘）并将结果返回给 Agent。
    

### 3. 代码层：在自定义 Agent 中编程调用

如果你是在开发自己的 Python 或 Node.js 脚本来调用 MCP 服务器，你需要使用官方提供的 **SDK**。

- **Python 示例：**
    
    ``` python
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    
    # 定义服务器参数
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化并调用工具
            await session.initialize()
            result = await session.call_tool("read_file", arguments={"path": "test.txt"})
            print(result)
    ```
    

---

### > 常见调用失败的排查建议

如果你发现指令发出后 Agent 无法完成操作，通常可以从以下**中英文术语对照**的角度进行排查：

- **权限拒绝 (Permission Denied)：** 检查 **Filesystem MCP** 授权的**绝对路径 (Absolute Path)** 是否包含目标文件。
    
- **环境未就绪 (Environment Not Ready)：** 检查本地是否安装了工具所需的运行环境（如 Node.js 或 Python 虚拟环境）。
    
- **工具冲突 (Tool Conflict)：** 如果你安装了多个功能类似的 MCP，请在提示词中明确指明具体名称（例如：`puppeteer` 还是 `playwright`）。
    

### 总结

对于 **Codex App** 用户，最简单有效的调用方式是**“把 Agent 当成指挥官”**。你只需关注“做什么”，而将“如何连接底层”的逻辑交给 MCP 协议处理。

你现在是在 Codex App 的对话框中尝试调用失败了，还是在尝试编写代码来对接 MCP？