---
aliases:
  - 智能体/工具/CLI转换工具制作(CLI-anything)
tags:
  - 智能体/工具/CLI-anything
description:
type:
ref-url:
create-date: 2026-03-12
---
## 内容
**CLI-Anything** 是由香港大学数据科学团队（HKUDS）开发的一个开源项目，旨在将**任何软件**转变为 AI 智能体（Agent）可直接控制的**命令行工具**。

### 核心功能与意义
- **让 AI 像专家一样使用软件**：AI 在逻辑推理上很强，但直接操作专业软件（如 Blender、OBS、GIMP）往往很困难。CLI-Anything 可以将这些软件的功能提取并封装成结构化的命令，让 AI 能够精准调用。
- **消除“点击”带来的不稳定性**：传统的 GUI 自动化依赖屏幕截图和坐标点击，非常脆弱且昂贵。转换为 CLI 后，智能体通过确定性的文本指令与程序交互，执行效率和准确率大幅提升。
- **统一碎片化的接口**：它可以将分散的 API、SDK 甚至是原本没有 API 的软件统一包装成一组连贯的命令组，减少智能体在任务执行中的 Token 消耗。
- **一键式转换**：该项目号称只需一条指令即可完成软件的“智能体化”改造，支持 [OpenClaw](https://github.com/HKUDS/CLI-Anything)、Claude Code 和 Cursor 等主流 AI 开发工具的集成。