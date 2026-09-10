const worksheets = [
  {
    group: "日常生活",
    file: "worksheets/01-daily-activities/ChatGPT Image Jun 5, 2026, 11_43_59 AM.png",
    title: "日常活动",
    description: "通过掷骰子和看图朗读，练习起床、吃饭、上学等常用日常活动词汇。",
    vocabulary: [
      { word: "起床", pinyin: "qǐ chuáng", meaning: "to get up" },
      { word: "穿衣服", pinyin: "chuān yī fu", meaning: "to get dressed" },
      { word: "吃饭", pinyin: "chī fàn", meaning: "to eat" },
      { word: "刷牙", pinyin: "shuā yá", meaning: "to brush teeth" },
      { word: "洗脸", pinyin: "xǐ liǎn", meaning: "to wash one's face" },
      { word: "上学", pinyin: "shàng xué", meaning: "to go to school" },
      { word: "上课", pinyin: "shàng kè", meaning: "to attend class" },
      { word: "放学", pinyin: "fàng xué", meaning: "school is over" },
      { word: "做功课", pinyin: "zuò gōng kè", meaning: "to do homework" },
      { word: "两点半", pinyin: "liǎng diǎn bàn", meaning: "half past two" },
      { word: "睡觉", pinyin: "shuì jiào", meaning: "to sleep" },
      { word: "打篮球", pinyin: "dǎ lán qiú", meaning: "to play basketball" }
    ],
    practiceSheets: [
      { title: "剪贴匹配", file: "worksheets/01-daily-activities/cut-paste.png" },
      { title: "看图选词（全词汇）", file: "worksheets/01-daily-activities/choice-all.png" },
      { title: "看图描红", file: "worksheets/01-daily-activities/trace.png" }
    ],
    games: [
      { title: "骰子闯关棋", file: "worksheets/01-daily-activities/dice-adventure.html" },
      { title: "听音选词", file: "worksheets/01-daily-activities/listening-choice.html" },
      { title: "句子小侦探", file: "worksheets/01-daily-activities/sentence-builder.html" },
      { title: "汉字接接乐", file: "worksheets/01-daily-activities/pinyin-match.html" }
    ]
  },
  {
    group: "日常生活", file: "worksheets/02-interest-activities/ChatGPT Image Jun 25, 2026, 10_55_58 AM.png", title: "兴趣活动",
    description: "通过掷骰子和看图朗读，练习电视、一家人、一起、游戏、音乐、游来游去和飞来飞去等词语。",
    vocabulary: [
      { word: "电视", pinyin: "diàn shì", meaning: "television" }, { word: "一家人", pinyin: "yì jiā rén", meaning: "the whole family" },
      { word: "一起", pinyin: "yì qǐ", meaning: "together" }, { word: "游戏", pinyin: "yóu xì", meaning: "game; to play" },
      { word: "音乐", pinyin: "yīn yuè", meaning: "music" }, { word: "游来游去", pinyin: "yóu lái yóu qù", meaning: "to swim around" },
      { word: "飞来飞去", pinyin: "fēi lái fēi qù", meaning: "to fly around" }
    ],
    practiceSheets: [
      { title: "剪贴匹配", file: "worksheets/02-interest-activities/cut-paste.png" },
      { title: "看图选词（全词汇）", file: "worksheets/02-interest-activities/choice-all.png" },
      { title: "看图描红", file: "worksheets/02-interest-activities/trace.png" }
    ],
    games: [
      { title: "兴趣骰子闯关", file: "worksheets/02-interest-activities/interest-dice.html" },
      { title: "兴趣听音选词", file: "worksheets/02-interest-activities/interest-listen.html" },
      { title: "兴趣句子小侦探", file: "worksheets/02-interest-activities/interest-sentence.html" },
      { title: "兴趣汉字接接乐", file: "worksheets/02-interest-activities/interest-catch.html" }
    ]
  },
  { group: "日常生活", file: "ChatGPT Image Jul 3, 2026, 02_52_59 PM.png", title: "打电话", description: "在情境中练习打电话、在家、请问、等一下和没空等常用表达。" },
  { group: "日常生活", file: "动作.png", title: "动作", description: "通过看图朗读练习看、闻、说、咬、听、拍和走等常用动作词汇。" },
  { group: "学校生活", file: "ChatGPT Image Jun 8, 2026, 02_54_07 PM.png", title: "我的学校", description: "练习幼儿园、小学、上学、同学和不同年级的中文表达。" },
  { group: "学校生活", file: "ChatGPT Image Jul 7, 2026, 01_32_16 PM.png", title: "学校文具", description: "认识橡皮、书、本子、书包、电脑、椅子、铅笔和桌子。" },
  { group: "学校生活", file: "ChatGPT Image Jul 23, 2026, 12_56_57 PM.png", title: "学校科目", description: "练习数学、社会学、写作、体育、科学、美术和图书馆等词汇。" },
  { group: "地点与方位", file: "ChatGPT Image Jun 11, 2026, 03_12_54 PM.png", title: "方位与物品", description: "通过生活物品练习上面、下面、里面、外面、前面和后面。" },
  { group: "地点与方位", file: "ChatGPT Image Jun 12, 2026, 12_07_52 PM.png", title: "房间与家具", description: "认识家里的房间、客厅、卧室、厨房、卫生间和常见家具。" },
  { group: "地点与方位", file: "ChatGPT Image Jun 16, 2026, 01_48_13 PM.png", title: "学校与国家", description: "练习住在、哪里、楼层、校长，以及中国和美国等词汇。" },
  { group: "地点与方位", file: "ChatGPT Image Jun 24, 2026, 03_14_46 PM.png", title: "国家与人物", description: "认识美国、中国、墨西哥、加拿大，并练习他是谁、几个人等问句。" },
  { group: "时间与日期", file: "ChatGPT Image Jun 23, 2026, 02_57_26 PM.png", title: "日期与生日", description: "练习今天、明天、生日、快乐、几月、几号及月份表达。" },
  { group: "时间与日期", file: "ChatGPT Image Jun 30, 2026, 11_27_45 AM.png", title: "星期与时间", description: "认识星期一到星期日，并练习昨天、今天和明天。" },
  { group: "食物词汇", file: "ChatGPT Image Jul 28, 2026, 11_05_45 AM.png", title: "美食", description: "通过掷骰子和看图朗读，认识果汁、汉堡、水饺、冰淇淋等常见食物词汇。" },
  { group: "食物词汇", file: "ChatGPT Image Jul 21, 2026, 11_29_23 AM.png", title: "水果", description: "认识草莓、西瓜、葡萄、橘子、苹果、梨和香蕉等水果词汇。" },
  { group: "基础词汇", file: "worksheets/16-colors/colors-roll-and-read.png", title: "颜色", description: "通过掷骰子和看图朗读，认识红色、黄色、绿色、蓝色、黑色、白色、紫色和粉色。" },
  { group: "地点与方位", file: "worksheets/17-home-positions/home-positions-roll-and-read.png", title: "房间与方位", description: "学习房间、方位和描述房子的常用词语。" },
  { group: "动物主题", file: "worksheets/18-animals-descriptions/animals-descriptions-roll-and-read.png", title: "动物与描述", description: "认识熊猫、狮子、斑马、老虎和袋鼠，并学习漂亮、有趣和毛等描述词。" }
];

for (const detail of globalThis.WORKSHEET_DETAIL_DATA || []) {
  Object.assign(worksheets[detail.index], detail);
}

const modules = document.querySelector("#worksheet-modules");
const library = document.querySelector(".library");
const detail = document.querySelector("#detail");
const detailImage = document.querySelector("#detail-image");
const detailTitle = document.querySelector("#detail-title");
const detailDescription = document.querySelector("#detail-description");
const downloadButton = document.querySelector("#download-button");
const printButton = document.querySelector("#print-button");
const vocabularyPanel = document.querySelector("#vocabulary-panel");
const vocabularyGrid = document.querySelector("#vocabulary-grid");
const playAllButton = document.querySelector("#play-all-button");
const stopSpeakingButton = document.querySelector("#stop-speaking-button");
const practicePanel = document.querySelector("#practice-panel");
const practiceGrid = document.querySelector("#practice-grid");
const gamePanel = document.querySelector("#game-panel");
const gameGrid = document.querySelector("#game-grid");
let activeSheet = null;
let speakingSequence = 0;
let backTarget = "home";

// Version local worksheet and game assets so browsers do not reuse stale previews.
const ASSET_VERSION = "20260910-mobile-direct-print-v2";
const source = (file) => {
  const encoded = encodeURI(file);
  return `${encoded}${encoded.includes("?") ? "&" : "?"}v=${ASSET_VERSION}`;
};

const groups = ["日常生活", "学校生活", "地点与方位", "时间与日期", "食物词汇", "基础词汇", "动物主题"];
const groupEnglish = {
  "日常生活": "Daily Life",
  "学校生活": "School Life",
  "地点与方位": "Places & Positions",
  "时间与日期": "Time & Dates",
  "食物词汇": "Food Vocabulary",
  "基础词汇": "Basic Vocabulary",
  "动物主题": "Animals"
};
const titleEnglish = [
  "Daily Activities", "Interests", "Phone Calls", "Actions", "My School", "School Supplies",
  "School Subjects", "Positions & Objects", "Rooms & Furniture", "School & Countries",
  "Countries & People", "Dates & Birthdays", "Days & Time", "Food", "Fruit", "Colors",
  "Rooms & Positions", "Animals & Descriptions"
];
const card = (sheet, index) => `
  <a class="worksheet-card" href="#sheet-${index}" aria-label="查看${sheet.title} · View ${titleEnglish[index]}">
    <div class="card-image">
      <img src="${source(sheet.file)}" alt="${sheet.title}中文词汇作业纸" loading="lazy" />
      <span class="card-index">${String(index + 1).padStart(2, "0")}</span>
    </div>
    <div class="card-meta"><span class="card-title"><span>${sheet.title}</span><small>${titleEnglish[index]}</small></span><span class="card-action"><span>查看 →</span><small>View</small></span></div>
  </a>`;

modules.innerHTML = groups.map((group, groupIndex) => {
  const cards = worksheets.map((sheet, index) => ({ sheet, index })).filter(({ sheet }) => sheet.group === group);
  return `<section class="worksheet-module tone-${groupIndex % 5}" aria-labelledby="group-${group}">
    <div class="module-head"><h2 id="group-${group}">${group}<small>${groupEnglish[group]}</small></h2><p><span>${cards.length} 张作业纸</span><small>${cards.length} worksheet${cards.length === 1 ? "" : "s"}</small></p></div>
    <div class="card-track">${cards.map(({ sheet, index }) => card(sheet, index)).join("")}</div>
  </section>`;
}).join("");

function renderRoute() {
  const sheetMatch = location.hash.match(/^#sheet-(\d+)$/);
  const practiceMatch = location.hash.match(/^#practice-(\d+)-(\d+)$/);
  const index = sheetMatch ? Number(sheetMatch[1]) : -1;
  const parentIndex = practiceMatch ? Number(practiceMatch[1]) : -1;
  const practiceIndex = practiceMatch ? Number(practiceMatch[2]) : -1;
  const parentSheet = worksheets[parentIndex];
  const practiceSheet = parentSheet?.practiceSheets?.[practiceIndex];
  const sheet = practiceSheet ? {
    ...practiceSheet,
    description: `配合“${parentSheet.title}”词汇学习使用的 Letter 练习纸。`
  } : worksheets[index];
  const isDetail = Boolean(sheet);
  library.hidden = isDetail;
  detail.hidden = !isDetail;
  detail.classList.toggle("practice-detail", Boolean(practiceSheet));
  if (!isDetail) return;
  const imageSource = source(sheet.file);
  activeSheet = sheet;
  detailImage.src = imageSource;
  detailImage.alt = `${sheet.title}中文词汇作业纸`;
  detailTitle.textContent = sheet.title;
  detailDescription.textContent = sheet.description;
  backTarget = practiceSheet ? `sheet-${parentIndex}` : "home";
  renderVocabulary(practiceSheet ? [] : (sheet.vocabulary || []));
  renderPracticeSheets(practiceSheet ? [] : (sheet.practiceSheets || []), index);
  renderGames(practiceSheet ? [] : (sheet.games || []));
  window.scrollTo({ top: 0, behavior: "auto" });
}

function clearSpeakingState() {
  vocabularyGrid.querySelectorAll(".is-speaking").forEach((card) => card.classList.remove("is-speaking"));
}

function speakWord(word, card, onEnd) {
  if (!("speechSynthesis" in window)) return;
  window.speechSynthesis.cancel();
  clearSpeakingState();
  card?.classList.add("is-speaking");
  const utterance = new SpeechSynthesisUtterance(word);
  utterance.lang = "zh-CN";
  utterance.rate = 0.78;
  utterance.onend = () => {
    card?.classList.remove("is-speaking");
    onEnd?.();
  };
  utterance.onerror = () => card?.classList.remove("is-speaking");
  window.speechSynthesis.speak(utterance);
}

function renderVocabulary(words) {
  vocabularyPanel.hidden = words.length === 0;
  vocabularyGrid.innerHTML = words.map((item, index) => `
    <button class="word-card" type="button" data-word-index="${index}" aria-label="朗读${item.word}">
      <span class="word-hanzi">${item.word}</span>
      <span class="word-copy">
        <span class="word-pinyin">${item.pinyin}</span>
        <span class="word-meaning">${item.meaning}</span>
      </span>
      <span class="word-speaker" aria-hidden="true">🔊</span>
    </button>`).join("");
  vocabularyGrid.querySelectorAll(".word-card").forEach((card) => {
    card.addEventListener("click", () => {
      speakingSequence += 1;
      speakWord(words[Number(card.dataset.wordIndex)].word, card);
    });
  });
}

function playAllWords() {
  const words = activeSheet?.vocabulary || [];
  if (!words.length) return;
  const sequence = ++speakingSequence;
  const cards = [...vocabularyGrid.querySelectorAll(".word-card")];
  const playNext = (index) => {
    if (sequence !== speakingSequence || index >= words.length) return;
    speakWord(words[index].word, cards[index], () => playNext(index + 1));
  };
  playNext(0);
}

function renderPracticeSheets(sheets, parentIndex) {
  practicePanel.hidden = sheets.length === 0;
  practiceGrid.innerHTML = sheets.map((sheet, index) => `
    <a class="practice-card" href="#practice-${parentIndex}-${index}" aria-label="查看${sheet.title}">
      <img src="${source(sheet.file)}" alt="${sheet.title}练习纸预览" loading="lazy">
      <span class="practice-card-copy">
        <span class="practice-card-title">${sheet.title}</span>
        <span class="practice-card-action"><span>PNG · Letter</span><span>查看 →</span></span>
      </span>
    </a>`).join("");
}

function renderGames(games) {
  gamePanel.hidden = games.length === 0;
  gameGrid.innerHTML = games.map((game) => `
    <a class="game-card is-ready" href="${source(game.file)}">
      <span class="game-preview"><iframe src="${source(game.file)}${source(game.file).includes("?") ? "&" : "?"}preview=1" tabindex="-1" loading="lazy" aria-hidden="true"></iframe></span>
      <span class="game-card-copy"><strong>${game.title}</strong><span>开始游戏 →</span></span>
    </a>`).join("");
}

window.addEventListener("hashchange", renderRoute);
document.querySelector("#back-button").addEventListener("click", () => { location.hash = backTarget; });

async function saveWorksheet() {
  if (!activeSheet) return;
  const filename = `${activeSheet.title}-Read-and-Roll.png`;
  const originalLabel = downloadButton.firstChild.textContent;
  downloadButton.firstChild.textContent = "正在下载 ";
  downloadButton.disabled = true;

  try {
    await downloadAsset(activeSheet.file, filename);
  } catch (error) {
    alert("下载未完成，请刷新页面后重试。");
  } finally {
    downloadButton.firstChild.textContent = originalLabel;
    downloadButton.disabled = false;
  }
}

async function downloadAsset(fileName, downloadName) {
  let file;
  const embeddedImage = globalThis.WORKSHEET_ASSETS?.[fileName];
  if (embeddedImage) {
    const base64 = embeddedImage.slice(embeddedImage.indexOf(",") + 1);
    const binary = atob(base64);
    const bytes = new Uint8Array(binary.length);
    for (let index = 0; index < binary.length; index += 1) bytes[index] = binary.charCodeAt(index);
    file = new Blob([bytes], { type: "image/png" });
  } else {
    const response = await fetch(source(fileName));
    if (!response.ok) throw new Error("无法读取作业纸文件");
    file = await response.blob();
  }
  const objectUrl = URL.createObjectURL(file);
  const link = document.createElement("a");
  link.href = objectUrl;
  link.download = downloadName;
  link.style.display = "none";
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(objectUrl), 2000);
}

function printWorksheet() {
  if (!activeSheet) return;
  const openPrintDialog = () => {
    document.body.classList.add("is-printing");
    requestAnimationFrame(() => requestAnimationFrame(() => window.print()));
  };
  if (detailImage.complete && detailImage.naturalWidth > 0) {
    openPrintDialog();
  } else {
    detailImage.addEventListener("load", openPrintDialog, { once: true });
  }
}

window.addEventListener("afterprint", () => document.body.classList.remove("is-printing"));

downloadButton.addEventListener("click", saveWorksheet);
printButton.addEventListener("click", printWorksheet);
playAllButton.addEventListener("click", playAllWords);
stopSpeakingButton.addEventListener("click", () => {
  speakingSequence += 1;
  window.speechSynthesis?.cancel();
  clearSpeakingState();
});
renderRoute();
