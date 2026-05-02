import subprocess

from classes.Layout import Layout
from utils.createFile import createFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate


def typeFunc():
    config_txt = getSelectedTemplate()
    if config_txt == "wp" and detectModuleSystem():
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="type")
    print(f"dir_path: {dir_path}")
    file_path = createFile(dir_path, "ts")
    print(f"file_path: {file_path}")
    Layout("type", file_path)
    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    class_name = file_name
    subprocess.run(["sed", "-i", f"s|TVue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)
