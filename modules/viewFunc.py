import subprocess
from classes.Layout import Layout
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate
def viewFunc():
    config_txt = getSelectedTemplate()
    dir_path = getConfigData(config_txt, path='pages')
    file_path = createFile(dir_path, 'vue')
    print(f"file_path: {file_path}")
    Layout('vue', file_path)

    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    class_name = camelToKebabCase(file_name)
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

