---
aliases:
  - KWs://UE/技术/Media/视频跨软件交换(推流)
tags:
  - 技术/视频推流
  - 技术/视频跨软件交换
  - MediaIO框架
description:
type:
---
## 1. NDI (Network Device Interface)

NDI 主要解决**跨网络**的实时视频传输，UE 5.6 对其进行了深度原生化集成。
- **原生集成与 Motion Design：** NDI 现在是 UE 5.6 新增 **Motion Design（运动设计）** 工具集的默认输出协议。你可以直接通过其广播窗口将带 Alpha 通道的画面推送到 OBS 或广播控制台。
- **NDI 6.2 支持：** 兼容最新的 NDI 6 标准，支持 **16位 HDR 颜色** 和多达 16 个浮点音频通道，在万兆网络下可实现接近无损的 4K/8K 传输。 #无损格式 #分辨率/4K-8K
- **蓝图控制：** 5.6 版本优化了蓝图节点，允许在运行时通过字符串或变量动态切换 NDI 接收源。 

## 2. Spout / Funnel (Syphon)
Spout 主要解决**同一台电脑内**不同软件间的“零延迟”画面共享（通过 GPU 显存直接传递，不走网络或采集卡）。
- **Spout：** 在 Windows 环境下，常用于将 UE 的渲染结果实时发送到 **[TouchDesigner]([Derivative |](https://derivative.ca/))、[Resolume]([Resolume VJ Software & Media Server](https://www.resolume.com/))** 或 **OBS**。 [[工具-影像制作-生态中3剑客]]
    - **优势：** 由于不涉及编码与解码，延迟几乎为零，且不占用网络带宽。
    - **5.6 兼容性：** 支持 Direct X 12 (DX12) 的纹理共享，解决了早期版本在开启硬件光追 (HWRT) 时的稳定性问题。
- **Funnel：** 这是一个由开发者 Keijiro Takahashi 开发的经典插件，专门用于简化 UE 画面到 Spout (Windows) 或 Syphon (macOS) 的导出。
    - **现状：** 虽然 Funnel 的独立插件版本更新较慢，但其核心逻辑已演变为 UE 5.6 中更强大的 **[[Media IO 框架]]**。 #MediaIO框架
    - **替代方案：** 现在更推荐使用官方的 **OWL Cinecam** 或 **Off World Live** 插件，它们集成了更稳定的 Spout/NDI 一键输出功能，支持渲染层级和透明度设置。 

## 3. 如何选择？

| 特性            | NDI                  | Spout (Funnel)            |
| ------------- | -------------------- | ------------------------- |
| **传输介质**      | 局域网 (Ethernet/Wi-Fi) | 显存共享 (GPU Memory)         |
| **延迟**        | 极低（取决于网络，约 100ms 内）  | **零延迟**                   |
| **距离**        | 跨房间、跨建筑              | **仅限单台机器**                |
| **UE 5.6 状态** | **深度原生集成**，支持 NDI 6  | 需通过三方插件（如 Off World Live） |

**建议：** 如果你是在单机进行直播或视觉交互（如 UE + OBS），优先使用 **Spout** 以获得最高性能；如果你需要将 UE 画面发送到另一台推流机或导播台，请使用 **NDI**