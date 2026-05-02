---
aliases:
  - "Hermes Skill Solidification Design Philosophy"
  - "skill固化设计哲学"
  - "hermes/skill设计/skill固化原则(SKGY, SSP)"
tags: [AI, AI-Agent, 设计, hermes]
description: 以 gbrain 案例说明 skill 与 memory 的分工：memory 存「是什么」，skill 存「为什么」+ 踩过的坑——只有非显而易见的决策和陷阱才值得固化。
type: note
create-date: 2026-05-02
---

# hermes-skill固化设计哲学

## 一句话定义

skill 的值不在于复述操作步骤，而在于固化「只有踩过坑才知道」的隐性知识。

---

## skill 与 memory 的分工

| 维度 | memory | skill |
|------|--------|-------|
| 存什么 | 事实（是什么） | 决策理由 + 陷阱（为什么 + 踩过什么） |
| 粒度 | 单条键值 | 结构化工作流 |
| 注入时机 | 每次会话 prompt | 按需加载（`skill_view`） |
| 更新频率 | 随时追加 | 流程稳定后一次性固化 |
| 示例 | `gbrain embedding 模型=Qwen/Qwen3-Embedding-8B` | 4 个陷阱 + 配置验证 + 编译命令 |

**边界规则**：

| 该存 memory | 该存 skill |
|------------|-----------|
| 模型名、API 端点、key 位置 | 为什么选这个模型而非其他 |
| 端口号、连接字符串 | 为什么 Docker 是唯一可行路径 |
| 工具版本号 | 中文文件名 slug 为空的变通方案及原因 |

---

## skill 固化标准（三重测试）

一条知识是否该进 skill，通过以下三问：

1. **非显而易见测试**：这条知识能从官方文档/README 直接推导吗？（是 → 不进 skill）
2. **重复踩坑测试**：如果丢失这条知识，下次是否大概率重蹈覆辙？（否 → 不进 skill）
3. **环境依赖测试**：这条知识是否依赖特定环境版本/配置组合，换环境就变？（是 → 优先进 skill）

**gbrain 案例映射**：

| 知识 | 测试1（非显然） | 测试2（重复踩） | 测试3（环境依赖） | 结论 |
|------|:--:|:--:|:--:|------|
| PGLite/WASM 不可用 | ✓ 文档没写 | ✓ 首坑即 blocker | ✓ macOS 26.3 特定 | **进 skill** |
| 中文 slug 为空 | ✓ 不是 bug 是行为 | ✓ 中文 Vault 必遇到 | ✗ 所有环境 | **进 skill** |
| embedding 维度=1536 | ✓ schema 隐式约束 | ✓ 选错不报错只返回空 | ✗ 代码硬编码 | **进 skill** |
| Docker pgvector 路径 | ✓ 排了 3 方案后结论 | ✓ 方向性错误代价大 | ✓ macOS 26.3 | **进 skill** |
| `bun build --compile` | ✗ README 有 | ✗ 不会忘 | ✗ 标准操作 | memory（工具版本） |

---

## 反例对照

| ✓ | ✗ |
|---|----|
| skill 里只写「embedding 模型必须兼容 1536 维，因为 schema 硬编码，选错不报错只返回空」 | skill 里写「执行 `gbrain embed agent` 命令嵌入页面」 |
| skill pitfalls 节写「中文文件名导致 slug 为空，需加英文前缀（如 `vec-向量检索`）」 | skill 里复述 gbrain CLI 所有子命令 |
| memory 存「模型名=Qwen/Qwen3-Embedding-8B」 | memory 存「上次 sync 成功，stats 显示 51 pages」 |

---

## 与 session_search 的协作

三层防护的调用顺序：

```
跨会话工程任务
  │
  ├─ 1. session_search 召回历史上下文
  │     └─ 输出：上次做到哪了、用户说过什么
  │
  ├─ 2. memory 加载持久化配置
  │     └─ 输出：模型名、API 端点、key 位置
  │
  └─ 3. skill_view 加载固化流程
        └─ 输出：陷阱列表、决策理由、验证步骤
```

三层各司其职：session_search 给上下文，memory 给事实，skill 给判断。

---

## 相关

- [[hermes-跨会话配置记忆复盘-gbrain案例]] — 本次复盘的事件与根因
- [[Hermes Skill 内容地图]] — skill 的全局导航
- [[Hermes-Claude-Code-Codex-Skill维护课题]] — 跨端 skill 同步
- `07-治理/skill规范/` — skill 整改台账
