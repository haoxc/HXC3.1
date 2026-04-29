---
type: term
category:
description: 虚幻引擎中所有可放置对象的`基类`（如立方体、球体、墙体、道具等均为Actor实例）
tags:
  - 最小单元
aliases:
domain: UE
---
- **定义**：UE中所有场景对象的`基类`，可放置于关卡的独立实体（如角色、道具、触发器），通过组件承载全部功能（如渲染、碰撞）。
- **特点**：
1. 无自带Transform（依赖RootComponent定位，如SceneComponent）；
2. 组件寄生性（功能全由附加组件实现，如StaticMeshComponent）；
3. 生命周期回调（BeginPlay/Tick/EndPlay驱动逻辑）；
4. 动态实例化（支持Spawn/销毁，适配玩家、AI、环境元素）。