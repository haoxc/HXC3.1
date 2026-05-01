---
aliases:
  - abbr://止善/看板/跟进事项(zs-follows-svy)
type: note
tags: [工具]
description: FROM "01-看板/01-项目管理/止善研究院项目看板"
create-date: 2026-04-29
---
## 未完成清单
```dataview
TASK
FROM "01-看板/01-项目管理/止善研究院项目看板"
WHERE !completed and contains(tags, "#跟进_follow-up")
GROUP BY file.link
```

