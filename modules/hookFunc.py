import os
import subprocess
from utils.createFile import createFile
from utils.getLayoutPath import getLayoutPath
from utils.layoutToFile import layoutToFile
def hookFunc():
    dir_path = 'src/hooks'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, 'ts')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('hook')
    layoutToFile(layout_path, file_path)
    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    subprocess.run(["sed", "-i", f"s|useHook|{file_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

