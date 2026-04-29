---
aliases:
  - 课程/面向对象/Python/实践/环境/管理工具/anaconda
tags:
description:
type:
category:
domain:
domain_en:
---

## conda常用命令
- **环境管理**
	- **确认当前**环境:  conda info
	- **查看**所有环境 :  conda env list
	- **激活**环境 :  conda activate {{env_name}}
	- **退出**环境: conda deactivate
- **环境内部**

## CLI

```conda
cd OmniParser
conda create -n "omni" python==3.12
conda activate omni
pip install -r requirements.txt
```

## GUI
- anaConda Navigator