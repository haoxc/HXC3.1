---
title: LangChain
type: note
aliases:
  - abbr:术语/LangChain
  - "#LLM/LangChain"
tags:
  - 术语
  - LLM/开源框架
created: 2025-11-16 12:09
description:
create-date: 2025-11-16
---
# LangChain 概述

LangChain 是一个用于**构建基于大语言模型（LLM）应用**的开源框架，旨在简化将 LLM 与外部数据、工具和业务逻辑集成的过程。
---
## 一、核心目标

> **让大语言模型“能做事”而不仅是“会聊天”**

- 连接 LLM 与**外部数据源**（如文档、数据库）
- 调用**工具/函数**（如计算器、API、代码解释器）
- 支持**多步骤推理**（如规划、反思、迭代）
- 构建**可维护、可扩展**的 LLM 应用架构

---

## 二、六大核心模块

|模块|功能说明|
|---|---|
|**Models**|封装 LLM 接口（OpenAI、Claude、本地模型等）|
|**Prompts**|管理提示词模板、动态变量注入|
|**Chains**|组合多个组件形成执行链（如“检索+生成”）|
|**Memory**|为对话添加记忆能力（短期/长期）|
|**Indexes**|处理外部数据（文本分割、向量存储、检索）|
|**Agents**|让 LLM 自主调用工具、决策执行流程|

---

## 三、典型应用场景

- 📚 **智能问答系统**：基于私有文档回答问题
- 💬 **对话机器人**：带记忆的客服/助手
- 🔍 **信息提取**：从非结构化文本中抽取结构化数据
- 🧠 **自动化任务代理**：如“查天气→写邮件→发日历”

---

## 四、简单示例（伪代码）

```python
from langchain import OpenAI, RetrievalQA
from langchain.document_loaders import TextLoader

# 1. 加载文档
loader = TextLoader("art_guide.txt")
docs = loader.load()

# 2. 创建向量索引（Index）
index = VectorstoreIndexCreator().from_documents(docs)

# 3. 构建问答链（Chain）
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever()
)

# 4. 提问
response = qa_chain.run("文艺复兴时期有哪些代表画家？")
```

---

## 五、关键优势

✅ **模块化设计**：灵活组合组件  
✅ **生态丰富**：支持主流 LLM、向量库、工具  
✅ **降低门槛**：无需从零实现 RAG、Agent 等复杂逻辑  
✅ **适合私有部署**：可对接本地模型与数据

---

> 💡 **一句话总结**：  
> LangChain 是连接大语言模型与现实世界的“桥梁”，让 AI 能真正理解你的数据、使用你的工具、完成你的任务。