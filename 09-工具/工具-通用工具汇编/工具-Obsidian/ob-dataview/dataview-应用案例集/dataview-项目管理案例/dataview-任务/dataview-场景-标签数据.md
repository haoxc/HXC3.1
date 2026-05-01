---
tags: [dataview, obsidian, 工具]
description: 显示 #hxc 的笔记
type: note
create-date: 2025-11-19
---

## 文件基本属性
显示 #hxc 的笔记
```dataview
TABLE  
	file.name,
	file.stem,
	file.folder,
	file.path, 
	file.ext

FROM #hxc  
LIMIT 10
```

## 文件时间相关
> 创建,变更相关属性 : [[dataview-内置元数据]]
> file.cday
> file.ctime
> file.mday
> file.mtime
> file.szie
```dataview
TABLE without ID
	file.name,
	file.test,
	file.cday,
	file.ctime,
	file.mday,
	file.cday
FROM
	#工具 
SORT  file.mday DESC
```

## 内容关联 

### 场景-标签

```dataview
TABLE without ID
	file.name,
	file.tags
FROM
	#工具 
LIMIT  10
```
### 场景-出链
```dataview
TABLE  
	file.links
FROM
	#工具 
LIMIT  10
```

---
### 场景-入链
```dataview
TABLE 
	file.inlinks
FROM
	#工具 
LIMIT  10
```
### 场景- 标题区块
```dataview
TABLE 
	file.headings
FROM
	#工具 
LIMIT  10
```

## 任务相关

```dataview
TABLE file.name, rating, date 
FROM #hxc  
SORT rating DESC 
LIMIT 10
```
