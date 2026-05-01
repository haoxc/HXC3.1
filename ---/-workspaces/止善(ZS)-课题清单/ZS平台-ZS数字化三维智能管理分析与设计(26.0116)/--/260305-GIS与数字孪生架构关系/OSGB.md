---
aliases:
  - 3D/格式/OSGB
tags:
  - 二进制
  - web端渲染
  - 倾斜摄影
description:
type:
ref-url:
create-date: 2026-03-05
---
## 内容
OSGB ([Open Scene Graph Binary](https://www.google.com/search?q=Open+Scene+Graph+Binary&num=10&newwindow=1&sca_esv=1257350bb2ab236f&sxsrf=ANbL-n4zqF-M73a8PnkUuBMdwTEA5b9sRQ%3A1772718832652&ei=8IqpaeK-J8Le2roP5ujc8Q4&biw=1209&bih=585&ved=2ahUKEwjGtfbb9YiTAxXxsVYBHTwVDFgQgK4QegYIAQgAEAM&uact=5&oq=OSGB&gs_lp=Egxnd3Mtd2l6LXNlcnAiBE9TR0IyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESI4HUKIEWKIEcAF4AZABAJgBf6ABf6oBAzAuMbgBA8gBAPgBAvgBAZgCAqAChwHCAgoQABiwAxjWBBhHmAMAiAYBkAYKkgcDMS4xoAeXArIHAzAuMbgHgwHCBwMwLjLIBwWACAA&sclient=gws-wiz-serp)) 是一种用于存储和传输大规模三维地理信息数据的二进制文件格式，常用于`倾斜摄影模型`、城市规划和`GIS应用`。其优势在于高效的数据压缩、支持细分层次细节（PagedLOD）机制，适用于在Web端流畅展示海量三维模型。

- **全称与定义**：Open Scene Graph Binary，是 OpenSceneGraph 开源图形引擎的自有二进制格式。
- **核心优势**：专为快速渲染大场景设计，通过二进制编码减少数据体积，支持`分页加载`。
- **适用场景**：[[倾斜摄影]]三维实景模型（如 Smart3D/ContextCapture 输出）、城市数字孪生、智慧城市。
- **查看与处理工具**：
    - **查看**：ContextCapture Viewer (CC Viewer)、[LocaSpaceViewer (LSV)](https://cloud.tencent.com/developer/article/1891240)。
    - **处理/转换**：CesiumLab（转为3DTiles）、[[FME-空间数据 ETL工具]]、MeshLab。
- **组成结构**：通常包含一个 metadata.xml 文件以及大量的二进制数据碎片 (.osgb) 和纹理图片。