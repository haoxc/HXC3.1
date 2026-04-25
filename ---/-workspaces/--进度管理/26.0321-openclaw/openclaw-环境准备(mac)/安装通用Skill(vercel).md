---
aliases:
  - skill/安装/vercel仓库
  - skill/安装/通过github 仓库
tags:
  - skill/安装
description:
type:
ref-url:
  - https://github.com/vercel-labs/skills
---
## 内容
- 通过skill github地址

```
npx skills  add  <skill技能github地址>
```

### 指南
通过此CLI，用户可便捷地安装技能，安装源格式丰富，涵盖GitHub简写、完整GitHub URL、GitLab URL、任意git URL及本地路径等。安装时可选用多种选项，如全局安装、指定代理、指定技能安装、列出可用技能等，并提供了诸多安装示例。同时，该工具具备多种命令操作，像列出已安装技能、搜索技能、移除技能、检查更新及更新技能等。此外，还详细阐述了代理技能的概念、创建技能的方法、技能发现机制、兼容性、故障排查及相关环境变量，且提到此工具会收集匿名使用数据以优化，遵循MIT许可协议。
**重要亮点**
- **技能安装**：可使用 `npx skills add` 命令安装技能，支持多种源格式，如 `npx skills add vercel - labs/agent - skills` 用GitHub简写格式安装。安装选项多样， `-g` 用于全局安装， `-a` 可指定特定代理， `-s` 能指定特定技能， `--list` 可列出可用技能不安装。例如， `npx skills add vercel - labs/agent - skills - a claude - code - a opencode` 可将技能安装到指定代理。
- **安装范围与方法**：安装范围分项目（默认，路径为 `.//skills/` ，与项目一同提交供团队共享）和全局（使用 `-g` 标志，路径为 `~//skills/` ，所有项目可用）。安装方法有推荐的符号链接（为各代理创建到规范副本的符号链接，单一数据源，便于更新）和复制（为各代理创建独立副本，适用于不支持符号链接的情况）。
- **其他命令操作**： `npx skills list` 可列出已安装技能（别名 `ls` ），如 `npx skills list -g` 列出全局技能； `npx skills find` 能交互式或按关键字搜索技能，如 `npx skills find typescript` ； `npx skills remove` 用于移除已安装技能，如 `npx skills remove web - design - guidelines` 移除指定技能； `npx skills check` 检查技能更新， `npx skills update` 更新所有技能到最新版本， `npx skills init` 创建新的SKILL.md模板。
- **代理技能概念与创建**：代理技能是可复用指令集，扩展编码代理能力，通过SKILL.md文件定义，文件含YAML前置元数据（ `name` 和 `description` 为必填字段， `metadata.internal` 为可选，设为 `true` 可隐藏技能，仅当 `INSTALL_INTERNAL_SKILLS = 1` 时可见并可安装）。技能目录含SKILL.md文件，文件内容为技能激活时代理遵循的指令，还应描述使用场景和步骤。