<%*
// 1. 字典维护
const domainDict = {
	"技术(Tech)": { cn: "技术", en: "Tech", abbr: "TECH", emoji: "⚙️" },
    "艺术(Art)": { cn: "艺术", en: "Art", abbr: "ART", emoji: "🎨" },
    "哲学(Phi)": { cn: "哲学", en: "Philosophy", abbr: "PHIL", emoji: "🏛️" },
    "数学(Math)": { cn: "数学", en: "Mathematics", abbr: "MATH", emoji: "🔢" },
    "管理学(Mgr)": { cn: "管理学", en: "Management", abbr: "MGMT", emoji: "📊" },
    "系统工程(SE)": { cn: "系统工程", en: "SystemEngine", abbr: "SE", emoji: "📊" }
};

// 【关键修复】在 try 块外部声明变量，给它们一个“全局”身份
let info, termCn, termEn, termAbbr, termAliase,fileName, newFileName;

try {
    // 2. 选择领域
    const fields = Object.keys(domainDict);
    const selectedField = await tp.system.suggester(fields, fields);

    if (!selectedField) {
        throw new Error("用户取消了选择");
    }

    // 赋值给外部声明的变量
    info = domainDict[selectedField];
    //检查未命名笔记
    fileName = tp.file.title;
    termCn = fileName;
	const defaultNames = ["未命名", "untitled", "无标题"];
	if (!fileName || defaultNames.includes(fileName.toLowerCase())) {
	     input= await tp.system.prompt("请输入笔记主题:", "", true);
		 termCn = input.trim();
	     if (input.includes("(") && input.includes(")")) {
			// 拆分中文和英文
			const parts = input.match(/^(.*?)\s*\(([^)]+)\)/);
			if (parts) {
				termCn = parts[1].trim();   // 提取结果: 色谱
				termEn = parts[2].trim(); // 提取结果: Color Palette
				termAliase =`${termCn}`
			}
		}
	} 
		 
	//输入英文
	if (!termEn){
		termEn = await tp.system.prompt("请输入英文术语名");
		termAliase =`${termCn}`
	}
	
    termAbbr = await tp.system.prompt("请输入缩略语")||"";
	
	
	newFileName = (termEn&&termEn.trim())? `${termCn}(${termEn.trim()})`:termCn;
	await tp.file.rename(newFileName);

} catch (error) {
    new Notice("⚠️ 脚本提醒: " + error.message);
    // 【关键修复】出错时的兜底数据，确保正文渲染不会报错
    info = { cn: "未知", en: "Unknown", abbr: "N/A", emoji: "❓" };
    termCn = tp.file.title;
    termEn = "Unknown";
    termAbbr = "N/A";
}
-%>
---
category: 术语笔记
type: term
aliases: <% termAliase %>
domain: <% info.cn %>
domain_en: <% info.en %>
abbr: <% termAbbr %>
tags: [术语, <% info.cn %>]
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
---

# <% info.emoji %> <% termCn %>

## 📋 基本信息
- **中文全称**：<% termCn %>
- **英文全称**：<% termEn %>
- **缩写/代号**：<% termAbbr %>
- **所属领域**：[[<% info.cn %>]] (<% info.en %>)

## 🔍 定义与内涵
> 在 <% info.cn %> 语境下，该术语的核心定义是：
>