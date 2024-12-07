import os
import subprocess
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getLayoutPath import getLayoutPath
from utils.getSelectedTemplate import getSelectedTemplate
from utils.layoutToFile import layoutToFile
def storeFunc():
    config_txt = getSelectedTemplate()
    is_vue = True if config_txt == 'vue' else False
    dir_path = getConfigData(is_vue, path='store')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    store_name = input("Enter store name, like popup: ")
    file_path = createFile(dir_path, 'ts', 'usePopupStore')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('store')
    layoutToFile(layout_path, file_path)
    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    subprocess.run(["sed", "-i", f"s|usePopupStore|{file_name}|g", file_path], check=True)
    subprocess.run(["sed", "-i", f"s|popup|{store_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

