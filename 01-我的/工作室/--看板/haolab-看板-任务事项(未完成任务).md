---
aliases:
  - abbr://看板/未完成任务(lab-kanban@lab-tasks-svy, lab-kanban@lab-rw-svy)
type: note
tags: [工具]
description: FROM "01-看板/04-工作室"
create-date: 2026-04-29
---
## 未完成清单

```dataview
TASK
FROM "01-看板/04-工作室"
WHERE !completed
GROUP BY file.link
```
