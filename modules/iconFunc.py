import os
import subprocess

from rich import print

from classes.Clipboard import ClipboardManager
from modules.Notification import Notification
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from modules.selectWithFzf import selectWithFzf
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getFromClipboard import getFromClipBoard
from utils.getSelectedTemplate import getSelectedTemplate

MODULES_DIR = "modules"


def iconFunc():
    svg_content = getFromClipBoard()
    if not "<svg" in svg_content:
        print("[red]This is not an svg content")
        return
    svg_content = f"<template>\n{svg_content}\n</template>"
    config_txt = getSelectedTemplate()

    if config_txt == "wp" and detectModuleSystem():
        destination = selectWithFzf(["icons", "modules"])
        if destination == "modules":
            module_name = chooseOrCreateDirectory(MODULES_DIR)
            dir_path = f"{MODULES_DIR}/{module_name}"
        else:
            dir_path = getConfigData(config_txt, path="icons")
    else:
        dir_path = getConfigData(config_txt, path="icons")

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    icon_name_input = input("Enter icon name, 'Icon' prefix will be added (e.g. Facebook): ")
    icon_name = f"Icon{icon_name_input}"
    print(f"[green]Icon name will be: {icon_name}")
    file_path = f"{dir_path}/{icon_name}.vue"

    create_file_name_from_path(file_path)
    with open(file_path, "w") as f:
        f.write(svg_content)
    subprocess.run(["bat", file_path], check=True)


def create_file_name_from_path(file_path):
    # // get last 2 segments of the file path without extension
    segments = file_path.replace("\\", "/").split("/")
    last_two_segments = segments[-2:]
    segments_without_extension = [os.path.splitext(seg)[0] for seg in last_two_segments]
    # join the segments without delimiter
    file_name = segments_without_extension[-1]
    file_to_copy = f"<{file_name} />"
    ClipboardManager.write(file_to_copy)
    Notification(file_to_copy, f"Copied to clipboard: {file_to_copy}").notify()
