from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re

ROOT = Path(__file__).parent
SITE = ROOT.parent.parent
SOURCE = ROOT / "ChatGPT Image Jun 25, 2026, 10_55_58 AM.png"
ICONS = ROOT / "game-icons"
ICONS.mkdir(exist_ok=True)
W, H = 1240, 1754
FONT = r"C:\Windows\Fonts\msyh.ttc"
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
INK, MUTED = "#172f52", "#68788c"

entries = [
    ("电视", "diàn shì", "tv"), ("一家人", "yì jiā rén", "family"),
    ("一起", "yì qǐ", "together"), ("游戏", "yóu xì", "game"),
    ("音乐", "yīn yuè", "music"), ("游来游去", "yóu lái yóu qù", "swim"),
    ("飞来飞去", "fēi lái fēi qù", "fly")
]

def font(size, bold=False): return ImageFont.truetype(BOLD if bold else FONT, size)
def center(draw, xy, text, fnt, fill=INK):
    b = draw.textbbox((0, 0), text, font=fnt)
    draw.text((xy[0]-(b[2]-b[0])/2, xy[1]-(b[3]-b[1])/2), text, font=fnt, fill=fill)
def rounded(draw, box, fill="white", outline="#d8e0e7", radius=16, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
def header(draw, title, subtitle):
    draw.text((55,42), "Name: ____________________", font=font(24), fill=INK)
    draw.text((855,42), "Date: ______________", font=font(24), fill=INK)
    center(draw,(W/2,125),title,font(58,True)); center(draw,(W/2,196),subtitle,font(27),MUTED)
    draw.line((48,235,W-48,235),fill="#d7dee7",width=2)
def paste(canvas, image, box):
    copy=image.copy(); copy.thumbnail((box[2]-box[0],box[3]-box[1]),Image.Resampling.LANCZOS)
    x=box[0]+((box[2]-box[0])-copy.width)//2; y=box[1]+((box[3]-box[1])-copy.height)//2
    canvas.paste(copy,(x,y))

source=Image.open(SOURCE).convert("RGB")
icons={}
for i,(word,pinyin,name) in enumerate(entries):
    col, top = (3, 418) if word == "飞来飞去" else (i, 240)
    x0=170+col*168
    crop=source.crop((x0+10,top+10,min(x0+158,source.width),top+125))
    crop.save(ICONS/f"{name}.png", optimize=True); icons[word]=crop

def matching():
    c=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(c); header(d,"看图连线","看图片，把它和正确的词语连起来。")
    shuffled=["音乐","游来游去","电视","一起","飞来飞去","一家人","游戏"]
    y=285
    for i,((word,_,_),right) in enumerate(zip(entries,shuffled),1):
        paste(c,icons[word],(75,y,285,y+150)); center(d,(325,y+75),str(i),font(27,True));
        d.ellipse((360,y+61,388,y+89),outline=INK,width=3); d.ellipse((845,y+61,873,y+89),outline=INK,width=3)
        center(d,(1030,y+75),right,font(35,True)); y+=190
    center(d,(W/2,1685),"小提示：先大声读一读，再开始连线。",font(23),MUTED); c.save(ROOT/"interest-match.png",optimize=True)

def choice():
    c=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(c); header(d,"看图选词","看图片，圈出正确的中文词语。")
    qs=[("电视",["电视","音乐","游戏"]),("一家人",["一起","一家人","电视"]),("一起",["游戏","一起","音乐"]),("游戏",["电视","游戏","一家人"]),("音乐",["飞来飞去","音乐","游来游去"]),("游来游去",["一起","飞来飞去","游来游去"])]
    for i,(answer,opts) in enumerate(qs):
        col,row=i%2,i//2; x=60+col*565; y=275+row*445
        rounded(d,(x,y,x+535,y+410),fill="#fbfcfe"); paste(c,icons[answer],(x+130,y+25,x+405,y+230))
        for j,opt in enumerate(opts):
            bx=x+22+j*170; rounded(d,(bx,y+280,bx+155,y+350),fill="white"); center(d,(bx+77,y+315),opt,font(24,True))
    c.save(ROOT/"interest-multiple-choice.png",optimize=True)

def fill_words():
    c=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(c); header(d,"看图填词","从词语库中选择正确的词语，写在图片下面。")
    rounded(d,(65,270,W-65,405),fill="#eef8ff",outline="#bcd7e8")
    center(d,(145,305),"词语库",font(25,True))
    bank="电视   一家人   一起   游戏   音乐   游来游去   飞来飞去"
    center(d,(W/2,355),bank,font(25,True))
    for i,(word,_,_) in enumerate(entries):
        col,row=i%3,i//3; x=75+col*380; y=455+row*390
        paste(c,icons[word],(x+45,y+5,x+295,y+205))
        d.line((x+20,y+275,x+330,y+275),fill=INK,width=3)
        center(d,(x+175,y+320),f"第 {i+1} 题",font(17),MUTED)
    center(d,(W/2,1685),"写完以后，大声读一读每个词语。",font(23),MUTED); c.save(ROOT/"interest-fill-words.png",optimize=True)

matching(); choice(); fill_words()

word_js="""const words=[
      {word:'电视',pinyin:'diàn shì',img:'game-icons/tv.png'},{word:'一家人',pinyin:'yì jiā rén',img:'game-icons/family.png'},{word:'一起',pinyin:'yì qǐ',img:'game-icons/together.png'},{word:'游戏',pinyin:'yóu xì',img:'game-icons/game.png'},{word:'音乐',pinyin:'yīn yuè',img:'game-icons/music.png'},{word:'游来游去',pinyin:'yóu lái yóu qù',img:'game-icons/swim.png'},{word:'飞来飞去',pinyin:'fēi lái fēi qù',img:'game-icons/fly.png'}
    ];"""

def make(template_name,out_name,title,heading,replacement_kind,replacement):
    text=(SITE/"worksheets"/"01-daily-activities"/template_name).read_text(encoding="utf-8")
    text=re.sub(r"<title>.*?</title>",f"<title>{title} · Read and Roll</title>",text,1)
    text=text.replace("../../index.html#sheet-0","../../index.html#sheet-1")
    if replacement_kind=="words": text=re.sub(r"const words=\[.*?\n    \];",replacement,text,1,flags=re.S)
    elif replacement_kind=="spaces": text=re.sub(r"const spaces=\[.*?\n    \];",replacement,text,1,flags=re.S)
    elif replacement_kind=="questions": text=re.sub(r"const questions=\[.*?\n    \];",replacement,text,1,flags=re.S)
    text=re.sub(r"<h1>.*?</h1>",f"<h1>{heading}</h1>",text,1)
    (ROOT/out_name).write_text(text,encoding="utf-8")

spaces="""const spaces=[
      ['起点','🏠','准备出发','大声说：“我准备好了！”'],['电视','game-icons/tv.png','朗读挑战','大声读三遍“电视”'],['一家人','game-icons/family.png','造句挑战','用“一家人”说一个句子'],['一起','game-icons/together.png','动作挑战','和同学击掌并说“一起”'],['游戏','game-icons/game.png','问答挑战','说一说你喜欢什么游戏'],
      ['音乐','game-icons/music.png','朗读挑战','大声读“我喜欢听音乐”'],['游来游去','game-icons/swim.png','动作挑战','做游泳动作并读出词语'],['飞来飞去','game-icons/fly.png','动作挑战','做飞翔动作并读出词语'],['电视','game-icons/tv.png','造句挑战','用“电视”说一个句子'],['一起','game-icons/together.png','朗读挑战','大声读“我们一起做游戏”'],
      ['音乐','game-icons/music.png','听说挑战','听一遍再跟读“音乐”'],['一家人','game-icons/family.png','问答挑战','说一说你家有几个人'],['游戏','game-icons/game.png','记忆挑战','说出三个兴趣活动词语'],['复习站','⭐','综合挑战','说出四个刚才练习过的词语'],['终点','🏆','终极挑战','用两个词语说一句完整的话']
    ];"""
questions="""const questions=[
      {img:'game-icons/tv.png',parts:['我','喜欢','看','电视'],answer:'我喜欢看电视。'},
      {img:'game-icons/family.png',parts:['我们','是','幸福的','一家人'],answer:'我们是幸福的一家人。'},
      {img:'game-icons/together.png',parts:['我们','一起','做','游戏'],answer:'我们一起做游戏。'},
      {img:'game-icons/game.png',parts:['两个小朋友','在','玩游戏'],answer:'两个小朋友在玩游戏。'},
      {img:'game-icons/music.png',parts:['我','喜欢','听','音乐'],answer:'我喜欢听音乐。'},
      {img:'game-icons/swim.png',parts:['小朋友','在水里','游来游去'],answer:'小朋友在水里游来游去。'},
      {img:'game-icons/fly.png',parts:['小鸟','在天上','飞来飞去'],answer:'小鸟在天上飞来飞去。'}
    ];"""
make("dice-adventure.html","interest-dice.html","兴趣骰子闯关","兴趣骰子闯关","spaces",spaces)
make("listening-choice.html","interest-listen.html","兴趣听音选词","兴趣听音选词","words",word_js)
make("sentence-builder.html","interest-sentence.html","兴趣看图造句","兴趣看图造句","questions",questions)
make("pinyin-match.html","interest-catch.html","兴趣汉字接接乐","兴趣汉字接接乐","words",word_js)
print("Built interest activities package.")
