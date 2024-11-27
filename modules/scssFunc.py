import os
import subprocess
from utils.appendToFile import appendToFile
from utils.createFile import createFile
from utils.createMyScssFile import createMyScssFile
from utils.getLayoutPath import getLayoutPath
from utils.layoutToFile import layoutToFile
def scssFunc():
    dir_path = 'src/scss/blocks'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, 'scss')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('scss')
    layoutToFile(layout_path, file_path)
    class_name = file_path.split('/')[-1].split('.')[0]
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    createMyScssFile()
    my_scss_file = 'src/scss/my.scss'
    appendToFile(my_scss_file, f"@import 'blocks/{class_name}';")
    subprocess.run(["bat", file_path], check=True)
    subprocess.run(["bat", my_scss_file], check=True)

