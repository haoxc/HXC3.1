---
type: 辨析
tags: []
aliases: []
---

<%*
// 1. 获取用户输入的主题（必填）
const userTopic = await tp.system.prompt("请输入笔记主题（必填）:", "", true);
if (!userTopic.trim()) {
  return; // 空主题时直接终止执行
}

// 2. 配置 Frontmatter
const newFrontmatter = {
  type: "辨析",
  tags: ["辨析", userTopic.trim()],
  aliases: ["abbr:辨析/" + userTopic.trim()]
};
Object.assign(tp.frontmatter, newFrontmatter);

// 3. 重命名文件
const finalTitle = "辨析-" + userTopic.trim();
await tp.file.rename(finalTitle);

// 4. 生成内容标题和结构
tR += `## 辨析-${userTopic.trim()}

### 核心差异
- 差异点1：
- 差异点2：

### 适用场景
- 场景1：
- 场景2：

### 总结
`;
%>