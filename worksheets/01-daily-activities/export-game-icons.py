from pathlib import Path
from PIL import Image

root = Path(__file__).parent
source = Image.open(root / "ChatGPT Image Jun 5, 2026, 11_43_59 AM.png").convert("RGB")
output = root / "game-icons"
output.mkdir(exist_ok=True)

names = [
    "get-up", "get-dressed", "eat", "brush-teeth", "wash-face", "go-school",
    "class", "school-over", "homework", "two-thirty", "sleep", "basketball"
]

for index, name in enumerate(names):
    row, col = divmod(index, 6)
    x0 = 143 + col * 165
    y0 = 226 + row * 181
    icon = source.crop((x0 + 12, y0 + 8, min(x0 + 153, source.width), y0 + 138))
    icon.save(output / f"{name}.png", optimize=True)

print(f"Exported {len(names)} Read and Roll game icons.")
