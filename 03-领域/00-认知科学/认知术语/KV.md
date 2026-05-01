---
tags: [术语, 编程, AI]
description: 缩写 KV 在编程、LLM、向量检索等领域的多重含义
type: note
create-date: 2026-05-01
---

# KV

缩写 KV 在不同领域有不同含义，需根据上下文消歧。

## 计算机科学

**Key-Value**：键值对，最基础的数据模型。

- Redis：内存 KV 数据库
- etcd：分布式 KV 存储
- 几乎所有语言内置（dict、map、HashMap）

## LLM 推理

**KV Cache**：Transformer 推理优化技术。缓存已计算的 Key-Value 注意力矩阵，避免每步重复计算。

- 显存占用 = `2 × 层数 × 头数 × 序列长度 × 头维度 × 精度`
- 长上下文场景下 KV Cache 是显存瓶颈
- 相关技术：GQA（分组查询注意力）、MLA（多头潜在注意力）

## 向量检索

**Metadata Filtering**：向量数据库中，KV 对用于预过滤。先按 metadata 条件筛选，再在子集做向量检索。

```
filter: {"category": "tech", "year": 2024}
vectors: query -> top_k 结果
```

## 其他

- 电压单位 kV（千伏），与本文无关
