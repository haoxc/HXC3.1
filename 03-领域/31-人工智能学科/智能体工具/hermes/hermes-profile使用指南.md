---
aliases:
  - Hermes Profile Guide
  - hermes多配置
  - hermes/配置/profile管理(PG, HPM)
tags: [Hermes, mac-工具, AI工具]
description: Hermes profile 的使用方法：创建、切换、管理多个独立配置的 Hermes 实例。
type: note
create-date: 2026-05-01
---

# Hermes Profile 使用指南

## 概述

Profile 允许在同一台机器上运行多个**完全独立**的 Hermes 实例——各自拥有独立的 config.yaml、.env、sessions、skills、memory。适合隔离不同项目或实验不同模型配置。

**结论**：需要隔离配置时用 profile，临时换模型用 `hermes chat -m`。

---

## 核心操作

### 创建 profile

```bash
# 从零创建
hermes profile create vault-only

# 克隆当前配置
hermes profile create dev --clone

# 克隆所有内容（config + sessions + skills + memory）
hermes profile create dev --clone-all

# 从指定 profile 克隆
hermes profile create test --clone-from vault-only
```

### 使用 profile

```bash
# 单次使用
hermes -p vault-only

# 设为 sticky 默认（后续不带 -p 也生效）
hermes profile use vault-only

# 取消 sticky
hermes profile use default
```

每个 profile 的数据目录：`~/.hermes/profiles/<name>/`

### 管理

```bash
hermes profile list          # 列出所有 profile
hermes profile show NAME     # 查看详情
hermes profile rename A B    # 重命名
hermes profile delete NAME   # 删除
hermes profile export NAME   # 导出为 tar.gz
hermes profile import FILE   # 从归档导入
```

---

## 典型场景：vault-only profile

为 Vault 笔记操作创建精简 profile，只开必要 toolsets：

```bash
# 1. 创建并克隆当前
hermes profile create vault-only --clone

# 2. 进入精简后的交互
hermes -p vault-only

# 3. 在会话中只保留核心工具
/tools    # 交互式 TUI，关闭 web/browser/vision/image_gen/tts/delegation/cronjob
          # 保留 terminal/file/skills/memory/session_search/clarify/todo
```

效果：系统 prompt 中去掉无关工具定义，减少 token 开销。

---

## 注意事项

| 项目 | 说明 |
|------|------|
| 配置隔离 | 每个 profile 有独立 `config.yaml` 和 `.env`，模型/provider/API key 完全独立 |
| API key | 不同 profile 可配不同 key，实现多账号轮换 |
| 不隔离 | 共享同一个 Hermes 安装和 Python 环境 |
| sticky 生效 | `hermes profile use X` 后，不带 `-p` 的 `hermes` 命令默认用 X |

---

## 相关

- [[hermes-模型配置]]
- [[hermes-mac安装笔记]]
