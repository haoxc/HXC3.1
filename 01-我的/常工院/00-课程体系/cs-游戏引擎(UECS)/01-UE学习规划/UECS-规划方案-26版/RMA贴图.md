---
aliases:
  - //UE/贴图/RMA(Roughness/Metallic/AO)
tags:
  - RMA贴图
description: RMA 是一种极其常见的贴图打包（Map Packing）技术
type:
---
## 内容
在 2026 年的 PBR（基于物理的渲染）工作流中，RMA是一种极其常见的**贴图打包（Map Packing）** 技术。为了节省显存和减少采样次数，美术师会将三张灰度图分别塞进一张彩色图片（RGB）的三个通道里。

### 1. 通道分配逻辑

这是行业内最通用的做法：
- **R 通道 (Red)**：**Roughness**（粗糙度）。控制表面光泽，越白越磨砂，越黑越像镜面。
- **G 通道 (Green)**：**Metallic**（金属度）。区分电解质（黑）和金属（白）。
- **B 通道 (Blue)**：**AO /Ambient Occlusion**（环境光遮蔽）。控制缝隙处的暗部细节。

### 2. 为什么要在 Three.js 或 UE 中使用它？

- **性能提升**：如果分开用三张图，显卡要读取 3 次；打包成 RMA 后，只需要读取 **1 张图** 就能获得三个属性。这在 Web 端的 Three.js 性能优化中尤为重要。
- **显存压缩**：减少了文件体积和 GPU 显存占用，让场景加载更快。

### 3. 在不同引擎中的设置（避坑指南）

#### **在 Unreal Engine (UE) 中：**
- **取消勾选 sRGB**：导入 RMA 贴图后，务必在贴图设置里取消勾选 `sRGB`，并将压缩设置（Compression Settings）设为 `Masks (no sRGB)`。因为这三类数据是非线性的数学数据，不是颜色。
- **连线**：从 Texture Sample 节点的 R、G、B 端口分别连入材质球对应的 Roughness、Metallic 和 Ambient Occlusion 槽位。
#### **在 Three.js 中：**

Three.js 的 `MeshStandardMaterial` 默认并不直接支持这种“三合一”贴图（它通常期望金属度和粗糙度是分开的，或者合在 `metalnessMap` 和 `roughnessMap` 中）。
- **如果你使用 GLTF 模型**：GLTF 标准通常使用 **ORM 贴图**（Occlusion, Roughness, Metallic），对应关系是 **R=AO, G=Roughness, B=Metallic**。
- **手动加载**：如果你坚持使用 RMA 顺序，你需要在着色器中手动分配通道，或者在加载后对材质属性进行偏移映射。
### 4. 软件导出设置
- **Substance Painter**：在导出贴图时，选择 `UE4 (Packed)` 或 `UE5` 预设，它会自动生成这种打包好的贴图。

### 总结
看到 RMA 贴图，你就把它当成一个“压缩包”。记得**关闭 sRGB**（非常重要，否则质感会发灰/出错），然后按 R-G-B 对应关系连线即可。