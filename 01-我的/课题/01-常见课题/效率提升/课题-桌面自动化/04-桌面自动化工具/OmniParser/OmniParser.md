---
aliases:
  - 桌面自动化/工具/OmniParser
tags:
category:
domain:
domain_en:
description:
type:
create-date: 2026-04-29
---
## 启示(教训)
 > [!warning] 警示
 > - 模块版本问题经常出现不兼容

## 环境
- C:\HXC_TOOLS\OmniParser
### 安装 依赖文件
```
cd OmniParser
conda create -n "omni" python==3.12
conda activate omni
pip install -r requirements.txt
```

### 安装 huggingface_hub
```
pip install -U huggingface_hub
```

### 安装权重

- Window

```powershell
# 下载 icon_detect 模块的权重文件 huggingface-cli download microsoft/OmniParser-v2.0 "icon_detect/train_args.yaml" --local-dir weights huggingface-cli download microsoft/OmniParser-v2.0 "icon_detect/model.pt" --local-dir weights huggingface-cli download microsoft/OmniParser-v2.0 "icon_detect/model.yaml" --local-dir weights # 下载 icon_caption 模块的权重文件 huggingface-cli download microsoft/OmniParser-v2.0 "icon_caption/config.json" --local-dir weights huggingface-cli download microsoft/OmniParser-v2.0 "icon_caption/generation_config.json" --local-dir weights huggingface-cli download microsoft/OmniParser-v2.0 "icon_caption/model.safetensors" --local-dir weights
```

- (Linux)
```
# 进入 weights 目录
cd weights/

# （可选）清空旧的权重文件
rm -rf icon_detect icon_caption icon_caption_florence

# 下载 V2 模型检查点
# 注意：这需要您预先安装并登录 huggingface-cli
for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; do huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir ../weights; done

# 重命名文件夹（将 icon_caption 改名为 icon_caption_florence）
mv icon_caption icon_caption_florence

```

