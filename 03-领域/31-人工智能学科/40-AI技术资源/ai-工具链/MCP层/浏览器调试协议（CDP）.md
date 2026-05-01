---
aliases:
  - CDP协议
type: note
tags: [工具]
description: `DevTools MCP` 本质是 **Chrome DevTools Protocol（CDP，Chrome 开发者工具协议）** 的模块化通信层表述，是 
create-date: 2026-01-09
---
### 一、CDP 核心定义（DevTools MCP 的正式全称）
`DevTools MCP` 本质是 **Chrome DevTools Protocol（CDP，Chrome 开发者工具协议）** 的模块化通信层表述，是 Chromium 内核（Chrome/Edge/Opera/新版 Brave 等）原生的调试/控制协议，基于 **JSON-RPC 2.0** 实现双向通信，是浏览器内核与外部工具（如 Chrome 开发者工具、Puppeteer、Playwright）交互的底层规范。

简单来说：CDP 是操作 Chromium 浏览器的“原生语言”，所有上层工具（如 Puppeteer）对 Chromium 的操控，最终都转化为 CDP 命令的调用。

---

### 二、CDP 核心架构与通信方式
#### 1. 协议基础
- **传输层**：主要基于 `WebSocket`（实时双向通信），也支持 HTTP/JSON（单次请求）；
- **通信模型**：客户端（如调试工具/脚本）通过浏览器暴露的调试端口（默认 `--remote-debugging-port=9222`）连接，发送 JSON-RPC 格式的命令，浏览器返回响应/事件；
- **模块化设计**：功能按 `Domain`（域）划分，每个 Domain 包含 `Command`（可调用的指令）、`Event`（浏览器主动推送的事件）、`Type`（数据结构）。

#### 2. 核心功能 Domain（模块）
CDP 覆盖 Chromium 所有底层能力，核心 Domain 及用途如下：

| Domain 名称 | 核心能力                                                                 |
|-------------|--------------------------------------------------------------------------|
| `Page`      | 页面导航、截图/录屏、弹窗处理、页面生命周期控制（如刷新、停止加载）|
| `Network`   | 网络请求拦截/修改/模拟、抓包（请求/响应详情）、设置请求头/代理、模拟网络限速 |
| `Runtime`   | 注入/执行 JS 代码、获取执行结果、设置断点、监听控制台输出                 |
| `DOM`       | 查询/修改 DOM 元素、监听 DOM 变化、获取元素布局/样式                     |
| `Performance` | 采集 FPS、内存占用、加载时间等性能指标，录制性能分析报告               |
| `Target`    | 管理标签页、iframe、浏览器进程（如新建/关闭标签、切换上下文）|
| `Security`  | 处理证书、模拟 HTTPS 错误、启用/禁用安全策略                             |
| `Emulation` | 模拟移动设备（分辨率/像素比）、地理定位、时区、网络条件                   |

---

### 三、如何直接使用 CDP（实操示例）
CDP 无需依赖框架，可直接通过 WebSocket 调用，以下是两种典型使用方式：

#### 方式 1：手动启动 Chrome + 调试端口（基础验证）
1. 启动 Chrome 并暴露调试端口：
   ```bash
   # Windows
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --no-first-run --no-default-browser-check

   # Mac/Linux
   google-chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check
   ```
2. 访问调试端点：打开浏览器访问 `http://localhost:9222`，可看到当前 Chrome 所有标签页的调试 WebSocket 地址（如 `ws://localhost:9222/devtools/page/xxx`）。
3. 用 WebSocket 客户端（如 wscat）连接并发送命令：
   ```bash
   # 安装 wscat（需 Node.js）
   npm install -g wscat

   # 连接调试地址（替换为自己的 ws 地址）
   wscat -c ws://localhost:9222/devtools/page/xxx

   # 发送 CDP 命令（JSON-RPC 格式）
   # 1. 启用网络监控
   {"id":1, "method":"Network.enable"}
   # 2. 导航到指定页面
   {"id":2, "method":"Page.navigate", "params":{"url":"https://example.com"}}
   # 3. 截取页面截图（返回 Base64 编码）
   {"id":3, "method":"Page.captureScreenshot"}
   ```

#### 方式 2：Node.js 脚本调用 CDP（自动化场景）
无需依赖 Puppeteer/Playwright，直接用 `ws` 库调用：
```javascript
const WebSocket = require('ws');

// 步骤1：获取 Chrome 调试端点（也可手动指定）
const getDebugEndpoint = async () => {
  const res = await fetch('http://localhost:9222/json/version');
  const data = await res.json();
  return data.webSocketDebuggerUrl;
};

// 步骤2：连接 CDP 并发送命令
(async () => {
  const wsUrl = await getDebugEndpoint();
  const ws = new WebSocket(wsUrl);

  ws.on('open', () => {
    // 1. 启用 Network 模块
    ws.send(JSON.stringify({
      id: 1,
      method: 'Network.enable'
    }));

    // 2. 导航到页面
    ws.send(JSON.stringify({
      id: 2,
      method: 'Page.navigate',
      params: { url: 'https://example.com' }
    }));

    // 3. 监听网络请求事件
    ws.send(JSON.stringify({
      id: 3,
      method: 'Network.requestWillBeSent',
      params: {}
    }));
  });

  // 接收浏览器响应/事件
  ws.on('message', (data) => {
    const message = JSON.parse(data);
    console.log('CDP 响应/事件：', message);
    // 如捕获到页面加载完成事件，触发截图
    if (message.method === 'Page.loadEventFired') {
      ws.send(JSON.stringify({
        id: 4,
        method: 'Page.captureScreenshot',
        params: { format: 'png' }
      }));
    }
  });
})();
```

#### 方式 3：Puppeteer 中调用 CDP（最常用）
Puppeteer 是 CDP 的“轻封装”，既提供高层 API，也支持直接调用原生 CDP 命令：
```javascript
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  
  // 创建 CDP 会话
  const cdpSession = await page.target().createCDPSession();
  
  // 1. 启用性能监控（CDP 原生命令）
  await cdpSession.send('Performance.enable');
  
  // 2. 模拟网络限速（3G）
  await cdpSession.send('Network.emulateNetworkConditions', {
    offline: false,
    latency: 100, // 延迟 100ms
    downloadThroughput: 1.5 * 1024 * 1024 / 8, // 1.5MB/s
    uploadThroughput: 750 * 1024 / 8 // 750KB/s
  });
  
  await page.goto('https://example.com');
  
  // 3. 获取性能指标（CDP 事件）
  cdpSession.on('Performance.metrics', (metrics) => {
    console.log('性能指标：', metrics);
  });
  
  await browser.close();
})();
```

---

### 四、CDP 的核心特点
#### 优点
1. **极致灵活**：覆盖 Chromium 所有底层能力（无功能阉割），可实现定制化调试/自动化；
2. **无依赖**：直接基于 WebSocket 通信，无需引入框架；
3. **实时性**：双向通信，可实时监听浏览器事件（如网络请求、DOM 变化）；
4. **深度控制**：可操控浏览器内核级行为（如禁用 JS、修改渲染参数、获取内存快照）。

#### 缺点
1. **浏览器限制**：仅原生支持 Chromium 系（Firefox/Safari 有各自协议，不兼容）；
2. **抽象度低**：需手动拼接 JSON-RPC 命令，处理异步逻辑（无内置等待机制）；
3. **版本兼容性**：CDP 命令随 Chromium 版本迭代（部分命令会新增/废弃）；
4. **易用性差**：无内置容错/重试，需手动处理异常（如页面加载超时、命令执行失败）。

---

### 五、CDP 典型使用场景
1. **自研调试工具**：定制化抓包工具、性能分析平台（如采集细粒度的 FPS/内存数据）；
2. **Chromium 专属自动化**：操控浏览器扩展、修改底层渲染参数、模拟特殊设备/网络；
3. **深度浏览器操控**：禁用浏览器安全策略、模拟证书错误、获取页面加密数据；
4. **调试/逆向分析**：分析页面 JS 执行流程、拦截加密网络请求、定位性能瓶颈。

---

### 六、注意事项
1. **安全风险**：暴露调试端口（`--remote-debugging-port`）会导致浏览器被外部操控，生产环境禁用；
2. **版本适配**：建议固定 Chromium 版本，避免因 CDP 命令变更导致脚本失效；
3. **异步处理**：CDP 命令无自动等待，需监听事件确认操作完成（如 `Page.loadEventFired` 确认页面加载完成）；
4. **替代方案**：若无需底层控制，优先使用 Puppeteer/Playwright（封装了 CDP，降低开发成本）。

综上，CDP 是 Chromium 调试/自动化的“底层基石”，适合需要深度定制的场景；若仅需通用自动化，建议使用基于 CDP 封装的框架（Puppeteer/Playwright）。