---
tags: ["AI", "LLM", "可视化", "开源工具", "大模型"]
category: 计算机·AI机器学习
aliases: ["开源大语言模型可视化工具", "LLM可视化框架大全"]
type: note
description: 专注展示Transformer模型中token间的关联权重，揭示模型"`关注重点`"
create-date: 2025-12-19
---
### 开源LLM可视化工具&框架全解（按功能分类）
---

### 一、注意力机制可视化（模型理解核心）
专注展示Transformer模型中token间的关联权重，揭示模型"`关注重点`"

| 工具名称                         | 核心功能                                                  | 适用场景             | 技术栈                  | GitHub                                                     |
| ---------------------------- | ----------------------------------------------------- | ---------------- | -------------------- | ---------------------------------------------------------- |
| **BertViz**                  | 三层视图（Head/Neuron/Model），支持Hugging Face全量模型，热力图+流向图双展示 | 学术研究、教学演示、模型调试   | Python/Notebook      | https://github.com/jessevig/bertviz                        |
| **Transformers Interpret**   | 一键生成注意力热力图，追踪决策路径，定位回答偏差原因                            | 模型评估、错误分析、可解释性研究 | PyTorch/Hugging Face | https://github.com/cdpierse/transformers-interpret         |
| **LLM Attention Visualizer** | 分层注意力可视化，token重要性评分，注意力流图                             | 快速分析、轻量级研究       | Streamlit/Python     | https://github.com/sunnynguyen-ai/llm-attention-visualizer |
| **GPT-2 Visualizer**（开源版）    | 零代码在线界面，输入文本即时查看GPT-2注意力分布                            | 教学演示、快速验证        | JavaScript/HTML      | https://github.com/openai/gpt-2-visualizer                 |

---

### 二、Token嵌入/语义空间可视化（语义理解）
将高维向量降维为2D/3D图形，展示文本语义关系与聚类模式

| 工具名称                                 | 核心功能                                | 适用场景          | 技术栈                | GitHub                                             |
| ------------------------------------ | ----------------------------------- | ------------- | ------------------ | -------------------------------------------------- |
| **Hugging Face Embedding Projector** | t-SNE/UMAP降维，交互式散点图，语义相似度分析         | 词嵌入研究、语义聚类分析  | 云端/本地双模式           | https://github.com/huggingface/embedding-projector |
| **TensorBoard Embedding Projector**  | 与PyTorch/TensorFlow无缝集成，实时监控训练中嵌入变化 | 模型训练监控、嵌入质量评估 | TensorFlow/PyTorch | https://github.com/tensorflow/tensorboard          |
| **UMAP Visualizer for LLM**          | 自定义维度与颜色映射，批量嵌入分析，支持大型语料            | 深度语义研究、语料分析   | Python/UMAP-learn  | https://github.com/lmcinnes/umap                   |

---

### 三、模型结构可视化（架构解析）
展示LLM的层级结构、模块连接与参数分布，理解模型"物理组成"

| 工具名称                          | 核心功能                                  | 适用场景          | 技术栈                | GitHub                                          |
| ----------------------------- | ------------------------------------- | ------------- | ------------------ | ----------------------------------------------- |
| **Netron**                    | 支持.pt/.onnx/.bin等模型格式，交互式拓扑图，逐层展开查看细节 | 模型结构分析、部署前验证  | C++/WebAssembly    | https://github.com/lutzroeder/netron            |
| **Hugging Face Model Viewer** | 自动解析模型配置，生成结构示意图，支持对比不同模型             | 快速了解模型架构、教学演示 | 云端/JavaScript      | https://huggingface.co/docs/hub/model-viewer    |
| **TensorBoard Graphs**        | 展示计算图，跟踪张量流向，分析计算瓶颈                   | 模型开发、训练优化     | TensorFlow/PyTorch | https://github.com/tensorflow/tensorboard       |
| **Transformer Lens**          | 可视化Transformer内部计算过程，神经元激活追踪，注意力头分析   | 深度模型研究、神经元级调试 | PyTorch            | https://github.com/neelnanda-io/TransformerLens |
|                               |                                       |               |                    |                                                 |
|                               |                                       |               |                    |                                                 |

---

### 四、生成过程/推理路径可视化（决策逻辑）
展示LLM文本生成的每一步选择与推理过程，揭示"思考逻辑"

| 工具名称 | 核心功能 | 适用场景 | 技术栈 | GitHub |
|---------|---------|---------|--------|--------|
| **ReasonGraph** | 实时更新推理路径图，支持50+主流LLM，多种推理方法可视化 | 复杂推理任务分析、Agent行为监控 | React/Python | https://github.com/ZongqianLi/ReasonGraph |
| **OpenAI Token Probability Viewer**（开源替代） | 展示token生成概率分布，top-k候选对比，生成轨迹追踪 | 生成质量评估、幻觉问题排查 | Python/Streamlit | https://github.com/ricklamers/llm-explorer |
| **LMV (Language Model Visualizer)** | 生成过程全链路追踪，注意力+概率双维度展示 | 模型生成机制研究 | Python | https://github.com/brendanbycroft/llm-visualization |

---

### 五、LLM工作流/应用构建可视化（低代码开发）
拖拽式界面构建LLM应用，可视化工作流与RAG管道，降低开发门槛

| 工具名称 | 核心功能 | 适用场景 | 技术栈 | GitHub |
|---------|---------|---------|--------|--------|
| **LangFlow** | LangChain官方可视化工具，拖拽构建LLM工作流，RAG管道，Agent开发 | 快速原型、企业应用构建 | TypeScript/Python | https://github.com/logspace-ai/langflow |
| **Flowise** | 拖放式UI构建LLM应用，支持自定义组件，内置RAG模板 | 非技术用户、快速开发 | TypeScript/Node.js | https://github.com/FlowiseAI/Flowise |
| **Dify** | 可视化工作流编排，Agent构建，50+内置工具集成，模型管理 | 全栈LLM应用开发 | React/Python | https://github.com/langgenius/dify |
| **ChainForge** | 提示工程可视化工具，系统比较不同LLM输出，模块化实验 | 提示优化、模型对比 | JavaScript | https://github.com/emergentmind/chainforge |

---

### 六、全流程可观测性可视化（应用监控）
追踪LLM应用从请求到响应的完整生命周期，监控性能与质量

| 工具名称                          | 核心功能                             | 适用场景           | 技术栈               | GitHub                                          |
| ----------------------------- | -------------------------------- | -------------- | ----------------- | ----------------------------------------------- |
| **Langfuse**                  | 提示日志、token使用统计、延迟分析、错误追踪，支持多模型对比 | 生产环境监控、成本优化    | TypeScript/Python | https://github.com/langfuse/langfuse            |
| **PostHog LLM Observability** | 全链路追踪，用户交互分析，性能监控，自定义仪表盘         | 产品迭代、用户行为研究    | Python/JavaScript | https://github.com/PostHog/posthog              |
| **LLM Canvas**                | 对话流可视化，工具调用追踪，分支树探索，隐私保护模式       | 复杂对话分析、Agent调试 | Python/Streamlit  | https://github.com/LittleLittleCloud/llm-canvas |

---

### 七、特殊用途可视化工具
针对特定LLM场景的专业可视化方案

1.  **LLM Transparency Tool**（Meta）
    - 核心：交互式分析Transformer内部工作机制，神经元激活可视化
    - 适用：模型可解释性研究，学术论文复现
    - GitHub：https://github.com/facebookresearch/llm-transparency

2.  **Reasoning Visualizer**
    - 核心：可视化LLM链式思考（CoT）过程，推理步骤拆解
    - 适用：复杂推理任务分析，教育场景
    - GitHub：https://github.com/kyegomez/reasoning-visualizer

3.  **Open WebUI**（原Ollama WebUI）
    - 核心：本地LLM可视化交互界面，模型管理，提示模板，历史记录
    - 适用：本地模型调试，个人LLM应用
    - GitHub：https://github.com/open-webui/open-webui

---

### 选型指南：如何选择合适的开源LLM可视化工具
| 需求场景 | 推荐工具 | 关键考量 |
|---------|---------|---------|
| 学术研究/模型可解释性 | BertViz + Transformer Lens | 支持自定义分析，可导出研究数据 |
| 教学演示/快速验证 | GPT-2 Visualizer + Hugging Face Embedding Projector | 零代码，可视化效果好 |
| 企业应用开发 | LangFlow/Flowise + Dify | 低代码，支持团队协作 |
| 生产环境监控 | Langfuse + PostHog | 性能稳定，支持大规模部署 |
| 本地模型调试 | Open WebUI + Netron | 离线可用，适配本地模型 |

---

### 关键提醒
1.  **开源LLM友好**：上述工具对开源模型（如Llama 3、Mistral）支持最完整，闭源模型（GPT-4o）受限于API权限，可视化能力有限
2.  **技术门槛差异**：
    - 低代码工具（LangFlow/Flowise）：适合快速开发，无需深度学习背景
    - 代码级工具（BertViz/Transformer Lens）：适合深度研究，需Python/ML基础
3.  **生态兼容性**：优先选择适配Hugging Face生态的工具，可兼容绝大多数开源LLM
