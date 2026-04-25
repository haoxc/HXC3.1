
### 过滤due的任务

```dataview
TASK
FROM "01-看板"
WHERE 
	!completed and  contains(tags, "#跟进_follow-up")
GROUP BY file.link
LIMIT  50
```





