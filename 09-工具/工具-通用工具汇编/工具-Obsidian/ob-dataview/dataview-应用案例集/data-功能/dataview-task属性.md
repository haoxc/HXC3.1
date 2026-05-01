---
tags: [dataview, obsidian, 工具]
description: 在 Dataview 中，`task` 对象包含一系列**原生属性**（内置支持）和**自定义属性**（用户标注），这些属性可用于筛选、排序、展示任务的各类信息
type: note
create-date: 2025-11-19
---

在 Dataview 中，`task` 对象包含一系列**原生属性**（内置支持）和**自定义属性**（用户标注），这些属性可用于筛选、排序、展示任务的各类信息。以下是 `task` 对象的核心属性及用法：


### 一、Dataview 原生 `task` 属性（内置支持）
这些属性无需额外配置，Dataview 会自动识别任务的基础特征：

| 属性名                | 类型     | 含义                                             | 示例值                                 |
| ------------------ | ------ | ---------------------------------------------- | ----------------------------------- |
| `task.text`        | 字符串    | 任务的文本内容（不含复选框和属性）                              | "完成需求文档"                            |
| `task.completed`   | 布尔值    | 任务是否已完成（`[x]` 为 `true`，`[ ]` 为 `false`）        | `true`/`false`                      |
| `task.completedAt` | 日期     | 任务的完成时间（需 Dataview ≥0.5.60，且任务完成后自动记录）         | `2025-11-20T14:30:00`               |
| `task.parent`      | 对象     | 父任务（仅子任务有此属性，指向缩进层级的上一级任务）                     | 父任务的 `task` 对象                      |
| `task.position`    | 对象     | 任务在笔记中的位置（含行号、字符位置等）                           | `{start: {line: 5}, end: {line:5}}` |
| `task.due`         | 日期     | 任务的截止日期（需用 `(due: YYYY-MM-DD)` 标注）             | `2025-11-30`                        |
| `task.priority`    | 字符串/字符 | 任务优先级（需用 `(priority: 高)` 或 `#A` 标注）            | `"高"`/`"A"`                         |
| `task.recurring`   | 字符串    | 任务重复规则（需用 `(recurring: daily)` 标注，兼容 Tasks 插件） | `"daily"`/`"weekly"`                |


### 二、自定义 `task` 属性（用户标注）
除原生属性外，你可以为任务添加**任意自定义属性**（用 `(属性名: 值)` 格式标注），Dataview 会自动解析为 `task` 对象的属性：

#### 1. 自定义属性标注格式
```markdown
- [ ] 完成项目报告 (due: 2025-11-30, priority: 高, assignee: 张三, estimated: 3h)
```

#### 2. 可自定义的属性示例
- `assignee`: 任务负责人  
- `estimated`: 预估耗时  
- `category`: 任务分类  
- `start`: 任务开始时间  
- `progress`: 任务进度  


### 三、`task` 属性的实用查询示例
结合属性实现项目任务的精细化管理：

#### 1. 提取任务优先级和负责人
```dataview
TABLE 
  task.text AS "任务内容",
  task.priority AS "优先级",
  task.assignee AS "负责人",
  choice(task.completed, "✅", "🔴") AS "状态"
FROM "Projects"
FLATTEN file.tasks AS task
WHERE task.priority  // 仅显示有优先级的任务
SORT task.priority DESC
```

#### 2. 筛选逾期且未完成的任务
```dataview
TABLE 
  task.text AS "任务内容",
  task.due AS "截止日期",
  date(today()) AS "当前日期"
FROM "dataview-项目管理案例/Projects"
FLATTEN file.tasks AS task
WHERE !task.completed AND task.due < date(today())  // 未完成+逾期
```

#### 3. 展示子任务及其父任务
```dataview
TABLE 
  task.text AS "子任务",
  task.parent.text AS "父任务",
  task.parent.parent.text AS "祖父任务"
FROM "Projects"
FLATTEN file.tasks AS task
WHERE task.parent  // 仅显示有父任务的子任务
```

#### 4. 按预估耗时排序任务
```dataview
TABLE 
  task.text AS "任务内容",
  task.estimated AS "预估耗时",
  task.category AS "分类"
FROM "Projects"
FLATTEN file.tasks AS task
WHERE task.estimated
SORT task.estimated DESC
```


### 四、注意事项
1. **属性值格式规范**：  
   - 日期属性（如 `due`/`start`）推荐用 `YYYY-MM-DD` 格式，Dataview 可直接识别为日期类型，支持比较和排序；  
   - 布尔属性（如 `urgent: true`）需用小写 `true`/`false`；  
   - 多值属性（如 `tags: [设计, 前端]`）需用数组格式标注。
1. **兼容性**：  
   部分原生属性（如 `completedAt`/`recurring`）需 Dataview ≥0.5.60，若版本过低，需升级插件。
2. **属性名大小写敏感**：  
   `task.Due` 和 `task.due` 会被视为不同属性，建议统一用小写（如 `due`/`priority`）。


通过灵活运用 `task` 对象的原生属性和自定义属性，你可以实现项目任务的多维度管理（如时间、优先级、负责人、进度等），满足精细化的项目跟进需求。
