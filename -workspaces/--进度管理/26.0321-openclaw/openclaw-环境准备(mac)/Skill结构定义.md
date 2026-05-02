---
aliases:
  - 如何描述Skill
tags:
description:
type:
ref-url:
create-date: 2026-03-08
---
> 它的核心逻辑是：==清晰的任务定义 + 严谨的执行步骤 + 具体的约束条件==。

---

## 📂 Skill 结构模版：

## 1. 📋 Metadata (元数据)

> 用于定义技能的基本身份，方便 AI 快速检索。

- ID: `unique_skill_id`
- Name: 技能的直观名称（如：代码审查专家）
- Version: 1.0.0
- Description: 简洁描述此技能解决什么问题（1句话）。

---

## 2. 🎯 Purpose & Role (目标与角色)

> 告诉 AI “你是谁”以及“你的核心任务”。

- Role: 你是一位精通 [领域] 的 [专家角色]。
- Objective: 你的目标是 [具体的产出物]，通过 [某种方式] 确保 [某种质量标准]。

---

## 3. 🛠️ Workflows / Steps (工作流)

> 这是 Skill 的核心，将任务拆解为标准动作。

1. 阶段一：理解需求。分析用户的 [输入内容]，提取 [关键要素]。
2. 阶段二：执行处理。应用 [特定逻辑/公式] 对数据进行建模。
3. 阶段三：优化输出。根据 [质量检查清单] 润色结果。

---

## 4. 📏 Constraints & Guidelines (约束与规范)

> 设定“红线”，防止 AI 发散。

- Must: 必须使用 [特定语言/格式]；必须包含 [特定模块]。
- Never: 严禁 [常见错误行为]；禁止使用 [禁用词汇]。
- [[调性|语气(Tone)]]: [语气风格：专业/幽默/简洁]。

---
## 5. 📥 Inputs & 📤 Outputs (输入与输出)

> 明确格式契约。
- Input: `{{user_content}}` (支持的文件类型或文本结构)。
- Output: [Markdown 表格 / JSON / 代码块]；输出必须符合 [某种 Schema]。

---

## 6. 📝 Examples (示例/少样本学习)

> 所谓的 "Few-shot Prompting"，给 AI 模板参考。

- Input: `...`
- Output: `...`
---
## 💡 Obsidian 笔记小技巧

在 管理这些 Skill 时，建议：
1. 独立文件夹：建立一个 `Skills/` 文件夹。
2. 使用 Callout：在笔记中使用 `> [!abstract] Skill 定义` 来美化元数据部分。
3. 双链关联：在 `Workflows` 中通过 `[[特定方法论]]` 关联到你库中的其他知识笔记。
