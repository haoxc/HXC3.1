
### 进行中
```dataview
TABLE 
  task.text AS "任务内容",
  task.due,
  task.parent,
  choice(task.completed, "✅ 已完成", "🔴 进行中") AS "状态"
FROM "Projects"
FLATTEN file.tasks AS task
```


## 任务数量
```dataview
TABLE file.name AS "笔记名", length(file.tasks) AS "任务数量"
FROM  "Projects"
```


## due日期

```dataview
TABLE 
  task.text AS "任务内容",
  regexreplace(task.text, ".*⏳\\s*(\\d{4}-\\d{2}-\\d{2}).*", "$1") AS "截止时间",
  regexreplace(task.text, ".*🛫\\s*(\\d{4}-\\d{2}-\\d{2}).*", "$1") AS "开始时间",
  choice(task.completed, "✅ 已完成", "🔴 进行中") AS "状态"
FROM "Projects"  
FLATTEN file.tasks AS task
LIMIT 5
```

  
## 其他模式
### 任务是否正确识别 (✅)
```dataview
TABLE file.name AS "笔记名", length(file.tasks) AS "任务数量"
FROM  "Projects"
```


### 任务提取 (list)
```dataview
TABLE 
  task.text,
  task.due AS "截止日期", 
  task.priority AS "优先级", 
  tags AS "标签", 
  file.link AS "来源"
FROM "Projects"
WHERE !completed
SORT due ASC
```



```dataview
table this
where file = this.file
```

``` dataview
table file.lists, file.tasks
where file = this.file
limit 1
```


