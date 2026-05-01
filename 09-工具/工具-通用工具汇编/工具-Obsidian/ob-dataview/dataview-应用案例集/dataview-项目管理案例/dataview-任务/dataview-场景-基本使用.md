---
tags: [dataview, obsidian, 工具]
description: ```plaintext
type: note
create-date: 2025-11-19
---

```plaintext
\```
	TABLE file.name, file.cday as "创建时间"
	FROM ""
	SORT file.mtime DESC
\```
```


##示例

```dataview
	TABLE file.name, file.cday as "创建时间"
	FROM ""
	SORT file.mtime DESC
    LIMIT 10	
```
