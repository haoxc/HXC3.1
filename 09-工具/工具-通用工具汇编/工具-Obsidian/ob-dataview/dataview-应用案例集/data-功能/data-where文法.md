
## 文法

```
dataview
WHERE [条件一] AND [条件二] AND [条件三] ...
```

- **运算符**

| 运算符   | 描述          | 示例                         |
| ----- | ----------- | -------------------------- |
| `AND` | 所有条件必须同时满足  | `A AND B`                  |
| `OR`  | 满足任一条件即可    | `A OR B`                   |
| `()`  | 用于分组和控制执行顺序 | `(A OR B) AND C`           |
| `!`   | 非（用于否定条件）   | `WHERE !completed`（查找未完成的） |
|       |             |                            |
### 示例

```dataview
task 
from ""
where priority="low" 
```



