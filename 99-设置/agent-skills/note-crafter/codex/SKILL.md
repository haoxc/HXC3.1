---
name: note-crafter
description: Create well-named, well-structured Obsidian knowledge notes with proper MOC integration. Use when the user asks in Chinese or English to 创建笔记, 新建笔记, 整理成笔记, 生成笔记, create note, new note, draft note, write a note, or normalize notes for knowledge management including concept definitions, tool references, how-to guides, domain summaries, and daily-note 新建 capture items.
---

# Note Crafter

创建符合 HXC Obsidian Vault 规范的知识笔记。核心流程：命名 → 定位目录（vault-index.yaml 快速路由）→ 写内容 → 质量审查 → 挂 MOC。

> 已合并原 hxc-obsidian-vault 技能。一次 skill_view 加载即可，不再需要双重加载。

## Vault 基本信息

| 项目 | 值 |
|------|-----|
| Vault 路径 | `/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)` |
| 声明层规则库 | `99-设置/vault-rules.yaml` — 目录角色、命名格式、Frontmatter 字段/枚举、标签词表、附件阈值的单源真相 |
| 预计算索引 | `99-设置/vault-index.yaml` — 目录结构 + 关键词路由，避免 filesystem scan |

---

> Merged with hxc-obsidian-vault skill. Former dual-skill loading no longer needed.
> Vault path: `/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)`
> Declarative rule base: `99-设置/vault-rules.yaml`

## Core Principles

Every note must satisfy three top-level principles, in order:

1. **见名知意** — The filename alone tells the reader what this note is and is not. No clicking required to decide relevance.
2. **辅助理解** — Content is structured for rapid comprehension: what it is, how to recognize it, how to use it.
3. **指导落地** — When the knowledge has an operational dimension, include actionable guidance. Pure reference concepts omit this.

## Execution Strategy

Target: 4 tool calls per note creation. Load only this skill — hxc-obsidian-vault is now merged in.

**Window 1** (1 call): `skill_view(note-crafter)` — this skill. Skip if already loaded in current session.

**Window 2** (1 execute_code): Use 「Route Cache」 table first (below). If keyword matches, skip vault-index.yaml. Fallback to `99-设置/vault-index.yaml` search_routing only on miss. Merge dedup + MOC read + existing note content read.

**Window 3** (1 write_file): write the note.

**Window 4** (1 execute_code): MOC backlink append + daily diary append, merged.

**Total: 4 calls (3 if route cache hits), 25-35s.**

Do NOT load unrelated skills (e.g. `hermes-agent` when creating a Hermes pitfall note — config.yaml has enough context).

### Route Cache (hit = skip vault-index.yaml read)

| Keyword contains | → Directory |
|----------|-------|
| liteLLM / alfred / shell / brew / macOS / mac | `09-工具/mac-工具/{tool}/` |
| hermes / codex | `03-领域/31-人工智能学科/智能体工具/{tool}/` |
| obsidian / chrome / git / excel / mermaid | `09-工具/工具-通用工具汇编/工具-{tool}/` |
| LLM / Agent / RAG / neural / transformer / attention / embedding | `03-领域/31-人工智能学科/` |
| algorithm / data structure / OS / database / programming / Rust / Python | `03-领域/30-计算机科学(CS)/` |
| cognition / learning / memory / psychology | `03-领域/00-认知科学/` |
| resume / goal / personal / reflection / diary | `01-我的/` |
| company / product / market / SaaS | `06-商业/` |
| audit / MOC / skill-spec / governance | `07-治理/` |
| tool / config / install / CLI | `09-工具/` |
| booklist / resource | `05-资源/` |

Miss → load vault-index.yaml full routing in Window 2.

## When To Use

- Creating a new knowledge note from scratch
- Renaming or restructuring an existing note to meet naming standards
- The user says "帮我写一篇笔记", "创建笔记", "整理成笔记", "新建一个", "create note", "new note", "draft note", "write a note"
- After the `concept-definer` skill produces a concept card and the user wants it saved as a proper note
- Processing pending items from a daily note's `## 新建` section (daily review → note creation)

Route to the Codex `concept-definer` skill when the primary task is defining a single concept. Use this skill when the scope is broader: guides, references, summaries, or any note that needs naming and MOC placement.

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
- 稳定笔记不加日期；一次性记录加日期后缀（`-26.0501.md`）
- 重命名时旧名写入 frontmatter `aliases`
- **别名规则**：每篇笔记需含以下别名格式，便于多路径搜索：
  - 英文主题名（如 `Hermes CLI Fuzzy File Reference`）
  - 中文简称（如 `hermes文件模糊引用`）
  - 速查码：`{一级}/{二级}/{中文主题}({拼音}, {英文缩写})`
    - 一级 = 工具名或领域名（`hermes` / `obsidian` / `AI`），不用泛型标签
    - 二级 = 功能子域（`文件操作` / `配置` / `安装` / `模型架构`）
    - 示例：`hermes/文件操作/文件模糊引用(WJMH, HFFR)`

---

## Step 2: 定位归档目录与 MOC（vault-index.yaml 路由）

### 2a. 关键词提取

从笔记主题提取 2-5 个搜索关键词，优先使用 vault-rules.yaml 标签词表中的领域标签（见下方「标签分类体系」）。

### 2b. 索引查询 + 去重 + MOC 读取（合并 execute_code）

```python
import yaml, subprocess, os

VAULT = "/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"
with open(f"{VAULT}/99-设置/vault-index.yaml") as f:
    idx = yaml.safe_load(f)

# 扁平化目录树
def flatten(node):
    if isinstance(node, dict):
        path = node.get("path")
        if path:
            yield (path, {k: v for k, v in node.items() if k != "children"})
        for child in node.get("children", []):
            yield from flatten(child)
        if not path and "children" not in node:
            for v in node.values():
                yield from flatten(v)
    elif isinstance(node, list):
        for item in node:
            yield from flatten(item)

flat = dict(flatten(idx["directories"]))

# 关键词路由
keywords = ["Hermes", "AI"]  # ← 替换
routing = idx["search_routing"]
candidates = {}
for kw in keywords:
    for path in routing.get(kw, []):
        candidates[path] = candidates.get(path, 0) + 1

if candidates:
    ranked = sorted(candidates.items(), key=lambda x: -x[1])
    for path, score in ranked:
        info = flat.get(path, {})
        print(f"  {score} hits → {path}  moc={info.get('moc','NONE')}")
else:
    print("search_routing 无匹配，用归属判断速查表")
```

### 2c. 确认目录与 MOC

对排名最高的候选目录：
1. 查 `flat` 中该路径的 `moc` 字段
2. 若 `moc` 为空，按文件夹笔记约定检查 `{路径}/{目录名}.md` 是否存在
3. 若无现成 MOC，判断是否需要新建（≥2 篇相关笔记时建；用户预判未来会多篇时即刻建）

**去重检查**：在目标目录下 grep 关键词，若已有同主题笔记 → 追加或链接，不重复创建。

### 2d. 新建主题目录（MOC 创建）

```bash
VAULT="/Users/haoxc/__Data/00_Knowledges/Vault_HXC3.1(Apple)"
mkdir -p "$VAULT/父目录/新主题"

cat > "$VAULT/父目录/新主题/新主题.md" << EOF
---
tags: [领域名, moc]
description: 领域名知识索引
type: moc
create-date: $(date +%Y-%m-%d)
---

# 新主题

## 基础

- [[第一篇笔记]]
EOF
```

- 文件名 = 所在目录名（如 `03-领域/AI/AI.md`）
- `type: moc`，至少一个 `##` 分组
- **03-领域**：最大深度 5 层，二层以下用语义名不加数字前缀

### 2e. 归属判断速查

| 笔记主题 | → 目标目录 | → MOC |
|----------|-----------|-------|
| 工具 CLI 用法、配置 | `09-工具/` | `09-工具/09-工具.md` 或子目录 MOC |
| 智能体工具（hermes/codex） | `03-领域/31-人工智能学科/智能体工具/{工具名}/` | 子目录 MOC |
| 领域原理、方法论 | `03-领域/` | 查 search_routing 定位子目录 MOC |
| 个人日记、反思 | `01-我的/` | `01-我的/01-我的.md` |
| 外部文章摘录 | `02-输入/` | `02-输入/02-输入.md` |
| 商业情报 | `06-商业/` | `06-商业/06-商业.md` |
| Vault 治理 | `07-治理/` | `07-治理/07-治理.md` |
| 资源清单、书单 | `05-资源/` | `05-资源/05-资源.md` |
| 不确定 | `04-笔记/` | 待整理 |

### 2f. 分类不确定时的用户确认流程

当路由命中了顶层领域目录（如 `03-领域/31-人工智能学科/`）但该主题没有现成子目录时，**必须用 `clarify` 让用户选择**，禁止自行决定最终子目录名称。

**触发条件**（满足任一）：
- search_routing 或路由速查只定位到顶层目录，无匹配的现成子目录
- 主题可归入多个现成子目录（歧义）
- 需要新建子目录来存放该主题笔记

**流程**：

1. 推理 3 个最可能的归类路径，每条含简短理由
2. 用 `clarify` 工具展示，choices 参数给出 3 个候选 + 让用户自定义
3. 用户选择或指定后，按选定路径创建

**clarify 模板**：

```
question: "笔记「{标题}」应归档到哪个目录？"
choices:
  - "{路径A} — {理由}"
  - "{路径B} — {理由}"
  - "{路径C} — {理由}"
```

**推理候选的规则**：

| 优先级 | 推理依据 | 示例（主题=gbrain） |
|--------|---------|---------------------|
| 1 | 同类笔记已存在的兄弟目录 | `智能体工具/`（gstack 已在此） |
| 2 | 语义匹配：从 vault 顶层目录角色反推 | `09-工具/`（它是工具） |
| 3 | 泛化归入：上层目录直放或 `---/` 工作区 | `31-人工智能学科/`（直放） |

> ✓ 推理后 clarify 确认；✗ 自行 mkdir + write_file 不确认。

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

**别名示例**：

| 笔记标题 | aliases |
|----------|---------|
| `hermes-CLI文件模糊引用` | `["Hermes CLI Fuzzy File Reference", "hermes文件模糊引用", "hermes/文件操作/文件模糊引用(WJMH, HFFR)"]` |
| `hermes-auxiliary模型配置踩坑` | `["Hermes Auxiliary Model Pitfalls", "hermes辅助模型", "hermes/配置/辅助模型配置(FZMX, AMC)"]` |
| `hermes-profile使用指南` | `["Hermes Profile Guide", "hermes多配置", "hermes/配置/profile管理(PG, HPM)"]` |
| `Transformer 架构` | `["Transformer Architecture", "transformer结构", "AI/模型架构/Transformer架构(T, TA)"]` |

速查码格式：`{一级}/{二级}/{中文主题}({拼音首字母}, {英文缩写})`。

| 段 | 取值规则 | 示例 |
|----|---------|------|
| 一级 | 工具名或领域名（hermes / obsidian / git / AI / 编程） | `hermes` |
| 二级 | 功能子域（文件操作 / 配置 / 安装 / CLI / 模型架构） | `文件操作` |
| 中文主题 | 笔记核心主题（中文） | `文件模糊引用` |
| 拼音 | 每字首字母大写 | `WJMH` |
| 英文缩写 | 每词首字母大写 | `HFFR` |

> 一级用工具名而非泛型标签（`hermes` 而非 `AI工具`），确保按工具搜索时能聚合。

### 3b. 正文结构

**概念定义**：
```
# 概念名

**一句话定义**：...

## 判断标准
- 是 X 当且仅当...

## 容易混淆
| 概念 | 区别 |

## 典型例子

## 相关
- [[关联笔记]]
```

**工具参考 / 操作指南**：
```
# 工具名-用途

## 概述
一段话说明是什么、什么时候用。

## 核心操作
1. 步骤一

## 常见问题
- Q: ...
- A: ...

## 相关
- [[关联笔记]]
```

**规约 / 规则**：规则在前，理由在后。表格做映射，列表做判断标准。含 `✓/✗` 反例对照。

### 3c. 风格约束

- 核心结论在前 15 行
- 陈述句直接下结论，每个结论自带理由
- 禁止口语化、情绪化词语、感叹号
- 正文末尾不加「总结」段
- 超过 80 行考虑拆分子页面
- 能用表格不用段落，能用列表不用表格（≤2 维时）
- 首次出现时 Wikilink，同篇不重复；链接文本 = 目标笔记标题

---

## Step 4: 内容质量审查（6 维度）

| 维度 | 检查要点 | 不通过标准 |
|------|---------|-----------|
| 概念精度 | 定义精准、无歧义 | 一句话定义无法独立成立 |
| 区分度 | 与相邻概念对比 | 漏了日常最常用的近似词 |
| 示例质量 | 跨场景、具体可感 | 例子只有一个场景 |
| 可操作性 | 读者能做什么 | 纯概念可省略，方法论的必须有 |
| 内部一致性 | 分类/例子/定义无矛盾 | 例子归类与概念区分冲突 |
| 表述简洁度 | 每句承载不可替代信息 | 有未定义的内部术语 |

≥2 维度不通过 → 重写。

---

## Step 5: 挂 MOC 反向链接

```python
# 合并到窗口 4 的 execute_code 中
import os

moc_path = f"{VAULT}/目标目录/MOC名.md"
note_link = "[[笔记标题]]"

with open(moc_path) as f:
    if note_link not in f.read():
        with open(moc_path, 'a') as f:
            f.write(f"- {note_link}\n")
        print(f"MOC 已追加: {note_link}")
```

验证：MOC 仍是导航页（`type: moc`），链接在正确的 `##` 分组下。

---

## Step 6: 写入每日笔记新建入口

每篇笔记创建后，在当天日记的 `## 新建` 节下追加 Wikilink。

```python
# 合并到窗口 4 的 execute_code 中
from datetime import date

today = date.today().isoformat()
diary_path = f"{VAULT}/01-我的/日常笔记/日记-{today}.md"
note_link = "[[笔记标题]]"
desc = "一句话描述"

if not os.path.exists(diary_path):
    os.makedirs(os.path.dirname(diary_path), exist_ok=True)
    with open(diary_path, 'w') as f:
        f.write(f"---\ntags: [日记]\ndescription: {today} 日常记录\ntype: log\ncreate-date: {today}\n---\n\n## 新建\n\n")

with open(diary_path) as f:
    content = f.read()

if note_link not in content:
    if "## 新建" not in content:
        content += "\n## 新建\n"
    content += f"- {note_link} — {desc}\n"
    with open(diary_path, 'w') as f:
        f.write(content)
    print(f"日记已追加: {diary_path}")
```

验证：日记 `type: log`，`## 新建` 节下出现新链接，同一天不重复。

---

## Vault 顶层目录设计

| 目录 | 用途 | 归属判断 |
|------|------|----------|
| `01-我的/` | 个人信息、目标、日记、思考 | 关于"我"的内容 |
| `02-输入/` | 阅读摘录、外部文章 | 外部内容的原文摘录或翻译 |
| `03-领域/` | 知识领域（AI、编程、设计等） | 领域原理、方法论、体系化知识 |
| `04-笔记/` | 零散笔记、待整理碎片 | 不成体系的知识碎片 |
| `05-资源/` | 资源清单、书单 | 列举型内容 |
| `06-商业/` | 商业情报：公司档案、产品对比、市场格局 | 跨领域的商业信息 |
| `07-治理/` | Vault自身治理：审计、MOC评估、skill规范 | 主题子目录，日期型文件名 `{yy.MMdd}-{主题}.md` |
| `09-工具/` | 具体工具使用笔记 | CLI 用法、配置步骤、故障排查 |
| `10-归档/` | 过时或不再维护的笔记 | 历史参考资料 |
| `98-附件/` | 集中附件存储（被 .gitignore 排除） | 图片、PDF 等静态资源 |
| `99-设置/` | 配置文件、模板、声明层规则库 | 系统级配置 |
| `---/` | 工作区、项目 | 日期前缀子目录 `YYYY-MM-DD-项目名/` |
| `z附件/` | 本地附件暂存 | 统一命名为 `z附件`，禁用变体 |

---

## 日记与周期笔记规范

| 项目 | 日记 | 周期笔记 |
|------|------|----------|
| 命名 | `日记-YYYY-MM-DD.md` | `周报-YYYY-WXX.md` / `月报-YYYY-MM.md` / `季报-YYYY-QX.md` |
| type | `log` | `log` |
| tags | `[日记]`，可追加子标签 | `[周报]` / `[月报]` / `[季报]` |
| description | 必填，当日核心事件一句话 | — |
| 内容 | 日常记录 | 产出 + 关键决策 + 下期计划 |

---

## 标签(tags)分类体系

### 领域标签

`AI` `AI-LLM` `AI-Agent` `AI-RAG` `AI-训练` `AI-推理` `编程` `编程-Python` `编程-JS` `编程-C++` `编程-Rust` `游戏引擎` `游戏引擎-蓝图` `游戏引擎-材质` `游戏引擎-动画` `设计` `设计-UI` `设计-交互` `设计-可视化` `管理` `管理-战略` `管理-项目` `管理-团队` `学术` `学术-论文` `学术-审阅` `学术-写作` `数媒` `数媒-动画` `数媒-视频` `数媒-交互` `术语`

### 类型标签

`教程` `参考` `速查` `对比` `观点` `实践` `模板` `清单` `复盘`

### 状态标签

`草稿` `已审阅` `过时` `待整理` `归档`

### 工具标签

`hermes` `obsidian` `claude-code` `git` `docker` `UE` `blender`

### 人员标签

格式 `人员/xxx`：`人员/zs` `人员/qq` `人员/导师`

> 组合示例：Hermes Agent 配置教程 → `[AI, AI-Agent, 教程, hermes]`

---

## 特殊规则

### MOC 页面规范
- MOC 只做**导航**：列出子笔记链接、简短描述
- 禁止在 MOC 中写长篇正文
- `type` 必须为 `moc`

### SVG 图表配套规则
- 每个 SVG 文件必须有同名 Markdown 说明页
- 说明页含：图表用途、关键节点说明、版本/来源
- 说明页 `type: note`

### 附件目录命名
- 本地附件目录统一命名为 `z附件`
- 禁止变体：`附件`、`zAttachments`、`attachments`、`assets`
- 集中附件归入 `98-附件/`

### 大文件归档（GitHub 10MB 限制）

扫描阈值 10MB。触发：Git 提交前 / 执行「整理大文件」。

```
find "$VAULT" -type f -size +10M ! -path "*/.git/*" ! -path "*/.obsidian/*" ! -path "*/98-附件/*"
```

分类映射：
| 文件类型 | → `98-附件/` 子目录 |
|----------|---------------------|
| 音视频 (.mp4 .mov .m4a .mp3 .wav) | `01-项目音视频记录/项目名/` |
| 文档底稿 (.docx .pptx .xmind .zip) | `02-项目方案与需求材料/项目名/` |
| 案例展示 | `03-数字孪生案例库/案例名/` |
| 课程/学习材料 (.pdf .pptx) | `04-学习与课程材料/主题/` |
| 不确定 | `05-待确认附件/` |

安全约束：移动前记录原始路径 → 不删 `.gitignore` 条目 → 批量前输出清单确认 → `98-附件/` 整体由 `.gitignore` 排除。

---

## 批量操作安全协议

执行批量操作前，先输出计划和影响清单：

```
【操作计划】
- 操作类型：移动 / 重命名 / 删除
- 涉及文件数：N
- 影响的反向链接：...
- 潜在风险：xxx
```

用 `clarify` 请求用户确认后再执行。用户指令「不再询问」「全部执行」时跳过确认但仍输出日志。

### 默认禁止操作

| 禁止行为 | 原因 |
|----------|------|
| 修改 `.obsidian/` 目录 | 不可逆，影响插件配置 |
| 删除附件文件（图片、PDF） | 可能破坏现有引用 |
| 写入含 secrets 的文件 | 安全风险 |
| 创建无 frontmatter 的笔记 | 违反 Vault 规范 |
| 创建无别名（aliases）的笔记 | 缺少多路径搜索入口，发现性差 |
| 创建零发现路径的笔记 | 不可检索，等价于丢失 |
| 重命名或删除 MOC 文件 | 破坏大量反向链接 |
| 跨目录移动笔记（未同时更新所有引用 MOC） | 导致断链 |
| 修改已有笔记 `type`（无明确理由+确认） | `type` 决定 MOC 归类逻辑 |

---

## Quality Checklist

- [ ] 文件名见名知意，离开目录上下文也能猜出内容
- [ ] 通过 vault-index.yaml search_routing 定位目录，未做全量扫描
- [ ] 去重检查通过（同目录无同主题笔记）
- [ ] Frontmatter 含 aliases（英文 + 中文简称 + 速查码）/ tags / description / type / create-date
- [ ] 笔记已挂载到对应 MOC（MOC 仍是导航页，`type: moc`）
- [ ] 当天日记 `## 新建` 节下已追加 Wikilink
- [ ] 内容通过 6 维度审查
- [ ] 无裸通用文件名
- [ ] 稳定笔记无日期后缀；一次性记录有

---

## Common Pitfalls

1. **跳过 vault-index.yaml 直接 find** —— 浪费 token。先查索引，再在锁定目录下精确搜索。
2. **索引过期** —— vault 目录结构变更后未刷新。运行 `generate_vault_index.py`。
3. **MOC 写成文章** —— MOC 只做导航，禁止长文。
4. **type 字段随意填** —— `moc` 只用于 MOC 页，`note` 用于普通笔记。
5. **03-领域 深度超标** —— 超过 5 层时向上合并或重新规划层级。
6. **frontmatter 缺少 create-date** —— 四字段缺一不可。
7. **日记用旧格式 type: 日记(Diary)** —— 已改为 `type: log`。
8. **串行调用过多导致慢** —— 4 次工具调用目标 25-35s。skill_view 只加载一次（本技能），索引/去重/MOC 合并到一次 execute_code。
9. **加载不相关的 skill** —— 创建笔记时只加载本技能。不需加载 `hermes-agent` 等主题无关 skill，除非笔记主题本身就是该 skill 的使用方法。
10. **同主题笔记散落不分组** —— ≥2 篇同主题笔记时创建主题子目录（如 `07-治理/skill规范/note-crafter规范/`）；用户明确预判某主题会有多篇笔记时，首篇即建目录，遵循 `subdir: semantic` 规则。
11. **忽略研究阶段直接写内容** —— 对陌生主题（如 gstack / OpenClaw / 新工具）跳过调研直接编造内容。先通过 GitHub API / curl 获取权威源信息（README、文档），再进入写作阶段。研究阶段额外 2-4 次终端调用，不计入 4 次窗口配额。GitHub API 是可靠的 fallback（`curl -s https://api.github.com/repos/{owner}/{repo}`），当 Google/DuckDuckGo 反爬时仍可用。
12. **子目录不确定时自行决定** —— 路由只定位到顶层目录、无现成子目录时，跳过 clarify 确认直接 mkdir。必须推理 3 候选、clarify 让用户选或指定。如 gbrain 应在 `智能体工具/`（兄弟目录 gstack 已存在），而非自行决定放 `09-工具/` 或直放。

## Maintenance Scripts

```bash
# Rebuild vault index after directory structure changes
python3 ~/.hermes/skills/note-taking/hxc-obsidian-vault/scripts/generate_vault_index.py

# Fix missing frontmatter on existing notes
python3 ~/.hermes/skills/note-taking/hxc-obsidian-vault/scripts/fix_frontmatter.py [subdir] [--dry]

# Full vault compliance audit (7 dimensions)
python3 ~/.hermes/skills/note-taking/hxc-obsidian-vault/scripts/audit.py [--verbose]
```

## References

- `99-设置/vault-rules.yaml` — declarative rule base (single source of truth)
- `99-设置/vault-index.yaml` — precomputed directory index + keyword routing
- `[[MOC-Wiki目录页规范]]` — MOC page design rules
- `[[知识管理目录规范]]` — 03-领域 structure rules
- `concept-definer` — single-concept definition card skill
