---
aliases: []
tags: []
description:
type:
ref-url:
create-date: 2026-04-23 21:36
---
##  常见错误

### 权限复位

`tccutil reset` 是 macOS 用来**重置隐私权限授权记录**的命令。

TCC = Transparency, Consent, and Control，也就是系统设置里的这些权限：
```text
Accessibility
Input Monitoring
Screen Recording
Camera
Microphone
Full Disk Access
Automation
```

常见用法：

```bash
tccutil reset Accessibility com.runningwithcrayons.Alfred
tccutil reset ListenEvent com.runningwithcrayons.Alfred
```

含义：

- `Accessibility`：重置 Alfred 的“辅助功能”权限。
- `ListenEvent`：重置 Alfred 的“输入监听 / Input Monitoring”权限。
- `com.runningwithcrayons.Alfred`：Alfred 的 bundle id。

执行后，macOS 会忘掉 Alfred 当前这项权限授权。你需要重新打开 Alfred，系统会再次弹权限请求；或者你手动去：

```text
System Settings > Privacy & Security
```

重新把 Alfred 加进去并打开。

注意：`tccutil reset` **不会删除 Alfred snippets，也不会删除 Alfred 配置**。它只清隐私权限授权记录。  
但如果 App 签名本身异常，reset 后重新授权也可能仍然不稳定。