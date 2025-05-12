import subprocess
from classes.FilesHandle import FilesHandle
from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate
def viewFunc():
    config_txt = getSelectedTemplate()
    dir_path = getConfigData(config_txt, path='pages')
    files_handle = FilesHandle(dir_path)
    files_handle.listFiles()
    inner_page = input("Do you want a inner page? (y/n): ")
    if inner_page.lower() == 'y':
        dir_name = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{dir_name}"
        new_dir = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{new_dir}"
    file_path = createFile(dir_path, 'vue')

    Layout('vue', file_path)

    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    class_name = camelToKebabCase(file_name)
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

