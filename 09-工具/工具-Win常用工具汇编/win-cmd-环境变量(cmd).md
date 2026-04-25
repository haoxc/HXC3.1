---
aliases:
tags:
description:
type:
ref-url:
create-date: 2026-04-04 09:43
---
## 内容

**环境变量**是存储在操作系统中的一组动态值，用于定义程序的运行环境。
- 系统变量
- 用户变量

### 定义

临时定义

```
set VAR = value
```

永久设置
```
set VAR  = "value"
```

### 查看

```
echo  %VAR%
```

### 常用
- **PATH**: ：**最重要的变量**,它包含一系列目录;
- **`USERPROFILE`**：当前用户的主目录路径（如 `C:\Users\YourName`）
-  **`APPDATA`**：应用程序存储配置数据的默认位置。
- **`LOCALAPPDATA`**: 一个非常关键的环境变量，它指向当前用户特定的**本地应用程序数据文件夹**