---
tags:
  - AI
  - AI-Agent
  - hermes
  - moc
description: Hermes Agent 85 个内置技能全量内容地图，按类别索引，覆盖所有已安装 Skill。更新于 2026-05-01。
type: moc
create-date: 2026-05-01
---

[[03-领域/31-人工智能学科/智能体工具/hermes/hermes|Hermes 工具入口]] | [[Hermes 技能清单|按影响力分级版]]

> 共 85 个技能，20 个类别。由 `~/.hermes/skills/` 自动生成。

## Apple 生态

| 技能 | 说明 |
|------|------|
| `apple-notes` | Manage Apple Notes via memo CLI: create, search, edit. |
| `apple-reminders` | Apple Reminders via remindctl: add, list, complete. |
| `findmy` | Track Apple devices/AirTags via FindMy.app on macOS. |
| `imessage` | Send and receive iMessages/SMS via the imsg CLI on macOS. |

## 自主 AI Agent

| 技能 | 说明 |
|------|------|
| `claude-code` | Delegate coding to Claude Code CLI (features, PRs). |
| `codex` | Delegate coding to OpenAI Codex CLI (features, PRs). |
| `hermes-agent` | Configure, extend, or contribute to Hermes Agent. |
| `opencode` | Delegate coding to OpenCode CLI (features, PR review). |

## 创意产出

| 技能 | 说明 |
|------|------|
| `architecture-diagram` | Dark-themed SVG architecture/cloud/infra diagrams as HTML. |
| `ascii-art` | ASCII art: pyfiglet, cowsay, boxes, image-to-ascii. |
| `ascii-video` | ASCII video: convert video/audio to colored ASCII MP4/GIF. |
| `baoyu-comic` | Knowledge comics (知识漫画): educational, biography, tutorial. |
| `baoyu-infographic` | Infographics: 21 layouts x 21 styles (信息图, 可视化). |
| `claude-design` | Design one-off HTML artifacts (landing, deck, prototype). |
| `design-md` | Author/validate/export Google's DESIGN.md token spec files. |
| `excalidraw` | Hand-drawn Excalidraw JSON diagrams (arch, flow, seq). |
| `humanizer` | Humanize text: strip AI-isms and add real voice. |
| `ideation` | Generate project ideas via creative constraints. |
| `manim-video` | Manim CE animations: 3Blue1Brown math/algo videos. |
| `p5js` | p5.js sketches: gen art, shaders, interactive, 3D. |
| `pixel-art` | Pixel art w/ era palettes (NES, Game Boy, PICO-8). |
| `popular-web-designs` | 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. |
| `songwriting-and-ai-music` | Songwriting craft and Suno AI music prompts. |
| `touchdesigner-mcp` | Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 native tools. |

## 数据科学

| 技能 | 说明 |
|------|------|
| `jupyter-live-kernel` | Iterative Python via live Jupyter kernel (hamelnb). |

## DevOps

| 技能 | 说明 |
|------|------|
| `webhook-subscriptions` | Webhook subscriptions: event-driven agent runs. |

## Dogfood

| 技能 | 说明 |
|------|------|
| `dogfood` | Exploratory QA of web apps: find bugs, evidence, reports. |

## 邮件

| 技能 | 说明 |
|------|------|
| `himalaya` | Himalaya CLI: IMAP/SMTP email from terminal. |

## 游戏

| 技能 | 说明 |
|------|------|
| `minecraft-modpack-server` | Host modded Minecraft servers (CurseForge, Modrinth). |
| `pokemon-player` | Play Pokemon via headless emulator + RAM reads. |

## GitHub 工作流

| 技能 | 说明 |
|------|------|
| `codebase-inspection` | Inspect codebases w/ pygount: LOC, languages, ratios. |
| `github-auth` | GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login. |
| `github-code-review` | Review PRs: diffs, inline comments via gh or REST. |
| `github-issues` | Create, triage, label, assign GitHub issues via gh or REST. |
| `github-pr-workflow` | GitHub PR lifecycle: branch, commit, open, CI, merge. |
| `github-repo-management` | Clone/create/fork repos; manage remotes, releases. |

## MCP 协议

| 技能 | 说明 |
|------|------|
| `native-mcp` | MCP client: connect servers, register tools (stdio/HTTP). |

## 媒体

| 技能 | 说明 |
|------|------|
| `gif-search` | Search/download GIFs from Tenor via curl + jq. |
| `heartmula` | HeartMuLa: Suno-like song generation from lyrics + tags. |
| `songsee` | Audio spectrograms/features (mel, chroma, MFCC) via CLI. |
| `spotify` | Spotify: play, search, queue, manage playlists and devices. |
| `youtube-content` | YouTube transcripts to summaries, threads, blogs. |

## MLOps

| 技能 | 说明 |
|------|------|
| `audiocraft-audio-generation` | AudioCraft: MusicGen text-to-music, AudioGen text-to-sound. |
| `axolotl` | Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO). |
| `dspy` | DSPy: declarative LM programs, auto-optimize prompts, RAG. |
| `evaluating-llms-harness` | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). |
| `fine-tuning-with-trl` | TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF. |
| `huggingface-hub` | HuggingFace hf CLI: search/download/upload models, datasets. |
| `llama-cpp` | llama.cpp local GGUF inference + HF Hub model discovery. |
| `obliteratus` | OBLITERATUS: abliterate LLM refusals (diff-in-means). |
| `outlines` | Outlines: structured JSON/regex/Pydantic LLM generation. |
| `segment-anything-model` | SAM: zero-shot image segmentation via points, boxes, masks. |
| `serving-llms-vllm` | vLLM: high-throughput LLM serving, OpenAI API, quantization. |
| `unsloth` | Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM. |
| `weights-and-biases` | W&B: log ML experiments, sweeps, model registry, dashboards. |

## 笔记

| 技能 | 说明 |
|------|------|
| `hxc-obsidian-vault` | 维护 HXC Obsidian Vault 的笔记规范：MOC 归属判断、frontmatter 模板、安全操作约束。 |
| `obsidian` | Read, search, and create notes in the Obsidian vault. |

## 生产力

| 技能 | 说明 |
|------|------|
| `airtable` | Airtable REST API via curl. Records CRUD, filters, upserts. |
| `google-workspace` | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. |
| `linear` | Linear: manage issues, projects, teams via GraphQL + curl. |
| `maps` | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. |
| `nano-pdf` | Edit PDF text/typos/titles via nano-pdf CLI (NL prompts). |
| `notion` | Notion API via curl: pages, databases, blocks, search. |
| `ocr-and-documents` | Extract text from PDFs/scans (pymupdf, marker-pdf). |
| `powerpoint` | Create, read, edit .pptx decks, slides, notes, templates. |

## 红队/越狱

| 技能 | 说明 |
|------|------|
| `godmode` | Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN. |

## 研究

| 技能 | 说明 |
|------|------|
| `arxiv` | Search arXiv papers by keyword, author, category, or ID. |
| `blogwatcher` | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. |
| `llm-wiki` | Karpathy's LLM Wiki: build/query interlinked markdown KB. |
| `polymarket` | Query Polymarket: markets, prices, orderbooks, history. |
| `research-paper-writing` | Write ML papers for NeurIPS/ICML/ICLR: design→submit. |

## 智能家居

| 技能 | 说明 |
|------|------|
| `openhue` | Control Philips Hue lights, scenes, rooms via OpenHue CLI. |

## 社交媒体

| 技能 | 说明 |
|------|------|
| `xurl` | X/Twitter via xurl CLI: post, search, DM, media, v2 API. |

## 软件开发

| 技能 | 说明 |
|------|------|
| `debugging-hermes-tui-commands` | Debug Hermes TUI slash commands: Python, gateway, Ink UI. |
| `hermes-agent-skill-authoring` | Author in-repo SKILL.md: frontmatter, validator, structure. |
| `node-inspect-debugger` | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. |
| `pjx-common-auditor` | Audit knowledge management vaults and software R&D projects — structure, naming, MOC load, frontmatter, link hygiene, governance boundaries, lifecycle references, and concept-scope alignment. |
| `plan` | Plan mode: write markdown plan to .hermes/plans/, no exec. |
| `python-debugpy` | Debug Python: pdb REPL + debugpy remote (DAP). |
| `requesting-code-review` | Pre-commit review: security scan, quality gates, auto-fix. |
| `subagent-driven-development` | Execute plans via delegate_task subagents (2-stage review). |
| `systematic-debugging` | 4-phase root cause debugging: understand bugs before fixing. |
| `test-driven-development` | TDD: enforce RED-GREEN-REFACTOR, tests before code. |
| `writing-plans` | Write implementation plans: bite-sized tasks, paths, code. |

## 元宝

| 技能 | 说明 |
|------|------|
| `yuanbao` | Yuanbao (元宝) groups: @mention users, query info/members. |
