# PJX Common Auditor

{{RUNTIME_PREPEND}}

## Purpose

审计三类目标：

1. **知识管理型 Vault**（如 Obsidian 个人知识库）——目录结构、笔记质量、MOC 信息负载、Frontmatter 完整性、链接卫生、标签一致性、附件管理。
2. **软件研发项目**（Agent/Skill/Prompt 仓库、交付型文档项目）——沿用 ZS/PJX 基线标准，规则详见 `references/naming-rules.md`。
3. **llm-wiki 课题**（`---/` 下按 llm-wiki 模式组织的研究课题）——检测 SCHEMA.md + raw/ + entities/ 签名，委托 llm-wiki skill lint 审计，不套用 KV 维度。

Before auditing module structure, detect concept-scope ambiguity. If the governing object, module center, or lifecycle object is unclear, pause for cognitive alignment instead of guessing a structure.

---

## Vault Type Detection

进入审计前，先判断目标类型：

| 特征 | 知识管理 Vault | 软件研发项目 | llm-wiki 课题 |
|------|---------------|-------------|-------------|
| 顶层目录 | `01-我的/` `02-输入/` `03-领域/` | `00-总览/` `10-需求/` `20-模块/` | `SCHEMA.md` + `raw/` + `entities/`（三个同时存在） |
| 核心概念 | 笔记、MOC、标签、Wikilink | 模块、需求、ADR、发布 | entity、concept、comparison、index、provenance |
| 入口方式 | 无统一入口，按领域/检索进入 | `00-总览/00-总览.md` 全局导航 | `index.md` 分区目录 |
| 声明层 | `99-设置/vault-rules.yaml` | 项目 `01-规范/` | 课题内 `SCHEMA.md` |
| `---/` 临时工作区 | 存在（临时 workspace / 实验区，不是正式课题层） | 通常不存在 | 可能承载临时 llm-wiki 课题现场 |

判定逻辑：
- 存在 `01-我的/` 且 `02-输入/` 且 `03-领域/` → 知识管理 Vault
- 存在 `00-总览/` 且 `20-模块/` → 软件研发项目
- 同时存在 `SCHEMA.md` + `raw/` + `entities/`（三个缺一不可）→ llm-wiki 课题
  - 若该目录位于 `---/` 下 → 标注为「Vault 内嵌 llm-wiki 课题」，主 vault 部分仍用 KV 维度，课题内部委托 llm-wiki lint
  - 若该目录为独立路径（非 `---/` 子目录）→ 独立 llm-wiki 实例，全量委托 llm-wiki lint
- 两者均不匹配 → 询问用户确认项目类型
- 混合特征（如 HXC Vault 中含有 llm-wiki 课题）→ 分别审计：主 vault 用 KV 维度，课题用委托路由

---

## Workflow

1. **识别类型与范围**
   - 用户提供路径 → 检查该路径
   - 未提供 → 使用当前工作区
   - 执行 Vault Type Detection
   - 若关键概念宽泛/过载（可能影响模块命名、链接、目录边界），先要求用户陈述概念定义和意图管理对象

2. **构建结构映射**
   - 列顶层目录
   - 知识 Vault：抽样 `01-我的/` `03-领域/` `09-工具/` `---/` 下的 MOC 和笔记
   - 软件项目：确认 `00-总览/00-总览.md` 是否存在；抽样 `01-规范/` `09-治理/` `10-需求/` `20-模块/` `60-资产/`
   - llm-wiki 课题：确认 `SCHEMA.md` `index.md` `log.md` 是否存在；抽样 `entities/` `concepts/` 下的页面
   - 混合特征：对 `---/` 下每个子目录检测 llm-wiki 签名，标记哪些课题已采用 wiki 模式
   - 检查关键 Markdown 文件的 Frontmatter
   - 抽样 MOC 和跨层引用，检查引用方向是否合理

3. **按维度审计**
   - 知识 Vault → 使用 KV-1 至 KV-11 维度
   - 软件项目 → 使用 PJX-1 至 PJX-13 维度（详见 `references/naming-rules.md`）
   - llm-wiki 课题 → **委托 llm-wiki skill 的 lint 功能**（12 项检查：orphans, broken links, index completeness, frontmatter, stale content, contradictions, quality signals, source drift, page size, tag audit, log rotation, report）。不套用 KV 维度，避免类别错误（index.md ≠ MOC, entity ≠ note）。
   - 规则来源优先级：本 skill → 目标声明层（`vault-rules.yaml` / `SCHEMA.md` / `01-规范/`）→ 用户当前对话确认
   - 未定义的规则不推断为强制规则

4. **分级**
   - P1：导航断裂、引用误导、规则边界丢失、严重模块错位
   - P2：检索削弱、迁移质量降低、生命周期/引用方向模糊、可审查性受损
   - P3：表面命名偏差、低风险不一致、可选优化

5. **建议修复**
   - 优先输出源→目标路径映射表
   - 区分立即修复和可选清理
   - 不重写历史 ADR（除非用户要求）
   - 不将审计过程中的新解释直接转化为规则；先陈述缺口，请求用户确认

6. **修复后验证**
   - 使用输出中的「验证命令」重跑检查
   - 确认 P1 全部消除，P2 按用户决定处理

---

## Rule Authority

1. **声明层**：`99-设置/vault-rules.yaml` — 目录结构、命名格式、Frontmatter 字段与枚举、MOC 量化阈值、标签词表。程序可直接校验，无需扫描文件系统。
2. 本 skill 显式定义的规则（判断逻辑、分级标准、✓/✗ 对照）
3. 目标项目的 `01-规范/`（或知识 Vault 的 `CLAUDE.md` + hxc-obsidian-vault skill）
4. 当前对话中用户确认的决定

声明层与 skill 关系：
- 声明层提供数据结构（What），skill 提供判断逻辑（How / How severe）
- 声明层变更时，本 skill 的对应表项自动失效，以 YAML 为准
- skill 保留 ✓/✗ 示例和分级逻辑，因为这是操作性知识

以下情况视为**规则未定义**，不得执行、分级或实施更改：
- 三个来源均无覆盖
- 概念边界未对齐

处理未定义规则：
- 说明规则未定义
- 列出可行选项和权衡
- 请求用户确认
- 确认后再应用

处理概念边界模糊：
- 说明概念边界未对齐
- 要求用户自行定义概念（最小管理单元、包含/排除范围）
- 确认后的边界视为用户决策
- 建议将持久规则写入 `01-规范/`

---

## Audit Dimensions — Knowledge Vault

| 分组 | 维度 | 关注点 |
|------|------|--------|
| 结构 | KV-1 Top-Level, KV-6 Naming, KV-8 Hygiene | 放哪里、叫什么、是否整洁 |
| 内容 | KV-2 Note Quality, KV-11 Utility | 写得好不好、有没有用 |
| 导航 | KV-3 MOC, KV-5 Links, KV-9 Cross-Ref | 找得到、链得通 |
| 元数据/资源 | KV-4 Frontmatter, KV-7 Tags, KV-10 Attachments | 可检索、可维护 |

### 结构

#### KV-1: Top-Level Structure

> **声明层源**：`99-设置/vault-rules.yaml` § `directories` — 目录角色、是否必须、子结构约定。本表为操作性展开，冲突时以 YAML 为准。

期望顶层目录（HXC Vault 3.1 标准）：

| 目录 | 用途 | 缺失 |
|------|------|------|
| `01-我的/` | 个人信息、目标、日记、思考 | P1 |
| `02-输入/` | 阅读摘录、外部文章、信息摄入 | P2 |
| `03-领域/` | 知识领域（AI、编程、设计等） | P2 |
| `04-笔记/` | 零散笔记、待整理碎片（收件箱） | P2 |
| `05-资源/` | 资源清单、工具清单、书单 | P2 |
| `06-商业/` | 商业情报：公司档案、产品对比、市场格局、SaaS评估 | P3 |
| `07-治理/` | Vault自身治理：结构审计、MOC评估、skill规范、命名方案 | P3 |
| `09-工具/` | 具体工具使用笔记 | P2 |
| `10-归档/` | 过时/不再维护的笔记 | P2 |
| `98-附件/` | 图片、PDF 等静态资源 | P2 |
| `99-设置/` | 配置、模板、系统设置 | P2 |
| `---/` | 临时工作区、实验区、短期 workspace；不是正式课题层 | P3 |
| `z附件/` | 额外附件暂存 | P3 |

| 规则 | ✓ | ✗ |
|------|---|---|
| 工具操作笔记进 `09-工具/` | `09-工具/git-rebase.md` | `03-领域/git-rebase.md` |
| 领域原理进 `03-领域/` | `03-领域/RAG 架构.md` | `09-工具/RAG 架构.md` |
| 零散笔记进 `04-笔记/` | `04-笔记/临时想法.md` | 直接放根目录 |
| `---/` 只承载临时 workspace | `---/-workspaces/临时分析/`（有入口说明） | 将稳定领域知识长期沉积在 `---/` |
| 不得创建未定义顶层目录 | — | `07-临时/` `08-测试/` `笔记/` |

分级：
- 缺少 `01-我的/`：P2（个人内容分散，检索不便）；若同时缺日记/周期笔记目录 → P1
- 缺少 `03-领域/` 或 `09-工具/`：P2（核心知识维度缺失）
- 缺少 `06-商业/` 或 `07-治理/` 或 `---/` 或 `z附件/`：P3（非必要维度，可后续创建）
- 顶层存在未定义目录：P2（污染检索命名空间）
- 笔记放置错误（领域原理在工具目录）：P2

`07-治理/` 子结构约定：主题子目录用语义名（不加数字前缀），文件用 `{yy.MMdd}-{主题}.md`，含 `_MOC_治理.md` 索引。

### 内容

#### KV-2: Note Quality

引用 `CLAUDE.md` 笔记风格规范。审计以下子维度：

**标题质量**

| 规则 | ✓ | ✗ |
|------|---|---|
| 见名知意，不加冗余词 | `PostgreSQL 索引优化` | `关于 PostgreSQL 索引的一些优化方法` |
| 名词为主，动作用动名词 | `环境配置指南` | `如何配置环境` |

**长度控制**

| 规则 | 量化 | ✓ | ✗ |
|------|------|---|---|
| 核心结论在前 15 行内 | 不滚动即见结论 | `**结论**：选 Redis。`（第 3 行） | 前言铺垫 30 行才入正题 |
| 超过 80 行考虑拆子页面 | 行数 > 80 → 标记 P2 | 80 行内收束 | 150 行无子页面链接 |
| 展开细节用 `## 细节` 收束 | 二级标题折叠 | `## 细节` 后跟详细内容 | 全文平铺无层次 |

**句式**

| 规则 | ✓ | ✗ |
|------|---|---|
| 陈述句，直接下结论 | `该方案覆盖三个场景。` | `我认为这个方案可能比较合适。` |
| 每个结论自带理由 | `选 Redis：内存操作 < 1ms，比 PG 快两个数量级。` | `选 Redis 比较好。` |
| 禁止口语化 | `性能显著优于方案 B。` | `方案 A 简直秒杀方案 B。` |
| 禁止情绪化词语 | `覆盖率 95%。` | `这个结果太惊人了！` |

**结论段模板**（技术决策/分析型笔记适用）

| 规则 | ✓ | ✗ |
|------|---|---|
| 三段式（结论+理由+出处） | `**结论**：选 Redis。\n**理由**：内存 < 1ms；原生 TTL。\n**出处**：Redis 7.0 benchmark，2024-03。` | `我建议用 Redis，因为快且支持过期。` |

> 日记和纯罗列型笔记不适用此模板。

**语气**

| 规则 | ✓ | ✗ |
|------|---|---|
| 冷静精确，如给一年后的自己留纸条 | `PyTorch 2.0 起 torch.compile() 替代大部分手动优化。` | `PyTorch 现在超级好用，强烈推荐升级！` |
| 中文为主，英文术语括号保留 | `智能体(Agent)通过规划(Planning)选择工具。` | `Agent 通过 planning 来选择 tools。` |
| 不加感叹号 | `注意：API 有速率限制。` | `注意！！！` |

**结尾**

| 规则 | ✓ | ✗ |
|------|---|---|
| 写完了就停 | 最后一个事实结束即止 | 加 "总之..."、"综上所述..." |
| 不要「总结」段（总结页除外） | 正文结束 | `## 总结\n\n通过以上分析可以看出...` |

分级：
- 情绪化/口语化词语：P3
- 核心结论不在前 15 行：P2（降低扫描效率）
- 无理由的断言式建议：P2（不可审查）
- 超过 80 行未拆分且无子页面链接：P2

### 导航

#### KV-3: MOC Quality & Information Load

MOC 定位：**导航表面**，非管理连续性记录。回答：此区域拥有什么、不拥有什么、稳定入口在哪、上游上下文去哪找。

> **规模敏感**：MOC 的审计严格度与 Vault 笔记总量正相关。
> - 笔记 < 200：MOC 规则降一级（P1→P2，P2→P3），仅文件夹笔记命名和 `type: moc` 保持原级。小规模下全文搜索比翻 MOC 快，MOC 维护成本可能高于收益。
> - 笔记 200–500：按默认规则审计。
> - 笔记 > 500：MOC 正文过载类规则自动升一级（P2→P1）。大 Vault 中 MOC 的导航价值放大，信息过载的代价随之上升。

| 规则 | ✓ | ✗ |
|------|---|---|
| 命名：文件夹笔记 `{目录名}.md`，放目录内 | `03-领域/AI/AI.md` | `_MOC_AI.md` `03-领域/AI/index.md` |
| Frontmatter `type: moc` | `type: moc` | `type: note` 或无 type |
| 至少一个 `##` 分组标题 | `## CLI 工具\n- [[git]]` | 只有平铺列表无分组 |
| 禁止长篇正文 | 仅链接 + 简短描述（≤2 句/条） | 在 MOC 中写教程正文 |
| 禁止进度日志 | 进度放管理/日记 | MOC 中记录 "已完成 X，待做 Y" |
| 禁止决策记录 | 决策放 `09-治理/` | MOC 中记录 "我们决定用 X 因为 Y" |
| 禁止复制标准正文 | 链接到 `01-规范/` | MOC 中粘贴完整规范条款 |
| 过渡说明 ≤ 2 句 | `本目录保存 X；Y 回到 Z。` | 三段落解释为什么目录这样设计 |
| 语气冷静专业 | 精确、直接、低修饰 | 宣传性、自我指涉措辞 |
| 禁止下游深层文件链接 | MOC 只链当前层 + 直接上游 | MOC 链到 `模块A/开发/具体实现.md` |

量化阈值：
- MOC 正文（不含链接列表）> 20 行 → P2 信息过载
- MOC 链接数 > 40 → P2（考虑拆分子 MOC）
- MOC 中进度/决策/日志类内容 > 0 行 → P2

分级：
- MOC `type` 非 `moc`：P2
- MOC 正文 > 20 行：P2；> 50 行：P1（严重影响导航效率）
- MOC 包含下游深层文件链接：P2（创建竞争检索路径）
- 无分组 MOC：P3

### KV-4: Frontmatter Completeness

> **声明层源**：`99-设置/vault-rules.yaml` § `frontmatter` — 必填字段、type 枚举、日期格式。本表为 ✓/✗ 判断参考。

每篇笔记必须包含以下四字段：

```yaml
---
tags: [分类标签]
description: 一句话说明核心内容
type: note  # note | moc | log | reference | template
create-date: YYYY-MM-DD
---
```

| 规则 | ✓ | ✗ |
|------|---|---|
| 四个字段全部存在 | `tags: [AI]` `description: "..."` `type: note` `create-date: 2026-04-30` | 缺少 `description` 或 `create-date` |
| `type` 值在枚举内 | `note` `moc` `log` `reference` `template` | `article` `tutorial` `draft` `journal` |
| `tags` 非空数组 | `[AI, 教程]` | `[]` 或 `tags:`（无值） |
| `description` 非空且有意义 | `PostgreSQL 索引类型与选择策略` | `笔记` `待补充` `` |
| `create-date` 格式 YYYY-MM-DD | `2026-04-30` | `2026-4-30` `2026/04/30` `昨天` |

type 枚举：

| type | 用途 | 误用 |
|------|------|------|
| `note` | 普通知识笔记 | MOC 标为 note |
| `moc` | Map of Content 导航页 | 普通笔记标为 moc |
| `log` | 日志/记录类（日记、会议） | 知识笔记标为 log |
| `reference` | 外部参考资料摘录 | 自己写的分析标为 reference |
| `template` | 模板文件 | 普通笔记标为 template |

分级：
- 缺少 `type` 或 `create-date`：P2
- 缺少 `tags` 或 `description`：P3
- `type` 不在枚举内：P2
- `type` 与实际用途不匹配：P2（MOC 标为 `note` → P2）
- 所有字段缺失（无 frontmatter）：P2（存量笔记）；新笔记 → P1

### KV-5: Link Quality & Wikilink Hygiene

| 规则 | ✓ | ✗ |
|------|---|---|
| 使用 Wikilink 格式 | `[[Transformer 架构]]` | `[Transformer](Transformer.md)` |
| 首次出现时链接，同篇不重复 | 开头 `[[向量检索]]` 一次 | 每个段落都 `[[向量检索]]` |
| 链接文本 = 目标笔记标题 | `[[RAG 架构]]` | `[[RAG 架构\|这里]]`（无意义重命名） |
| 别名仅用于消歧义或语法需要 | `[[Python\|Python 语言]]`（消歧义） | `[[Python\|点我]]`（美化） |
| 链接指向存在的笔记 | `[[存在的笔记]]` → 文件存在 | `[[不存在的笔记]]` → 断链 |
| 附件用 Wikilink 引用（非裸路径） | `[[架构图.png]]` | `![](98-附件/架构图.png)` |

分级：
- 断链（指向不存在的笔记）：P2；知识库核心笔记断链 → P1
- 重复链接（同篇 > 3 次同一目标）：P3
- 无意义别名：P3
- 使用 Markdown 链接代替 Wikilink（内部笔记）：P3
- 附件使用裸路径而非 Wikilink：P2（Obsidian 无法渲染/跟踪）

### KV-6: File Naming

> **声明层源**：`99-设置/vault-rules.yaml` § `naming` — 格式模板（MOC、项目目录、日记/周报/月报）、禁止字符。本表为 ✓/✗ 判断参考。

| 规则 | ✓ | ✗ |
|------|---|---|
| 文件名 = 笔记标题（中文） | `PostgreSQL 索引优化.md` | `pg-idx-opt.md` |
| MOC 用文件夹笔记 `{目录名}.md` | `03-领域/AI/AI.md` | `_MOC_工具.md` `MOC-工具.md` |
| 临时 workspace 命名说明主题，日期按需确认 | `课题-知识内容治理与结构优化(26.0502)/` | `新建文件夹/` `方案/` |
| 日记命名 | `日记-2026-04-30.md` | `2026-04-30.md` `日记430.md` |
| 周报命名 | `周报-2026-W18.md` | `第18周周报.md` |
| 月报命名 | `月报-2026-04.md` | `4月总结.md` |
| 避免空格和特殊字符 | `环境配置指南.md` | `环境 配置 指南.md` |
| 附件目录统一 `z附件` | `工具-Obsidian/z附件/` | `工具-Obsidian/附件/` `zAttachments/` |

分级：
- MOC 不用文件夹笔记命名：P2
- 临时 workspace 主题不清：P3；长期沉积稳定知识不回流：P2
- 日记/周期笔记命名不符格式：P2
- 文件名含空格或特殊字符：P3（macOS 可用但降低 CLI 兼容性）
- `z附件` 变体（`附件` `zAttachments`）：P2

### KV-7: Tag Consistency

> **声明层源**：`99-设置/vault-rules.yaml` § `tags` — 完整标签词表（领域、类型、状态、工具、人员格式）。本表为 ✓/✗ 判断参考。

使用推荐标签词表（详见 hxc-obsidian-vault skill 的「标签分类体系」）：

| 规则 | ✓ | ✗ |
|------|---|---|
| 领域标签用推荐前缀 | `AI-LLM` `编程-Python` | `大模型` `py`（非标准缩写） |
| 类型标签用推荐词 | `教程` `速查` `对比` | `howto` `cheatsheet` |
| 状态标签用推荐词 | `草稿` `已审阅` `过时` | `wip` `done` |
| 人员标签格式 `人员/xxx` | `人员/zs` | `zs` `@zs` |
| 组合示例匹配预期 | `[AI, AI-Agent, 教程, hermes]` | `[ai, agent, howto]` |

分级：
- 使用非推荐标签且无一致替代体系：P3
- 标签中英文混用且无规律：P3
- 同一概念用多个标签变体（如 `AI-agent` `ai-agent` `Agent`）：P2

### KV-8: Work-Area Hygiene

| 规则 | ✓ | ✗ |
|------|---|---|
| `04-笔记/` 作为收件箱，不应堆积 | < 30 篇待整理 | > 100 篇堆积超过 3 个月 |
| `10-归档/` 笔记已明确过时 | 归档条目含归档原因/日期 | 仅移动不加说明 |
| `---/` 下临时 workspace 有入口说明 | `---/-workspaces/课题-X/课题-X.md` | 目录内只有散文件 |
| 已完成 workspace 完成回流 | 稳定知识 → `03-领域/`；规则决策 → `07-治理/`；过程保留或归档 | 稳定结论长期只留在 `---/` |

分级：
- `04-笔记/` 堆积 > 50 篇且无近期整理痕迹：P2
- `---/` 下临时 workspace 无入口说明 > 3 个：P2
- 明显过时内容未归档（> 1 年未更新且不再适用）：P3

### KV-9: Cross-Reference Integrity

> **声明层源**：`99-设置/vault-rules.yaml` § `cross_reference` — 发现路径定义、孤儿阈值、SVG 配套要求。本表为 ✓/✗ 判断参考。

| 规则 | ✓ | ✗ |
|------|---|---|
| 无断链（Wikilink 目标存在） | 所有 `[[...]]` 可解析 | `[[已删除的笔记]]` 指向空 |
| SVG 文件有同名 .md 说明页 | `架构图.svg` + `架构图.md` | 只有 `架构图.svg` 无配套 |
| SVG 配套 .md 的 `type: note` | `type: note` | `type: moc` 或无 type |
| 核心 MOC 中的链接全部可达 | `grep '\[\[' _MOC_AI.md` 全部存在 | MOC 中有断链 |
| `---/` 项目有入口索引 | 项目目录下有 README 或入口 MOC | 项目目录只有散文件 |
| 笔记至少有一条发现路径 | MOC 引用 / 反向链接 / 有意义的 tags 三者有其一 | 零 MOC 引用 + 零反向链接 + tags 为空或仅 `[]` |

分级：
- 断链（任何笔记间）：P2
- MOC 中链接断链：P1
- SVG 缺配套 .md：P2
- `---/` 下项目无入口索引：P3
- 零发现路径（无 MOC + 无反向链接 + 无有效 tags）：P2；> 500 笔记时 P1

### KV-10: Attachment Management

> **声明层源**：`99-设置/vault-rules.yaml` § `attachments` — 大文件阈值、目标路径、Git 策略。本表为 ✓/✗ 判断参考。

| 规则 | ✓ | ✗ |
|------|---|---|
| 附件目录统一 `z附件`（非根级附件归 `98-附件/`） | `工具-CLI/z附件/screenshot.png` | `工具-CLI/附件/` `工具-CLI/assets/` |
| 大文件（≥10MB）归入 `98-附件/` | `98-附件/01-项目音视频记录/proj/video.mp4` | 留在项目目录内 |
| `98-附件/` 由 .gitignore 排除 | Git 只提交索引 .md | 附件直接推入 Git |
| 移动大文件后原位置创建 Wikilink 占位 | `[[screenshot.png]]` 指向新位置 | 移动后断链 |

分级：
- 附件目录使用变体名（`附件` `zAttachments`）：P2
- ≥10MB 文件在 Git 跟踪路径内（非 98-附件/）：P1（GitHub 推送阻塞）
- 附件移动后无占位链接：P2

### KV-11: Note Utility — Goal-Driven vs Passive Collection

核心原则：笔记是用来用的——决策、理解、创作。纯信息囤积产生噪音。

**用途可识别**

| 规则 | ✓ | ✗ |
|------|---|---|
| description 表明笔记用途/回答的问题 | `description: 对比 Redis 与 Memcached 的适用场景与选型边界` | `description: Redis 笔记` `description: 待补充` |
| 教程/操作型笔记含可执行步骤 | 命令 + 预期输出 + 常见错误 | "用 Docker 部署" 无任何命令 |
| 对比/选型型笔记含明确结论 | 推荐方案 + 理由 + 边界条件 | 列 5 个方案不表态 |

**加工深度**

| 规则 | ✓ | ✗ |
|------|---|---|
| `02-输入/` 摘录含个人批注或 outgoing link | "原文：...\n\n我的理解：这适用于小团队但大团队需要 X" | 纯粘贴，无任何个人文字 |
| `04-笔记/` 半加工内容定期向成型目录迁移 | `04-笔记/` 内容 < 50 篇，近期有迁移 | > 100 篇堆积无迁移 |
| 成型知识笔记自包含（单篇可独立理解） | 术语在文中定义或链接到定义页 | 依赖读者已知 3 篇前置笔记才可读 |

**输入→产出链接**

| 规则 | ✓ | ✗ |
|------|---|---|
| `02-输入/` 笔记含到产出笔记的链接 | `基于此摘录的分析见 [[RAG 架构选型]]` | 摘录孤立，无任何 outgoing link |
| 一篇输入可链向多篇产出（一对多） | 一篇论文摘录 → [[方案A]] [[方案B]] | — |

分级：
- `02-输入/` 纯粘贴无加工 > 10 篇：P3（噪音积累，检索稀释）
- `02-输入/` 笔记 > 20 篇且零 outgoing link：P2（输入与知识体系完全断裂）
- `04-笔记/` > 100 篇且 > 3 个月无迁移：P2（收件箱退化为垃圾场）
- 教程/操作笔记无可执行步骤：P2（不可用）
- 选型笔记无结论：P3（信息罗列，未完成思考）
- 成型笔记不自包含（需读 N 篇前置才能理解）：P3（模块化不足）

---

## Audit Dimensions — llm-wiki Topic (Delegation)

> **核心原则**：llm-wiki 与 HXC Vault 是互补关系，非替代关系。HXC Vault 管广度（多域混杂），llm-wiki 管深度（单一知识域的编译产物）。`---/` 下的课题天然适合 llm-wiki 模式。不将 KV 维度套用到 llm-wiki 结构上——这会产生类别错误（把 index.md 当 MOC 审计、把 entity 当 note 审计）。

### 检测签名

**必要条件**（三个全满足才判定为 llm-wiki 课题）：

| 文件/目录 | 角色 | 为何是签名 |
|-----------|------|-----------|
| `SCHEMA.md` | 声明层：约定、标签分类、页面阈值 | llm-wiki 独有的自文档化入口 |
| `raw/` | 不可变源材料层 | 与 HXC `02-输入/` 的摘录模式不同 |
| `entities/` | 实体页面 | 类型扁平的核心目录之一 |

单有 `SCHEMA.md` 不够（可能是其他工具），单有 `entities/` 不够（可能是普通目录命名）。

### 路由规则

| 场景 | 审计方式 |
|------|----------|
| `---/课题名/` 含 llm-wiki 签名 | 课题内部 → 委托 llm-wiki skill lint（12 项）；课题与主 vault 的交叉引用 → KV-9（断链检测） |
| 独立 `~/wiki/` 路径 | 全量委托 llm-wiki skill lint |
| `---/课题名/` 不含 wiki 签名 | 按 HXC 临时 workspace 规则（KV-8 工作区卫生：入口索引、完成后回流） |

### 委托时的输出约定

审计到 llm-wiki 课题时，输出格式与  KV/PJX 统一（P1/P2/P3 分级），但问题来源标注 `[llm-wiki lint]`：

```markdown
**llm-wiki 课题：---/领域-智能体调研/**

- [P1] 3 broken wikilinks in concepts/agent-architecture.md
  - Evidence: [[non-existent-page]] → 目标不存在
  - Fix: 创建缺失页面或修正链接目标
  - Source: llm-wiki lint → broken wikilinks

- [P2] index.md 缺少 2 个 entities/ 页面的条目
  - Evidence: entities/new-company.md, entities/new-model.md 不在 index.md 中
  - Fix: 按字母序添加到 index.md 的 ## Entities 节
  - Source: llm-wiki lint → index completeness
```

### 不做什么

- ✗ 不给 llm-wiki 页面套 KV-4 frontmatter 规则（字段和 type 枚举完全不同）
- ✗ 不给 entities/ 套 KV-6 命名规则（en-lowercase vs 中文标题）
- ✗ 不给 index.md 套 KV-3 MOC 规则（分区目录 ≠ 文件夹笔记）
- ✗ 不将 raw/ 目录标记为「应迁移到 02-输入/」（raw/ 不可变是设计意图）

---

## Audit Dimensions — Software R&D Project

| 维度 | 编号 | 说明 |
|------|------|------|
| Top-Level Structure | PJX-1 | `00-总览` 必须存在；`00-总控` 已弃用 |
| Requirements Management | PJX-2 | `10-需求/` 结构与台账 |
| Management vs Module | PJX-3 | `10-管理/` vs `20-模块/{module}/` |
| Standards vs Governance | PJX-4 | `01-规范/` vs `09-治理/` |
| Decision Records vs Indexes | PJX-5 | ADR 源记录 vs 管理摘要 |
| Temporary Collaboration | PJX-6 | `05-协同/` 角色 |
| Module Naming | PJX-7 | `{module}-{topic}.md` |
| Management Naming | PJX-8 | `PLAN-0001-*` `TASK-0001-*` |
| Governance Naming | PJX-9 | `ADR-0001-*` `CR-0001-*` |
| Lifecycle Reference Direction | PJX-10 | 上下游引用方向约束 |
| MOC Information Load | PJX-11 | 软件项目 MOC 规范 |
| Work-Product Role Separation | PJX-12 | 交付物 vs 过程记录 vs 外发 |
| Obsidian Retrieval | PJX-13 | Frontmatter + 生命周期别名 |

### 关键规则速查

**00-总览 是唯一标准入口**（`00-总控` 已弃用）：

| 规则 | ✓ | ✗ |
|------|---|---|
| 默认入口目录 | `00-总览/` | `00-总控/` `00-MOC/` |
| 默认入口笔记 | `00-总览/00-总览.md` | `00-总览/index.md` |
| 入口角色：全局导航，非正文存储 | 项目简介 + 目录导航 + 角色说明 | 进度表、会议记录、详细正文 |

**09-治理 是默认治理证据目录**（`02-治理` 仅遗留项目兼容）：

| 规则 | ✓ | ✗ |
|------|---|---|
| ADR 源记录位置 | `09-治理/20-决策记录/ADR-0001-*.md` | `02-治理/20-决策记录/` `10-管理/60-决策索引/` |
| 决策索引位置 | `10-管理/60-决策索引.md`（链接到 09-治理） | 在决策索引中存储 ADR 正文 |

**第三层及更深目录禁止数字前缀**：

| 规则 | ✓ | ✗ |
|------|---|---|
| 第三层用语义名 | `20-模块/{module}/设计/` | `20-模块/{module}/20-设计/` |
| 证据包目录用 `{topic}-{yy.MMdd}` | `接口治理/场景资源统一接口/规划/V001-26.0417` | `26.0417-接口治理/V001` |

详细规则、反例和分级标准见 `references/naming-rules.md`。

---

## Skill Governance Tracking

每次修改任何 skill（本 skill 或其他 skill）后，必须在 Vault 治理目录创建整改台账笔记，用于复盘 skill 演进。

**台账路径**：`07-治理/skill规范/{yy.MMdd}-{主题}.md`

**台账模板**：
```yaml
---
tags: [治理, skill]
description: {一句话变更摘要}
type: log
create-date: YYYY-MM-DD
---

# {标题}

## 变更背景
为什么需要这次变更。

## 变更内容
- 具体修改项
- 涉及文件和版本号

## 设计决策
关键取舍和理由。
```

**触发条件**（任一满足）：
- skill 版本号变更
- 规则表/维度新增或删除
- 声明层 `vault-rules.yaml` 变更
- 命名约定或目录结构变更
- 跨 skill 一致性修复

**台账价值**：复盘 skill 演进路径，追溯设计决策上下文，避免未来回退到已弃用方案。

> 本 skill 自身的版本历史台账见 `07-治理/skill规范/` 下的 `26.0501-pjx-common-auditor-v2.0.md` 和 `26.0501-vault-rules-declaration-layer.md`。

## Upward Routing To HXC Model Auditor

当用户请求主要涉及**管理模型本身**而非项目结构时，路由到 `hxc-model-auditor`：

- 管理对象不明确或问题需先分析提炼为课题
- 课题驱动管理、课题生命周期、课题进入机制
- 管理模型成熟度
- 信息负载审计、精益/极简治理、文档负担
- 可控-可观测-可审查的过程设计
- 跨项目管理机制
- OKR、交付物、过程材料、决策、证据之间的关系

冲突规则：先保留结项所需的最小证据，再用 `hxc-model-auditor` 降低信息负载。不要让此项目型审计器将结项要求变成过度记录。

> 此路由目前仅适用于软件研发项目。知识管理 Vault 不涉及管理模型审计。

---

## Project Applicability

**知识管理 Vault**：本 skill 的 KV-1 至 KV-10 维度默认适用 HXC Vault 3.1 标准。若用户使用其他 Vault 结构（如 PARA、Zettelkasten），先确认适用的目录体系再审计。

**软件研发项目**：ZS/PJX 基线标准适用于 Agent/Skill/Prompt 仓库和文档密集型技术项目。对于其他项目类型（工程建设、咨询交付、研究、制造、销售运营、培训、硬件交付、通用业务管理），不要直接套用软件研发生命周期模型：

- 先确认项目类型
- 询问预期生命周期、主要交付物、协作模式、治理需求
- 将需求、管理、模块、资产、治理、归档等顶层角色视为可配置
- 用户确认适用模型后再审计

---

## Output Format

```markdown
**结论**
One-paragraph assessment of overall structure health.

**Findings**
- [P1/P2/P3] Finding title
  - Evidence: path and line if available
  - Why it matters: concrete impact
  - Fix: exact rename, move, or rule update

**建议调整**
| 当前 | 建议 | 原因 |
| --- | --- | --- |
| path | path | reason |

**迁移适配**
- What is reusable
- What is project-specific
- What should remain historical

**验证命令**
- Commands to rerun after changes
```

若无发现，明确说明"未发现违规"，并列出未检查的区域或残余风险。

---

## Guardrails

- 不推断或发明本 skill、项目 `01-规范/`、CLAUDE.md 中未定义的规则
- 不将默认软件研发模型套用到非软件项目（先确认类型）
- 不将未定义偏好分级为 P1/P2/P3（先确认规则）
- 不在规则未确认时实施结构变更
- 不在概念边界模糊时自行选择通用行业定义（先对齐认知）
- 不在用户确认治理对象和排除的相邻概念之前重命名模块、重写计划链接或创建生命周期别名
- 不移动或重命名文件（除非用户要求实施）
- 不让上游生命周期文件以下游文件为证据、来源、设计输入或权威
- 不向上游 MOC 添加下游深层文件导航（用入口、管理台账、治理索引或追溯矩阵做跨层导航）
- 不将 MOC 用作进度日志、决策记录、详细解释或复制的管理台账
- MOC 中过渡说明保持简短、准确、可操作
- 不因同一主题将当前交付物、源/支持资产、过程/控制记录和外发材料混在一起
- 不按文件格式分类产物（先按用途、受众和生命周期角色）
- 不合并 `01-规范/` 和默认治理证据目录 `09-治理/`
- 不为新 ZS/PJX 项目推荐 `02-治理` 或 `02-管理`（遗留/外部兼容）
- 不使用 `00-总控` 作为默认入口（已弃用，统一为 `00-总览`）
- 不将 ADR 源记录存储在管理视图（`10-管理/60-决策索引` `15-管理/60-决策`）
- 不将治理证据目录用作管理仪表板
- 不在模块内放置永久的 `05-协同/` `10-管理/` `09-治理/`
- 不将项目级业务需求并入项目管理
- 不在顶层需求层存在时使用模块级 `10-需求`（优先 `10-承接`）
- 不合并 `20-场景分析` `30-需求定义` `40-功能定义`
- 不在第三层及更深目录推荐数字前缀命名
- 不将历史 ADR 措辞视为缺陷（除非影响当前导航或当前规则）
- 不提交、推送或删除文件（除非明确请求）
- 知识 Vault 审计时，不禁用 hxc-obsidian-vault skill 的安全操作协议（批量操作需先输出计划和确认）


{{RUNTIME_APPEND}}
