---
aliases:
  - //UE/视觉/光照/概念/环境光(Ambient Lgiht)
tags:
description: 模拟现实世界中天光、大气散射以及物体间二次反弹的光线
type:
Positioning: 模拟现实世界中天光、大气散射以及物体间二次反弹的光线
---
# Unreal Engine 技术专题：环境光 (Ambient Light) 与环境系统

---

## 1. 核心知识要点 (Key Knowledge Points)

在 Unreal Engine 中，**环境光 (Ambient Light)** 不再是一个简单的全局亮度数值，而是一个由多个系统协同构建的**光照环境**。它的核心目标是模拟现实世界中天光、大气散射以及物体间二次反弹的光线。

### A. 天光 (Sky Light)

- **定义**：环境光的最主要来源。它捕捉远处（天空、大气、背景）的信息，并将其作为光源均匀地照射到场景中。
- **实时捕捉 (Real Time Capture)**：在 UE5 中，开启此项可以让天空颜色变化（如黄昏到深夜）实时反映在场景光照上。

### B. 大气系统 (Sky Atmosphere)

- **物理基础**：模拟瑞利散射 (Rayleigh Scattering) 和米氏散射 (Mie Scattering)。
- **作用**：决定了天空的颜色、夕阳的红光以及远山的漫射效果。
	- ![[img-瑞利散射.jpg]]
	- ![[img-米氏散射.jpg]]

### C. 间接光照 (Indirect Lighting / Global Illumination)
- **Lumen**：UE5 的核心。它不仅处理直射光，还处理光线在物体表面弹射后的“环境感”。
- **环境光遮蔽 (AO)**：正如我们之前讨论的，[[UE技术-环境光遮罩(AO)|AO]] 是环境光的“减法”，负责在角落处扣除多余的环境光。

---

## 2. 知识关联关系 (Relationship Topology)

环境光不是孤立存在的，它依赖于一套“环境套件”的组合：

| **组件名称**                | **角色**   | **关联逻辑**                                                  |
| ----------------------- | -------- | --------------------------------------------------------- |
| **Sky Light**           | **光源载体** | 负责“发光”，必须关联大气或 HDRI。                                      |
| **Sky Atmosphere**      | **色彩源**  | 为 Sky Light 提供物理准确的颜色背景。                                  |
| **Volumetric Cloud**    | **遮挡物**  | 云层会遮挡天光，产生动态的阴影和光影变化。                                     |
| **Post Process Volume** | **调色盘**  | 通过 Exposure (曝光) 和 Indirect Lighting Intensity 控制最终看到的亮度。 |
|                         |          |                                                           |

---

## 3. 聚焦实践：构建标准户外环境 (Practical Workflow)

### 第一步：环境“全家桶”快速搭建

在 UE5 中，你可以通过 `Window -> Env. Light Mixer` ([[环境光混合器]]) 一键创建以下五个核心组件：
1. **Sky Light** (天光)
2. **Atmospheric Atomosphere** (大气)
3. **Volumetric Cloud** (体积云)
4. **Height Fog** (指数级高度雾 - 增加空间深度)
5. **Directional Light** (太阳光)

### 第二步：HDRI 进阶（针对室内或产品展示）

如果你需要特定的环境反射（如工厂内部、影棚）：
- 使用 **HDRI Backdrop** 插件。
- 导入一张 `.exr` 或 `.hdr` 格式的高动态范围图像。
- Sky Light 会自动捕捉这张图的色彩信息，作为环境光压入场景。
> [[UE技术-HDRI与基于与基于图像的光照 (IBL)]]

### 第三步：Lumen 调优

- 在 **Post Process Volume** 中，找到 `Global Illumination`，确保 Method 设置为 **Lumen**。
- 调整 `Lumen Scene Lighting Quality` 以平衡性能与室内漏光问题。

---

> [!TIP] 实践指南
>
> 解决“阴影过黑”问题：
>
> 如果你的场景在阴影处完全看不见细节，通常是因为 Sky Light 强度不足，或者 Lumen 没有正确计算二次弹射。
>
> 快速检查：尝试提高 Sky Light 的 Intensity，或者在太阳光 (Directional Light) 中增加 Indirect Lighting Intensity。

---

## 4. 成果达成 Checklist

- [ ] **动态响应**：旋转太阳光（Ctrl+L），天空颜色和环境暗部会随之自然变化。
- [ ] **室内表现**：在完全封闭的房间内，即便没有灯光，也应该有微弱的、由于外部天光弹射进来的间接光。
- [ ] **深度感**：通过 **Exponential Height Fog**，远处的物体呈现出淡淡的蓝色或灰色，产生空气透视感。
- [ ] **反射一致性**：金属材质表面能清晰看到天空或环境的倒影，而非纯黑色。

 