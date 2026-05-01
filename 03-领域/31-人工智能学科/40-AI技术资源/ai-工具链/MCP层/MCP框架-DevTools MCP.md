---
aliases:
  - 技能/Playwright MCP
  - DevTools MCP
  - 课题/端到端测试
tags:
  - mcp
  - 工具链
type: note
description: MCP 全称是 **Module Communication Protocol（模块通信协议）**，是软件模块间标准化通信的底层规范。在浏览器调试/自动化领域，
create-date: 2026-03-08
---
### 一、核心概念厘清
MCP 全称是 **Module Communication Protocol（模块通信协议）**，是软件模块间标准化通信的底层规范。在浏览器调试/自动化领域，`DevTools MCP` 和 `Playwright MCP` 是针对不同层级、不同场景的协议实现：
- `DevTools MCP`：Chrome [[浏览器调试协议（CDP）]]的核心模块化通信层，聚焦 Chromium 系浏览器的底层操控；
- `Playwright MCP`：微软 Playwright 框架封装的跨浏览器自动化通信层，兼容多种底层协议并提供统一抽象。

---

### 二、DevTools MCP（Chrome DevTools 模块通信协议）
#### 1. 本质
是 Chromium 内核（Chrome/Edge/Opera 等）的原生调试协议（CDP）的核心层，基于 **JSON-RPC 2.0** 实现，是 Chrome DevTools 前端（开发者工具界面）与浏览器内核通信的底层规范。

#### 2. 核心能力
直接操控浏览器内核的核心模块（Page、Runtime、Network、DOM、Performance 等），支持：
- 断点调试、JS 代码注入/执行；
- 网络请求拦截、抓包、修改请求/响应；
- DOM 元素直接操作、页面截图/录屏；
- 性能指标采集（FPS、加载时间、内存占用）。
#### 3. 关键特点
| 特性    | 说明                                     |
| ----- | -------------------------------------- |
| 协议层级  | 底层（浏览器内核级），无封装                         |
| 浏览器支持 | 仅原生支持 Chromium 系，Firefox/Safari 需额外兼容层 |
| 抽象程度  | 极低，需手动拼接 CDP 命令（如 `Network.enable`）    |
| 灵活性   | 极致灵活，可实现定制化调试/自动化                      |
| 易用性   | 低，需熟悉 CDP 命令体系和浏览器版本适配                 |

#### 4. 典型使用场景
- Chrome DevTools 前端与浏览器的原生通信；
- Puppeteer（原生基于 CDP）开发 Chromium 专属自动化工具；
- 定制化 Chromium 浏览器调试工具（如自研性能分析平台）。

---

### 三、Playwright MCP（微软 Playwright 模块通信协议）
#### 1. 本质
Playwright 框架封装的 **跨浏览器自动化通信层**，底层兼容 `DevTools MCP（CDP）`、Firefox Remote Debugging Protocol、WebKit Web Inspector Protocol，向上提供统一的高层抽象 API。

#### 2. 核心能力
屏蔽不同浏览器底层协议差异，提供通用自动化能力：
- 跨浏览器页面操作、元素定位/交互（点击、输入、滚动）；
- 网络请求全局拦截、修改、模拟；
- 多上下文/多标签页/多浏览器并行管理；
- 自动等待元素可交互（内置防 Flaky 机制）；
- 同时支持直接调用底层 `DevTools MCP` 命令（兼顾灵活性）。

#### 3. 关键特点
| 特性    | 说明                                  |
| ----- | ----------------------------------- |
| 协议层级  | 高层（框架封装级），基于底层协议扩展                  |
| 浏览器支持 | 原生跨 Chromium/Firefox/WebKit（Safari） |
| 抽象程度  | 高，API 简洁统一（如 `page.click()`）        |
| 灵活性   | 高（可直接调用 CDP 命令）                     |
| 易用性   | 极高，学习成本低，内置自动化最佳实践                  |

#### 4. 典型使用场景
- 跨浏览器 E2E 测试（如 Playwright Test + Jest）；
- 通用型浏览器自动化（爬虫、UI 操作、批量截图）；
- 跨浏览器兼容性验证（一次编码，多浏览器执行）。

---

### 四、核心对比
| 对比维度 | DevTools MCP（CDP）                             | Playwright MCP        |
| ---- | --------------------------------------------- | --------------------- |
| 核心定位 | Chromium 底层调试协议                               | 跨浏览器自动化抽象协议层          |
| 协议依赖 | 无（浏览器原生协议）                                    | 兼容 DevTools MCP 等底层协议 |
| 代码示例 | `session.send('Page.navigate', {url: 'xxx'})` | `page.goto('xxx')`    |
| 等待机制 | 需手动实现（如 `setTimeout`）                         | 内置自动等待（元素可交互才执行）      |
| 跨浏览器 | 不支持                                           | 原生支持 3 大浏览器内核         |

---

### 五、关联与使用建议
#### 1. 两者关联
Playwright MCP 是对 DevTools MCP（CDP）等底层协议的**封装和扩展**，同时保留了调用底层 CDP 命令的能力：
```javascript
// Playwright 中直接调用 DevTools MCP（CDP）命令示例
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  // 创建 CDP 会话（调用 DevTools MCP）
  const cdpSession = await page.context().newCDPSession(page);
  // 启用网络监控（CDP 命令）
  await cdpSession.send('Network.enable');
  // 设置自定义 HTTP 头（CDP 命令）
  await cdpSession.send('Network.setExtraHTTPHeaders', {
    headers: { 'X-Custom-Header': 'playwright-cdp' }
  });
  await page.goto('https://example.com');
  await browser.close();
})();
```

#### 2. 使用建议
- **选 DevTools MCP（CDP）**：需深度定制 Chromium 浏览器（如自研调试工具、极致性能分析）、仅需支持 Chromium 系；
- **选 Playwright MCP**：跨浏览器自动化/测试、快速开发通用脚本、追求易用性和稳定性；
- **混合使用**：用 Playwright 实现通用逻辑，通过 CDP 调用补充 Chromium 专属底层能力。

---

### 总结
DevTools MCP 是 Chromium 浏览器调试/自动化的“地基”，提供极致底层控制；Playwright MCP 是基于地基搭建的“`通用上层建筑`”，解决了跨浏览器兼容和易用性问题。两者互补，而非对立——Playwright 既封装了 DevTools MCP 的复杂性，又保留了其灵活性，是多数自动化场景的首选。
