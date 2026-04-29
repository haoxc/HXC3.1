---
type: term
category:
description: 是游戏世界的核心单元，本质是一个包含所有可交互元素（如地形、角色、光源）的独立数据容器
tags:
  - 场景容器
aliases:
---
**UE场景中的Level（关卡）** 是游戏世界的核心单元，本质是一个包含所有可交互元素（如地形、角色、光源）的独立数据容器，存储为`.umap`文件。其核心特点包括：
1. **模块化设计**：可单独编辑、测试，支持子关卡（Sublevel）和动态流送（Level Streaming），例如通过流送体积（Level Streaming Volume）自动加载/卸载场景片段，优化内存占用。
2. **层级结构**：每个World包含一个**Persistent Level（持久关卡）** 作为主场景，以及多个Sublevels作为动态扩展，例如《黑客帝国：觉醒》中通过Sublevels组合实现无缝虚拟城市。
3. **协作友好**：支持“一Actor一文件”架构，团队成员可并行编辑不同Sublevels，避免文件冲突。

**应用场景**涵盖开放世界游戏、虚拟仿真等，常与World Partition（世界分区）、Nanite虚拟几何体等技术结合，实现超大规模场景的高效管理与渲染。