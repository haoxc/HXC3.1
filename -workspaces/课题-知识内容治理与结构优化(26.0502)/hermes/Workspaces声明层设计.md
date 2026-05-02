---
aliases:
  - workspaces声明层设计
  - 声明层补缺
tags: [知识管理, 治理, 声明层, workspaces]
description: vault-rules.yaml workspaces 节的设计方案——含 pattern/date_policy/organization_modes/domain_reference/lifecycle 五字段。
type: note
create-date: 2026-05-02
---

# Workspaces 声明层设计

**结论**：`99-设置/vault-rules.yaml` 的 `---` 节当前只有 `role` + `description` + `naming.project_dir` 三字段，需补 5 个声明字段使其成为机器可校验的完整约束：`pattern`（目录结构模式）、`date_policy`（日期策略）、`organization_modes`（组织模式）、`domain_reference`（领域引用规则）、`lifecycle`（生命周期状态机）。这些字段声明后，Note Crafter（新建时校验 pattern+date）和 Vault Steward（审计时校验 lifecycle+threshold）可直接读取。

## 论点 1：pattern 声明 workspaces 的标准目录层次结构

**论点**：workspaces 有三层标准结构——主题目录 → 课题目录 → 课题目录内容。每层有各自的命名规则和约束，声明后脚本可校验 new 和 rename 操作。

**论据**——三层结构：

```
---/-workspaces/
├── {主题}课题/                    ← L1: 主题目录
│   ├── {主题}课题.md              ← L1 MOC（文件夹笔记）
│   └── 课题-{名称}[({日期})]/     ← L2: 课题目录
│       ├── 课题-{名称}.md         ← L2 MOC（课题入口）
│       ├── hermes/                ← L3: 决策子目录（可选）
│       ├── concepts/              ← L3: 编译产物（可选，llm-wiki模式）
│       ├── raw/                   ← L3: 原始材料（可选，llm-wiki模式）
│       ├── 50-管理学科整改计划/   ← L3: 子课题（可选）
│       └── z附件/                 ← L3: 本地附件
└── 止善(ZS)-课题清单/             ← L1: 项目级课题清单（特殊模式）
```

**各层命名规则**：

| 层级 | 模式 | 规则 | ✓ | ✗ |
|------|------|------|---|---|
| L1 主题目录 | `{主题}课题/` | 主题词 + 「课题」后缀 | `AI课题/` `管理课题/` | `AI项目管理/`（不是课题清单，是子课题） |
| L2 课题目录 | `课题-{名称}/` | 「课题-」前缀，名称见名知意 | `课题-知识内容治理与结构优化(26.0502)/` | `管理优化/`（缺前缀，难以区分是课题还是知识页） |
| L2 MOC | `课题-{名称}.md` | 与目录同名 | `课题-知识内容治理与结构优化(26.0502).md` | `入口.md` `README.md` |
| L3 决策子目录 | `hermes/` | 固定名，含 `hermes.md` 时间线 MOC | `hermes/hermes.md` | `决策记录/` `agent-logs/` |
| L3 附件 | `z附件/` | 固定名，存放 SVGs/图片/文档 | `z附件/架构图.svg` | `附件/` `assets/` `images/` |

**论据**——当前实际目录中的反例（违反 pattern）：

- `止善(ZS)-课题清单/ZS平台-ZS数字化三维智能管理分析与设计(26.0116)/--/` — L2 下出现 `--/`（无意义目录名），嵌套过深
- `止善(ZS)-课题清单/` — 不遵循 `{主题}课题/` 模式，是项目级清单的特殊命名

**材料**：`---/-workspaces/` 目录实际结构（50 子目录）；[[课题目录建构规则]] L1 推荐主题目录

---

## 论点 2：date_policy 声明日期前缀的触发条件与格式

**论点**：课题目录默认不加日期，只在三种场景触发加日期前缀。日期格式固定为 `(YY.MMDD)`，与治理台账日期格式一致。

**判据表**：

| 场景 | 加日期？ | 格式 | 示例 |
|------|----------|------|------|
| 长期研究课题（默认） | 否 | — | `课题-Agent技术能力边界/` |
| 会议驱动/短期冲刺 | 是 | `(YY.MMDD)` | `课题-1月战略会复盘(26.0115)/` |
| 阶段性调研（有明确结束时间） | 是 | `(YY.MMDD)` | `课题-UE引擎竞品调研(26.0310)/` |
| 日期不确定 | 否 | — | 创建时不加，后续若明确可重命名（少做） |

**反例**：
- 不加日期的默认选择是有意的——创建时无法判断是短期还是长期，加了日期后再删除比不加后再补更麻烦
- 不应该所有课题都加日期——日期前缀使课题在文件列表中按时间而非主题排列，破坏主题聚合

**格式规则**：
- 日期放在课题名后，括号包裹：`课题-{名称}(YY.MMDD)/`
- 不加连字符分隔符（不是 `YY-MM-DD`），以区分项目目录的 `YYYY-MM-DD-项目名/` 格式
- 日期不可省略年份（`0502` 会产生歧义）

**材料**：`99-设置/vault-rules.yaml` naming.project_dir（现有 `YYYY-MM-DD-项目名/` 规则）；[[课题目录建构规则]] 日期默认不加原则

---

## 论点 3：organization_modes 声明课题目录内部的两种组织模式

**论点**：课题目录内部有两种合法组织模式——普通模式（自由目录）和 llm-wiki 嵌入模式（三要素签名）。模式在新建时声明于 MOC frontmatter 的 `org_mode` 字段。

**论据**——两种模式：

### 模式 A：普通模式（默认）

```
课题-{名称}/
├── 课题-{名称}.md          ← MOC
├── {任意子课题}/             ← 自由组织
├── hermes/                   ← Hermes Agent 决策记录
└── z附件/                    ← 本地附件
```

- 适用：单一主题、材料来源≤3、不需要实体/概念分离
- 判据：课题复杂度低，不需要追踪多源材料的 provenance

### 模式 B：llm-wiki 嵌入模式

```
课题-{名称}/
├── 课题-{名称}.md          ← MOC，org_mode: llm-wiki
├── SCHEMA.md                ← 三要素签名（实体/概念/原始材料）
├── raw/                     ← 原始材料归档
├── entities/                ← 提取的实体页
├── concepts/                ← 编译的知识页
├── hermes/
└── z附件/
```

- 适用：多源材料、需要实体/概念分离、需要来源追溯
- 判据：材料来源≥3 且有交叉验证需求 OR 需要脱敏处理 OR 预计产出 canonical 知识页
- 三要素签名见 `pjx-common-auditor` v2.7.0 的 llm-wiki lint 集成

**模式选择决策表**：

| 条件 | 选模式 A | 选模式 B |
|------|----------|----------|
| 材料来源数 | ≤2 | ≥3 |
| 需要实体/概念分离 | 否 | 是 |
| 需要 provenance 追溯 | 否 | 是 |
| 预计产出 canonical 页 | 0-1 | ≥2 |

**材料**：`pjx-common-auditor` v2.7.0 llm-wiki lint 审计；llm-wiki 三要素签名 SCHEMA.md

---

## 论点 4：domain_reference 声明课题与领域层的链接规则

**论点**：课题与领域层的链接是单向的——领域层可链接课题入口页（服务于来源追溯），但不应链接课题过程碎片（raw/log/临时分析）。链接决策按 4 种场景分别判断。

**论据**——4 场景判断表：

| 场景 | 领域→课题链接 | 课题→领域链接 | 理由 |
|------|:---:|:---:|------|
| 稳定知识已可独立理解 | ✗ | ✓ | 领域层已完成沉淀，过程链接增加噪音 |
| 结论仍需来源追溯 | ✓（仅课题入口） | ✓ | 正文底部加「形成来源：[[课题入口]]」 |
| 课题仍在推进，知识未稳定 | ✗ | ✓ | 未成熟判断不应污染知识层 |
| 领域 MOC 需提示研究方向 | ✓（课题索引链接） | — | MOC 的「研究课题」分组列出活跃课题 |

**反例**：
- MOC 退化：如果领域 MOC 大量链接课题入口而非知识页，MOC 从知识地图退化为项目进度入口 → 限制每个领域 MOC 的课题链接 ≤5 条
- 循环引用：领域层 → 课题入口 → 课题层 raw → 领域层 → … → 断链策略：只允许一层深度，不链向 raw/ 和临时分析页

**材料**：[[课题目录建构规则]] 领域层引用边界节

---

## 论点 5：lifecycle 声明课题的状态机与转换规则

**论点**：课题有 5 种状态——active / completed / needs_transfer / archived / merged_to_domain。状态通过 frontmatter `status` 字段声明，转换需满足前置条件。

**论据**——状态机：

```
                    ┌──────────────────────────┐
                    │                          │
                    ▼                          │
  active ──→ completed ──→ needs_transfer ──→ merged_to_domain
    │            │
    │            └──→ archived
    │
    └──→ archived（直接归档，未完成）
```

| 状态 | 含义 | 前置条件 | 转换触发 |
|------|------|----------|----------|
| `active` | 课题正在推进 | — | 新建课题（默认） |
| `completed` | 课题工作完成，产出已稳定 | 课题入口标记完成 + 产出物清单齐全 | 用户标记 |
| `needs_transfer` | 产出稳定但未提炼入领域层 | Knowledge Transfer 评分 ≥8 但未执行 | Steward 审计发现 |
| `archived` | 课题已归档（未转入领域或放弃） | 标记归档日期 + reason | 用户确认 or Steward cron（>6 个月 inactive） |
| `merged_to_domain` | 课题产出已提炼入领域层 | Transfer 执行完成 + 领域层 canonical 页已创建/更新 | Transfer 完成后自动设置 |

**状态校验规则**（声明层可审计）：

| 校验项 | 触发条件 | 动作 |
|--------|----------|------|
| active >6 个月无修改 | Steward cron | 标记 `status: needs_review`，提醒用户 |
| completed 但无产出物清单 | Steward 审计 | 标记警告，需补充 `deliverables` frontmatter 字段 |
| needs_transfer 但未评分 | Steward 审计 | 自动评分（如果 Transfer skill 可用），否则提醒 |
| archived 但有活跃 Wikilink 引用 | Steward 审计 | 标记断链风险 |

**材料**：[[课题知识转入领域知识的判定标准]]（5 条件评分表）转层判定

---

## 当前 vault-rules.yaml 补丁预览

补丁后 `---` 节从：

```yaml
"---":
    role: workspace
    description: 工作区/项目
    required: false
    naming:
      project_dir: "YYYY-MM-DD-项目名/"
```

变为：

```yaml
"---":
    role: workspace
    description: 工作区/项目；过程产物，非稳定知识
    required: false
    naming:
      topic_dir: "{主题}课题/"                  # L1 主题目录
      project_dir: "课题-{名称}[({日期})]/"      # L2 课题目录（日期可选）
      project_moc: "课题-{名称}.md"              # L2 MOC 文件名
      decision_subdir: "hermes/"                 # L3 决策子目录（固定名）
      attachment_local: "z附件/"                 # L3 本地附件（固定名）
    date_policy:
      default: no_date
      triggers:
        - meeting_driven       # 会议驱动的短期课题
        - sprint               # 有时间边界的冲刺
        - research_phase       # 阶段性调研
      format: "(YY.MMDD)"
    organization_modes:
      - mode: normal           # 默认：自由组织
        min_files: 0
        frontmatter: { org_mode: normal }
      - mode: llm_wiki         # Karpathy llm-wiki 嵌入
        min_files: 3           # SCHEMA.md + raw/ + entities/
        frontmatter: { org_mode: llm_wiki }
    domain_reference:
      max_backlinks_per_moc: 5   # 每个领域 MOC 最多链接 5 个课题入口
      max_link_depth: 1          # 只允许链接课题入口，不链 raw/log
      source_trace: footer       # 正文底部「形成来源：[[课题入口]]」
    lifecycle:
      states:
        - active
        - completed
        - needs_transfer
        - archived
        - merged_to_domain
      default: active
      audits:
        inactive_6mo: needs_review
        completed_no_deliverables: warn
        needs_transfer_unscored: auto_score_or_remind
    threshold:
      max_note_count_per_topic_dir: 500  # 主题目录 note 上限
```

---

## 完备度

| 已覆盖 | 未覆盖 |
|--------|--------|
| pattern（三层结构+命名约束） | L3 子课题目录命名规则（当前自由组织） |
| date_policy（触发场景+格式） | 旧课题日期补标策略 |
| organization_modes（普通/llm-wiki） | 模式迁移规则（普通→llm-wiki 转换路径） |
| domain_reference（4 场景+反例） | — |
| lifecycle（5 状态+状态机+审计规则） | archived→merged 跨越（如果已归档但后续决定提炼？） |
