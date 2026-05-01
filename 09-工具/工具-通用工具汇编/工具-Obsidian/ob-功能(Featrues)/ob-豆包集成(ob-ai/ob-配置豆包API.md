---
tags: [AI, obsidian, 工具]
description: 1. 新建一条笔记，输入以下代码块（替换 `API_KEY` 和 `SECRET_KEY` 为你的实际密钥）：
type: note
create-date: 2025-12-03
---

#### 步骤 3：配置 API 调用（以 “Advanced URI” 为例）

1. 新建一条笔记，输入以下代码块（替换 `API_KEY` 和 `SECRET_KEY` 为你的实际密钥）：
    ```markdown
    [调用豆包答疑](obsidian://advanced-uri?command=api-call&method=POST&url=https://aquasearch.bytedance.com/api/v1/chat/completions&headers={"Authorization":"Bearer e35fbcee-945b-4c93-a1a1-a1294f660475","Secret-Key":"WmpJM09UYzFaVFEzWWpkaU5ETTBObUZtWldZek1HWTBOV0poTnpFMk1UQQ==","Content-Type":"application/json"}&body={"model":"doubao-pro","messages":[{"role":"user","content":"{{如何优化 Dataview 查询}}"}],"temperature":0.7})
    ```

- [测试](obsidian://advanced-uri?command=api-call&method=POST&url=https://aquasearch.bytedance.com/api/v1/chat/completions&headers={"Authorization":"Bearer e35fbcee-945b-4c93-a1a1-a1294f660475","Secret-Key":"WmpJM09UYzFaVFEzWWpkaU5ETTBObUZtWldZek1HWTBOV0poTnpFMk1UQQ==","Content-Type":"application/json"}&body={"model":"doubao-pro","messages":[{"role":"user","content":"{{如何优化 Dataview 查询}}"}],"temperature":0.7})

2. 替换 `{{query}}` 为你的实际问题（如 “如何优化 Dataview 查询”），点击链接即可触发 API 调用；
3. 若需将回答插入笔记，配合 **“Templater”** 插件，在模板中添加响应结果渲染逻辑（示例）：
    
    ```javascript
    <%*
    const response = await fetch("https://aquasearch.bytedance.com/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "Bearer e35fbcee-945b-4c93-a1a1-a1294f660475",
        "Secret-Key": "WmpJM09UYzFaVFEzWWpkaU5ETTBObUZtWldZek1HWTBOV0poTnpFMk1UQQ==",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "doubao-pro",
        messages: [{ role: "user", content: "如何优化 Dataview 查询" }]
      })
    });
    const data = await response.json();
    tR = data.choices[0].message.content; // 将回答插入笔记
    %>
    ```
