---
tags: [mermaid, 工具]
description: [[446eaa35b3bbc8ecf0f535226376d2bf_MD5.jpg|Open: Pasted image 20251030210443.png
type: note
create-date: 2026-04-29
---

[[446eaa35b3bbc8ecf0f535226376d2bf_MD5.jpg|Open: Pasted image 20251030210443.png]]
![[446eaa35b3bbc8ecf0f535226376d2bf_MD5.jpg]]
flowchart TD

 ```  mermaid
flowchart TD
    A@{ shape: circle, label: "开始" } --> C{循环套件}
    C -->|是| D[循环体]
    C -->|否| E@{ shape: dbl-circ, label: "结束" }
    D --> |继续| C
 ```

---
### 流程图
``` mermaid
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)

    B --> C{Let me think}

    C -->|One| D[Laptop]

    C -->|Two| E[iPhone]

    C -->|Three| F[fa:fa-car Car]
```


## ganntchart

```mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
```
