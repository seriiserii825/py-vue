import subprocess
from classes.Layout import Layout
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate

def apiFunc():
    config_txt = getSelectedTemplate()
    is_vue = True if config_txt == 'vue' else False
    dir_path = getConfigData(is_vue, path='api')
    print(f"dir_path: {dir_path}")
    file_path = createFile(dir_path, 'ts')
    print(f"file_path: {file_path}")
    Layout('api', file_path)
    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    class_name = file_name
    subprocess.run(["sed", "-i", f"s|apiFunc|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

