---
tags: [dataview, obsidian, 工具]
description: Obsidian 的内置元数据是无需手动配置、插件自动索引的文件/内容属性，核心用于快速查询、筛选和管理笔记，以下是完整梳理：
type: note
create-date: 2025-11-19
---

Obsidian 的内置元数据是无需手动配置、插件自动索引的文件/内容属性，核心用于快速查询、筛选和管理笔记，以下是完整梳理：

### 一、核心内置元数据分类（按用途划分）
#### 1. 文件基础属性（最常用）
- `file.name`：笔记文件名（含后缀，如 `学习笔记.md`）
- `file.stem`：笔记文件名（不含后缀，如 `学习笔记`）
- `file.path`：笔记完整路径（如 `知识库/编程/学习笔记.md`）
- `file.folder`：笔记所在文件夹路径（如 `知识库/编程`）
- `file.ext`：文件扩展名（固定为 `md`，Markdown 文件）

#### 2. 时间相关属性
- `file.cday`：笔记创建日期（格式为 ISO 日期时间，如 `2025-11-10T09:30:00`）
- `file.ctime`：同 `file.cday`，创建时间的别名
- `file.mday`：笔记最后修改日期（自动更新，格式同上）
- `file.mtime`：同 `file.mday`，修改时间的别名
- `file.size`：笔记文件大小（单位：字节）

#### 3. 内容关联属性
- `file.tags`：笔记中所有标签的数组（自动抓取 `#标签`，如 `["编程", "Python"]`）
- `file.links`：笔记中所有出站链接（即 `[[目标笔记]]` 的集合）
- `file.inlinks`：所有指向当前笔记的入站链接（谁引用了这篇笔记）
- `file.aliases`：笔记的别名（从 YAML 前置元数据的 `aliases` 字段读取）
- `file.link` : 一个**内置元数据字段**，它提供了指向文件本身的链接

#### 4. 任务相关属性（自动识别任务列表）
- `file.tasks`：笔记中所有任务的数组（包含 `-[ ]` 未完成、`-[x]` 已完成任务）
- 任务子属性（需配合 `file.tasks` 使用）：
  - `completed`：布尔值（`true` 已完成，`false` 未完成）
  - `text`：任务描述文本
  - `line`：任务在笔记中的行号
  - `status`：任务状态（如 `x` 已完成、空格未完成，支持自定义状态如 `w` 进行中）

### 二、常用查询示例（直接复制可用）
#### 1. 按创建时间筛选笔记
```dataview
TABLE 
  file.name as "笔记名",
  dateformat(file.cday, "yyyy-MM-dd") as "创建日期",
  file.folder as "所在文件夹"
FROM "知识库"
WHERE file.cday >= date("2025-11-01")
SORT file.cday DESC
```

#### 2. 统计并展示所有未完成任务
```dataview
TASK
FROM ""
WHERE !completed 
  AND file.folder != "归档"
SORT file.mtime DESC
```

#### 3. 查看某篇笔记的引用（入站链接）
```dataview
LIST file.name as "引用笔记"
FROM [[]]  // 方括号内填当前笔记名，或直接在目标笔记中使用
SORT file.cday DESC
```

#### 4. 按标签分组展示笔记
```dataview
TABLE 
  file.name as "笔记名",
  dateformat(file.mday, "MM-dd") as "最后修改"
FROM #学习 
GROUP BY file.tags
SORT group DESC
```

### 三、使用注意事项
1. 内置元数据无需手动添加，Obsidian 自动索引，修改笔记后会实时更新
2. 字段区分大小写（如 `file.Name` 无效，必须写 `file.name`）
3. 时间属性默认是 ISO 格式，需用 `dateformat()` 函数转换为易读格式
4. `file.tasks` 仅识别标准 Markdown 任务语法（`- [ ]`），自定义符号需配合插件扩展
5. 大型知识库中查询时，建议用 `FROM` 指定文件夹/标签缩小范围，提升性能

要不要我帮你整理一份 **内置元数据查询模板合集**？包含日常高频使用场景（如最近修改笔记、标签分类、任务统计），可直接粘贴到 Obsidian 中使用。
