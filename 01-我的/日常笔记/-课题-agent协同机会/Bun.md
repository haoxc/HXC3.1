---
aliases:
  - 技术/Javascript/运行时/Bun
tags:
description: Bun是以Zig语言编写的一套JavaScript运行时系统、包管理器、测试运行器及打包工具。Bun设计上是Node.js的直接替代品，但它使用JavaScriptCore作为引擎，不同于Node.js和Deno使用V8引擎。 Bun可以对JavaScript文件进行打包构建、代码压缩，也支持服务器端渲染 。
type:
ref-url:
---
## 内容
Bun 是一款极其快速、全能的 JavaScript 运行时（类似于 [[node.js]]和 Deno），其核心价值体现在 **性能** 和 **集成度**：
- **极致速度**：Bun 基于 Apple 的 JavaScriptCore 引擎构建，在启动速度、包管理（`bun install` 比 npm 快几十倍）和运行效率上显著优于 Node.js。
- **全能工具链**：它不仅是运行时，还集成了打包器 (Bundler)、测试运行器 (Test Runner) 和包管理器，减少了配置复杂度。
- **近期动态**：2025 年底，[Anthropic 宣布收购了 Bun 团队](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone)，以支持其 AI 开发工具（如 Claude Code）的底层性能