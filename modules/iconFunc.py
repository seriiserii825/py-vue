import os
import subprocess
from rich import print
from utils.createFile import createFile
from utils.getFromClipboard import getFromClipBoard

def iconFunc():
    svg_content = getFromClipBoard()
    if not '<svg' in svg_content:
        print("[red]This is not an svg content")
        return
    svg_content = f"<template>\n{svg_content}\n</template>"
    dir_path = 'src/icons'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, 'vue')
    print(f"file_path: {file_path}")
    with open(file_path, 'w') as f:
        f.write(svg_content)
    subprocess.run(["bat", file_path], check=True)

