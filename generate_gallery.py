#!/usr/bin/env python3

import os


image_folder = "./fem/"

# Extensions you want to include
EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

# Scan current folder
files = [f for f in sorted(os.listdir(image_folder)) if os.path.splitext(f)[1].lower() in EXTS]

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Image Gallery</title>
<style>
body { font-family: sans-serif; background: #111; color: #eee; }
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(600px, 1fr));
    gap: 12px;
    padding: 20px;
}
.gallery img {
    width: 100%;
    height: auto;
    border-radius: 6px;
}
</style>
</head>
<body>
<h1>Image Gallery</h1>
<div class="gallery">
"""

for f in files:
    html += f'  <a href="fem/{f}" target="_blank"><img src="fem/{f}" alt="fem/{f}"></a>\n'

html += """
</div>
</body>
</html>
"""

with open("fem_images.html", "w", encoding="utf-8") as fp:
    fp.write(html)

print(f"Generated fem_images.html with {len(files)} images")
