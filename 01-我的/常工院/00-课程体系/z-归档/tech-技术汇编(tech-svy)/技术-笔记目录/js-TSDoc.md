---
tags: [工具]
description: TSDoc 是一项为 TypeScript 代码中文档注释（doc comments）制定标准的提案，核心目标是让不同工具提取注释内容时，不会因彼此的标记（ma
type: note
create-date: 2026-04-29
---

## 一、TSDoc 核心定义

TSDoc 是一项为 TypeScript 代码中文档注释（doc comments）制定标准的提案，核心目标是让不同工具提取注释内容时，不会因彼此的标记（markup）差异产生混淆。其关键特征包括：
- **语法熟悉性**：基于 JSDoc/Markdown 风格，开发者易上手，且能最大程度兼容遗留注释。
- **配套工具**：提供开源参考实现解析器库 @microsoft/tsdoc，确保工具 100% 符合标准；另有 TSDoc Playground 提供交互式解析器演示。

- **示例代码**：通过 Statistics 类的 getAverage 方法示例，直观展示 TSDoc 注释格式（含 @remarks、@param、@returns、@beta 等标签）。

---

## 二、为什么需要 TSDoc？

---

### 1. 工具兼容性痛点

单个 TypeScript 源文件可能被多个工具分析，但这些工具虽基于 JSDoc 语法，却各有扩展，导致兼容性问题：

- 常见涉事工具：TypeDoc（API 参考生成器）、DocFX（多语言 API 内容处理工具）、API Extractor（TypeScript API 构建工具）、ESLint（代码检查工具）、Visual Studio Code（编辑器，支持注释语法高亮与重构）、开发者自定义构建脚本。

---

### 2. 典型冲突案例

以 isInlineTag 函数注释为例，不同工具解析结果差异显著：

- 关于 “是否标记为 @internal”：API Extractor 因支持 CommonMark 构造，判定 “否”；TypeScript 编译器将所有内容视为文本，判定 “是”。

- 关于 “@see 块是否属于 @example”：不同工具处理逻辑不同，导致解析结果不一致。

- 影响：日常场景中偶发故障影响较小，但涉及专业网站内容或构建输出时，错误解析会引发严重问题。

---

## 三、TSDoc 的三大核心需求

TSDoc 在制定标准时，平衡了三个关键设计需求：

1. **可扩展性**：工具可定义自定义标签，以自然方式承载领域特定元数据。

2. **互操作性**：自定义标签不会阻碍其他工具正确分析注释 —— 需遵循既定语法模式，确保解析时可安全识别并忽略。

3. **语法熟悉性**：最大限度保留 JSDoc/Markdown 风格，同时提高遗留注释解析为 TSDoc 的兼容性。

---

### 补充：为何不直接使用 JSDoc？

- JSDoc 语法无严格规范，仅通过特定实现推断行为。

- JSDoc 多数标准标签聚焦于为纯 JavaScript 提供类型标注，而 TypeScript 作为强类型语言，无需此核心功能，故 JSDoc 不适合作为 TypeScript 注释标准。

---

## 四、TSDoc 的参与方与贡献者

---

### 1. 实现贡献者

- Pete Gonzalez：创建初始概念与解析器 API。

- Ron Buckton：重新设计声明引用语法，并重写 Markdown 解析器。

- Ian Clanton-Thuon：贡献 TSDoc Playground。

- Brian Folts：贡献 ESLint 插件 eslint-plugin-tsdoc。

- 其他多位贡献者：参与功能实现与漏洞修复（支持通过 “Suggest an update” 补充遗漏姓名）。

---

### 2. 设计输入贡献方

- 微软 TypeScript 编译器团队

- API Extractor 社区

- DocFX 维护者

- TypeDoc 社区

- SimplrJS 开发者（维护 ts-docs-gen 工具）

- Tom Dale（为 Ember.js、Glimmer.js 等项目开发文档引擎）

- Rob Eisenberg（为 Aurelia 开发文档引擎）

---

## 五、TSDoc 相关资源与后续步骤

---

### 1. 核心资源

- **NPM 包**：@microsoft/tsdoc（解析器库）、@microsoft/tsdoc-config（配置相关）、eslint-plugin-tsdoc（ESLint 集成插件）。

- **规范与参考**：TSDoc spec（核心规范）、Tag kinds（标签类型）、Standardization groups（标准化小组）、Tag reference（标签参考，含 @alpha/@beta/@deprecated/@param/@returns 等标准标签）。

- **帮助资源**：Getting help（帮助文档）、TSDoc Playground（交互式演示）、GitHub（代码仓库）。

---

### 2. 后续步骤

- 了解更多：学习 TSDoc 的目标与实现方法（“Learn more” 链接）。

- 上手使用：通过 “How can I use TSDoc?” 了解开发相关工具与资源。

格式调整已完成，所有标题前均已添加 “---” 分割线。若你还需要调整分割线样式、修改标题层级，或对内容进行补充删减，欢迎随时告知我。
