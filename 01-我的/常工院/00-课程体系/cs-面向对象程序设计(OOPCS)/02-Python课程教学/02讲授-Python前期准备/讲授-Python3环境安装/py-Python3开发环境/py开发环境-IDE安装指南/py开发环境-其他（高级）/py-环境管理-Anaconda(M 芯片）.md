---
aliases:
type: note
tags: [工具]
description: *创建时间*：2022年4月16日 19:28:02
create-date: 2026-04-29
---
*创建时间*：2022年4月16日 19:28:02


## 安装及更新

1. 使用Anaconda 安装Jupyter Notebook
[Anaconda | The World's Most Popular Data Science Platform](https://www.anaconda.com/).
2. mac 下安装(ZSH + Anaconda)后 可以通过如下命令:
```shell
更新
	conda update  --all
安装
	conda install package-name
	conda install package-name=2.3.4
参看环境
	conda env list
```

[参考(英文)](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)

###  关于 Jupyter Notebook
**Jupyter** Notebook是一个开源的Web应用程序，允许用户创建和共享包含代码、方程式、可视化和文本的文档。 它的用途包括：数据清理和转换、数值模拟、统计建模、数据可视化、机器学习等等。 它具有以下优势： 可选择语言：支持超过40种编程语言，包括Python、R、Julia.
>   https://anaconda.org/anaconda/jupyter
>   `conda install -c anaconda jupyter`


### Mac(M1)安装说明
>[Miniconda — miniconda documentation](https://docs.conda.io/projects/miniconda/en/latest/)

要点
```shell
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

```


## Conda 命令
- 创建环境
	- 命令: 
		- conda create --name my__test python=3.7#创建一个名称为my__test
- 激活虚拟环境
	- 命令
		- activate my_test
- [切换环境](https://zhuanlan.zhihu.com/p/141122337)
	- 官方文档
		- [Installing with conda — conda 4.12.0.post48+51d89f89c documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/installing-with-conda.html)
	- 命令
		- conda env list
- 查看环境
	- conda info --envs
- 在当前环境里安装package
	- conda install ipykernel
	- 

## 启动Jupyter Notebook 
> jupyter notebook



## 参考
- [macOS M1(AppleSilicon)安装配置 Conda 环境(miniforge)-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1955714)