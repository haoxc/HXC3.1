
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


