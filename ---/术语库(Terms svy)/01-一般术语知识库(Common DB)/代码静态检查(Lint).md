---
aliases:
  - lint
  - Lint
  - Linting
  - 代码规范检查
  - 代码静态检查
tags:
  - 术语
  - 软件工程
  - 代码质量
description: 解释 Lint/Linting 的含义、边界，以及它与格式化、测试、静态分析的区别。
type: 术语卡片
create-date: 2026-05-01
---

# 术语解析：代码静态检查 (Lint)

> [!IMPORTANT] 快速理解
> Lint 是在不运行程序的前提下，用规则自动检查代码中的风格、潜在错误和可维护性问题。

## 1. 概念界定 (Concept Definition)

代码静态检查 (Lint) 指通过工具扫描源代码，发现不符合约定或可能导致问题的写法。它关注的不是“功能是否正确运行”，而是“代码看起来是否存在明显风险”。

常见检查对象包括：

- 命名是否符合规范；
- 未使用变量、未使用导入；
- 可能的空值、类型、作用域问题；
- 复杂度过高或不可维护写法；
- 安全、兼容性或框架约定问题；
- 团队约定的代码风格。

Lint 的核心机制是规则集：工具把代码解析成语法结构，再按规则判断是否违规。

典型工具：

- JavaScript / TypeScript：`ESLint`
- Python：`Ruff`、`flake8`、`pylint`
- Go：`golangci-lint`
- Markdown：`markdownlint`

## 2. 替代范式 (Alternative Paradigms)

- 代码静态检查 (Lint)：强调规则检查和风险提示，常用于提交前、CI、编辑器实时提示。
- 格式化 (Formatting)：强调排版统一，例如缩进、换行、引号风格。
- 静态分析 (Static Analysis)：范围更大，可包括类型分析、安全扫描、控制流分析。
- 测试 (Testing)：运行代码或模拟运行，验证行为是否符合预期。
- 代码审查 (Code Review)：由人判断设计、业务语义、可读性和长期维护风险。

## 3. 边界辨析 (Boundary Analysis)

| 维度 | Lint | Formatting | Testing | Code Review |
| --- | --- | --- | --- | --- |
| 是否运行代码 | 否 | 否 | 是 | 不一定 |
| 核心对象 | 代码规则与潜在问题 | 代码排版 | 功能行为 | 设计与语义质量 |
| 输出结果 | warning/error | 改写后的格式 | pass/fail | 评论、建议、决策 |
| 自动化程度 | 高 | 很高 | 高 | 中 |
| 典型工具 | ESLint、Ruff | Prettier、Black | pytest、Jest | GitHub PR Review |
| 常见误用 | 以为 lint 能证明功能正确 | 以为格式化能提高设计质量 | 以为测试能覆盖风格问题 | 把机械问题交给人肉检查 |

## 4. 典型工作流

```text
写代码
  ↓
格式化 formatter
  ↓
Lint 检查风格与潜在问题
  ↓
测试验证行为
  ↓
代码审查处理设计和语义问题
```

## 5. 实践指南 (Practice Guide)

> [!IMPORTANT] 实践指南
>
> 1. 把 Lint 放到编辑器、pre-commit 和 CI 中，让机械问题尽早暴露。
> 2. 能自动修复的规则交给工具，例如 `eslint --fix`、`ruff --fix`。
> 3. 不要把 Lint 当成测试；Lint 发现“可疑写法”，测试验证“行为正确”。
> 4. 团队规则应少而稳定，避免把个人偏好塞进 Lint 规则。

类比：Lint 像写作里的“语法和格式检查器”。它能指出拼写、标点和明显语病，但不能保证文章观点正确。

示例：

```bash
ruff check .
eslint .
markdownlint "**/*.md"
```

不适合称为 Lint 的情况：

- 人工评审架构设计；
- 运行单元测试；
- 端到端验证业务流程；
- 手工判断一段代码是否符合产品目标。
