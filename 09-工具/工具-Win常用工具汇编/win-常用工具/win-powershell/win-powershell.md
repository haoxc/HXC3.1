---
aliases:
  - win/win-shell
description:
title: win-powershell
domain:
created: 2026-01-03 13:07
type: note
tags: [shell, windows, 工具]
create-date: 2026-01-03
---
## 内容

### 底层哲学的碰撞

| **维度**   | **Linux (Bash)**              | **PowerShell (PS)**                         |
| -------- | ----------------------------- | ------------------------------------------- |
| **数据单元** | **纯文本 (Strings)**             | **对象 (Objects)**                            |
| **管道传递** | 传递一串字符，需要 `grep/awk` 重新解析。    | 传递完整的属性和方法，直接提取数据。                          |
| **命名规则** | 缩写极简（`ls`, `ps`, `df`），记忆成本高。 | 动词-名词（`Get-ChildItem`, `Get-Process`），可读性高。 |

### 核心语法差异速查表

|**功能**|**Linux (Bash)**|**PowerShell**|**备注**|
|---|---|---|---|
|**变量声明**|`VAR="value"`|`$VAR = "value"`|PS 变量统一带 `$`|
|**获取帮助**|`man [cmd]`|`Get-Help [cmd]`|PS 也有 `man` 别名|
|**逻辑判断**|`if [ $a -eq $b ]; then`|`if ($a -eq $b) {`|PS 使用大括号，更像 C/Java|
|**循环**|`for i in {1..5}; do`|`foreach ($i in 1..5) {`|-|
|**字符串内插**|`"Hello $NAME"`|`"Hello $NAME"`|两者双引号都支持内插|
|**JSON 处理**|需安装 `jq`|`ConvertFrom-Json`|PS 原生支持 JSON 对象|
### 万能公式
**万能三部曲**：在 PS 中遇到不认识的东西，按此顺序自救：
- `Get-Command`：找命令
- `Get-Help`：看文档
- `Get-Member` (最重要)：**查看这个命令吐出来的对象里到底有哪些属性**。

