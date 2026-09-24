import os

from py_libs.Command import Command
from py_libs.FilesHandle import FilesHandle
from py_libs.InputValidator import InputValidator
from py_libs.Print import Print

from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from utils.autoCreateModuleScss import autoCreateModuleScss
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate


def viewFunc():
    config_txt = getSelectedTemplate()
    is_wp_module = config_txt == "wp" and detectModuleSystem()
    if is_wp_module:
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="pages")
    Print.info(f"dir_path: {dir_path}")
    # check if the directory exists in system
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    files_handle = FilesHandle()
    # check if the directory is empty
    if files_handle.directory_is_empty(dir_path):
        Print.error("Directory is empty")
    else:
        files_handle.list_files(dir_path)
    if InputValidator.get_bool("Do you want a inner page? (y/n): "):
        dir_name = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{dir_name}"

        if InputValidator.get_bool("Do you want a inner page? (y/n): "):
            dir_name = chooseOrCreateDirectory(dir_path)
            dir_path = f"{dir_path}/{dir_name}"

    file_path = createFile(
        dir_path,
        "vue",
        placeholder="PascalCase, 'View' suffix will be added (e.g. PageContatti -> PageContattiView.vue)",
        suffix="View",
    )

    Layout("vue", file_path)

    # get file name from file path without extension
    file_name = file_path.split("/")[-1].split(".")[0]
    class_name = camelToKebabCase(file_name)
    Command.run(f"sed -i 's|vue|{class_name}|g' '{file_path}'")
    Command.run(f"bat '{file_path}'")
    if is_wp_module:
        autoCreateModuleScss(dir_path, class_name)
