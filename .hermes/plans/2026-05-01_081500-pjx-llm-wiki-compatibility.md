# Plan: pjx-common-auditor × llm-wiki 兼容性评估与改造

## Goal

评估 pjx-common-auditor（KV 维度）对 llm-wiki 知识库结构的兼容性；确定是否需要改造、改造到什么程度。

## Context

- pjx-common-auditor v2.6.0 目前支持两类目标：知识管理 Vault（KV-1~KV-11）和软件研发项目（PJX-1~PJX-13）
- llm-wiki 是 Karpathy 风格的类型扁平 wiki（entities/concepts/comparisons/ + raw/ + SCHEMA.md + index.md + log.md）
- 当前 HXC Vault 3.1 是主知识库，功能层级组织；无独立 llm-wiki 实例
- llm-wiki 自带完整的 lint 功能（12 项检查：orphans, broken links, index completeness, frontmatter, stale content, contradictions, quality signals, source drift, page size, tag audit, log rotation, report）

## Compatibility Assessment (completed)

```
KV-1  顶层结构        互斥   0%   HXC 功能层级 vs llm 类型扁平
KV-2  笔记质量       概念迁移 60%  句式/语气可迁移，命名/阈值冲突
KV-3  MOC质量        不适用  0%   index.md ≠ MOC
KV-4  Frontmatter    互斥   0%   字段/type 枚举完全不同
KV-5  链接质量       直接迁移 80%  Wikilink 规则适用
KV-6  文件命名       概念迁移 30%  禁止特殊字符可迁，命名体系互斥
KV-7  标签一致性     概念迁移 70%  治理原则同，声明层不同
KV-8  工作区卫生     不适用  0%   无对应目录
KV-9  交叉引用完整性 概念迁移 60%  断链检测适用，约定不同
KV-10 附件管理       概念迁移 40%  规则逻辑可迁，路径不同
KV-11 笔记效用       直接迁移 70%  通用知识管理原则

总体: 2/11 直接兼容, 5/11 需适配, 4/11 不适用
```

三个根维度不可调和：组织轴（功能层级 vs 类型扁平）、导航面（MOC vs index.md）、元数据 schema（不同字段和 type 枚举）。其余维度均从这三个根维度派生。

## Key Insight: Use-Case Complementarity (not Substitution)

讨论后确认：

- **HXC Vault** = 「我的全部知识」的容器，管广度（日记/工具/领域/商业/治理...）
- **llm-wiki** = 「一个知识域」的深度编译产物，管深度（单一主题，Agent 编译，交叉引用，矛盾管理）
- 两者不是同一抽象层级的替代品。一个知识域在「阅读摘录」阶段放 HXC 的 02-输入/，在「需要深度交叉引用」阶段才值得独立建 wiki。

## Recommended Approach: Minimal Adaptation

不要做原方案 A（完整 LW 维度嵌入 pjx）。理由：

1. llm-wiki 自带 lint 已经覆盖 wiki 级审计的 12 项检查
2. 当前无独立 wiki 实例，LW 维度无实际审计对象
3. HXC Vault 和 llm-wiki 服务不同知识阶段，强行统一审计维度制造概念混淆
4. 维护两套高度重复的规则（LW-4 ≈ llm-wiki lint broken links, LW-5 ≈ tag audit...）是负担

**替代方案**：在 pjx-common-auditor 中做最小改动：

1. **Vault Type Detection**：增加 llm-wiki 类型签名（`SCHEMA.md` + `raw/` + `entities/` 三个同时存在），用于自动识别
2. **路由逻辑**：检测到 llm-wiki 类型时，输出「检测到 llm-wiki 结构，建议使用 llm-wiki skill 的 lint 功能审计」并列出可用检查项
3. **不新增 LW 维度**：不做规则迁移，不做共享维度标注

## Step-by-Step Plan

### Phase 1: 评估结论存档

- [ ] 创建笔记 `03-领域/知识管理/llm-wiki 与 HXC Vault 互补分析.md`
  - 记录兼容性矩阵
  - 记录使用场景对比
  - 记录互补关系结论
- [ ] 创建治理台账 `07-治理/skill规范/26.0501-pjx-llm-wiki-compatibility.md`

### Phase 2: pjx-common-auditor 最小改造

- [ ] Vault Type Detection 表增加第三列（llm-wiki）
  - 特征：顶层目录 `raw/ entities/ concepts/`、核心概念 `entity concept comparison index`、入口方式 `index.md`、声明层 `SCHEMA.md`
  - 检测签名：`SCHEMA.md` + `raw/` + `entities/` 三个同时存在
- [ ] Workflow step 2 增加 llm-wiki 采样说明
- [ ] Workflow step 3 增加路由：llm-wiki → 提示使用 llm-wiki skill lint
- [ ] 版本号递增：2.6.0 → 2.7.0

### Phase 3: 验证

- [ ] 用当前 HXC Vault 路径验证：应正确识别为知识管理 Vault（不变）
- [ ] 在临时目录创建最小 llm-wiki 结构，验证类型检测
- [ ] 确认不产生误报（普通目录不会被误判为 llm-wiki）

## Files to Change

| File | Change |
|------|--------|
| `~/.hermes/skills/software-development/pjx-common-auditor/SKILL.md` | Vault Type Detection + Workflow 路由 |
| `03-领域/知识管理/llm-wiki 与 HXC Vault 互补分析.md` | 新建：评估结论笔记 |
| `07-治理/skill规范/26.0501-pjx-llm-wiki-compatibility.md` | 新建：治理台账 |

## Risks

- **签名误判**：`SCHEMA.md` 是通用文件名，可能与 llm-wiki 无关的 SCHEMA.md 冲突。缓解：用三要素联合签名（SCHEMA.md + raw/ + entities/），减少单点误判。
- **未来需求变化**：如果后续确实建了独立 wiki 且需要 pjx 统一审计入口，再考虑 LW 维度。当前不做过度设计。

## Open Questions

- 是否需要将 `scripts/generate_vault_index.py` 扩展为支持 llm-wiki 结构的索引生成？（当前不需要——llm-wiki 用 index.md 做导航，不需要额外的 YAML 索引）
- 未来如果 `~/wiki/` 和 HXC Vault 并存，pjx 审计时如何处理跨系统引用？（远期课题，不在本次范围）
