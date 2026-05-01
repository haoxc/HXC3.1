---
title: Claude App 与 Claude Code 分层工作流
aliases:
  - Claude App 与 Claude Code 工作流
  - claude-app-claude-code-workflow
tags:
  - ai/智能体/工具/claude
  - 工作流
created: 2026-04-26
description: 用 Wiki 知识库方式表达 Claude App 与 Claude Code 的分层协作关系。
type: note
create-date: 2026-04-26
---
## 内容

<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="700" viewBox="0 0 1080 700" role="img" aria-labelledby="title desc" style="max-width: 100%; height: auto;">
  <title id="title">Claude App 与 Claude Code 分层工作流</title>
  <desc id="desc">Claude App 负责前台思考，Claude Code 负责后台执行和知识资产沉淀。</desc>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#596579" />
    </marker>
  </defs>

  <rect x="0" y="0" width="1080" height="700" rx="18" fill="#f7f8fb" />
  <text x="54" y="58" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="28" font-weight="700" fill="#26313f">Claude App 与 Claude Code 分层工作流</text>
  <text x="54" y="86" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="15" fill="#627084">前台思考用 Claude App，后台沉淀与执行用 Claude Code。</text>

  <rect x="44" y="120" width="468" height="420" rx="18" fill="#ffffff" stroke="#d9dee8" stroke-width="1.5" />
  <rect x="568" y="120" width="468" height="420" rx="18" fill="#ffffff" stroke="#d9dee8" stroke-width="1.5" />

  <text x="74" y="158" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="21" font-weight="700" fill="#26313f">Claude App：前台思考空间</text>
  <text x="74" y="181" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="13" fill="#627084">适合开放讨论、快速发散、表达试写、轻量原型</text>

  <text x="598" y="158" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="21" font-weight="700" fill="#26313f">Claude Code：后台执行工作流</text>
  <text x="598" y="181" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="13" fill="#627084">适合读写 Vault、拆分笔记、建立索引、形成可维护资产</text>

  <rect x="74" y="215" width="180" height="86" rx="14" fill="#eef6f2" stroke="#4d8b68" />
  <text x="96" y="246" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">1. 需求澄清</text>
  <text x="96" y="272" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">问题、目标、约束</text>

  <rect x="302" y="215" width="180" height="86" rx="14" fill="#eef6f2" stroke="#4d8b68" />
  <text x="324" y="246" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">2. 方案设计</text>
  <text x="324" y="272" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">路径、结构、取舍</text>

  <rect x="74" y="345" width="180" height="86" rx="14" fill="#eef6f2" stroke="#4d8b68" />
  <text x="96" y="376" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">3. 写作表达</text>
  <text x="96" y="402" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">口径、草稿、版本</text>

  <rect x="302" y="345" width="180" height="86" rx="14" fill="#eef6f2" stroke="#4d8b68" />
  <text x="324" y="376" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">4. 原型表达</text>
  <text x="324" y="402" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">Artifacts、Demo</text>

  <path d="M254 258 H302" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />
  <path d="M392 301 V345" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />
  <path d="M302 388 H254" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />

  <path d="M392 431 C392 500 292 500 292 555" stroke="#596579" stroke-width="2.2" fill="none" stroke-dasharray="6 6" marker-end="url(#arrowhead)" />

  <rect x="598" y="215" width="180" height="86" rx="14" fill="#f3f0fb" stroke="#7562a8" />
  <text x="620" y="246" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">5. 输入材料</text>
  <text x="620" y="272" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">读取笔记、资料、目录</text>

  <rect x="826" y="215" width="180" height="86" rx="14" fill="#f3f0fb" stroke="#7562a8" />
  <text x="848" y="246" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">6. 结构建模</text>
  <text x="848" y="272" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">MOC、Wiki、子笔记</text>

  <rect x="598" y="345" width="180" height="86" rx="14" fill="#f3f0fb" stroke="#7562a8" />
  <text x="620" y="376" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">7. 文件沉淀</text>
  <text x="620" y="402" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">写入 Markdown / Vault</text>

  <rect x="826" y="345" width="180" height="86" rx="14" fill="#f3f0fb" stroke="#7562a8" />
  <text x="848" y="376" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">8. 元数据治理</text>
  <text x="848" y="402" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">frontmatter、标签、状态</text>

  <path d="M778 258 H826" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />
  <path d="M916 301 V345" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />
  <path d="M826 388 H778" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />

  <path d="M522 592 C555 592 548 402 598 402" stroke="#596579" stroke-width="2.2" fill="none" stroke-dasharray="6 6" marker-end="url(#arrowhead)" />
  <path d="M763 555 V431" stroke="#596579" stroke-width="2.2" fill="none" marker-end="url(#arrowhead)" />

  <rect x="92" y="555" width="430" height="74" rx="14" fill="#fff7e8" stroke="#c1842f" />
  <text x="126" y="586" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">进入沉淀阶段</text>
  <text x="126" y="611" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">当内容需要写入文件、复用、统计、维护</text>

  <rect x="558" y="555" width="430" height="74" rx="14" fill="#fff7e8" stroke="#c1842f" />
  <text x="592" y="586" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" font-weight="700" fill="#26313f">复盘检查</text>
  <text x="592" y="611" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="14" fill="#26313f">链接、拆分、命名、统计口径</text>

  <text x="54" y="670" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="13" fill="#627084">判断口径：只是想清楚，用 Claude App；要沉淀进 Vault、文档或项目结构，用 Claude Code。</text>
</svg>

> [!summary] 固定口径
> Claude App 负责“想清楚、说清楚、快速表达”；Claude Code 负责“读写文件、拆分结构、归档沉淀、形成可维护知识资产”。
