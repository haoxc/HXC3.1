# Google Maps UX 框架深度分析

> 面向 GIS 数字孪生基座设计的参考解读

---

## 一、设计哲学总纲

Google Maps 的 UX 建立在一个核心信条之上：**地图是主角，UI 是配角**。所有界面元素——搜索栏、面板、控件、弹窗——都作为浮层 (overlay) 叠加在全屏地图画布之上，永远不会完全遮挡地图。这种「地图优先」(Map-first) 的理念贯穿了从信息架构到微交互的每一个设计决策。

---

## 二、信息架构总览
Google Maps 的信息架构由 **4 个功能区** 组成，它们浮于地图画布之上，形成清晰的视觉层级：
<svg width="100%" viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="50" width="600" height="440" rx="20" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.8"/>
  <text x="340" y="78" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#0C447C">地图画布层 (Map Canvas)</text>
  <text x="340" y="96" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">全屏沉浸式底图 · 所有 UI 浮于其上</text>

  <rect x="70" y="118" width="320" height="50" rx="12" fill="#EEEDFE" stroke="#AFA9EC" stroke-width="0.5"/>
  <text x="230" y="140" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#3C3489">搜索栏 (Search Bar)</text>
  <text x="230" y="156" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">全局入口 · 语音输入 · 筛选器</text>

  <rect x="420" y="118" width="190" height="50" rx="12" fill="#F1EFE8" stroke="#B4B2A9" stroke-width="0.5"/>
  <text x="515" y="140" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444441">用户头像 / 图层</text>
  <text x="515" y="156" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">账户 · 地图类型切换</text>

  <rect x="70" y="188" width="320" height="220" rx="12" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="230" y="214" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#085041">侧面板 / 底部抽屉</text>
  <text x="230" y="232" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">POI 详情 · 路线 · 评论</text>

  <rect x="90" y="250" width="130" height="36" rx="8" fill="#9FE1CB" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="155" y="272" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#04342C">地点详情卡</text>

  <rect x="240" y="250" width="130" height="36" rx="8" fill="#9FE1CB" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="305" y="272" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#04342C">路线规划面板</text>

  <rect x="90" y="300" width="130" height="36" rx="8" fill="#9FE1CB" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="155" y="322" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#04342C">评论 / 照片</text>

  <rect x="240" y="300" width="130" height="36" rx="8" fill="#9FE1CB" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="305" y="322" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#04342C">收藏 / 列表</text>

  <rect x="90" y="350" width="280" height="36" rx="8" fill="#9FE1CB" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="230" y="372" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#04342C">街景 / 时间线 / 分享</text>

  <rect x="420" y="188" width="190" height="120" rx="12" fill="#FAEEDA" stroke="#EF9F27" stroke-width="0.5"/>
  <text x="515" y="214" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#633806">地图控件</text>
  <text x="515" y="232" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">缩放 / 指南针 / 定位</text>
  <rect x="440" y="252" width="150" height="36" rx="8" fill="#FAC775" stroke="#EF9F27" stroke-width="0.5"/>
  <text x="515" y="274" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#412402">+/- · 3D · 罗盘</text>

  <rect x="420" y="328" width="190" height="80" rx="12" fill="#FAECE7" stroke="#F0997B" stroke-width="0.5"/>
  <text x="515" y="354" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#712B13">快捷操作</text>
  <text x="515" y="372" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">导航 · 实况 · 分享</text>
  <text x="515" y="390" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">浮动按钮 (FAB)</text>

  <rect x="70" y="426" width="540" height="46" rx="10" fill="#F1EFE8" stroke="#B4B2A9" stroke-width="0.5"/>
  <text x="340" y="454" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444441">底部导航栏：探索 · 通勤 · 已保存 · 贡献 · 动态</text>
</svg>

**关键设计决策：**

| 区域 | 定位 | 行为 |
|------|------|------|
| 搜索栏 | 全局入口 | 常驻顶部，支持语音、筛选 chip |
| 侧面板 / 底部抽屉 | 信息展示 | 桌面端左侧面板 / 移动端底部抽屉 |
| 地图控件 | 视角操作 | 右侧浮动，缩放/旋转/定位 |
| 快捷操作 | 核心动作 | FAB 浮动按钮，1-click 导航 |
| 底部导航栏 | 功能切换 | 探索/通勤/已保存/贡献/动态 |

---

## 三、空间布局模型

### 3.1 桌面端布局

<svg width="100%" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowG" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#1D9E75" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
  </defs>

  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">桌面端空间分区</text>

  <rect x="40" y="40" width="600" height="290" rx="8" fill="none" stroke="#B4B2A9" stroke-width="0.5" stroke-dasharray="4 2"/>
  <text x="440" y="200" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#B4B2A9">Map Canvas (100%)</text>

  <rect x="56" y="52" width="220" height="32" rx="8" fill="#EEEDFE" stroke="#AFA9EC" stroke-width="0.5"/>
  <text x="166" y="72" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#3C3489">搜索栏</text>

  <rect x="56" y="92" width="220" height="220" rx="10" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="166" y="122" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#085041">左侧面板</text>
  <text x="166" y="142" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">宽度 ≈ 400px (≈30%)</text>
  <text x="166" y="166" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">可折叠 / 可拖拽</text>
  <text x="166" y="190" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">独立滚动区域</text>
  <text x="166" y="214" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">· POI 详情</text>
  <text x="166" y="232" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">· 路线信息</text>
  <text x="166" y="250" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">· 搜索结果列表</text>
  <text x="166" y="268" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#666">· 街景入口</text>
  <text x="166" y="296" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#999">与地图滚动互不干扰</text>

  <rect x="584" y="52" width="44" height="130" rx="6" fill="#FAEEDA" stroke="#EF9F27" stroke-width="0.5"/>
  <text x="606" y="95" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#633806">+</text>
  <text x="606" y="115" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#633806">−</text>
  <text x="606" y="135" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#633806">◎</text>
  <text x="606" y="160" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#633806">⊕</text>

  <line x1="276" y1="200" x2="320" y2="200" stroke="#1D9E75" stroke-width="1" marker-end="url(#arrowG)"/>
  <text x="330" y="196" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">面板操作与</text>
  <text x="330" y="210" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">地图双向联动</text>
</svg>

**桌面端设计要点：**

- **左侧面板**宽度约 400px (占屏幕 ≈30%)，面板折叠时地图自动扩展到全宽
- 面板拥有**独立滚动区域**，与地图的拖拽/缩放操作互不干扰
- 搜索栏**嵌入面板顶部**，而非独立于面板之外
- 右侧地图控件 (缩放、罗盘、定位) 采用**垂直堆叠**布局

### 3.2 移动端布局

<svg width="100%" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowT" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#D85A30" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
  </defs>

  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">移动端底部抽屉 — 三档吸附模型</text>

  <rect x="40" y="50" width="170" height="320" rx="14" fill="none" stroke="#B4B2A9" stroke-width="1"/>
  <text x="125" y="145" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#ccc">Map</text>
  <rect x="40" y="280" width="170" height="90" rx="0" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <rect x="95" y="286" width="60" height="4" rx="2" fill="#5DCAA5" opacity="0.6"/>
  <text x="125" y="308" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">Peek (120px)</text>
  <text x="125" y="324" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">名称 + 评分</text>
  <text x="125" y="340" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">快捷按钮行</text>
  <text x="125" y="392" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#0F6E56">① Peek 态</text>

  <rect x="255" y="50" width="170" height="320" rx="14" fill="none" stroke="#B4B2A9" stroke-width="1"/>
  <text x="340" y="110" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#ccc">Map</text>
  <rect x="255" y="190" width="170" height="180" rx="0" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <rect x="310" y="196" width="60" height="4" rx="2" fill="#5DCAA5" opacity="0.6"/>
  <text x="340" y="218" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">Half (50%)</text>
  <text x="340" y="236" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">详情摘要</text>
  <text x="340" y="254" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">照片轮播</text>
  <text x="340" y="272" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">操作按钮行</text>
  <text x="340" y="290" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">评论预览</text>
  <text x="340" y="392" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#0F6E56">② Half 态</text>

  <rect x="470" y="50" width="170" height="320" rx="14" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <rect x="525" y="58" width="60" height="4" rx="2" fill="#5DCAA5" opacity="0.6"/>
  <text x="555" y="82" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">Full (90%)</text>
  <text x="555" y="104" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">完整详情页</text>
  <text x="555" y="122" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">全部评论</text>
  <text x="555" y="140" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">照片网格</text>
  <text x="555" y="158" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">营业时间</text>
  <text x="555" y="176" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">附近推荐</text>
  <text x="555" y="194" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">问答区域</text>
  <text x="555" y="392" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#0F6E56">③ Full 态</text>

  <path d="M216 310 Q235 310 235 270 Q235 230 254 230" fill="none" stroke="#D85A30" stroke-width="1" marker-end="url(#arrowT)"/>
  <text x="236" y="260" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#D85A30">上拉</text>

  <path d="M431 230 Q450 230 450 270 Q450 310 469 310" fill="none" stroke="#D85A30" stroke-width="1" marker-end="url(#arrowT)"/>
  <text x="450" y="260" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#D85A30">上拉</text>
</svg>

**移动端底部抽屉设计要点：**

| 吸附档位 | 高度 | 显示内容 | 手势 |
|---------|------|---------|------|
| **Peek** | ~120px | 名称、评分、快捷按钮 | 上拉展开 |
| **Half** | ~50% | 详情摘要、照片、操作行 | 上拉/下滑 |
| **Full** | ~90% | 完整信息、评论、推荐 | 下滑收起 |

- 抽屉顶部有**拖拽指示条** (drag handle)，暗示可手势操作
- 到达 Full 态时，顶部仍保留 ~10% 的地图可见区，维持空间感知
- 快速下滑可直接从 Full 跳回 Peek，无需逐级收起

---

## 四、核心交互模式

### 4.1 渐进式信息披露 (Progressive Disclosure)

这是 Google Maps 最核心的交互设计模式。用户从浏览到导航的完整流程被分为 **5 个层级**，每层只展示当前任务所需的最少信息量：

<svg width="100%" viewBox="0 0 680 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowD" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#888" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
    <marker id="arrowBack" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#B4B2A9" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
  </defs>

  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">渐进式信息披露 — 5 层模型</text>

  <text x="60" y="60" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="500" fill="#999">L0</text>
  <rect x="80" y="44" width="500" height="40" rx="8" fill="#F1EFE8" stroke="#B4B2A9" stroke-width="0.5"/>
  <text x="330" y="68" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444441">浏览模式 — 地图 + 图标标记 + 搜索栏</text>

  <line x1="330" y1="84" x2="330" y2="108" stroke="#888" stroke-width="0.8" marker-end="url(#arrowD)"/>
  <text x="344" y="100" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">点击标记 / 搜索</text>

  <text x="60" y="134" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="500" fill="#999">L1</text>
  <rect x="80" y="118" width="500" height="40" rx="8" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="330" y="142" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#085041">预览卡片 — 名称 · 评分 · 类型 · 快捷按钮</text>

  <line x1="330" y1="158" x2="330" y2="182" stroke="#888" stroke-width="0.8" marker-end="url(#arrowD)"/>
  <text x="344" y="174" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">上拉抽屉 / 点击卡片</text>

  <text x="60" y="210" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="500" fill="#999">L2</text>
  <rect x="80" y="192" width="500" height="52" rx="8" fill="#EEEDFE" stroke="#AFA9EC" stroke-width="0.5"/>
  <text x="330" y="214" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#3C3489">详情面板 — 地址 / 营业时间 / 评论 / 照片</text>
  <text x="330" y="232" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#534AB7">操作行：路线 · 保存 · 分享 · 电话</text>

  <line x1="330" y1="244" x2="330" y2="268" stroke="#888" stroke-width="0.8" marker-end="url(#arrowD)"/>
  <text x="344" y="260" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">点击「路线」</text>

  <text x="60" y="290" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="500" fill="#999">L3</text>
  <rect x="80" y="274" width="500" height="52" rx="8" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="330" y="296" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#0C447C">路线模式 — 多方案对比 + 实时交通叠加</text>
  <text x="330" y="314" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#185FA5">驾车 · 公交 · 步行 · 骑行 · 叫车</text>

  <line x1="330" y1="326" x2="330" y2="350" stroke="#888" stroke-width="0.8" marker-end="url(#arrowD)"/>
  <text x="344" y="342" text-anchor="start" font-family="sans-serif" font-size="12" fill="#666">点击「开始导航」</text>

  <text x="60" y="376" text-anchor="end" font-family="sans-serif" font-size="11" font-weight="500" fill="#999">L4</text>
  <rect x="80" y="358" width="500" height="52" rx="8" fill="#FAECE7" stroke="#F0997B" stroke-width="0.5"/>
  <text x="330" y="380" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#712B13">导航模式 — 全屏 + 语音 + 实时重路由</text>
  <text x="330" y="398" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#993C1D">地图视角自动切换为第一人称跟随</text>

  <path d="M70 380 C40 380, 40 64, 70 64" fill="none" stroke="#B4B2A9" stroke-width="0.5" stroke-dasharray="4 2" marker-end="url(#arrowBack)"/>
  <text x="28" y="225" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#999" transform="rotate(-90, 28, 225)">返回 / ESC 可跳回 L0</text>

  <rect x="100" y="434" width="150" height="30" rx="6" fill="#FAEEDA" stroke="#EF9F27" stroke-width="0.5"/>
  <text x="175" y="453" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#633806">最少点击原则</text>

  <rect x="270" y="434" width="150" height="30" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="345" y="453" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">上下文保持原则</text>

  <rect x="440" y="434" width="150" height="30" rx="6" fill="#EEEDFE" stroke="#AFA9EC" stroke-width="0.5"/>
  <text x="515" y="453" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#3C3489">空间连续性原则</text>
</svg>

**三大子原则：**

1. **最少点击原则**：从搜索到导航最多 3 次点击 (搜索 → 选结果 → 路线 → 导航)
2. **上下文保持原则**：层级切换时地图不跳转、不刷新，保持用户的空间认知
3. **空间连续性原则**：面板展开/收起使用动画过渡，不产生视觉断裂

### 4.2 面板-地图双向联动 (Bi-directional Sync)

这是 Google Maps 体验流畅感的关键：面板与地图之间的每一次交互都是**双向的、实时的**。

| 用户操作 | 面板响应 | 地图响应 |
|---------|---------|---------|
| 点击地图标记 | 底部弹出预览卡 | 标记放大高亮 |
| 搜索输入 | 结果列表更新 | Pin 标记叠加到地图 |
| Hover 列表项 | 该项高亮 | 对应标记高亮 + 信息气泡 |
| 拖动地图 | 列表更新为视口范围内 | 标记按视口过滤 |
| 点击路线方案 | 方案详情展开 | 地图绘制该路线 |
| 面板关闭 | 面板收起 | 地图恢复默认状态 |

### 4.3 搜索交互流程

```
用户输入
  ├→ 实时联想建议 (历史 + 热门 + 收藏)
  ├→ Chip 快速筛选器 (餐厅/加油站/药店/ATM/...)
  ├→ 结果基于当前视口 + 缩放级别
  │
  ├→ 搜索结果呈现方式:
  │   ├ 列表模式: 面板内滚动列表
  │   ├ 标记模式: 地图上 Pin 标记
  │   └ 双向联动: hover 列表 ↔ 高亮标记
  │
  └→ 选中结果:
      ├ 地图飞行至目标位置 (animated flyTo)
      ├ 面板切换为详情模式
      └ 搜索栏显示选中项名称
```

---

## 五、视觉设计系统

### 5.1 色彩体系

<svg width="100%" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg">
  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">Google Maps 色彩语义系统</text>

  <rect x="40" y="44" width="90" height="44" rx="6" fill="#4285F4"/>
  <text x="85" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">Google Blue</text>
  <text x="85" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">导航/选中态</text>

  <rect x="146" y="44" width="90" height="44" rx="6" fill="#34A853"/>
  <text x="191" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">Green</text>
  <text x="191" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">畅通/成功</text>

  <rect x="252" y="44" width="90" height="44" rx="6" fill="#FBBC04"/>
  <text x="297" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">Yellow</text>
  <text x="297" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">缓行/警告</text>

  <rect x="358" y="44" width="90" height="44" rx="6" fill="#EA4335"/>
  <text x="403" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">Red</text>
  <text x="403" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">拥堵/错误</text>

  <rect x="464" y="44" width="90" height="44" rx="6" fill="#F9AB00"/>
  <text x="509" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">Amber</text>
  <text x="509" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">公交线路</text>

  <rect x="570" y="44" width="90" height="44" rx="6" fill="#5C6BC0"/>
  <text x="615" y="62" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">Indigo</text>
  <text x="615" y="78" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">步行路线</text>

  <text x="40" y="116" font-family="sans-serif" font-size="12" fill="#666">底图色板：</text>

  <rect x="40" y="126" width="60" height="30" rx="4" fill="#F5F5F3" stroke="#ddd" stroke-width="0.5"/>
  <text x="70" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Land</text>

  <rect x="112" y="126" width="60" height="30" rx="4" fill="#A5D6A7"/>
  <text x="142" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">Park</text>

  <rect x="184" y="126" width="60" height="30" rx="4" fill="#AADAFF"/>
  <text x="214" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#333">Water</text>

  <rect x="256" y="126" width="60" height="30" rx="4" fill="#FFFFFF" stroke="#ddd" stroke-width="0.5"/>
  <text x="286" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Road</text>

  <rect x="328" y="126" width="60" height="30" rx="4" fill="#FFECB3"/>
  <text x="358" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Highway</text>

  <rect x="400" y="126" width="60" height="30" rx="4" fill="#E8EAF6"/>
  <text x="430" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Building</text>

  <rect x="472" y="126" width="60" height="30" rx="4" fill="#F3E5F5"/>
  <text x="502" y="145" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Transit</text>

  <text x="40" y="188" font-family="sans-serif" font-size="12" fill="#666">POI 色彩语义：</text>

  <rect x="40" y="198" width="90" height="30" rx="4" fill="#D32F2F"/>
  <text x="85" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">餐饮 (红)</text>

  <rect x="146" y="198" width="90" height="30" rx="4" fill="#1976D2"/>
  <text x="191" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">购物 (蓝)</text>

  <rect x="252" y="198" width="90" height="30" rx="4" fill="#7B1FA2"/>
  <text x="297" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">休闲 (紫)</text>

  <rect x="358" y="198" width="90" height="30" rx="4" fill="#0097A7"/>
  <text x="403" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">服务 (青)</text>

  <rect x="464" y="198" width="90" height="30" rx="4" fill="#F57C00"/>
  <text x="509" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">交通 (橙)</text>

  <rect x="570" y="198" width="90" height="30" rx="4" fill="#388E3C"/>
  <text x="615" y="217" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#fff">户外 (绿)</text>

  <text x="340" y="252" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#999">色彩 = 语义 · 用户无需阅读文字即可识别类别</text>
</svg>

**色彩设计要点：**

- **交通流量**使用红黄绿三色渐变，与交通灯心智模型一致
- **POI 类别**用色彩而非形状区分，保证在小尺寸下的可辨识度
- **底图配色**极度克制，使用低饱和度色彩，确保叠加数据层的可读性
- **夜间模式**采用深灰底 + 降饱和度 + 提亮道路，而非简单反色

### 5.2 排版层级

| 层级      | 用途      | 字号      | 字重            | 颜色       |
| ------- | ------- | ------- | ------------- | -------- |
| H1      | 地点名称    | 20-22px | Bold (700)    | 纯黑       |
| H2      | 分类标题    | 16px    | Medium (500)  | 深灰       |
| Body    | 地址、描述   | 14px    | Regular (400) | 中灰       |
| Caption | 营业时间、标签 | 12px    | Regular (400) | 浅灰       |
| Chip    | 筛选标签    | 12-13px | Medium (500)  | 品牌蓝 / 深灰 |

### 5.3 图标系统

- **POI 图标**：采用 Material Icons 圆形风格，放置在彩色圆形底板上
- **操作图标**：24px 线性图标，与 Material Design 一致
- **地图标记**：倒水滴形 + 内嵌类别图标，支持选中态放大 + 投影
- **聚合标记**：数字气泡，缩小级别时自动聚合相近 POI

---

## 六、图层系统 (Layer System)

<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">图层系统 — 基础层 (互斥) + 叠加层 (可组合)</text>

  <rect x="40" y="44" width="280" height="110" rx="10" fill="none" stroke="#85B7EB" stroke-width="0.8" stroke-dasharray="4 2"/>
  <text x="180" y="64" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#185FA5">基础图层 (三选一)</text>

  <rect x="58" y="78" width="76" height="56" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="96" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">默认</text>
  <text x="96" y="116" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#185FA5">矢量路网</text>

  <rect x="144" y="78" width="76" height="56" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="182" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">卫星</text>
  <text x="182" y="116" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#185FA5">影像底图</text>

  <rect x="230" y="78" width="76" height="56" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="268" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">地形</text>
  <text x="268" y="116" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#185FA5">等高线</text>

  <rect x="360" y="44" width="280" height="240" rx="10" fill="none" stroke="#5DCAA5" stroke-width="0.8" stroke-dasharray="4 2"/>
  <text x="500" y="64" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0F6E56">叠加图层 (可多选)</text>

  <rect x="378" y="78" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="434" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">交通实况</text>

  <rect x="510" y="78" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="566" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">公交线路</text>

  <rect x="378" y="126" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="434" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">骑行路线</text>

  <rect x="510" y="126" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="566" y="148" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">3D 建筑</text>

  <rect x="378" y="174" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="434" y="196" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">室内地图</text>

  <rect x="510" y="174" width="112" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="566" y="196" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">街景覆盖</text>

  <rect x="378" y="222" width="244" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="500" y="244" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">空气质量 / 山火 / 天气 (特殊事件)</text>

  <text x="340" y="296" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#444">最终渲染 = 基础层 × 1 + 叠加层 × N + POI 标记层 + UI 浮层</text>
</svg>

---

## 七、自适应 LOD (Level of Detail)

| 缩放级别 | 地理范围 | 显示内容 | 信息密度 |
|---------|---------|---------|---------|
| Z 0-5 | 洲 / 国 | 国界线、主要城市标注 | 极低 |
| Z 6-10 | 省 / 市 | 高速路网、区县标注、大型水系 | 低 |
| Z 11-14 | 区 / 街道 | 街道名、商业区域、公园 | 中 |
| Z 15-18 | 建筑级别 | 门牌号、POI 图标、3D 建筑、人行道 | 高 |
| Z 19+ | 室内级别 | 楼层切换、室内 POI、通道导航 | 极高 |

**LOD 核心规则：**

- 缩小时 POI 自动聚合为数字气泡 (clustering)
- 放大时标注逐步显现，避免视觉爆炸
- 3D 建筑仅在 Z15+ 渲染，减少低级别性能消耗
- 文字标注有碰撞检测 (collision detection)，重叠时自动隐藏低优先级标注

---

## 八、手势与多模态输入

### 8.1 地图手势

| 手势 | 桌面端 | 移动端 | 功能 |
|------|--------|-------|------|
| 拖拽 | 鼠标左键拖拽 | 单指拖动 | 平移地图 |
| 缩放 | 滚轮 / 双击 | 双指捏合 | 缩放级别 |
| 旋转 | Ctrl + 拖拽 | 双指旋转 | 地图朝向 |
| 倾斜 | Ctrl + 上下拖拽 | 双指上下滑 | 3D 倾斜角 |
| 选点 | 左键单击 | 单指点按 | 选中 POI |
| 投放标记 | 右键长按 | 长按 | 自定义标记 |

### 8.2 面板手势 (移动端)

| 手势 | 功能 |
|------|------|
| 上拉抽屉 | 展开到下一档位 (peek → half → full) |
| 下滑抽屉 | 收起到上一档位 |
| 快速下滑 | 直接关闭 (回到 peek 或消失) |
| 左右滑动 | 照片轮播 / 卡片切换 |
| 点击拖拽条 | 切换 peek ↔ half |

### 8.3 其他输入方式

- **语音输入**：搜索栏内麦克风按钮，支持自然语言 ("附近的中餐馆")
- **键盘快捷键**：桌面端支持 +/− 缩放、方向键平移、Esc 返回
- **URL 参数**：支持通过 URL 传入坐标、缩放级别、路线参数

---

## 九、性能与体验优化模式

| 策略 | 实现方式 | 目的 |
|------|---------|------|
| 瓦片按需加载 | 仅请求当前视口 + 周边 1 级缓冲区的瓦片 | 减少带宽 |
| 矢量瓦片 | 使用 vector tiles 替代 raster tiles | 缩放流畅 + 样式可变 |
| 预加载 | 用户缩放/拖拽方向预判，提前加载可能进入的瓦片 | 减少白屏 |
| 骨架屏 | 数据加载期间显示灰色占位块 | 减少感知延迟 |
| 飞行动画 | 从 A 到 B 不是瞬移，而是平滑 flyTo 动画 | 保持空间认知 |
| 渐进渲染 | 先加载低精度底图，再叠加高精度细节 | 首屏速度 |
| 标注碰撞检测 | 重叠标注自动隐藏低优先级项 | 视觉整洁 |

---

## 十、对数字孪生基座的设计映射

<svg width="100%" viewBox="0 0 680 430" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrowM" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#1D9E75" stroke-width="1.5" stroke-linecap="round"/>
    </marker>
  </defs>

  <text x="340" y="24" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="600" fill="#444">Google Maps UX → 数字孪生基座设计映射</text>

  <text x="150" y="52" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#185FA5">Google Maps 模式</text>
  <text x="530" y="52" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0F6E56">数字孪生基座适配</text>

  <rect x="50" y="64" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="86" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">地图画布优先</text>
  <line x1="250" y1="82" x2="430" y2="82" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="64" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="86" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">3D 场景常驻主视图</text>

  <rect x="50" y="114" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="136" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">底部抽屉 / 侧面板</text>
  <line x1="250" y1="132" x2="430" y2="132" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="114" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="136" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">浮层属性面板</text>

  <rect x="50" y="164" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="186" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">渐进式 5 层披露</text>
  <line x1="250" y1="182" x2="430" y2="182" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="164" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="186" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">概览→详情→操控→监控</text>

  <rect x="50" y="214" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="236" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">面板 ↔ 地图联动</text>
  <line x1="250" y1="232" x2="430" y2="232" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="214" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="236" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">面板 ↔ 3D 对象联动</text>

  <rect x="50" y="264" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="286" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">缩放级别 LOD</text>
  <line x1="250" y1="282" x2="430" y2="282" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="264" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="286" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">模型精度动态加载</text>

  <rect x="50" y="314" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="336" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">可组合图层系统</text>
  <line x1="250" y1="332" x2="430" y2="332" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="314" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="336" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">数据维度图层叠加</text>

  <rect x="50" y="364" width="200" height="36" rx="6" fill="#E6F1FB" stroke="#85B7EB" stroke-width="0.5"/>
  <text x="150" y="386" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#0C447C">上下文感知搜索</text>
  <line x1="250" y1="382" x2="430" y2="382" stroke="#1D9E75" stroke-width="0.8" marker-end="url(#arrowM)"/>
  <rect x="430" y="364" width="200" height="36" rx="6" fill="#E1F5EE" stroke="#5DCAA5" stroke-width="0.5"/>
  <text x="530" y="386" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="500" fill="#085041">场景感知搜索与筛选</text>

  <text x="340" y="424" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#999">保留空间认知模式 · 替换地理信息为数字孪生数据</text>
</svg>

### 具体适配建议

| #   | Google Maps 模式 | 数字孪生适配                                     | 实施优先级 |
| --- | -------------- | ------------------------------------------ | ----- |
| 1   | 地图画布优先         | 3D 引擎 (Cesium/Three.js) 作为常驻主视图，所有 UI 浮于其上 | ★★★★★ |
| 2   | 底部抽屉三档吸附       | 设备/资产属性面板采用 peek/half/full 三档，手势驱动         | ★★★★★ |
| 3   | 渐进式披露          | 远看楼宇轮廓 → 近看楼层 → 再近看设备 → 点击看实时数据            | ★★★★★ |
| 4   | 双向联动           | 点击 3D 模型高亮 + 弹面板，面板操作反向高亮 3D 对象            | ★★★★☆ |
| 5   | 图层系统           | 基础层: 地图/卫星/白模；叠加层: IoT/告警/能耗/人流            | ★★★★☆ |
| 6   | LOD 自适应        | 3D 模型精度 + 数据标注密度 跟随相机距离动态切换                | ★★★★☆ |
| 7   | 上下文搜索          | 搜索设备/空间时自动限定当前 3D 视口范围                     | ★★★☆☆ |
| 8   | 飞行动画           | 场景跳转使用平滑 flyTo 而非瞬移，保持空间感知                 | ★★★☆☆ |

---

## 附录：8 条设计原则速查

1. **Map-first** — 3D 场景/地图是永不遮挡的「第零层」
2. **Overlay model** — 所有 UI 元素浮于画布之上，不用传统分栏布局
3. **Progressive disclosure** — 5 层渐进，每层只展示当前任务所需
4. **Bottom sheet + snap points** — 移动端 peek/half/full 三档手势切换
5. **Bi-directional sync** — 面板与地图之间 hover/click/drag 双向实时联动
6. **Contextual search** — 搜索结果基于当前视口 + 缩放级别
7. **Adaptive LOD** — 信息密度跟随缩放级别动态调整
8. **Composable layers** — 基础层互斥 + 叠加层可组合的图层体系

---
*本文档用于 GIS 数字孪生基座的 UX 设计参考，基于 Google Maps 2024-2025 版本分析。*
