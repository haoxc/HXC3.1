---
aliases:
  - node/包管理/npm,pnpm
tags:
description:
type:
ref-url:
---
## 内容
```shell
npm config set registry https://registry.npmmirror.com

```

### pnpm
| 特性           | npm               | pnpm                |
| ------------ | ----------------- | ------------------- |
| 安装速度         | 较慢（重复下载依赖）        | 极快（复用全局依赖）          |
| 磁盘占用         | 高（每个项目重复存储依赖）     | 极低（硬链接复用）           |
| 依赖结构         | 扁平 / 嵌套混合，易出幽灵依赖  | 严格的嵌套结构，无幽灵依赖       |
| 锁文件          | package-lock.json | pnpm-lock.yaml（更精确） |
| 兼容性          | 完全兼容 Node.js 所有场景 | 兼容 99%+ npm 场景      |
| OpenClaw 优先级 | 支持，但非首选           | 推荐（源码构建优先用 pnpm）    |
