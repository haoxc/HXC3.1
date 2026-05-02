---
aliases:
  - PGLite WASM Bug Workaround Comparison
  - gbrain后端方案对比
  - gbrain/配置/后端迁移方案(HDQY, BMW)
tags: [课题, gbrain, 诊断, 对比]
description: 绕过 macOS 26.3 PGLite WASM bug 的两条路径对比：降级 Bun vs Docker Postgres
type: note
create-date: 2026-05-02
---

# PGLite 方案对比：降级 Bun vs Docker Postgres

**背景**：macOS 26.3 + Bun ≥ 1.3.11 导致 PGLite WASM 初始化崩溃（`ENOENT: /$bunfs/root/pglite.data`），gbrain 所有涉及 PGLite 的操作（CLI config/stats/extract/embed、MCP serve）均不可用。Bun 1.3.11 → 1.3.13 均未修复，重启 macOS 无效。

## 方案概览

| 维度 | A: 降级 Bun 1.3.10 | B: Docker Postgres + pgvector |
|------|---------------------|------------------------------|
| 机制 | 回退到 PGLite 兼容的 Bun 版本，复用现有 `.gbrain/brain.pglite` | 用 Docker 起 `pgvector/pgvector:pg16` 容器，gbrain 切到 `db.type: postgres` |
| 数据迁移 | 无需——PGLite 数据原地保留 | 需重跑 `gbrain sync`（100/3235 页进度丢失） |
| 操作时间 | ~30 秒（安装脚本） | ~10 分钟（拉镜像 + 起容器 + 建库 + 重 sync） |
| 可逆性 | 完全可逆（`bun upgrade` 回新版本） | 可逆（切回 pglite 引擎即可，但 sync 进度不同步） |
| 风险 | Bun 1.3.10 可能有其他回归 | Postgres 端口 5432 已被 LiteLLM 占用（需换端口或共用实例） |
| 长期维护 | 消极方案——Bun 迟早升级，下次可能再坏 | 积极方案——绕过 Bun/PGLite 依赖链，gbrain 官方推荐 |
| 副作用 | 降级 Bun 影响所有 Bun 项目（构建/运行） | 需维护一个 Docker 容器 + 磁盘占用（PG data ~100MB+） |

## 细节

### A: 降级 Bun 1.3.10

```
curl -fsSL https://bun.sh/install | bash -s -- bun-v1.3.10
```

**结论**：最快路径，一次性操作，PGLite 原地可用。
**理由**：Bun 1.3.10 是最后一个确认无此 bug 的版本。gbrain 数据完整，sync 进度 100/3235 保留。
**风险**：Bun 1.3.10 可能缺少 1.3.11+ 的某些修复（需排查 changelog）。下次 `bun upgrade` 会再次触发 bug。
**出处**：gbrain issue #223，skill `references/macos-wasm-bug-diagnosis.md`。

### B: Docker Postgres + pgvector

```
docker run -d --name gbrain-pg \
  -e POSTGRES_USER=gbrain -e POSTGRES_PASSWORD=xxx -e POSTGRES_DB=gbrain \
  -p 5433:5432 pgvector/pgvector:pg16
```

然后修改 `~/.gbrain/config.json`：

```json
{
  "db": {
    "type": "postgres",
    "url": "postgresql://gbrain:xxx@localhost:5433/gbrain"
  }
}
```

**结论**：根治方案，但需重建数据库。
**理由**：gbrain 设计上支持 Postgres 后端（`docs/ENGINES.md`），官方推荐千页以上 Vault 用 Postgres。绕过 Bun WASM 文件系统依赖链后不再受 Bun 版本影响。
**风险**：当前 Docker 已有一个 LiteLLM Postgres 占 5432 端口。可选方案：① 换端口（5433）独立容器；② 共用 LiteLLM 实例（在 `litellm` 数据库旁建 `gbrain` 库，需装 pgvector 扩展到 alpine 镜像）。
**出处**：gbrain AGENTS.md `docs/ENGINES.md`，skill `references/macos-wasm-bug-diagnosis.md`。

## 推荐

**选 A，先跑通流程。** PGLite 数据原地复用，sync 进度不丢失。跑通后再评估是否切 B 做长期方案。

## 相关

- [[环境诊断与阻塞记录]]
- [[重启后操作清单]]
- [[课题-跑通gbrain流程]]
