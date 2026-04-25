---
aliases:
  - czu/学习实践/AI时代下的心流模型(czu-LearningModel, czuLM)
tags:
description:
type:
ref-url:
create-date: 2026-04-02 12:16
---

## 目标规划
- [[czuLM-学习规划-V1.0-0402]]

## 学习追踪
```dataview
TABLE
    rows.file.link AS "笔记名称",
    rows.tags AS "标签",
    rows.type AS "类型",
    rows.description AS "描述"
FROM "---/-workspaces/czu-学习路径和实践(26.0402)"
GROUP BY dateformat(default(file.day, default(date(create-date), file.ctime)), "yyyy-MM-dd") AS "学习日期"
SORT rows.file.mtime DESC
```
