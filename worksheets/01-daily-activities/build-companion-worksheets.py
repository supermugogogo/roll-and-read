from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
SOURCE = ROOT / "ChatGPT Image Jun 5, 2026, 11_43_59 AM.png"
W, H = 1240, 1754

COLORS = {
    "ink": "#172f52",
    "blue": "#cce9fb",
    "yellow": "#fff0ad",
    "green": "#dff1c5",
    "pink": "#f9d6e4",
    "purple": "#e5dcf7",
    "orange": "#ffe0bd",
    "line": "#26364a",
    "muted": "#68788c",
}

FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FONT_BOLD_PATH = r"C:\Windows\Fonts\msyhbd.ttc"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD_PATH if bold else FONT_PATH, size)


def centered(draw, xy, text, fnt, fill=COLORS["ink"]):
    x, y = xy
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text((x - (box[2] - box[0]) / 2, y - (box[3] - box[1]) / 2), text, font=fnt, fill=fill)


def header(draw, title, subtitle):
    draw.text((55, 42), "Name: ____________________", font=font(24), fill=COLORS["ink"])
    draw.text((855, 42), "Date: ______________", font=font(24), fill=COLORS["ink"])
    centered(draw, (W / 2, 125), title, font(58, True))
    centered(draw, (W / 2, 196), subtitle, font(27), COLORS["muted"])
    draw.line((48, 235, W - 48, 235), fill="#d7dee7", width=2)


def rounded(draw, box, fill="#ffffff", outline="#d7dee7", radius=18, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


source = Image.open(SOURCE).convert("RGB")
words = ["起床", "穿衣服", "吃饭", "刷牙", "洗脸", "上学", "上课", "放学", "做功课", "两点半", "睡觉", "打篮球"]


def cell_crop(index):
    row, col = divmod(index, 6)
    x0 = 143 + col * 165
    y0 = 226 + row * 181
    crop = source.crop((x0 + 7, y0 + 7, min(x0 + 158, source.width), y0 + 145))
    return crop


icons = {word: cell_crop(i) for i, word in enumerate(words)}


def paste_contain(canvas, image, box):
    x0, y0, x1, y1 = box
    copy = image.copy()
    copy.thumbnail((x1 - x0, y1 - y0), Image.Resampling.LANCZOS)
    x = x0 + ((x1 - x0) - copy.width) // 2
    y = y0 + ((y1 - y0) - copy.height) // 2
    canvas.paste(copy, (x, y))


def build_matching():
    canvas = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(canvas)
    header(draw, "看图连线", "看图片，把它和正确的词语连起来。")
    selected = ["起床", "穿衣服", "刷牙", "上学", "放学", "睡觉", "做功课", "打篮球"]
    shuffled = ["上学", "睡觉", "穿衣服", "做功课", "起床", "打篮球", "刷牙", "放学"]
    y = 275
    for i, (left, right) in enumerate(zip(selected, shuffled), 1):
        paste_contain(canvas, icons[left], (82, y + 17, 273, y + 143))
        centered(draw, (315, y + 81), str(i), font(28, True))
        draw.ellipse((354, y + 66, 382, y + 94), outline=COLORS["ink"], width=3)
        draw.ellipse((848, y + 66, 876, y + 94), outline=COLORS["ink"], width=3)
        centered(draw, (1020, y + 80), right, font(36, True))
        y += 174
    centered(draw, (W / 2, 1695), "小提示：先大声读一读，再开始连线。", font(23), COLORS["muted"])
    canvas.save(ROOT / "daily-match.png", optimize=True)


def build_choice():
    canvas = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(canvas)
    header(draw, "看图选词", "看图片，圈出正确的中文词语。")
    questions = [
        ("起床", ["起床", "睡觉", "上课"]),
        ("刷牙", ["洗脸", "刷牙", "吃饭"]),
        ("上学", ["放学", "上学", "打篮球"]),
        ("做功课", ["穿衣服", "上课", "做功课"]),
        ("睡觉", ["睡觉", "起床", "洗脸"]),
        ("打篮球", ["吃饭", "打篮球", "放学"]),
    ]
    positions = [(60, 275), (635, 275), (60, 725), (635, 725), (60, 1175), (635, 1175)]
    tone_fills = [COLORS["yellow"], COLORS["blue"], COLORS["green"], COLORS["pink"], COLORS["purple"], COLORS["orange"]]
    for number, ((answer, options), (x, y), tone) in enumerate(zip(questions, positions, tone_fills), 1):
        rounded(draw, (x, y, x + 545, y + 410), fill="#ffffff", outline="#d4dde7")
        draw.rounded_rectangle((x, y, x + 62, y + 52), radius=16, fill=tone)
        centered(draw, (x + 31, y + 26), str(number), font(24, True))
        paste_contain(canvas, icons[answer], (x + 150, y + 25, x + 395, y + 205))
        option_y = y + 230
        for option in options:
            draw.ellipse((x + 60, option_y + 4, x + 84, option_y + 28), outline=COLORS["ink"], width=2)
            draw.text((x + 105, option_y - 4), option, font=font(27), fill=COLORS["ink"])
            option_y += 55
    canvas.save(ROOT / "daily-multiple-choice.png", optimize=True)


def build_cut_sort():
    canvas = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(canvas)
    header(draw, "剪一剪，分一分", "剪下词语卡片，贴到合适的时间栏目里。")
    categories = [("早上", COLORS["yellow"]), ("在学校", COLORS["blue"]), ("放学以后", COLORS["green"]), ("晚上", COLORS["purple"])]
    x_positions = [50, 345, 640, 935]
    for (label, tone), x in zip(categories, x_positions):
        rounded(draw, (x, 275, x + 255, 875), fill="#fbfcfe", outline="#cbd5df")
        draw.rounded_rectangle((x, 275, x + 255, 345), radius=17, fill=tone)
        centered(draw, (x + 127, 309), label, font(29, True))
        for y in (475, 650, 825):
            draw.line((x + 25, y, x + 230, y), fill="#d2d9e1", width=2)
    draw.line((45, 930, W - 45, 930), fill=COLORS["muted"], width=2)
    centered(draw, (W / 2, 970), "沿虚线剪下词语卡片", font(23), COLORS["muted"])
    cards = ["起床", "穿衣服", "刷牙", "洗脸", "吃饭", "上学", "上课", "放学", "做功课", "打篮球", "两点半", "睡觉"]
    card_w, card_h = 275, 210
    for index, word in enumerate(cards):
        row, col = divmod(index, 4)
        x = 50 + col * 295
        y = 1015 + row * 225
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=10, fill="white", outline="#79889a", width=2)
        for dx in range(x + 8, x + card_w - 8, 16):
            draw.line((dx, y, min(dx + 8, x + card_w), y), fill="white", width=3)
        paste_contain(canvas, icons[word], (x + 60, y + 10, x + 215, y + 135))
        centered(draw, (x + card_w / 2, y + 169), word, font(27, True))
    canvas.save(ROOT / "daily-cut-sort.png", optimize=True)


build_matching()
build_choice()
build_cut_sort()
print("Created daily-match.png, daily-multiple-choice.png, and daily-cut-sort.png")
