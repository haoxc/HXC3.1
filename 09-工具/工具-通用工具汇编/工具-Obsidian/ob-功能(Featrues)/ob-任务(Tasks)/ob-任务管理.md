---
tags: [obsidian, 工具]
description: **基础任务语法**：
type: note
create-date: 2025-11-18
---

# Obsidian任务管理

## 一、核心方法：原生Markdown任务+插件增强

**基础任务语法**：
- `- [ ] 未完成任务`（标准格式）
- `- [x] 已完成任务`
- `- [.] 进行中任务`（自定义状态，需插件支持）

**推荐插件组合**：
| 插件 | 核心优势 | 适用场景 |
|-----|---------|---------|
| **Tasks** | 全局任务查询+过滤+排序 | 日常待办、项目任务管理  |
| **TaskNotes** | 任务→独立笔记双向同步 | 复杂任务、需详细记录  |
| **Day Planner** | 日历视图+时间块规划 | 日程安排、时间管理  |
| **Dataview** | 自定义查询+统计分析 | 任务报表、进度追踪  |

## 二、方案一：Tasks插件 

### 1. 安装与基础设置

- **安装**：设置→社区插件→搜索"Tasks"→安装并启用 
- **基础配置**：
  - 设置全局过滤标签（如#task），只追踪特定标签任务 
  - 快捷键：将"Toggle Checkbox Status"改为"Tasks: Toggle Done"，推荐`Ctrl+Enter` 

### 2. 任务创建进阶

**基础语法**：
```
- [ ] 任务描述 (due: 2025-11-30) #priority_high
```

**高级属性**：
- **截止日期**：`(due: 2025-11-30)` 或 `(due: next Friday)` 
- **优先级**：`(priority: A)` 或用标签 `#prio_high` 
- **重复任务**：`(recurring: daily)` 或 `(recurring: every 2 weeks)` 
- **子任务**：在任务下缩进添加 `- [ ] 子任务` 

### 3. 任务查询魔法（核心功能）

在笔记中插入任务查询块：
```
```tasks
not done 
due before tomorrow 
path includes Projects 
sort by priority 
group by folder
```
```

**常用查询指令**：
- **过滤**：`not done`（未完成）、`due today`（今日到期）、`tag includes work`（含work标签）
- **范围**：`due between 2025-11-01 and 2025-11-30`（指定日期范围）
- **排序**：`sort by due date`（按截止日期）、`sort by priority desc`（按优先级降序）
- **分组**：`group by folder`（按文件夹分组）、`group by tag`（按标签分组）

## 三、方案二：GTD工作流（高效人士首选）

### 1. 核心文件夹结构

```
📁 Inbox          # 临时收集所有任务
📁 Projects       # 所有项目总览
├── 📁 Project A  # 项目A的任务与文档
└── 📁 Project B  # 项目B的任务与文档
📁 Next Actions   # 下一步行动清单（扁平列表）
📁 Waiting        # 等待他人完成的任务
📁 Someday/Maybe  # 未来可能做的任务
📁 Archives       # 已完成任务归档
```

### 2. 实施步骤（GTD五步法）

**1️⃣ 收集(Capture)**：
- 任何灵感/任务→直接记入Inbox文件夹的`inbox.md` 
- 每天定时（如早9点）处理Inbox，避免堆积

**2️⃣ 明确(Clarify)**：
- 问自己："这是什么？需要做什么？"
- 将模糊任务转化为具体行动（如"整理资料"→"收集客户数据并分类"）

**3️⃣ 组织(Organize)**：
- **项目**：需要多步骤完成的任务→移至Projects文件夹
- **下一步行动**：立即可执行的→移至`next-actions.md`，按项目分组 
- **等待/将来**：分别放入相应文件夹 

**4️⃣ 回顾(Reflect)**：
- **日回顾**：检查当天任务+更新进度
- **周回顾**：全面检查所有项目+更新下一步行动
- **月回顾**：评估目标进度+调整计划

**5️⃣ 执行(Engage)**：
- 从`next-actions.md`中选择优先级最高的任务，专注完成 
- 完成后→移入Archives或项目文档中归档 

## 四、方案三：艾森豪威尔矩阵（优先级管理）

### 1. 任务分类（四象限法）

| 象限 | 特征 | 处理策略 | 示例 |
|-----|-----|---------|------|
| **紧急且重要** | 必须立即做 | 优先处理 | 客户投诉、即将到期项目  |
| **重要不紧急** | 长期价值 | 计划时间做 | 技能提升、关系维护  |
| **紧急不重要** | 干扰项 | 委托或减少 | 无关会议、临时帮忙  |
| **不紧急不重要** | 浪费时间 | 尽量避免 | 无意义刷手机、低效社交  |

### 2. Obsidian实现方式

**方法A：文件夹分类**
- 创建四个文件夹对应四象限，任务按类别存放 
- 使用Custom Folder Files Tree CSS片段，为不同文件夹设置不同颜色 

**方法B：标签+查询**
- 为任务添加标签：`#urgent #important` 等组合
- 查询示例：
```
```tasks
not done 
(tag includes urgent AND tag includes important) OR 
(tag includes important AND NOT tag includes urgent)
sort by due date
```
```

## 五、方案四：任务+笔记深度集成（知识工作者推荐）

### 1. TaskNotes插件（双向关联）

- **基础用法**：在普通笔记中写任务→选中→右键"转换为TaskNote" 
- **神奇效果**：
  - 自动创建独立任务笔记，保留原任务信息
  - 原笔记替换为任务链接，显示任务状态
  - 任务与原笔记双向同步，修改任一处另一处自动更新 

### 2. 任务模板化（提高效率）

**创建任务模板**：
```
---
type: 项目任务
status: 待办
priority: B
due: {{date:YYYY-MM-DD}}
---

# 任务: {{title}}

## 描述
{{description}}

## 子任务
- [ ] 子任务1
- [ ] 子任务2

## 相关笔记
```

**使用方法**：
- 安装Templater插件
- 在命令面板中选择"QuickAdd: Create task from template" 

## 六、多插件协同：打造个人任务中枢

### 1. 日历视图（Day Planner+Tasks）
- 安装Day Planner插件
- 创建日程笔记，插入：
```
```dayplanner
tasks
```
```
- 效果：在日历中直观显示所有带日期任务，支持拖放调整 

### 2. 任务统计（Dataview+Tasks）
```
```dataview
TABLE WITHOUT ID
	file.ctime as "创建时间", 
	due as "截止日期", 
	priority as "优先级", 
	status as "状态"
FROM #task 
WHERE !completed 
SORT due ASC, priority DESC
```
```

## 七、实用技巧与避坑指南

### 1. 快捷键设置（提升效率）

| 操作 | 推荐快捷键 | 说明 |
|-----|-----------|------|
| 标记任务完成 | `Ctrl+Enter` | 选中任务后一键打钩  |
| 快速创建任务 | `Ctrl+Shift+T` | 在任何位置快速添加任务  |
| 任务查询 | `Ctrl+P` → "tasks query" | 快速插入任务查询块  |

### 2. 常见问题解决方案

**问题1：任务过多难以管理**
- 解决：使用查询+分组，如按项目、日期或优先级分组
- 示例：每周创建周计划笔记，查询本周任务：
```
```tasks
not done 
due between monday and sunday
sort by due date
```
```

**问题2：任务遗漏**
- 解决：建立固定回顾机制（日/周回顾）
- 每周日晚上花30分钟检查所有项目和任务 

**问题3：任务与笔记脱节**
- 解决：使用TaskNotes或双链链接，确保任务与相关知识文档关联
- 示例：在任务笔记中添加`## 相关笔记`部分，链接到参考资料 

## 八、总结与行动建议

**Obsidian任务管理核心优势**：
- **灵活性**：从简单清单到复杂项目管理，适应各种需求
- **集成性**：任务与知识、笔记无缝连接，构建完整知识-行动体系
- **可视化**：通过查询和插件，实现任务多维展示与分析

**推荐行动计划**：

1. **基础起步**（1天）：
   - 安装Tasks插件并配置基础设置
   - 创建"Inbox.md"和"Next Actions.md"
   - 开始用标准语法记录任务

2. **系统构建**（1周）：
   - 选择GTD或艾森豪威尔矩阵建立任务分类体系
   - 为常用任务创建模板
   - 设置每日/每周回顾习惯

3. **进阶优化**（1个月）：
   - 尝试TaskNotes或Day Planner等插件
   - 建立任务与知识文档的链接关系
   - 定制查询和报表，监控任务进度

Obsidian任务管理不是简单的待办事项列表，而是将"知识"与"行动"融为一体的个人生产力系统，让你的笔记真正成为改变行动的工具。
