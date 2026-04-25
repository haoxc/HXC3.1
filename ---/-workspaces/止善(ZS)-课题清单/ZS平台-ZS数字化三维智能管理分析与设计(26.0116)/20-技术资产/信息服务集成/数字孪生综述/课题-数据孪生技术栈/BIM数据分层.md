---
aliases:
  - 课题/BIM数据分层
tags:
description:
type:
ref-url:
---
## 内容
将 Revit/Tekla 导出的原始 BIM 数据拆解为三个独立的逻辑层：
- **几何层 (Geometry - 只有皮囊)**：
    - **策略**：通过 Datasmith 导入，开启 **Nanite**。
    - **处理**：剔除所有非必要的视觉构件（如天花板内部的加固件），只保留可见部分。
    - **性能目标**：确保 GPU 渲染维持在 **60FPS (16.6ms)**。
- **属性层 (Static Properties - 静态档案)**：
    - **策略**：**脱离 UE 存储**。将厂家、材质、安装日期等 80% 的静态元数据存入外部数据库（如 PostgreSQL 或 MongoDB）。
    - **链接**：模型中仅保留一个唯一的 `GUID` (全局统一标识符)。
- **实时层 (Dynamic Data - 动态神经)**：
    - **策略**：通过 **MQTT/WebSocket** 实时推送到 UE 内存。
    - **内容**：仅传输 `{GUID: Value}`（如：`{Pump_001: 75℃}`）。