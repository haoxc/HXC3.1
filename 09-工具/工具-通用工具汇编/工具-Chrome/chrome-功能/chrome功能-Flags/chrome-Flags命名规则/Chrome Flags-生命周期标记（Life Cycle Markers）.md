---
tags: [chrome, 工具]
description: 在 Chrome Flags 中，一个功能的“生命周期”并不仅仅是它存在的时间，更是它**从实验室走向大众的过程**。生命周期标记（Life Cycle Mar
type: note
create-date: 2025-12-29
---

## 定义和范畴

在 Chrome Flags 中，一个功能的“生命周期”并不仅仅是它存在的时间，更是它**从实验室走向大众的过程**。生命周期标记（Life Cycle Markers）主要通过**命名前缀**、**UI 状态栏**以及**隐藏的元数据**这三个维度来体现

| **命名标记**                | **生命周期阶段**             | **含义解读**                          |
| ----------------------- | ---------------------- | --------------------------------- |
| `enable-experimental-*` | **初生期 (Experimental)** | 最早期的功能，可能极度不稳定。                   |
| `temporary-*`           | **过渡期 (Migration)**    | 用于旧功能向新功能迁移时的临时开关，随后会被删除。         |
| `deprecated-*`          | **衰退期 (Deprecation)**  | 该功能即将被移除，提供此 Flag 是为了给开发者最后的兼容时间。 |
| `ui-refresh-*`          | **迭代期 (Iteration)**    | 专门针对界面风格（如 Material Design）更新的阶段。 |
## 🎨 视觉化理解：一个功能的“一生”

1. **孵化阶段**：以 `#enable-experimental-web-platform-features` 这种大类 Flag 形式存在。
2. **独立阶段**：获得专属命名，如 `#prompt-api-for-gemini-nano`。
3. **默认开启**：状态变为 `Default (Enabled)`，不再需要手动开启。
4. **清理阶段**：代码彻底稳固，Flag 命名标记为 `deprecated` 或直接从 `chrome://flags` 中注销。
