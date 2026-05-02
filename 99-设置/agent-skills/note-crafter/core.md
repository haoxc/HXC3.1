# Note Crafter

创建符合 HXC Obsidian Vault 规范的知识笔记。核心流程：命名 → 定位目录（vault-index.yaml 快速路由）→ 写内容 → 质量审查 → 挂 MOC。

> 标签词表、顶层目录角色、MOC 分组策略、大文件归档流程等详见 `99-设置/vault-rules.yaml` 和 `vault-index.yaml`。本文只保留内联必需部分。

## Vault 基本信息

| 项目 | 值 |
|------|-----|
| Vault 路径 | `/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)` |
| 声明层规则库 | `99-设置/vault-rules.yaml` — 目录角色、命名格式、Frontmatter 字段/枚举、标签词表、附件阈值的单源真相 |
| 预计算索引 | `99-设置/vault-index.yaml` — 目录结构 + 关键词路由，避免 filesystem scan |

---

{{RUNTIME_PREPEND}}

---

## Step 1: 命名

文件名 = 笔记标题。规则：

| 笔记类型 | 命名格式 | ✓ | ✗ |
|----------|---------|---|---|
| 概念定义 | `{概念名}.md` | `Transformer 架构.md` | `关于Transformer.md` |
| 工具参考 | `{工具名}-{用途}.md` | `claude-code-使用备忘录.md` | `claude-code笔记.md` |
| 操作指南 | `{对象}-{操作}.md` | `mac-cli-常用操作.md` | `CLI操作.md` |
| 规约/规则 | `{范围}-{规约名}.md` | `MOC-目录页规范.md` | `规范.md` |

- 禁止裸通用名：`方案.md`、`设计.md`、`配置.md`
- 中文为主，英文术语保留
- 稳定笔记不加日期；一次性记录加日期后缀（`-26.0501`）
- 重命名时旧名写入 frontmatter `aliases`
- **别名规则**：每篇笔记含三要素——英文主题名、中文简称、速查码 `{一级}/{二级}/{中文主题}({拼音首字母}, {英文缩写})`。一级取工具名或领域名（`hermes` / `obsidian` / `AI`），二级取功能子域（`文件操作` / `配置` / `模型架构`）。示例：`hermes/文件操作/文件模糊引用(WJMH, HFFR)`

---

## Step 2: 定位归档目录与 MOC

### 2a. 关键词提取 + 索引查询

从主题提取 2-5 个关键词，用 `vault-index.yaml` 的 `search_routing` 定位候选目录：

```python
import yaml

VAULT = "/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"
with open(f"{VAULT}/99-设置/vault-index.yaml") as f:
    idx = yaml.safe_load(f)

# 扁平化目录树
flat = {}
def walk(node):
    if isinstance(node, dict):
        p = node.get("path")
        if p: flat[p] = {k:v for k,v in node.items() if k != "children"}
        for c in node.get("children", []): walk(c)
    elif isinstance(node, list):
        for i in node: walk(i)
walk(idx["directories"])

# 关键词路由
keywords = ["Hermes", "AI"]  # ← 替换为实际关键词
routing = idx["search_routing"]
candidates = {}
for kw in keywords:
    for path in routing.get(kw, []):
        candidates[path] = candidates.get(path, 0) + 1

for path, score in sorted(candidates.items(), key=lambda x: -x[1]):
    info = flat.get(path, {})
    print(f"  {score} hits → {path}  moc={info.get('moc','NONE')}")
```

### 2b. 确认目录 + 去重

对排名最高候选：查 `flat` 中 `moc` 字段，若空则检查 `{路径}/{目录名}.md`。无现成 MOC 时 ≥2 篇相关笔记建 MOC；预判未来多篇时首篇即建。

**去重**：目标目录 grep 关键词，已有同主题笔记 → 追加或链接，不重复创建。

**归属速查**（索引无匹配时用）：

| 笔记主题 | → 目标目录 |
|----------|-----------|
| 工具 CLI 用法、配置 | `09-工具/` |
| 智能体工具 | `03-领域/31-人工智能学科/智能体工具/{工具名}/` |
| 领域原理、方法论 | `03-领域/`（search_routing 定位子目录） |
| 个人日记、反思 | `01-我的/` |
| 外部文章摘录 | `02-输入/` |
| 商业情报 | `06-商业/` |
| Vault 治理 | `07-治理/` |
| 通用术语、概念术语 | `03-领域/00-概念术语/` |
| 学科术语 | 对应 `03-领域/{学科}/` 下的现有术语目录 |
| 课题、研究问题、长期分析 | 先确认课题承载目录，不默认新建一级目录 |
| 不确定 | `04-笔记/` |

### 2c. 分类不确定时确认

触发条件：路由只到顶层目录无匹配子目录 / 多目录歧义 / 需新建子目录。

→ 推理 3 候选路径（含理由），用 `clarify` 让用户选。禁止自行 mkdir。推理优先级：① 同类笔记兄弟目录 ② 语义匹配顶层目录角色 ③ 泛化归入上层。课题类内容必须确认承载目录，不默认创建新的一级目录。

---

## Step 3: 写内容

### 3a. Frontmatter

```yaml
---
aliases:
  - 英文主题名
  - 中文简称
  - 分类/中文主题(拼音首字母缩写, 英文缩写)
tags: [领域标签1, 领域标签2]
description: 一句话说明核心内容
type: note
create-date: YYYY-MM-DD
---
```

`type` 枚举：`note` | `moc`（导航页） | `log`（日记/周报） | `reference`（外部摘录） | `template`

术语笔记固定使用 `type: note`，不得使用 `type: 术语卡片`。通用术语放入 `03-领域/00-概念术语/`；学科术语放入对应领域下的现有术语目录；课题中的临时术语表可暂存在 workspace，但完成后必须回流到 `03-领域/`。

速查码格式 `{一级}/{二级}/{中文主题}({拼音}, {英文缩写})`：一级取工具名（`hermes`/`obsidian`）或领域名（`AI`/`编程`），二级取功能子域（`文件操作`/`配置`/`模型架构`）。例：`hermes/文件操作/文件模糊引用(WJMH, HFFR)`。aliases 服务检索：中文名、英文名、缩写、必要速查路径；Wikilink alias 只用于消歧义或语法需要，不用于美化显示。

### 3b. 正文结构

**概念定义**：一句话定义 → 判断标准 → 容易混淆（表格） → 典型例子 → `## 相关`（Wikilink 列表）。

**工具参考 / 操作指南**：概述 → 核心操作（有序列表） → 常见问题（Q&A） → `## 相关`。

**规约 / 规则**：规则在前，理由在后。表格做映射，列表做判断标准。含 `✓/✗` 反例对照。

### 3c. 风格约束

- 核心结论前 15 行，不用「总结」段
- 陈述句直接下结论，禁止口语化/情绪化词语/感叹号
- 首次出现 Wikilink，链接文本=目标标题；能用表格不用段落，能用列表不用表格（≤2 维时）
- 超过 80 行考虑拆分子页面

> 完整风格规范见 `CLAUDE.md`。

---

## Step 4: 内容质量审查（6 维度）

| 维度 | 不通过标准 |
|------|-----------|
| 概念精度 | 一句话定义无法独立成立 |
| 区分度 | 漏了日常最常用的近似词 |
| 示例质量 | 例子只有一个场景 |
| 可操作性 | 方法论缺失操作指引（纯概念可省略） |
| 内部一致性 | 例子归类与概念区分冲突 |
| 表述简洁度 | 有未定义的内部术语 |

≥2 维度不通过 → 重写。

---

## Step 5: 挂 MOC 反向链接

```python
moc_path = f"{VAULT}/目标目录/MOC名.md"
note_link = "[[笔记标题]]"
with open(moc_path) as f:
    if note_link not in f.read():
        with open(moc_path, 'a') as f:
            f.write(f"- {note_link}\n")
```

验证：MOC 仍是导航页（`type: moc`），链接在正确的 `##` 分组下。

---

## Step 6: 课题创建模式

触发词：创建课题、新建课题、建立课题、课题、create topic、new topic。

核心差异：创建的是**带分层结构的目录**，而非单个 `.md` 文件。

### 6a. 目录结构（渐进式分层）

固定最小集：`课题-{主题}/` 含同名 MOC + `过程/` + `z附件/`。按需生长 `调研/`（方案对比）、`设计/`（架构设计）、`资产/`（可复用产出）——不预判层级，中途需要时再建。日期默认不写入目录名；若是短期冲刺、会议、阶段性调研，创建前确认是否加日期。

### 6b. 创建流程

1. **确认承载目录、主题与日期**：不得默认新建一级目录；从现有候选目录或用户指定目录中确认课题位置。
2. **创建最小结构**：
   ```bash
   mkdir -p "$VAULT/{已确认课题承载目录}/课题-{主题}/{过程,z附件}"
   ```
3. **生成 MOC.md**：从 `99-设置/zTemplates/课题-MOC模板.md` 加载。`category` 从枚举选：`知识管理` / `AI智能体` / `教学设计` / `工具链与基础设施` / `外部项目`。`status` 初始 `进行中`。
4. **生成首篇过程日志**：`过程/{日期}-启动.md`

MOC 分组策略（comparison/timeline/concept_hierarchy）见 `vault-rules.yaml` `moc.grouping_strategies`。

### 6c. 完成后归档

稳定知识迁至 `03-领域/`，规则与结构决策迁至 `07-治理/`，课题目录保留问题、过程、证据和知识回流记录。`---/` 只用于临时实验或短期工作现场，是否承载某个课题需由用户确认。

---

## 批量操作安全协议

批量操作前输出计划和影响清单，用 `clarify` 请求确认。用户指令「不再询问」时跳过确认但仍输出日志。

| 禁止行为 | 原因 |
|----------|------|
| 修改 `.obsidian/` | 不可逆，影响插件配置 |
| 删除附件文件（图片/PDF） | 可能破坏现有引用 |
| 写入含 secrets 的文件 | 安全风险 |
| 创建无 frontmatter 的笔记 | 违反 Vault 规范 |
| 创建无 aliases 的笔记 | 缺少多路径搜索入口，发现性差 |
| 重命名或删除 MOC 文件 | 破坏大量反向链接 |
| 跨目录移动笔记未同步更新所有引用 MOC | 导致断链 |
| 修改已有笔记 type（无明确理由+确认） | type 决定 MOC 归类逻辑 |

---

## Quality Checklist

- [ ] 文件名见名知意，离开目录上下文也能猜出内容
- [ ] 通过 vault-index.yaml search_routing 定位目录，未做全量扫描
- [ ] 去重检查通过（同目录无同主题笔记）
- [ ] Frontmatter 含 aliases（英文+中文简称+速查码）/ tags / description / type / create-date
- [ ] 笔记已挂载到对应 MOC（MOC 仍是导航页，`type: moc`）
- [ ] 内容通过 6 维度审查
- [ ] 无裸通用文件名
- [ ] 稳定笔记无日期后缀；一次性记录有

---

## Common Pitfalls

1. **跳过 vault-index.yaml 直接 find** — 先查索引再精确搜索。
2. **索引过期** — 目录变更后运行 `generate_vault_index.py`。
3. **MOC 写成文章** — MOC 只做导航，禁止长文。
4. **type 字段随意填** — `moc` 只用于 MOC 页，`note` 用于普通笔记。
5. **03-领域 深度超标** — 超过 5 层时向上合并或重新规划。
6. **frontmatter 缺少 create-date** — 四字段缺一不可。
7. **日记用旧格式 type: 日记(Diary)** — 已改为 `type: log`。
8. **工具调用过多导致慢** — 3~4 次工具调用目标 20-40s。skill_view 只加载一次，先用路由速查和 vault-index 精确读取；Hermes 终端窄屏时避免大型代码执行审计，优先 native file/terminal 的小输出检查。
9. **加载不相关的 skill** — 创建笔记时只加载本技能，除非笔记主题本身是某 skill 的使用方法。
10. **同主题笔记散落不分组** — ≥2 篇同主题建子目录（如 `07-治理/skill规范/note-crafter规范/`）；预判多篇时首篇即建。
11. **忽略研究阶段直接写内容** — 陌生主题先通过 GitHub API / curl 获取权威源信息，再进入写作。研究阶段额外 2-4 次终端调用，不计入 4 次窗口配额。
12. **子目录不确定时自行决定** — 路由只到顶层目录无现成子目录时，必须推理 3 候选 clarify 让用户选，禁止自行 mkdir。

{{RUNTIME_APPEND}}
