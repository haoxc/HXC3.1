---
tags:
  - 能力/数据处理/序列化
  - 能力/数据处理/数据校验
---

Pydantic 是 Python 中最流行的`数据验证`和`序列化库`，核心用于 **数据模型定义、类型校验、数据转换**，尤其适合 API 开发（如 [[python类库-FastAPI]] 内置依赖）、配置管理、数据解析等场景。它基于 Python 类型注解，语法简洁且功能强大，能自动处理数据校验、类型转换、错误提示，大幅减少手动校验代码。

## 一、核心特性
1. **类型注解驱动**：用 Python 原生类型注解定义数据结构，直观易懂；
2. **自动数据校验**：对输入数据进行类型、范围、格式等校验，无效数据直接抛出明确错误；
3. **数据转换**：自动将输入数据（如 JSON 字符串、字典）转换为 Python 对象，反之也能序列化对象为字典/JSON；
4. **嵌套模型支持**：支持复杂的嵌套数据结构定义；
5. **配置灵活**：可通过配置类自定义校验规则、序列化行为等；
6. **与生态兼容**：完美适配 FastAPI、Starlette、Django 等框架，支持 Pydantic V1/V2 两个主要版本（V2 基于 Rust 重构，性能提升 5-10 倍）。

## 二、快速入门（Pydantic V2）
### 1. 安装
```bash
# 安装最新版（V2）
pip install pydantic
# 如需兼容 V1 代码，安装兼容层
pip install pydantic[legacy]
```

### 2. 定义数据模型（BaseModel）
所有数据模型都需继承 `pydantic.BaseModel`，通过类型注解定义字段：
```python
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

# 定义基础模型
class User(BaseModel):
    # 必选字段（类型注解 + 可选描述）
    id: int = Field(description="用户唯一ID")
    username: str = Field(min_length=3, max_length=20, description="用户名（3-20字符）")
    email: EmailStr = Field(description="合法邮箱格式")
    # 可选字段（用 Optional 标记，默认值为 None）
    age: Optional[int] = Field(default=None, ge=0, le=120, description="年龄（0-120）")
    # 嵌套模型（字段类型为另一个 BaseModel 子类）
    address: "Address"  # 前向引用（解决循环导入或未定义问题）
    # 列表类型（元素为指定类型）
    hobbies: List[str] = Field(default_factory=list, description="兴趣爱好列表")
    # 自动生成的字段（default_factory 用于动态默认值）
    create_time: datetime = Field(default_factory=datetime.utcnow, description="创建时间")

# 定义嵌套模型（需在引用前定义，或用前向引用）
class Address(BaseModel):
    province: str
    city: str
    detail: Optional[str] = None
```

### 3. 数据校验与实例化
传入数据（字典/JSON）实例化模型，Pydantic 会自动校验并转换类型：
```python
# 合法数据
user_data = {
    "id": 1001,
    "username": "alice",
    "email": "alice@example.com",
    "age": 25,
    "address": {
        "province": "Guangdong",
        "city": "Shenzhen"
    },
    "hobbies": ["reading", "coding"]
}

# 实例化（自动校验 + 类型转换）
user = User(**user_data)
print(user)
# 输出：
# id=1001 username='alice' email='alice@example.com' age=25 address=Address(province='Guangdong', city='Shenzhen', detail=None) hobbies=['reading', 'coding'] create_time=datetime.datetime(2025, 12, 19, 8, 0, 0, tzinfo=datetime.timezone.utc)
```

### 4. 错误处理（无效数据）
如果输入数据不符合规则，会抛出 `ValidationError`，包含详细错误信息：
```python
from pydantic import ValidationError

# 无效数据（username 长度不够，email 格式错误）
invalid_data = {
    "id": "not_int",  # 类型错误
    "username": "ab",  # 长度不足
    "email": "invalid-email",  # 邮箱格式错误
    "age": 150,  # 年龄超出范围
    "address": {"province": "Guangdong"}  # 缺少必填字段 city
}

try:
    User(**invalid_data)
except ValidationError as e:
    # 打印错误详情（字典格式）
    print(e.errors())
```

输出的错误信息示例：
```python
[
    {"type": "int_parsing", "loc": ["id"], "msg": "Input should be a valid integer", "input": "not_int"},
    {"type": "string_too_short", "loc": ["username"], "msg": "String should have at least 3 characters", "input": "ab", "ctx": {"min_length": 3}},
    {"type": "value_error.email", "loc": ["email"], "msg": "value is not a valid email address", "input": "invalid-email"},
    {"type": "number_not_le", "loc": ["age"], "msg": "Input should be less than or equal to 120", "input": 150, "ctx": {"le": 120}},
    {"type": "value_error.missing", "loc": ["address", "city"], "msg": "Field required", "input": {"province": "Guangdong"}}
]
```

## 三、核心功能详解
### 1. 字段约束（Field 常用参数）
`Field` 用于定义字段的校验规则，常用参数：
- 类型相关：`type_`（显式指定类型，默认用注解）；
- 长度约束：`min_length`/`max_length`（字符串）、`min_items`/`max_items`（列表）；
- 数值约束：`ge`（>=）、`gt`（>）、`le`（<=）、`lt`（<）、`multiple_of`（倍数）；
- 默认值：`default`（固定默认值）、`default_factory`（动态默认值，如 `list`/`datetime.utcnow`）；
- 其他：`required`（是否必填）、`alias`（字段别名，序列化/反序列化用）、`description`（描述）、`regex`（正则表达式校验字符串）。

示例：
```python
class Product(BaseModel):
    name: str = Field(min_length=2, max_length=50, regex=r"^[A-Za-z0-9_]+$")  # 只允许字母、数字、下划线
    price: float = Field(gt=0, multiple_of=0.01)  # 价格>0，且为0.01的倍数（金额）
    stock: int = Field(default=0, ge=0)  # 库存默认0，不能为负
```

### 2. 数据序列化（对象转字典/JSON）
模型实例可通过以下方法转换为序列化格式：
- `model_dump()`：转为字典（V2 新增，替代 V1 的 `dict()`）；
- `model_dump_json()`：转为 JSON 字符串；
- 支持自定义序列化（通过 `Config` 或 `field_serializer`）。

示例：
```python
# 模型实例转字典
user_dict = user.model_dump()
print(user_dict["address"]["city"])  # 访问嵌套字段

# 转 JSON 字符串（支持缩进、排序键）
user_json = user.model_dump_json(indent=2, sort_keys=True)
print(user_json)

# 只序列化指定字段
user_dict_partial = user.model_dump(include={"id", "username", "email"})
print(user_dict_partial)  # {'id': 1001, 'username': 'alice', 'email': 'alice@example.com'}
```

### 3. 数据解析（外部数据转模型）
支持从多种数据源解析为模型实例：
- 字典：直接解包 `User(**dict_data)`；
- JSON 字符串：`User.model_validate_json(json_str)`；
- 文件：读取 JSON/YAML 文件后解析；
- 环境变量：结合 `pydantic-settings` 库（见下文“配置管理”）。

示例（JSON 字符串解析）：
```python
json_str = '''
{
    "id": 1002,
    "username": "bob",
    "email": "bob@example.com",
    "address": {"province": "Beijing", "city": "Beijing"}
}
'''
user2 = User.model_validate_json(json_str)
print(user2.username)  # bob
```

### 4. 配置类（Model Config）
通过内部类 `Config` 自定义模型行为（V2 推荐用 `model_config` 字典，兼容 V1 的 `Config` 类）：
```python
class User(BaseModel):
    id: int
    username: str
    password: str  # 敏感字段，序列化时需隐藏

    # V2 配置方式（推荐）
    model_config = {
        "extra": "forbid",  # 禁止传入模型未定义的字段
        "str_strip_whitespace": True,  # 自动去除字符串首尾空格
        "validate_default": True,  # 校验默认值是否符合规则
        "json_encoders": {  # 自定义类型序列化（如 datetime 转 ISO 格式）
            datetime: lambda v: v.isoformat()
        }
    }

# 测试：传入额外字段会报错
try:
    User(id=1003, username="  charlie  ", password="123456", extra_field="invalid")
except ValidationError as e:
    print(e.errors()[0]["msg"])  # "Extra inputs are not permitted"

# 字符串自动去空格
user3 = User(id=1003, username="  charlie  ", password="123456")
print(user3.username)  # charlie

# 敏感字段隐藏（需配合 field_serializer）
from pydantic import field_serializer

@field_serializer('password')
def serialize_password(self, password: str) -> str:
    return "******"  # 序列化时隐藏密码

print(user3.model_dump())  # {'id': 1003, 'username': 'charlie', 'password': '******'}
```

## 四、常见场景用法
### 1. API 数据校验（FastAPI 联动）
FastAPI 内置 Pydantic，可直接用 Pydantic 模型作为请求体/响应体，自动完成校验和文档生成：
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 请求体模型
class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=6)

# 响应体模型（隐藏密码）
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    # 模拟数据库存储
    db_user = {
        "id": 1,
        "username": user.username,
        "email": user.email
    }
    return db_user  # 自动序列化为 UserResponse 格式
```

启动服务后，访问 `http://127.0.0.1:8000/docs`，FastAPI 会自动生成含校验规则的接口文档。

### 2. 配置管理（pydantic-settings）
`pydantic-settings` 是 Pydantic 官方扩展，用于从环境变量、配置文件读取配置，自动校验：
```bash
pip install pydantic-settings
```

示例（从环境变量读取配置）：
```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # 环境变量名默认与字段名一致，可通过 alias 自定义
    DB_HOST: str = Field(default="localhost", alias="DATABASE_HOST")
    DB_PORT: int = Field(default=3306)
    DB_USER: str = Field(default="root")
    DB_PASSWORD: Optional[str] = None
    DB_NAME: str = Field(..., description="数据库名必填")  # ... 表示必填

    # 配置：从 .env 文件读取（优先于环境变量）
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# 实例化配置（自动读取环境变量/.env 文件）
settings = Settings()

# 访问配置
print(settings.DB_HOST)  # localhost（若环境变量 DATABASE_HOST 存在则优先）
print(settings.DB_NAME)  # 从 .env 或环境变量读取
```

### 3. 嵌套复杂数据
支持多层嵌套、列表嵌套模型等复杂结构：
```python
class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)
    price: float = Field(gt=0)

class Order(BaseModel):
    order_id: str = Field(regex=r"^ORD-\d{8}$")  # 订单号格式：ORD-8位数字
    user_id: int
    items: List[OrderItem]  # 列表嵌套模型
    total_amount: float = Field(gt=0)
    create_time: datetime = Field(default_factory=datetime.utcnow)

# 实例化
order_data = {
    "order_id": "ORD-20251219",
    "user_id": 1001,
    "items": [
        {"product_id": 1, "quantity": 2, "price": 99.9},
        {"product_id": 2, "quantity": 1, "price": 199.9}
    ],
    "total_amount": 399.7
}
order = Order(**order_data)
print(order.items[0].product_id)  # 1
```

## 五、V1 与 V2 主要差异
| 特性    | Pydantic V1                 | Pydantic V2                                       |
| ----- | --------------------------- | ------------------------------------------------- |
| 性能    | 纯 Python 实现，性能一般            | Rust 重构，性能提升 5-10 倍                               |
| 核心类   | `BaseModel`（主要）             | `BaseModel`（兼容，底层优化）                              |
| 序列化方法 | `dict()`、`json()`           | `model_dump()`、`model_dump_json()`（兼容旧方法）         |
| 解析方法  | `parse_obj()`、`parse_raw()` | `model_validate()`、`model_validate_json()`（兼容旧方法） |
| 配置方式  | `Config` 类                  | `model_config` 字典（推荐）+ 兼容 `Config` 类              |
| 扩展    | `pydantic.dataclasses`      | 内置支持 `@dataclass` 装饰器                             |
|       |                             |                                                   |
|       |                             |                                                   |

**迁移建议**：新项目直接用 V2；旧项目可先安装 `pydantic[legacy]` 兼容层，逐步迁移到 V2 语法。

## 六、总结
Pydantic 的核心价值是 **“用类型注解驱动数据校验与序列化”**，让开发者无需编写大量手动校验代码，同时保证数据合法性。其主要应用场景：
- API 接口请求/响应体校验（FastAPI 首选）；
- 配置文件/环境变量解析（配合 `pydantic-settings`）；
- 数据清洗与转换（如 CSV/JSON 数据解析）；
- 复杂数据结构定义（嵌套模型、列表嵌套等）。

如果需要进一步深入（如自定义校验器、数据转换器、与其他框架集成），可以告诉我具体场景！