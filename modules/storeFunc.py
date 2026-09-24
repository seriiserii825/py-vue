import os

from classes.Layout import Layout
from py_libs.Command import Command
from py_libs.InputValidator import InputValidator
from py_libs.Print import Print
from utils.createFile import createFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate


def storeFunc():
    config_txt = getSelectedTemplate()
    if config_txt == "wp" and detectModuleSystem():
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="store")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    store_name = InputValidator.get_string("Enter store name, like popup: ")
    file_path = createFile(dir_path, "ts", placeholder="e.g. usePopupStore")
    Print.info(f"file_path: {file_path}")
    Layout("store", file_path)
    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    Command.run(f"sed -i 's|usePopupStore|{file_name}|g' '{file_path}'")
    Command.run(f"sed -i 's|popup|{store_name}|g' '{file_path}'")
    Command.run(f"bat '{file_path}'")
