import os
import subprocess
from classes.Layout import Layout
from utils.appendToFile import appendToFile
from utils.createFile import createFile
from utils.createMyScssFile import createMyScssFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate
def scssFunc():
    config_txt = getSelectedTemplate()
    dir_path = getConfigData(config_txt, path='scss')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, 'scss')
    print(f"file_path: {file_path}")
    Layout('scss', file_path)
    class_name = file_path.split('/')[-1].split('.')[0]
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    my_scss_file = getConfigData(config_txt, path='my.scss')
    createMyScssFile(my_scss_file)
    # appendToFile(my_scss_file, f"@import 'blocks/{class_name}';")
    appendToFile(my_scss_file, f"@use 'blocks/{class_name}' as *;")
    subprocess.run(["bat", file_path], check=True)
    subprocess.run(["bat", my_scss_file], check=True)

