---
title: 变量声明(Let)
aliases:
  - 变量声明(Let)
  - abbr:辨析(bx)//const, Let， var
  - abbr://JavaScript/变量/变量声明(Let)
tags:
created: 2025-12-21 12:06
description:
---
## 要点
- **作用**
	- 在 JavaScript 中，**`let`** 是现代开发（ES6+）中声明变量的最常用方式
- **特性**
	- 核心特性：块级作用域 (Block Scope)
	-  允许“重新赋值”，但不允许“重复声明”

## 特征
### 块级作用域
这是 `let` 最重要的特征。使用 `let` 声明的变量只在它被定义的 `{ }`（花括号）内部有效。
``` javascript
if (true) {
    let tempName = "临时主题";
    console.log(tempName); // ✅ 正常输出
}

console.log(tempName); // ❌ 报错：tempName is not defined
```

> **为什么这对你有用？** 它可以防止变量“污染”全局环境，避免不同脚本之间因为同名变量产生冲突。
### 重新赋值
在你的脚本中，`let` 是最佳选择，因为你的 `userTopic` 需要被修改。
- **重新赋值（允许）**：
    ```JavaScript
    let userTopic = "未命名";
    userTopic = "我的新笔记"; // ✅ 没问题
    ```
- **重复声明（禁止）**：
    ```JavaScript
    let userTopic = "未命名";
    let userTopic = "新笔记"; // ❌ 报错：Identifier 'userTopic' has already been declared
    ```

    这能帮你`避免`在长代码中不小心把已经存在的变量给“覆盖”掉。

### 比较 const  let var

| **关键字**     | **作用域** | **允许重新赋值** | **建议使用场景**                              |
| ----------- | ------- | ---------- | --------------------------------------- |
| **`const`** | 块级 `{}` | **❌ 不允许**  | **默认首选**。用于配置项、固定的列表（如 `defaultNames`）。 |
| **`let`**   | 块级 `{}` | **✅ 允许**   | 用于**会改变**的变量（如提示输入后的 `userTopic`）。      |
| **`var`**   | 函数级     | ✅ 允许       | **过时的写法**。容易产生 Bug，现代脚本中不建议使用。          |

---

