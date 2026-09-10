from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, re, shutil

SITE=Path(__file__).parent.parent; WORK=SITE/'worksheets'; W,H=1240,1754
FONT=r'C:\Windows\Fonts\msyh.ttc'; BOLD=r'C:\Windows\Fonts\msyhbd.ttc'; INK='#172f52'; MUTED='#68788c'

def E(w,p,m,r,c,n): return dict(word=w,pinyin=p,meaning=m,row=r,col=c,name=n)
topics=[
 (2,'03-phone','ChatGPT Image Jul 3, 2026, 02_52_59 PM.png','打电话',[E('打电话','dǎ diàn huà','to make a phone call',0,0,'phone'),E('在家','zài jiā','at home',0,1,'home'),E('你找谁','nǐ zhǎo shéi','who are you looking for?',0,2,'who'),E('喂','wèi','hello (on the phone)',0,3,'hello'),E('没空','méi kòng','not available',0,4,'busy'),E('请问','qǐng wèn','excuse me; may I ask',0,5,'ask'),E('等一下','děng yí xià','wait a moment',1,0,'wait')]),
 (3,'04-actions','动作.png','动作',[E('看','kàn','to look',0,0,'look'),E('闻','wén','to smell',0,1,'smell'),E('说','shuō','to speak',0,2,'speak'),E('咬','yǎo','to bite',0,3,'bite'),E('听','tīng','to listen',0,4,'listen'),E('拍','pāi','to clap; pat',0,5,'clap'),E('走','zǒu','to walk',1,1,'walk')]),
 (4,'05-my-school','ChatGPT Image Jun 8, 2026, 02_54_07 PM.png','我的学校',[E('幼儿园','yòu ér yuán','kindergarten',0,0,'kindergarten'),E('一年级','yì nián jí','first grade',0,1,'grade1'),E('二年级','èr nián jí','second grade',0,2,'grade2'),E('四年级','sì nián jí','fourth grade',0,3,'grade4'),E('五年级','wǔ nián jí','fifth grade',0,4,'grade5'),E('几年级','jǐ nián jí','which grade',0,5,'which-grade'),E('小学','xiǎo xué','elementary school',1,0,'school'),E('上学','shàng xué','to go to school',1,1,'go-school'),E('同学','tóng xué','classmate',1,2,'classmate')]),
 (5,'06-school-supplies','ChatGPT Image Jul 7, 2026, 01_32_16 PM.png','学校文具',[E('橡皮','xiàng pí','eraser',0,0,'eraser'),E('书','shū','book',0,1,'book'),E('书包','shū bāo','schoolbag',0,2,'bag'),E('电脑','diàn nǎo','computer',0,3,'computer'),E('椅子','yǐ zi','chair',0,4,'chair'),E('铅笔','qiān bǐ','pencil',0,5,'pencil'),E('本子','běn zi','notebook',1,0,'notebook'),E('桌子','zhuō zi','desk',1,3,'desk')]),
 (6,'07-school-subjects','ChatGPT Image Jul 23, 2026, 12_56_57 PM.png','学校科目',[E('数学','shù xué','math',0,0,'math'),E('社会学','shè huì xué','social studies',0,1,'social'),E('写作','xiě zuò','writing',0,2,'writing'),E('体育','tǐ yù','physical education',0,3,'pe'),E('科学','kē xué','science',0,4,'science'),E('图书馆','tú shū guǎn','library',0,5,'library'),E('美术','měi shù','art',1,0,'art'),E('课间','kè jiān','recess',1,3,'recess')]),
 (7,'08-position-objects','ChatGPT Image Jun 11, 2026, 03_12_54 PM.png','方位与物品',[E('它们','tā men','they; them',0,0,'they'),E('上面','shàng miàn','above; on top',0,1,'above'),E('下面','xià miàn','below; under',0,2,'below'),E('冰箱','bīng xiāng','refrigerator',0,3,'fridge'),E('里面','lǐ miàn','inside',0,4,'inside'),E('外面','wài miàn','outside',0,5,'outside'),E('老鼠','lǎo shǔ','mouse',1,0,'mouse'),E('电脑','diàn nǎo','computer',1,1,'computer'),E('前面','qián miàn','in front',1,2,'front'),E('后面','hòu miàn','behind',1,3,'behind')]),
 (8,'09-rooms-furniture','ChatGPT Image Jun 12, 2026, 12_07_52 PM.png','房间与家具',[E('房间','fáng jiān','room',0,0,'room'),E('客厅','kè tīng','living room',0,1,'living'),E('卧室','wò shì','bedroom',0,2,'bedroom'),E('厨房','chú fáng','kitchen',0,3,'kitchen'),E('卫生间','wèi shēng jiān','bathroom',0,4,'bathroom'),E('沙发','shā fā','sofa',0,5,'sofa'),E('床','chuáng','bed',1,0,'bed'),E('书架','shū jià','bookshelf',1,1,'shelf'),E('衣柜','yī guì','wardrobe',1,2,'wardrobe'),E('玩具','wán jù','toy',1,3,'toy')]),
 (9,'10-school-country','ChatGPT Image Jun 16, 2026, 01_48_13 PM.png','学校与国家',[E('住在','zhù zài','to live in',0,0,'live'),E('哪里','nǎ lǐ','where',0,1,'where'),E('一楼','yī lóu','first floor',0,2,'floor1'),E('校长','xiào zhǎng','principal',0,3,'principal'),E('美国','Měi guó','United States',0,4,'usa'),E('中国','Zhōng guó','China',0,5,'china'),E('二楼','èr lóu','second floor',1,1,'floor2'),E('三楼','sān lóu','third floor',2,0,'floor3'),E('四楼','sì lóu','fourth floor',3,2,'floor4')]),
 (10,'11-countries-people','ChatGPT Image Jun 24, 2026, 03_14_46 PM.png','国家与人物',[E('美国','Měi guó','United States',0,0,'usa'),E('中国','Zhōng guó','China',0,1,'china'),E('墨西哥','Mò xī gē','Mexico',0,2,'mexico'),E('他是谁','tā shì shéi','who is he?',0,3,'who'),E('加拿大','Jiā ná dà','Canada',0,4,'canada'),E('我家','wǒ jiā','my home; my family',0,5,'home'),E('几个人','jǐ ge rén','how many people',1,0,'people')]),
 (11,'12-dates-birthday','ChatGPT Image Jun 23, 2026, 02_57_26 PM.png','日期与生日',[E('今天','jīn tiān','today',0,0,'today'),E('明天','míng tiān','tomorrow',0,1,'tomorrow'),E('生日','shēng rì','birthday',0,2,'birthday'),E('快乐','kuài lè','happy',0,3,'happy'),E('几月','jǐ yuè','which month',0,4,'month'),E('几号','jǐ hào','what date',0,5,'date'),E('五月','wǔ yuè','May',1,4,'may'),E('六月','liù yuè','June',1,5,'june'),E('礼物','lǐ wù','gift',2,4,'gift')]),
 (12,'13-week-time','ChatGPT Image Jun 30, 2026, 11_27_45 AM.png','星期与时间',[E('星期一','xīng qī yī','Monday',0,0,'mon'),E('星期二','xīng qī èr','Tuesday',0,1,'tue'),E('星期三','xīng qī sān','Wednesday',0,2,'wed'),E('星期四','xīng qī sì','Thursday',0,3,'thu'),E('星期五','xīng qī wǔ','Friday',0,4,'fri'),E('星期六','xīng qī liù','Saturday',0,5,'sat'),E('星期日','xīng qī rì','Sunday',1,0,'sun'),E('昨天','zuó tiān','yesterday',1,1,'yesterday'),E('今天','jīn tiān','today',1,2,'today'),E('明天','míng tiān','tomorrow',1,3,'tomorrow')]),
 (13,'14-food','ChatGPT Image Jul 28, 2026, 11_05_45 AM.png','美食',[E('果汁','guǒ zhī','juice',0,0,'juice'),E('汉堡','hàn bǎo','hamburger',0,1,'burger'),E('水饺','shuǐ jiǎo','dumplings',0,2,'dumpling'),E('冰淇淋','bīng qí lín','ice cream',0,3,'icecream'),E('三明治','sān míng zhì','sandwich',0,4,'sandwich'),E('薯条','shǔ tiáo','French fries',0,5,'fries'),E('包子','bāo zi','steamed bun',1,0,'bun'),E('可乐','kě lè','cola',1,2,'cola')]),
 (14,'15-fruit','ChatGPT Image Jul 21, 2026, 11_29_23 AM.png','水果',[E('水果','shuǐ guǒ','fruit',0,0,'fruit'),E('草莓','cǎo méi','strawberry',0,1,'strawberry'),E('西瓜','xī guā','watermelon',0,2,'watermelon'),E('葡萄','pú tao','grapes',0,3,'grapes'),E('橘子','jú zi','orange',0,4,'orange'),E('苹果','píng guǒ','apple',0,5,'apple'),E('梨','lí','pear',1,1,'pear')])
]

def fnt(n,b=False): return ImageFont.truetype(BOLD if b else FONT,n)
def center(d,xy,t,f,fill=INK):
 b=d.textbbox((0,0),t,font=f); d.text((xy[0]-(b[2]-b[0])/2,xy[1]-(b[3]-b[1])/2),t,font=f,fill=fill)
def roundrect(d,b,fill='white',outline='#d8e0e7'): d.rounded_rectangle(b,radius=16,fill=fill,outline=outline,width=2)
def header(d,title,sub):
 d.text((55,42),'Name: ____________________',font=fnt(24),fill=INK); d.text((855,42),'Date: ______________',font=fnt(24),fill=INK); center(d,(W/2,125),title,fnt(56,True)); center(d,(W/2,196),sub,fnt(25),MUTED); d.line((48,235,W-48,235),fill='#d7dee7',width=2)
def paste(c,img,b):
 x0,y0,x1,y1=b; cp=img.copy(); cp.thumbnail((x1-x0,y1-y0),Image.Resampling.LANCZOS); c.paste(cp,(x0+(x1-x0-cp.width)//2,y0+(y1-y0-cp.height)//2))
def crop_icon(src,e):
 sw,sh=src.size; x=int(sw*.142+e['col']*sw*.14); y=int(sh*.182+e['row']*sh*.126); return src.crop((x+int(sw*.01),y+int(sh*.008),min(x+int(sw*.132),sw),min(y+int(sh*.105),sh)))
def js_words(entries): return 'const words=[\n      '+','.join("{word:%s,pinyin:%s,img:%s}"%(json.dumps(e['word'],ensure_ascii=False),json.dumps(e['pinyin'],ensure_ascii=False),json.dumps('game-icons/'+e['name']+'.png')) for e in entries)+'\n    ];'
def make_games(folder,title,index,entries):
 templates=WORK/'01-daily-activities'; words=js_words(entries)
 spaces=[['起点','🏠','准备出发','大声说：“我准备好了！”']]
 for i in range(13):
  e=entries[i%len(entries)]; spaces.append([e['word'],'game-icons/'+e['name']+'.png',['朗读挑战','造句挑战','记忆挑战'][i%3],f"大声读出“{e['word']}”，再用它说一句话"])
 spaces.append(['终点','🏆','终极挑战','说出四个今天练习过的词语'])
 spaces_js='const spaces='+json.dumps(spaces,ensure_ascii=False,separators=(',',':'))+';'
 qs=[]
 for e in entries[:8]: qs.append(dict(img='game-icons/'+e['name']+'.png',parts=['我','认识','这个词',e['word']],answer='我认识这个词：'+e['word']+'。'))
 qs_js='const questions='+json.dumps(qs,ensure_ascii=False,separators=(',',':'))+';'
 specs=[('dice-adventure.html','dice.html',title+'骰子闯关','spaces',spaces_js),('listening-choice.html','listen.html',title+'听音选词','words',words),('sentence-builder.html','sentence.html',title+'看图造句','questions',qs_js),('pinyin-match.html','catch.html',title+'汉字接接乐','words',words)]
 for srcname,outname,heading,kind,data in specs:
  text=(templates/srcname).read_text(encoding='utf-8'); text=text.replace('../../index.html#sheet-0',f'../../index.html#sheet-{index}'); text=re.sub(r'<title>.*?</title>',f'<title>{heading} · Read and Roll</title>',text,1); text=re.sub(r'<h1>.*?</h1>',f'<h1>{heading}</h1>',text,1)
  pattern={'words':r'const words=\[.*?\n    \];','spaces':r'const spaces=\[.*?\n    \];','questions':r'const questions=\[.*?\n    \];'}[kind]; text=re.sub(pattern,data,text,1,flags=re.S); (folder/outname).write_text(text,encoding='utf-8')

detail=[]
for index,slug,filename,title,entries in topics:
 folder=WORK/slug; folder.mkdir(parents=True,exist_ok=True); source=SITE/filename
 if source.exists(): shutil.move(str(source),str(folder/filename))
 source=folder/filename; src=Image.open(source).convert('RGB'); icon_dir=folder/'game-icons'; icon_dir.mkdir(exist_ok=True); icons={}
 for e in entries:
  icon=crop_icon(src,e); icon.save(icon_dir/(e['name']+'.png'),optimize=True); icons[e['word']]=icon
 # matching
 c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); header(d,'看图连线','看图片，把它和正确的词语连起来。'); shuffled=[e['word'] for e in entries[2:]]+[e['word'] for e in entries[:2]]
 y=260
 for n,(e,right) in enumerate(zip(entries,shuffled),1): paste(c,icons[e['word']],(70,y,270,y+115)); center(d,(315,y+58),str(n),fnt(24,True)); d.ellipse((350,y+45,376,y+71),outline=INK,width=3); d.ellipse((850,y+45,876,y+71),outline=INK,width=3); center(d,(1030,y+58),right,fnt(30,True)); y+=140
 c.save(folder/'match.png',optimize=True)
 # choice
 c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); header(d,'看图选词','看图片，圈出正确的中文词语。')
 for i,e in enumerate(entries[:6]):
  col,row=i%2,i//2; x=60+col*565; y=275+row*445; roundrect(d,(x,y,x+535,y+410),fill='#fbfcfe'); paste(c,icons[e['word']],(x+130,y+20,x+405,y+225)); wrong=[q['word'] for q in entries if q['word']!=e['word']][:2]; opts=[e['word']]+wrong
  for j,opt in enumerate(opts): bx=x+20+j*172; roundrect(d,(bx,y+280,bx+158,y+350)); center(d,(bx+79,y+315),opt,fnt(21,True))
 c.save(folder/'choice.png',optimize=True)
 # fill words
 c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); header(d,'看图填词','从词语库中选择正确的词语，写在图片下面。'); roundrect(d,(55,265,W-55,395),fill='#eef8ff'); bank='  ·  '.join(e['word'] for e in entries); center(d,(W/2,330),bank,fnt(20,True))
 for i,e in enumerate(entries):
  col,row=i%3,i//3; x=70+col*380; y=420+row*300; paste(c,icons[e['word']],(x+50,y,x+290,y+145)); d.line((x+20,y+210,x+330,y+210),fill=INK,width=3)
 c.save(folder/'fill.png',optimize=True); make_games(folder,title,index,entries)
 detail.append(dict(index=index,file=f'worksheets/{slug}/{filename}',description=f'通过掷骰子和看图朗读，学习{title}主题的常用中文词语。',vocabulary=[dict(word=e['word'],pinyin=e['pinyin'],meaning=e['meaning']) for e in entries],practiceSheets=[dict(title='看图连线',file=f'worksheets/{slug}/match.png'),dict(title='看图选词',file=f'worksheets/{slug}/choice.png'),dict(title='看图填词',file=f'worksheets/{slug}/fill.png')],games=[dict(title=title+'骰子闯关',file=f'worksheets/{slug}/dice.html'),dict(title=title+'听音选词',file=f'worksheets/{slug}/listen.html'),dict(title=title+'看图造句',file=f'worksheets/{slug}/sentence.html'),dict(title=title+'汉字接接乐',file=f'worksheets/{slug}/catch.html')]))
(SITE/'all-worksheet-details.js').write_text('globalThis.WORKSHEET_DETAIL_DATA='+json.dumps(detail,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f'Built {len(topics)} remaining worksheet packages.')
