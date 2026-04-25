---
aliases:
  - skill/受控浏览器(managed browser, dedicated chrome)
tags:
description:
type:
ref-url:
---
## 内容

### 安装 托管浏览器(Playwright)


> 安装[[MCP框架-DevTools MCP|技能/Playwright MCP]]

``` shell
# 1. 安装 Playwright 核心包
npm install -g playwright

# 2. 安装受控浏览器内核（Chromium, Firefox, WebKit）
npx playwright install chromium
```


### 启动
```shell
openclaw browser start
```
### 参考
- https://www.kdnuggets.com/7-essential-openclaw-skills-you-need-right-now