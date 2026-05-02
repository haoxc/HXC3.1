---
aliases:
  - HXC Vault 与 Karpathy 知识组织对比
  - HXC Vault vs Karpathy llm-wiki
tags: [知识管理, llm-wiki, HXC-Vault]
description: 对比 HXC Vault 领域治理方案与 Karpathy/llm-wiki 式知识编译思想。
type: note
create-date: 2026-05-02
---

# HXC Vault与Karpathy知识组织对比

**结论**：HXC Vault 方案适合做“领域知识书架”，Karpathy/llm-wiki 思想适合做“单一课题的知识编译机”。两者不是替代关系，而是层级分工关系。

## 对比矩阵

| 维度 | HXC Vault 领域治理 | Karpathy / llm-wiki 思想 |
| --- | --- | --- |
| 核心目标 | 人类长期管理一个领域 | Agent 深度编译一个课题 |
| 组织轴 | 术语 / 课题 / 方法工具 / 知识 | raw / entities / concepts / comparisons / queries |
| 导航入口 | MOC 文件夹笔记 | `index.md` + 高密度交叉链接 |
| 知识状态 | 已沉淀、可复用、可教学 | 正在抽取、链接、验证 |
| 适合对象 | 管理学科整体 | 战略指标量化、Agent 全景等单一课题 |
| 来源追溯 | 较弱，依赖描述与链接 | 较强，强调 sources/provenance/confidence |
| 主要读者 | 未来的自己、人类使用者 | 人类 + LLM/Agent 共同使用 |

## 一致之处

两者都反对碎片化堆积。HXC Vault 的“一棵树一张嘴”和 llm-wiki 的 canonical page 思想一致：一个概念应有一个主解释页，其他地方用链接引用。

因此，清理 `经营维度`、`战略维度`、`指标设计` 等重复概念，与 Karpathy 思想同向。

## 冲突之处

冲突主要发生在 `02-管理-课题`。

如果 `02-管理-课题` 只是领域目录里的研究主题入口，问题不大；但如果它承载资料、案例、辨析、来源、问题回答、版本演进，就已经接近 llm-wiki 场景。

继续塞在 `03-领域/50-管理学科/02-管理-课题` 下，会带来三个问题：

- 课题越来越深，目录层级失控。
- 来源、矛盾、版本、原始材料没有独立治理面。
- 最终沉淀页和研究过程页混在一起，降低复用质量。

## 判断

`03-领域/50-管理学科` 不应整体改成 llm-wiki。它应保留为 HXC Vault 的领域沉淀层；只有边界清晰、材料多、需要 Agent 持续编译的课题，才迁到 `---/` 下按 llm-wiki 思路组织。
