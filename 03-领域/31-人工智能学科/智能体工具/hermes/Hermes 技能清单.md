---
tags:
  - AI
  - AI-Agent
  - hermes
description: Hermes Agent 84 个内置技能按影响力分级清单：Agent 自举、MLOps 全栈、创意产出、产品覆盖。
type: note
create-date: 2026-04-30
---
[[hermes|Hermes 工具入口]]

## 一等 — Agent 自身进化

| 技能                                                                            | 价值                                          |
| ----------------------------------------------------------------------------- | ------------------------------------------- |
| `claude-code` / `codex` / `opencode`                                          | 把 Claude Code / Codex / OpenCode 当子代理用，并行编码 |
| `plan` + `subagent-driven-development` + `writing-plans`                      | 先写计划、再拆成子代理并行执行、两阶段审查                       |
| `requesting-code-review` + `systematic-debugging` + `test-driven-development` | 安全扫描 → 质量门禁 → 自动修复；4 阶段根因调试；红绿重构            |
| `hermes-agent-skill-authoring`                                                | 写 Skill 的 Skill，自举                          |

## 二等 — MLOps 全栈

| 技能                                             | 价值                                    |
| ---------------------------------------------- | ------------------------------------- |
| `axolotl` / `unsloth` / `fine-tuning-with-trl` | 三大微调框架全覆盖（YAML 配置 / 2-5x 加速 / RLHF）   |
| `evaluating-llms-harness`                      | 标准化评测（MMLU/GSM8K 等）                   |
| `obliteratus`                                  | 消除 LLM 拒绝——diff-in-means abliteration |
| `segment-anything-model`                       | 零样本图像分割                               |
| `audiocraft-audio-generation`                  | MusicGen 文本到音乐                        |

## 三等 — 创意产出

| 技能                         | 价值                                   |
| -------------------------- | ------------------------------------ |
| `baoyu-infographic`        | 21 布局 × 21 风格知识可视化                   |
| `manim-video`              | 3Blue1Brown 风格数学动画                   |
| `popular-web-designs`      | 54 个知名设计系统（Stripe/Linear/Vercel）精确复刻 |
| `songwriting-and-ai-music` | Suno AI 作曲提示词工程                      |
| `p5js`                     | 生成艺术 / 着色器 / 3D                      |

## 四等 — 产品广度覆盖

| 类别 | 覆盖 |
|------|------|
| GitHub | `github-pr-workflow` `github-code-review` `github-issues` `github-repo-management` `codebase-inspection` |
| SaaS | `google-workspace` `notion` `airtable` `linear` `powerpoint` |
| Apple | `apple-notes` `apple-reminders` `imessage` `findmy` |
| 媒体 | `youtube-content` `spotify` `gif-search` `heartmula` `songsee` |
| 研究 | `arxiv` `blogwatcher` `polymarket` `research-paper-writing` `llm-wiki` |

## 最有区分度的 5 个

1. `claude-code` — agent 调用 agent，委托编码
2. `obliteratus` — 拒绝向量消除
3. `manim-video` — 数学动画
4. `axolotl` — 微调框架
5. `baoyu-infographic` — 知识可视化

Hermes Hub 上有更多社区贡献的 Skill，可用 `hermes skill install` 搜索安装。
