---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-03-31
---
## 内容
`grep` 是 Linux/Unix 系统中最强大的文本搜索工具，其名称源自 `ed` 编辑器命令 `g/re/p`（Global Regular Expression Print），意为“全局正则表达式版本并打印”。它通过匹配指定的模式（Pattern）来查找文件中的特定内容。

## 1. 基本语法

```bash
grep [选项] "模式" [文件名]
```

- 模式：可以是普通字符串，也可以是正则表达式。
- 文件名：支持单个文件、多个文件或配合管道符（`|`）使用。 [3, 4, 5, 6]

## 2. 常用参数（最实用部分）

| 参数   | 说明                  | 示例                               |
| ---- | ------------------- | -------------------------------- |
| `-i` | 忽略大小写 (Ignore case) | `grep -i "error" log.txt`        |
| `-v` | 反向查找，显示不匹配的行        | `grep -v "success" log.txt`      |
| `-r` | 递归搜索，查找目录下所有文件      | `grep -r "function_name"./src`   |
| `-n` | 显示行号                | `grep -n "todo" main.py`         |
| `-l` | 仅列出文件名，不显示匹配的具体内容   | `grep -l "secret" *.txt`         |
| `-c` | 统计匹配行数              | `grep -c "warning" log.txt`      |
| `-w` | 全字匹配，避免匹配到子字符串      | `grep -w "is" file`（不会匹配 "this"） |

## 3. 上下文搜索 (调试日志必备)

当你需要查看匹配行附近的逻辑时，这三个参数非常有用：

- `-A n` (After)：显示匹配行及之后的 $n$ 行。
- `-B n` (Before)：显示匹配行及之前的 $n$ 行。
- `-C n` (Context)：显示匹配行前后的 $n$ 行。

## 4. 正则表达式示例

- 查找以 `root` 开头的行：`grep "^root" /etc/passwd`
- 查找以 `bash` 结尾的行：`grep "bash$" /etc/passwd`
- 多模式搜索：使用 `-E` 开启扩展正则，查找 "error" 或 "warning"：
    `grep -E "error|warning" log.txt`

## 5. 配合管道符使用

`grep` 常用于过滤其他命令的输出：

- 查看正在运行的 python 进程：`ps -ef | grep python`
- 查看已安装的特定包：`dpkg -l | grep ssh`

提示：在模式中包含特殊字符（如 `$`、`*`、`(`）时，建议使用单引号包裹模式，以防被 Shell 误解析。

