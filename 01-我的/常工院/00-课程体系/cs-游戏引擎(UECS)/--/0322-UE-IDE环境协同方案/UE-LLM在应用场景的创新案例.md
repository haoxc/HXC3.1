---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-04-29
---
## 成功案例汇总
![[01-我的/03-常工院/00-课程体系/cs-游戏引擎(UECS)/--/0322-UE-IDE环境协同方案/z附件/image.png]]
**开发辅助类**

Cashworth.net 的开发者将本地 Ollama 与 JetBrains Rider 集成，在不违反 NDA 的前提下为 UE C++ 代码提供补全和路径分析——AI 不仅正确识别出寻路启发式函数，还建议了新的启发式类型并给出实现方式。

**场景构建类**

UnrealGenAISupport 插件（支持 GPT、Claude、Qwen、Deepseek 等）已实现"AI 自动场景生成"功能，可通过 MCP UE5 服务器让 LLM 直接控制场景物体的变换、材质，并生成蓝图、函数和变量。

**角色动画类**

Convai 的 NeuroSync 动画系统实时处理音频流，无需离线处理或预烘焙，开发者只需在 MetaHuman 蓝图中添加 BP_ConvaiFaceSync 组件，即可实现 AI 驱动的口型同步和实时面部表情。

**运行时 AI 类**

`UnrealAiConnector` 插件通过 [[Blueprint 接口]]暴露"命令系统"，让 AI 直接控制游戏角色响应文字指令，支持 Claude、GPT、Gemini 等模型，并附带完整演示项目。

**本地 LLM 完全离线类**
Cactus AI 框架可在设备本地（包括手机等边缘设备）运行 LLM、VLM 和 TTS，已集成进 UE5.6，通过蓝图暴露多轮对话、图像处理和对话导出功能，适合对隐私和延迟有要求的场景。

---

## 成熟度对比

|场景|成熟度|推荐工具|
|---|---|---|
|蓝图/C++ 辅助|⭐⭐⭐⭐⭐ 最成熟|UE LLM Toolkit + Claude Code|
|NPC 对话动画|⭐⭐⭐⭐ 成熟|Convai / Inworld|
|场景自动摆放|⭐⭐⭐ 发展中|Ultimate Copilot / UnrealGenAI|
|运行时动态剧情|⭐⭐ 实验阶段|自定义 + 本地 LLM|
|动捕/动画生成|⭐⭐ 实验阶段|DeepMotion + 手工绑定|