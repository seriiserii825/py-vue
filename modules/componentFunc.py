import subprocess

from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate
from utils.showDirectories import showDirectories


def componentFunc():
    config_txt = getSelectedTemplate()
    if config_txt == "wp" and detectModuleSystem():
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="components")
    showDirectories(dir_path)
    need_a_dir = input("Do you need a directory? (y/n): ").strip().lower()
    if need_a_dir == "y":
        dir_name = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{dir_name}"
    file_path = createFile(dir_path, "vue")
    print(f"file_path: {file_path}")
    Layout("vue", file_path)
    file_name = file_path.split("/")[-1].split(".")[0]
    class_name = camelToKebabCase(file_name)
    subprocess.run(
        ["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)
