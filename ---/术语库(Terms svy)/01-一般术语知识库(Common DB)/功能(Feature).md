---
type: term
category:
description:
tags:
  - 需求分析
  - 功能模块
  - 系统分解
aliases:
field:
---

---
# 特性 (Feature)

### 1. 🎯 一句话定义 (Definition)

> **Feature 是产品或系统为了满足用户特定需求、解决特定问题而提供的可感知的、独立的功能模块或属性。**

### 2. ⚡ 核心特征 (Key Characteristics)

* **原子性 (Atomicity)**：理想的 Feature 应该是功能独立的，可以被单独定义、开发和测试。
* **可见性 (Visibility)**：它是用户能直接体验到或感知到的“`价值点`”（区别于底层的技术实现）。
* **交付导向 (Delivery-oriented)**：每一个 Feature 都是项目计划中的一个交付单位，具有明确的生命周期（从 `Backlog` 到 Done）。
* **可量化性 (Measurability)**：可以通过指标验证该 Feature 是否达到了设计初衷（如：转化率、点击率）。

### 3. 🚀 应用场景 (Use Cases)
* **产品路线图 (Roadmap)**：将 Feature 按优先级排布，展示产品进化的路径。
* **销售与市场 (Sales Pitch)**：向客户推销产品时，强调核心 Feature 如何解决他们的痛点。
* **软件架构**：通过“特性开关 (Feature Toggle)”来控制不同用户群体对新功能的访问。
* **需求评审 (PRD)**：详述 Feature 的逻辑细节、边界条件和异常处理。
### 4. 📍 战略定位 (Positioning)
* **位置：它是连接“用户价值”与“代码实现”的中间件。**
* 向上对接：**Benefit (益处)**。Feature 告诉你“它是什么”，Benefit 告诉你“它对我有什么好处”。
* 向下对接：**Function/Implementation (功能实现)**。Feature 是用户视角，Function 是开发视角。
* **层级关系**：通常遵循 **Epic (史诗) > Feature (特性) > User Story (用户故事)** 的层级。

### 5. 💡 教练私房话 (Coach's Tip)

* **沟通陷阱：不要错把“手段”当“Feature”。**
	* *错误表达*：“我们的 Feature 是使用了分布式数据库。”（这是实现细节，不是 Feature）
	* *专业表达*：“我们的 Feature 是‘秒级全球数据同步’，这能解决您的多地协作延迟问题。”
* **进阶技巧：[[FAB 模型]]**
	* 在沟通中遵循：**Feature (属性) -> Advantage (优势) -> Benefit (利益)**。
	* “这个充电宝有 20000 毫安容量 (**Feature**)，所以它能充 5 次电 (**Advantage**)，这意味着你出差一周都不用带充电头 (**Benefit**/这是客户最想听的)。”

---

**你想继续探讨 Feature 的“近亲”——Benefit (益处) 和 Function (功能) 的区别，还是想聊聊如何通过 Feature 来进行产品优先级排序（如：[[KANO 模型]]）？**