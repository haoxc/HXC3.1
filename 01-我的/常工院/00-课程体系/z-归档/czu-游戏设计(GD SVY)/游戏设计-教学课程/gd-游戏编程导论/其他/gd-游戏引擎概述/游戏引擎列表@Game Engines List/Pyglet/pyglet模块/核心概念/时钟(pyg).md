---
aliases: clock
type: note
tags: [工具]
description: *创建时间*：2022年5月15日 15:54:32
create-date: 2026-04-29
---
*创建时间*：2022年5月15日 15:54:32

>[!tlbr]  模块
 >  [pyglet.clock — pyglet v1.5.24](https://pyglet.readthedocs.io/en/latest/modules/clock.html)
 
 ## 概念
 时钟目的根据**时间变化**(常常成为:**周期**,**时钟**), 进而实现游戏中的精确计算功能的机制. 比如游戏时间进度提示等

## 调度
每一个周期变化都会执行某一过程, 也就是说,当一个周期结束`时刻`,就要调用一个函数:
```python
from pyglet import clock
def callback(dt):
    print(f"{dt} seconds since last callback")

clock.schedule(callback)
```


## Clock类
- 常用方法
	- 加载调度 `schedule`(_func_, _*args_, _**kwargs_)[](https://pyglet.readthedocs.io/en/latest/modules/clock.html#pyglet.clock.Clock.schedule "Permalink to this definition")
	- 卸载调度 `unschedule`(_func_) [doc](https://pyglet.readthedocs.io/en/latest/modules/clock.html#pyglet.clock.Clock.unschedule)
	- 调度区间
		- `schedule_interval`(_func_, _interval_, `*args`, `**kwargs`)
			- _func_,
			-  *internal*(float) : 周期间隔(秒)
		- 
