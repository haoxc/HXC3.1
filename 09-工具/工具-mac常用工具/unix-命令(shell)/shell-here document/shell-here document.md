---
aliases:
  - shell/知识点/heredoc
tags:
description:
type:
ref-url:
---
## 内容

**在此文档(Here Document / Here-doc)** 语法。
- **作用(Function)**：它允许你将多行字符串（即 Python 代码）作为输入直接传递给命令（`python3`），而无需创建一个临时的 `.py` 文件。
- **[[定界符(Delimiter)]]**：`PYEOF` 是自定义的标识符。`<< 'PYEOF'` 告诉系统：“接下来的内容直到遇到下一个 `PYEOF` 为止，全部交给 python3 处理。”
- **引号的作用(Quoting)**：给 `PYEOF` 加引号（`'PYEOF'`）是为了防止 Shell 对其中的特殊字符（如 `$` 或 `` ` ``）进行 **变量替换(Variable Expansion)**，确保 Python 代码原封不动地执行。
- ## 示例
	- [[createExclidraw.txt]]

在计算机领域，Here Document（通常简称为 heredoc）是一种在 shell 脚本或编程语言中定义多行字符串的方法，它允许你直接在代码中嵌入大段文本，而无需频繁使用 `echo` 或处理复杂的转义字符。

## 1. 基本语法 (Bash 示例)

在 Bash 中，heredoc 使用 `<<` 符号后跟一个自定义的 结束标识符（通常是 `EOF` 或 `END`）。 [2, 4, 5]

```bash
cat << EOF
这是一段多行文本。
它会被直接传递给 cat 命令。
变量 $USER 也会被解析（除非标识符被加了引号）。
EOF
```

## 2. 核心特性

- `多行支持`：能够完整保留文本中的换行和空白字符。
- `变量解析`：默认情况下，heredoc 会解析其中的 shell 变量（如 `$HOME`）。
- `禁止解析`：如果你希望文本是字面量（即不解析变量），可以将标识符用引号括起来，例如 `<< 'EOF'`。
- `自动缩进`：使用 `<<-`（带减号）可以自动忽略行首的 制表符 (Tabs)，方便在函数或条件语句中保持代码整洁。

## 3. 常见用途

- 生成配置文件：在脚本中动态创建 `.conf` 或 `.yaml` 文件。
- 执行远程命令：通过 SSH 将多行指令发送到服务器执行。
- 运行数据库查询：将多行 SQL 语句传递给数据库客户端。
- 打印帮助信息：在脚本中显示格式化的使用说明。 [2, 3, 4, 8, 9, 10, 11]
除了 Shell 之外，PHP、Perl、Ruby、Python 和 Terraform 等语言也都支持类似的 heredoc 语法.

