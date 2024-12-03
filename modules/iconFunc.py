import os
import subprocess
from utils.createFile import createFile
from utils.getLayoutPath import getLayoutPath
from utils.layoutToFile import layoutToFile

def iconFunc():
    dir_path = 'src/icons'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, 'vue')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('vue')
    layoutToFile(layout_path, file_path)
    subprocess.run(["bat", file_path], check=True)

