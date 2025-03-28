import subprocess
from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate

def componentFunc():
    config_txt = getSelectedTemplate()
    dir_path = getConfigData(config_txt, path='components')
    print(f"dir_path: {dir_path}")
    file_path = createFile(dir_path, 'vue')
    print(f"file_path: {file_path}")
    Layout('vue', file_path)
    dir_name = chooseOrCreateDirectory(dir_path)
    print(f'dir_name: {dir_name}')
    # file_name = file_path.split('/')[-1].split('.')[0]
    # class_name = camelToKebabCase(file_name)
    # subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    # subprocess.run(["bat", file_path], check=True)
    #
