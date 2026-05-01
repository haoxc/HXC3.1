---
tags:
  - 能力/接口
  - web框架
type: note
description: FastAPI 是 Python 高性能 Web 框架，核心优势：**极速开发、自动生成接口文档、强类型校验**，特别适合数媒生快速搭建「素材管理API」「设计
create-date: 2026-04-29
---
# FastAPI 数媒场景入门教程（结合解包/类实例化）
FastAPI 是 Python 高性能 Web 框架，核心优势：**极速开发、自动生成接口文档、强类型校验**，特别适合数媒生快速搭建「素材管理API」「设计工具后端」等轻量服务。

## 一、基础准备：安装与核心概念
### 1. 安装（用之前讲的pip语法）
```bash
# 安装FastAPI + 运行服务器（uvicorn）
pip install fastapi uvicorn
```

### 2. 数媒生核心场景
用 FastAPI 搭建「数媒素材管理API」：
- 查询素材信息（图片/音频/视频）；
- 新增素材数据；
- 批量获取素材列表；
- 自动生成接口文档，方便前端/团队调用。

## 二、快速上手：第一个数媒素材API（极简示例）
### 1. 完整代码（结合之前的Material类）
```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel  # 数据校验（替代手动if判断）
import uvicorn

# 1. 初始化FastAPI应用
app = FastAPI(title="数媒素材管理API", version="1.0")

# 2. 定义素材数据模型（强类型校验，数媒素材属性）
class MaterialModel(BaseModel):
    name: str          # 素材名称
    type: str          # 类型：image/audio/video
    size: float        # 大小(KB)
    resolution: str | None = None  # 图片分辨率（可选）
    duration: float | None = None  # 音频/视频时长（可选）
    fps: float | None = None       # 视频帧率（可选）

# 3. 模拟素材数据库（数媒素材列表）
material_db = [
    {"name": "海报.png", "type": "image", "size": 204.5, "resolution": "1920×1080"},
    {"name": "背景音乐.mp3", "type": "audio", "size": 512.2, "duration": 30.5},
    {"name": "宣传视频.mp4", "type": "video", "size": 10240.0, "duration": 120.0, "fps": 25.0}
]

# 4. 接口1：获取所有素材（GET请求）
@app.get("/materials/", summary="获取所有数媒素材")
def get_all_materials():
    return {"code": 200, "data": material_db}

# 5. 接口2：获取单个素材（路径参数 + 解包赋值）
@app.get("/materials/{material_name}", summary="按名称查询素材")
def get_material(material_name: str):
    # 遍历数据库，匹配素材名称
    for mat in material_db:
        if mat["name"] == material_name:
            # 解包赋值：快速提取素材属性（之前讲的解包语法）
            name, type_, size = mat["name"], mat["type"], mat["size"]
            # 扩展解包：提取可选属性（用**解包字典）
            extra = {k: v for k, v in mat.items() if k not in ["name", "type", "size"]}
            return {
                "code": 200,
                "data": {
                    "基础信息": {"名称": name, "类型": type_, "大小(KB)": size},
                    "专属属性": extra  # 解包后的可选属性
                }
            }
    return {"code": 404, "msg": f"素材{material_name}不存在"}

# 6. 接口3：新增素材（POST请求 + 数据校验）
@app.post("/materials/", summary="新增数媒素材")
def add_material(material: MaterialModel):
    # 将Pydantic模型转字典，解包后加入数据库（**解包语法）
    new_mat = material.dict()
    material_db.append(new_mat)
    return {"code": 201, "msg": "素材新增成功", "data": new_mat}

# 运行服务器（直接执行该文件）
if __name__ == "__main__":
    uvicorn.run("main.py:app", host="127.0.0.1", port=8000, reload=True)
```

### 2. 运行与访问
1. 执行代码：`python main.py`；
2. 访问接口文档（FastAPI自动生成）：
   - 交互式文档：http://127.0.0.1:8000/docs（数媒生友好，可直接测试接口）；
   - 备用文档：http://127.0.0.1:8000/redoc。

### 3. 核心语法解析（结合之前的知识点）
| 语法/功能          | 数媒场景理解                | 代码示例                          |
|---------------------|-----------------------------|-----------------------------------|
| `**字典` 解包       | 快速传递素材属性到数据库    | `material_db.append(**new_mat)`   |
| 解包赋值 `a,b=c,d`  | 提取素材核心属性            | `name, type_, size = mat["name"], mat["type"], mat["size"]` |
| Pydantic模型        | 校验素材参数（避免格式错误） | `class MaterialModel(BaseModel):` |
| 路径参数 `/{name}`  | 按素材名称精准查询          | `@app.get("/materials/{material_name}")` |

## 三、关键功能拓展（数媒生常用）
### 1. 批量素材操作（解包+列表推导式）
```python
# 接口4：批量删除素材（POST请求，接收列表）
@app.post("/materials/batch/delete", summary="批量删除素材")
def batch_delete_materials(names: list[str]):
    # 保留不在删除列表中的素材（列表推导式）
    global material_db
    material_db = [mat for mat in material_db if mat["name"] not in names]
    return {"code": 200, "msg": f"已删除素材：{names}", "剩余素材": [mat["name"] for mat in material_db]}
```

### 2. 素材类型过滤（查询参数）
```python
# 接口5：按类型过滤素材（如只查图片/音频）
@app.get("/materials/filter/type", summary="按类型过滤素材")
def filter_material_by_type(material_type: str):
    filtered = [mat for mat in material_db if mat["type"] == material_type]
    return {"code": 200, "count": len(filtered), "data": filtered}
```

 

## 五、核心优势（数媒生为什么学FastAPI）
1. **零成本文档**：自动生成可视化接口文档，不用手动写说明，团队协作更高效；
2. **强类型校验**：避免上传错误格式的素材（如非图片文件标为图片类型）；
3. **极速开发**：几行代码就能搭建素材管理后端，适配数媒小项目快速落地；
4. **兼容之前的代码**：可直接调用之前写的 `Material` 类，复用素材解析逻辑。

## 六、避坑提示
1. 运行报错 `ModuleNotFoundError`：确保安装了所有依赖（`pip install fastapi uvicorn python-multipart`，`python-multipart` 用于文件上传）；
2. 端口被占用：修改 `port` 参数（如 `port=8001`）；
3. 跨域问题：如果前端调用API，需安装 `pip install fastapi-cors`，并添加跨域配置：
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # 允许所有前端域名
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

如果需要把之前的 `Material`/`ImageMaterial` 类整合到FastAPI中（比如上传文件后自动解析分辨率/时长），我可以补充完整代码。