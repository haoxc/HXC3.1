---
tags: [mermaid, obsidian, 工具]
description: ``` mermaid
type: note
create-date: 2025-10-30
---

``` mermaid 
flowchart TD
    A[开始] --> B[初始化循环变量]
    B --> C{序列中还有元素?}
    C -- 是 --> D[执行循环体]
    D --> E[自动取下一个元素]
    E --> C
    C -- 否 --> F[结束循环]
```
