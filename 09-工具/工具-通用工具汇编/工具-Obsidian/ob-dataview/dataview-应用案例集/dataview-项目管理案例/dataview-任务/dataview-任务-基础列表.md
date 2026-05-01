---
tags: [dataview, obsidian, 工具]
description: ```dataview
type: note
create-date: 2025-11-20
---

````
```dataview
TASK
FROM "Projects"
WHERE !completed
GROUP BY file.link
```
````

形式如下: 

```dataview
TASK
FROM "01-看板"
WHERE !completed
GROUP BY file.link
```
