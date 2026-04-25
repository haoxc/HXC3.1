## 一、项目基本信息
- **项目定位**：为大语言模型（LLMs）提供结构化输出工具，基于 [[python类库-Pydantic]] 实现数据验证、类型安全与 IDE 支持，核心是让开发者无需手动处理 JSON 解析、错误处理与重试，仅通过定义模型即可获取结构化数据。
- **核心指标**：12k+ GitHub 星标、910+ Fork、56 个分支、102 个标签、246 名贡献者，月下载量超 300 万次。
- **许可证**：MIT 许可证，开源免费可商用。
- **官方资源**：官网（python.useinstructor.com/）、文档、示例代码库、Discord 社区、博客教程。

## 二、核心价值：解决 LLMs 结构化输出痛点
传统从 LLMs 获取结构化数据需解决 5 大难题，Instructor 通过统一接口一站式处理：
1. 无需手动编写复杂 JSON Schema
2. 自动处理数据验证错误
3. 验证失败时自动重试（带错误提示）
4. 无需手动解析非结构化响应
5. 兼容不同 LLM 提供商的 API 差异

## 三、快速使用与安装
### 1. 安装方式
支持多种 Python 包管理工具，秒级安装：
```bash
# pip 安装
pip install instructor
# uv 安装
uv add instructor
# poetry 安装
poetry add instructor
```

### 2. 基础示例（以提取用户信息为例）
```python
import instructor
from pydantic import BaseModel

# 1. 定义结构化模型
class User(BaseModel):
    name: str
    age: int

# 2. 初始化 LLM 客户端（以 OpenAI gpt-4o-mini 为例）
client = instructor.from_provider("openai/gpt-4o-mini")

# 3. 调用 LLM 并直接获取结构化数据
user = client.chat.completions.create(
    response_model=User,  # 指定输出模型
    messages=[{"role": "user", "content": "John is 25 years old"}],
)

print(user)  # 直接输出类型安全的对象：User(name='John', age=25)
```

## 四、关键特性
### 1. 多 LLM 提供商兼容
用统一代码调用不同厂商的 LLM，支持本地模型（如 Ollama），可直接传入 API Key（无需环境变量）：
```python
# OpenAI
client = instructor.from_provider("openai/gpt-4o", api_key="sk-...")
# Anthropic Claude
client = instructor.from_provider("anthropic/claude-3-5-sonnet", api_key="sk-ant-...")
# Google Gemini
client = instructor.from_provider("google/gemini-pro")
# 本地 Ollama（如 llama3.2）
client = instructor.from_provider("ollama/llama3.2")
```

### 2. 生产级能力
- **自动重试**：验证失败时（如年龄为负数），自动携带错误信息重试（可配置 `max_retries`）：
  ```python
  from pydantic import field_validator
  class User(BaseModel):
      name: str
      age: int
      @field_validator('age')
      def validate_age(cls, v):
          if v < 0: raise ValueError('Age must be positive')
          return v
  # 自动重试 3 次
  user = client.chat.completions.create(response_model=User, messages=..., max_retries=3)
  ```
- **流式支持**：通过 `Partial[Model]` 实时获取生成中的部分结构化数据：
  ```python
  from instructor import Partial
  for partial_user in client.chat.completions.create(
      response_model=Partial[User], messages=..., stream=True
  ):
      print(partial_user)  # 逐步输出：User(name=None, age=None) → User(name="John", age=25)
  ```
- **嵌套对象提取**：自动处理复杂嵌套结构（如用户+多地址）：
  ```python
  from typing import List
  class Address(BaseModel): street: str; city: str; country: str
  class User(BaseModel): name: str; age: int; addresses: List[Address]
  # 直接提取嵌套数据
  user = client.chat.completions.create(response_model=User, messages=...)
  ```

### 3. 多语言支持
除原生 Python 外，还提供多语言实现：TypeScript、Ruby、Go、Elixir、Rust。

## 五、对比优势
| 对比对象                 | 核心优势                                 |
| -------------------- | ------------------------------------ |
| Raw JSON mode        | 无需手动写 Schema，自带数据验证、自动重试、流式与嵌套对象支持   |
| LangChain/LlamaIndex | 专注结构化提取单一场景，更轻量、更快、调试更简单（无冗余功能）      |
| 自定义解决方案              | 经数万开发者验证，覆盖边缘场景（如异常重试、嵌套解析），减少重复开发成本 |

## 六、采用与社区情况
- **企业用户**：被 OpenAI、Google、Microsoft、AWS 及众多 YC 创业公司采用。
- **社区支持**：100k+ 开发者信任，提供 GitHub Discussions 交流、贡献指南（含“good first issues”），支持提交反馈与 PR。
- **扩展推荐**：若需 Agent 能力（如类型化工具、可回放数据集、生产仪表盘），可搭配 PydanticAI（Pydantic 官方 Agent 运行时，兼容 Instructor 模型）。

## 七、快速入门资源
- **基础提取示例**：如提取产品信息（名称、价格、库存状态）。
- **详细文档**：含全面指南与最佳实践。
- **示例库**：可直接复制的代码片段（覆盖多场景）。
- **社区帮助**：Discord 社区获取实时支持。