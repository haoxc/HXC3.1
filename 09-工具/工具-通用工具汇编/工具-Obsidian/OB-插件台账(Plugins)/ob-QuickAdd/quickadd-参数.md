
 
## 1. 基本日期时间占位符

- `{{DATE}}`：获取当前日期（注意：QuickAdd中的DATE是大写的）
- `{{TIME}}`：获取当前时间
- `{{DATE:格式}}`：格式化日期，例如：
    - `{{DATE:yyyy-MM-dd}}` → 2025-11-17
    - `{{DATE:gggg-MM-DD - ddd MMM D}}` → 2025-11-17 - Mon Nov 17
- `{{TIME:格式}}`：格式化时间，例如 `{{TIME:HH:mm}}` → 19:30

## 2. 内容捕获设置
 ## 2. 内容捕获设置
- `{{VALUE}}`：用户输入的内容
- `Capture format`：指定内容格式，如 `{{DATE:HH:mm}} {{VALUE}}` → "19:30 我今天想做点什么"
 