---
tags: [工具]
description: //模板变量
type: note
create-date: 2025-12-21
---

<%*
//模板变量
const fileType = "术语"; //🚨修改当前主题

//获取用户输入的主题（必填）
const area= "信息技术(it)"
userTopic = tp.file.title
const defaultNames = ["未命名", "untitled", "无标题"];
// 如果当前名称属于默认列表中的一个，则提示输入
//console.debug(userTopic)
if (userTopic && defaultNames.includes(userTopic.toLowerCase())) {
	userTopic = await tp.system.prompt("请输入笔记主题:", "", true);
}

const fileTitle = fileType +"-" + userTopic.trim();
await tp.file.rename(fileTitle);

//配置 Frontmatter
const title = userTopic;
const creationDate = tp.date.now("YYYY-MM-DD HH:mm");

abbr= `"term://${userTopic}( )"`;
if (area.trim()){
	abbr= `"term://${area}/${userTopic}"`;
}

//const statusOptions = ["Draft", "Published", "In Review"];
//const status = await tp.system.suggester(statusOptions, statusOptions, false, "选择状态");

// 构建包含动态数据的 YAML 字符串
	//status: ${status}
const metaData = `---
aliases:
  - ${abbr}
  - ${userTopic}
description:
title: ${title}
type: term
tags:
  - ${fileType}
created: ${creationDate}
---`;

// 将 YAML 字符串添加到笔记内容中
tR += metaData;

//动态生成内容生成内容和结构
const content = `
`;
tR+= content;
%>
## 概述
-
