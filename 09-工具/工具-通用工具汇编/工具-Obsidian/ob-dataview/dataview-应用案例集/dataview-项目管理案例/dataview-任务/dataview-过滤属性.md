
## 基础(单属性)
### 包含截止日期(due)
**定义**
````
```dataview
TASK
FROM "Projects"
WHERE duedate  //有截止日期
GROUP BY file.link
```
````
**样式:** 
```dataview
TASK
FROM "Projects"
WHERE duedate   //测试
GROUP BY file.link
```

---
### 任务包含标签 
**定义**
````
```dataview
TASK
FROM "Projects"
WHERE  contains(tags, "#imp-重点")
GROUP BY file.link
```
````
```dataview
TASK
FROM "Projects"
WHERE  contains(tags, "#imp-重点")
GROUP BY file.link
```

---
### 优先级
**定义**
````
```dataview
TASK
FROM "Projects"
WHERE  priority="low"
GROUP BY file.link
```
````

**示例**
```dataview
TASK
FROM "Projects"
WHERE  priority="low"
GROUP BY file.link
```

