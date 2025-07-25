import subprocess

from classes.Layout import Layout
from utils.createFile import createFile
from utils.getConfigData import getConfigData
from utils.getSelectedTemplate import getSelectedTemplate


def typeFunc():
    config_txt = getSelectedTemplate()
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
