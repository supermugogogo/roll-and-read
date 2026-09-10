from pathlib import Path

site = Path(__file__).parent.parent
count = 0
for path in (site / "worksheets").glob("[0-9][0-9]-*/*.html"):
    text = path.read_text(encoding="utf-8")
    old_marker = '<link rel="stylesheet" href="../../game-compact.css">'
    marker = '<link rel="stylesheet" href="../../game-compact.css?v=3">'
    if old_marker in text:
        text = text.replace(old_marker, marker)
        path.write_text(text, encoding="utf-8")
        count += 1
    elif marker not in text:
        text = text.replace('</head>', f'  {marker}\n</head>', 1)
        path.write_text(text, encoding="utf-8")
        count += 1
print(f"Updated {count} game files.")
