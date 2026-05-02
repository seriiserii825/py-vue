import os
import subprocess

from classes.Layout import Layout
from utils.createFile import createFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate


def hookFunc():
    config_txt = getSelectedTemplate()
    print(f"config_txt: {config_txt}")
    if config_txt == "wp" and detectModuleSystem():
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="hooks")
    print(f"dir_path: {dir_path}")
    # if not exists dir in system create
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    print(f"dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = createFile(dir_path, "ts")
    print(f"file_path: {file_path}")
    Layout("hook", file_path)
    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    subprocess.run(["sed", "-i", f"s|useHook|{file_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)
