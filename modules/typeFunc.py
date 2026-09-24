from classes.Layout import Layout
from py_libs.Command import Command
from py_libs.Print import Print
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
    Print.info(f"dir_path: {dir_path}")
    file_path = createFile(dir_path, "ts")
    Print.info(f"file_path: {file_path}")
    Layout("type", file_path)
    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    class_name = file_name
    Command.run(f"sed -i 's|TVue|{class_name}|g' '{file_path}'")
    Command.run(f"bat '{file_path}'")
