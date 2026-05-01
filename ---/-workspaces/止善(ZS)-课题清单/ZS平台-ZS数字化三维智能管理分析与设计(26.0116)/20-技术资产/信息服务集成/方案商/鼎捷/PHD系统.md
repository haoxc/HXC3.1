---
aliases:
  - 数字化/方案/构成/PHD系统（Process History Database，过程历史数据库）
tags:
description: 工厂级的信息管理平台,通过 RDI（Real-time Data Interface，实时数据接口） 从底层的 DCS 或 PLC 系统中采集数据
type:
ref-url:
create-date: 2026-02-13
---
## 内容
PHD 通常作为工厂级的信息管理平台，通过 **RDI（Real-time Data Interface，实时数据接口）** 从底层的 DCS 或 PLC 系统中采集数据：
- **数据流向**：DCS（生产控制层） → RDI 采集服务器 → PHD Server（数据存储与管理层）。
- **核心组件**：RDI Server 负责周期性地从 DCS 扫描[[点位数据]]，并将其发送至 PHD 数据库进行长期历史存储.