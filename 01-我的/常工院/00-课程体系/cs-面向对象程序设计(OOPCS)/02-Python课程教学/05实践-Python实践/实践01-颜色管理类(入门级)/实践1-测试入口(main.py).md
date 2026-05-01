---
tags: [工具]
description: if __name__ == "__main__":
type: note
create-date: 2026-04-29
---

``` python
if __name__ == "__main__":
    # 思考4：实例化=创建具体的“颜色工具”，选数媒设计常用颜色
    main_color = Color(230, 46, 46)    # 品牌主红（电商/海报常用）
    secondary_color = Color(66, 133, 244)  # 辅助浅蓝（界面/图标常用）
    accent_color = Color(251, 188, 4)  # 点缀暖黄（按钮/强调文字常用）

    # 测试1：转十六进制（直接复制到设计软件用）
    print("=== 设计色码（可直接复制到PS/Figma）===")
    print(f"主色调（红）：{main_color.to_hex()}")
    print(f"辅助色（蓝）：{secondary_color.to_hex()}")
    print(f"点缀色（黄）：{accent_color.to_hex()}")

    # 测试2：调整亮度（生成设计需要的明暗变体）
    print("\n=== 设计色系变体（适配界面层级）===")
    dark_main = main_color.adjust_brightness(0.7)  # 主色变暗（背景用）
    bright_secondary = secondary_color.adjust_brightness(1.2)  # 辅助色变亮（高亮用）
    print(f"主色暗变体（背景）：{dark_main.to_hex()}")
    print(f"辅助色亮变体（高亮）：{bright_secondary.to_hex()}")
```
