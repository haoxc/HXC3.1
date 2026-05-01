---
tags: [dataview, obsidian, 工具]
description: - **脚本**
type: note
create-date: 2025-11-20
---

## Table-任务清单(List 清单)

- **脚本** 
````

```dataview
TABLE
  item.parent as "P",
  item.text as "内容",
  item.tags as "标签",
  item.section
FROM "01-看板/01-项目管理/止善研究院项目看板"
FLATTEN file.lists AS item
WHERE contains(item.tags, "#imp-重点")
```


````

- **示例**
```dataview

TABLE 
  item.text as "内容",
  item.tags as "标签",
  item.section as "章节"
FROM "01-看板"
FLATTEN file.lists AS item
WHERE contains(item.tags, "#跟进_follow-up")
```

### 避坑指南
- 搜索范围圈定
- 通过`标签` 搜索
