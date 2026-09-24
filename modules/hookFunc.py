import os

from classes.Layout import Layout
from py_libs.Command import Command
from py_libs.Print import Print
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate


def hookFunc():
    config_txt = getSelectedTemplate()
    Print.info(f"config_txt: {config_txt}")
    dir_path = getConfigData(config_txt, path="hooks")
    Print.info(f"dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, "ts")
    Print.info(f"file_path: {file_path}")
    Layout("hook", file_path)
    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    Command.run(f"sed -i 's|useHook|{file_name}|g' '{file_path}'")
    Command.run(f"bat '{file_path}'")
