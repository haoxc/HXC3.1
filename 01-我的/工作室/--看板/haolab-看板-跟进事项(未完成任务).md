---
aliases:
  - abbr://止善/看板/未完成任务(lab-kanban@gj-rw-svy)
---
## 未完成清单
```dataview
TASK
FROM "01-看板/04-工作室"
WHERE !completed and contains(tags, "#跟进_follow-up")
GROUP BY file.link
```



