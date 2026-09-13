import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const base = "https://supermugogogo.github.io/roll-and-read/";
const meta = [
  ["daily-activities","日常活动","Daily Activities","日常生活"],
  ["interest-activities","兴趣活动","Interests and Activities","日常生活"],
  ["phone-calls","打电话","Phone Calls","日常生活"],
  ["actions","动作","Action Verbs","日常生活"],
  ["my-school","我的学校","My School","学校生活"],
  ["school-supplies","学校文具","School Supplies","学校生活"],
  ["school-subjects","学校科目","School Subjects","学校生活"],
  ["positions-objects","方位与物品","Positions and Objects","地点与方位"],
  ["rooms-furniture","房间与家具","Rooms and Furniture","地点与方位"],
  ["school-countries","学校与国家","School and Countries","地点与方位"],
  ["countries-people","国家与人物","Countries and People","地点与方位"],
  ["dates-birthdays","日期与生日","Dates and Birthdays","时间与日期"],
  ["days-time","星期与时间","Days and Time","时间与日期"],
  ["food","美食","Food Vocabulary","食物词汇"],
  ["fruit","水果","Fruit Vocabulary","食物词汇"],
  ["colors","颜色","Colors","基础词汇"],
  ["rooms-positions","房间与方位","Rooms and Positions","地点与方位"],
  ["animals-descriptions","动物与描述","Animals and Descriptions","动物主题"]
];

const first = [
  {
    index: 0,
    file: "worksheets/01-daily-activities/ChatGPT Image Jun 5, 2026, 11_43_59 AM.png",
    description: "通过掷骰子和看图朗读，练习起床、吃饭、上学等常用日常活动词汇。",
    vocabulary: [["起床","qǐ chuáng","to get up"],["穿衣服","chuān yī fu","to get dressed"],["吃饭","chī fàn","to eat"],["刷牙","shuā yá","to brush teeth"],["洗脸","xǐ liǎn","to wash one's face"],["上学","shàng xué","to go to school"],["上课","shàng kè","to attend class"],["放学","fàng xué","school is over"],["做功课","zuò gōng kè","to do homework"],["两点半","liǎng diǎn bàn","half past two"],["睡觉","shuì jiào","to sleep"],["打篮球","dǎ lán qiú","to play basketball"]].map(([word,pinyin,meaning])=>({word,pinyin,meaning})),
    practiceSheets: [["剪贴匹配","worksheets/01-daily-activities/cut-paste.png"],["看图选词（全词汇）","worksheets/01-daily-activities/choice-all.png"],["看图描红","worksheets/01-daily-activities/trace.png"]].map(([title,file])=>({title,file})),
    games: [["骰子闯关棋","worksheets/01-daily-activities/dice-adventure.html"],["听音选词","worksheets/01-daily-activities/listening-choice.html"],["句子小侦探","worksheets/01-daily-activities/sentence-builder.html"],["汉字接接乐","worksheets/01-daily-activities/pinyin-match.html"]].map(([title,file])=>({title,file}))
  },
  {
    index: 1,
    file: "worksheets/02-interest-activities/ChatGPT Image Jun 25, 2026, 10_55_58 AM.png",
    description: "通过掷骰子和看图朗读，练习电视、一家人、一起、游戏、音乐、游来游去和飞来飞去等词语。",
    vocabulary: [["电视","diàn shì","television"],["一家人","yì jiā rén","the whole family"],["一起","yì qǐ","together"],["游戏","yóu xì","game; to play"],["音乐","yīn yuè","music"],["游来游去","yóu lái yóu qù","to swim around"],["飞来飞去","fēi lái fēi qù","to fly around"]].map(([word,pinyin,meaning])=>({word,pinyin,meaning})),
    practiceSheets: [["剪贴匹配","worksheets/02-interest-activities/cut-paste.png"],["看图选词（全词汇）","worksheets/02-interest-activities/choice-all.png"],["看图描红","worksheets/02-interest-activities/trace.png"]].map(([title,file])=>({title,file})),
    games: [["兴趣骰子闯关","worksheets/02-interest-activities/interest-dice.html"],["兴趣听音选词","worksheets/02-interest-activities/interest-listen.html"],["兴趣句子小侦探","worksheets/02-interest-activities/interest-sentence.html"],["兴趣汉字接接乐","worksheets/02-interest-activities/interest-catch.html"]].map(([title,file])=>({title,file}))
  }
];

const raw = fs.readFileSync(path.join(root, "all-worksheet-details.js"), "utf8");
const details = JSON.parse(raw.slice(raw.indexOf("[") , raw.lastIndexOf("]") + 1));
const data = [...first, ...details].sort((a,b)=>a.index-b.index);
const esc = (s="") => String(s).replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll('"',"&quot;");
const href = (p="") => "../../" + p;

for (const [index, item] of data.entries()) {
  const [slug, zh, en, group] = meta[index];
  const canonical = `${base}topics/${slug}/`;
  const words = item.vocabulary || [];
  const keywordText = words.map(w=>w.word).join("、");
  const description = `${zh}儿童中文词汇学习资源，提供可打印作业纸、剪贴匹配、看图选词、描红练习和互动小游戏。${en} printable Mandarin worksheets and games for beginners.`;
  const games = (item.games || []).map(g=>`<a class="resource-link game-link" href="${href(g.file)}"><strong>${esc(g.title)}</strong><span>开始游戏 Play →</span></a>`).join("");
  const practice = (item.practiceSheets || []).map(p=>`<a class="practice-card" href="${href(p.file)}"><img src="${href(p.file)}" alt="${esc(zh)}${esc(p.title)}可打印中文作业纸" loading="lazy"><strong>${esc(p.title)}</strong><span>打开打印版 Open printable →</span></a>`).join("");
  const vocabulary = words.map(w=>`<li><strong>${esc(w.word)}</strong><span>${esc(w.pinyin)}</span><small>${esc(w.meaning)}</small></li>`).join("");
  const schema = {"@context":"https://schema.org","@type":"LearningResource","name":`${zh}中文词汇作业纸与小游戏 | ${en} Chinese Worksheets`,"description":description,"url":canonical,"inLanguage":["zh-CN","en"],"educationalLevel":"Beginner","learningResourceType":["Worksheet","Educational game"],"isAccessibleForFree":true,"keywords":`${zh}, 儿童中文作业纸, 中文词汇小游戏, printable Mandarin worksheets, ${en}`};
  const html = `<!doctype html>
<html lang="zh-CN"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(zh)}中文作业纸与小游戏｜${esc(en)} Chinese Worksheets</title>
<meta name="description" content="${esc(description)}"><link rel="canonical" href="${canonical}">
<meta property="og:type" content="website"><meta property="og:title" content="${esc(zh)}中文作业纸与小游戏｜${esc(en)}">
<meta property="og:description" content="${esc(description)}"><meta property="og:url" content="${canonical}">
<meta property="og:image" content="${base}${encodeURI(item.file)}"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="../../topic.css?v=20260912-topics-v1">
<script type="application/ld+json">${JSON.stringify(schema).replaceAll("</","<\\/")}</script>
</head><body>
<header class="site-head"><a href="../../">中文词汇 <span>Read and Roll</span></a><nav><a href="../../">全部课程 All lessons</a></nav></header>
<main>
<nav class="crumb" aria-label="面包屑"><a href="../../">首页 Home</a><span>›</span><span>${esc(group)}</span><span>›</span><span>${esc(zh)}</span></nav>
<section class="hero"><div class="hero-copy"><p class="eyebrow">FREE PRINTABLE CHINESE LEARNING RESOURCES</p><h1>${esc(zh)}<small>${esc(en)}</small></h1><p>${esc(item.description)}</p><p class="english">Learn beginner Mandarin vocabulary through a printable Roll and Read worksheet, three companion activities, and four interactive games.</p><div class="actions"><a class="primary" href="../../#sheet-${index}">查看完整课程 View lesson</a><a href="${href(item.file)}">打开主作业纸 Open worksheet</a></div></div><figure><img src="${href(item.file)}" alt="${esc(zh)} Roll and Read 儿童中文词汇作业纸"><figcaption>Letter尺寸可打印中文词汇作业纸 · Letter-size printable Mandarin worksheet</figcaption></figure></section>
<section class="section"><p class="eyebrow">VOCABULARY</p><h2>本课词汇 <small>Words in this lesson</small></h2><p class="index-copy">本课练习：${esc(keywordText)}。</p><ul class="word-grid">${vocabulary}</ul></section>
<section class="section"><p class="eyebrow">PRINTABLE PRACTICE</p><h2>配套练习纸 <small>Companion worksheets</small></h2><div class="practice-grid">${practice}</div></section>
<section class="section"><p class="eyebrow">INTERACTIVE GAMES</p><h2>配套小游戏 <small>Interactive Chinese games</small></h2><div class="game-grid">${games}</div></section>
<section class="teacher-note"><h2>适合怎样使用？ <small>How to use</small></h2><p>适合中文初学者、海外儿童中文课堂、家庭学习和复习。先用主作业纸朗读词汇，再完成剪贴、选词和描红练习，最后用小游戏巩固。</p><p>Designed for beginner Mandarin learners, heritage-language families, homeschool practice, and elementary Chinese classrooms.</p></section>
</main><footer>© 2026 Read and Roll · Free Chinese learning resources</footer>
</body></html>`;
  const dir = path.join(root,"topics",slug);
  fs.mkdirSync(dir,{recursive:true});
  fs.writeFileSync(path.join(dir,"index.html"),html,"utf8");
}
console.log(`Built ${data.length} topic pages.`);
