---
tags: [chrome, 工具]
description: 大多数 Chrome Flag 的命名都遵循：`[功能模块]-[具体操作]-[技术细节]`。
type: note
create-date: 2025-12-29
---

# 📔 Obsidian 笔记：Chrome Flag 命名规范与逻辑

## 🧬 Flag 命名的三段式结构

大多数 Chrome Flag 的命名都遵循：`[功能模块]-[具体操作]-[技术细节]`。
### 1. 模块前缀 (Module Prefix)
指明这个 Flag 属于哪个子系统。
- `prompt-api-*`: 指代 Web 平台层面的 AI 接口（Window AI）。
- `enable-well-known-*`: 指代网络协议或知名地址。
- `ui-*`: 指代用户界面相关的改动。
- `gpu-*`: 指代硬件加速相关的底层逻辑。
### 2. 操作谓词 (Action Verb)
指明这个 Flag 是做什么的。
- `for`: 为某个特定对象准备（如：`...-for-gemini-nano`）。
- `disable`: 强制关闭某功能。
- `ignore`: 忽略某种错误或限制。
---
## 🏗 Chrome 官方命名潜规则 (Internal Conventions)

### ✅ 潜规则 1：Kebab-case (短横线隔开)

在 `chrome://flags` 页面上，所有的 Flag ID 必须是小写字母并用短横线连接。
> 示例：optimization-guide-on-device-model
>
> 逻辑：易于在 URL 中传输，且符合 Linux/Unix 的传统。

### ✅ 潜规则 2：功能对齐 (Feature Alignment)

Flag 的名字通常与代码中 `base::Feature` 对象的字符串名称保持一致。
- **代码中**：`kPromptAPIForGeminiNano`
- **Flag 页面**：`prompt-api-for-gemini-nano`

> **转换规则**：大写转小写，大写字母前加短横线。

### ✅ 潜规则 3：生命周期标记
虽然在 UI 上看不见，但 Flag 的命名往往暗示了其阶段：
- **Experimental**: 实验性功能。
- **Temporary**: 临时性迁移工具。
- **Staging**: 灰度测试阶段。

---

## 📊 案例拆解：`#prompt-api-for-gemini-nano`

我们将你之前提到的这个 Flag 拆解开看：

| **组成部分**        | **命名语意** | **专家解读**             |
| --------------- | -------- | -------------------- |
| **prompt-api**  | 核心对象     | 定义了这是一个关于“提示词接口”的功能。 |
| **for**         | 关联词      | 表示后续是该 API 的支撑/目标。   |
| **gemini-nano** | 目标模型     | 指明了 API 绑定的具体模型实例。   |
