---
aliases: image
type: note
tags: [工具]
description: *创建时间*：2022年5月8日 16:09:21
create-date: 2026-04-29
---
*创建时间*：2022年5月8日 16:09:21

## 概述
>[pyglet.image — pyglet v1.5.23](https://pyglet.readthedocs.io/en/latest/modules/image/index.html)

通过该模块加载`图像`以及`纹理处理函数`


## 使用
```python
from pyglet import image
pic = image.load('picture.png')
```
 
> 支持图片类型: PNG, BMP, GIF, JPG


## 常用方法
- `blit`(_x_, _y_, _z=0_)[link](https://pyglet.readthedocs.io/en/latest/modules/image/index.html#pyglet.image.AbstractImage.blit "Permalink to this definition")
在当前活动帧中绘制该图片
Draw this image to the active framebuffers.
The image will be drawn with the lower-left corner at (`x -` anchor_x, `y -` anchor_y, `z`).
