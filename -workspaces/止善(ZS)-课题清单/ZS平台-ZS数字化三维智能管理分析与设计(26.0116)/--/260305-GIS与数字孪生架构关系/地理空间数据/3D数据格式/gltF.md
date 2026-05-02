---
aliases:
  - 3D/格式/glTF(#轻量化)
tags:
  - 3D/可视化
  - 3D/数据格式
description:
type:
ref-url:
create-date: 2026-03-05
---
## 内容
- glTF（GL Transmission Format）是一种用于 3D 场景和模型的 。它由 Khronos Group 开发，旨在提供一种轻量级、高效的方式来传输和加载 3D 内容，特别是在 Web 和移动应用中。glTF 定义了一种 JSON 格式，用于描述 3D 场景的图形和动画，并且支持高动态范围（HDR）纹理和物理基础渲染（PBR）材料。
- 是一种高效的 3D 模型交换格式，专为 Web 和移动设备优化，支持物理基础渲染和高动态范围纹理。

**核心特性与技术细节：**
- **格式结构：**
    - **.gltf：** ASCII格式的JSON文件，用于定义场景结构，通常与.bin（二进制数据）和图片（纹理）分开存放。
    - **.glb：** 二进制格式，将所有数据（JSON、二进制缓存、图片）打包成一个文件，加载效率更高。
- **内容支持：** 支持PBR（物理渲染）材质、骨骼动画、蒙皮、顶点颜色、摄像机和光照。
- **优势：**
    - **高效传输：** 减小了3D模型的大小。
    - **快速加载：** 减少了运行时解压和渲染的计算量。
- **应用场景：**
    - **Web 3D：** Three.js、Babylon.js、WebGL。
    - **游戏开发：** Unity Godot。
    - **工具支持：** Blender、Maya等软件的导出/导入。
    - **地理空间：** [Cesium](https://yun.gstarcad.com/news/275/)。