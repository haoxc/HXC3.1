---
aliases: [端点, API endpoint, API端点]
tags: [概念定义, API, LiteLLM]
description: 快速理解 endpoint 在 API、LiteLLM 与 agent 编程工具中的含义和易错边界
type: 概念定义
ref-url:
create-date: 2026-04-26 19:02
---

## 一句话定义

Endpoint 是一个服务对外暴露的“可访问地址 + 协议入口”，客户端把请求发到这个入口，服务再根据路径、鉴权、请求格式和模型名决定如何处理。

## 最小理解图

```text
客户端工具
  ↓ 请求 URL + token + payload
endpoint
  ↓ 路径匹配 / 鉴权 / 协议解析
服务端能力
  ↓
返回结果
```

在 LiteLLM 场景中：

```text
Claude Code / Aider / OpenCode
  ↓
LiteLLM 本地 endpoint
  ↓
上游模型供应商 endpoint
```

## 判断标准

1. 它必须是客户端能访问的网络入口，例如 `http://localhost:4000` 或 `https://api.example.com/v1`。
2. 它不仅是域名，还隐含协议形态，例如 OpenAI-compatible、Anthropic-compatible。
3. 它通常要和鉴权方式、请求路径、请求体格式一起使用，单独一个 URL 不一定够。
4. 同一个服务可以暴露多个 endpoint，不同 endpoint 可能对应不同协议或能力。

## 和相近概念的区别

| 概念         | 区别                                                     |
| ---------- | ------------------------------------------------------ |
| URL        | URL 是地址字符串；endpoint 是可被某类客户端调用的服务入口，包含“这个地址接受什么请求”的含义。 |
| API        | API 是一组能力和规则；endpoint 是 API 中某个具体入口。                   |
| Base URL   | Base URL 是基础地址；endpoint 往往是 base URL 加具体路径后的调用入口。      |
| Model name | Model name 决定请求哪个模型；endpoint 决定请求发到哪个服务入口。             |
| Provider   | Provider 是服务供应方；endpoint 是访问 provider 的入口地址。           |
|            |                                                        |

## 在 LiteLLM 中的典型例子

Claude Code 使用 Anthropic-compatible endpoint：

```bash
ANTHROPIC_BASE_URL=http://localhost:4000
claude --model deepseek-v4-pro
```

Aider / OpenCode 使用 OpenAI-compatible endpoint：

```bash
OPENAI_API_BASE=http://localhost:4000/v1
aider --model openai/sonnet-4-6
```

LiteLLM 再把本地请求转发到上游 endpoint：

```yaml
model_list:
  - model_name: deepseek-v4-pro
    litellm_params:
      model: anthropic/deepseek-v4-pro
      api_base: https://api.deepseek.com/anthropic
```

## 常见误区

### 误区 1：把 endpoint 当成普通网址

能打开网页不代表它是可用 API endpoint；浏览器能访问也不代表模型客户端能调用。

API endpoint 还要求：

- 路径正确；
- 鉴权正确；
- 请求方法正确；
- 请求体格式正确；
- 模型名被上游支持。

### 误区 2：Claude Code 和 OpenAI 客户端共用同一个写法

Claude Code 不走 OpenAI `/v1/chat/completions`，它走 Anthropic Messages API。

因此：

```bash
# Claude Code
ANTHROPIC_BASE_URL=http://localhost:4000
```

```bash
# Aider / OpenCode / OpenAI SDK
OPENAI_API_BASE=http://localhost:4000/v1
```

不要把 Claude Code 配成：

```bash
ANTHROPIC_BASE_URL=http://localhost:4000/v1
```

### 误区 3：上游 OpenAI-compatible endpoint 漏掉 `/v1`

很多 OpenAI-compatible 服务要求 base URL 带 `/v1`。

例如：

```bash
OHMYGPT_API_BASE=https://api.ohmygpt.com/v1
```

如果写成：

```bash
OHMYGPT_API_BASE=https://api.ohmygpt.com
```

常见结果是 LiteLLM 能启动，本地 `/v1/models` 也能返回，但真实模型调用上游时报 `404 Not Found`。

### 误区 4：本地 endpoint 通了，不等于上游 endpoint 通了

`http://localhost:4000/v1/models` 正常，只说明 LiteLLM 本地服务和模型列表正常。

它不能证明：

- 上游 API Key 有效；
- 上游 endpoint 正确；
- 上游模型名正确；
- 当前协议适配正确。

必须再做一次真实最小调用，例如要求模型只返回 `OK`。

## 压缩记忆

> Endpoint 不是“一个网址”这么简单，而是“某个协议下可被客户端调用的服务入口”。在 LiteLLM 中，最容易错的是把 Claude Code 的 Anthropic endpoint 和 OpenAI-compatible `/v1` endpoint 混成一类。
