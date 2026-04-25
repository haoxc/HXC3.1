---
aliases:
  - ai/智能体/开发框架/执行网关/Browser-use API (动作接口)
tags:
  - Agent框架/执行网关
  - 角色/翻译官
  - 角色/执行者
title: Browser-use API (动作接口)
description:
domain: Browser-use API (动作接口)
created: 2026-01-09 18:10
---

> [!ERROR]
> 命名逻辑 : Browser(工具) + use(动作)
## 描述

在 2026 年的 AI 开发语境下，**Browser-use API** 通常是指让大型语言模型（LLM）能够像人类一样操作浏览器的库或接口（如 Playwright、Puppeteer 的 AI 封装版）。

这类 API 的“动作（Actions）”通常分为以下几类核心接口：
1. 基础交互动作 (Element Interaction)
这是最常用的接口，用于模拟鼠标和键盘操作：
- **`click(selector)`**: 点击特定元素。
- **`type(selector, text)`**: 在输入框输入文本。
- **`scroll_to(direction/element)`**: 向上/下滚动或滚动到特定位置。
- **`hover(selector)`**: 悬停在某个元素上以触发浮窗。
- **`drag_and_drop(source, target)`**: 拖拽操作。

2. 页面导航与管理 (Page Management)

用于控制浏览器的状态：

- **`goto(url)`**: 跳转至指定网址。
- **`go_back()` / `go_forward()`**: 后退或前进。
- **`refresh()`**: 刷新页面。
- **`switch_tab(index/title)`**: 切换标签页。
- **`close_tab()`**: 关闭当前页面。

3. 感知与提取 (Perception & Extraction)

AI 需要通过这些接口“看见”网页内容：

- **`screenshot()`**: 获取当前页面的截图（常用于多模态模型视觉分析）。
- **`get_dom_tree()`**: 获取简化的 DOM 树结构，方便 LLM 理解页面布局。
- **`extract_text()`**: 提取页面纯文本。
- **`get_accessibility_tree()`**: 获取无障碍树，这是目前 AI 识别网页元素最精准的方式。

4. 高级动作 (Advanced/Scripting)

- **`execute_javascript(code)`**: 直接在页面执行自定义 JS 脚本。
- **`wait_for_network_idle()`**: 等待网络请求完成，确保页面加载完毕。
- **`solve_captcha()`**: 自动调用验证码识别服务。

---

推荐工具库

如果你正在寻找现成的实现方案，可以参考以下项目：

1. **Browser-use (GitHub)**: 专为 LangChain 和 Playwright 设计，支持让 AI 自动编排上述动作。
2. **Skyvern**: 利用计算机视觉和 DOM 解析自动完成复杂工作流。
3. **LaVague**: 专注于将自然语言指令转换为 Selenium/Playwright 代码的框架。

**使用建议：**
在 2026 年，建议优先使用基于 **Accessibility Tree (无障碍树)** 的动作接口，因为相比 CSS 选择器，它受网页前端改版的影响更小，AI 理解起来更稳定。