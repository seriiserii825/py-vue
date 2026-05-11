import subprocess

from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from modules.select import selectOne
from utils.appendToFile import appendToFile
from utils.autoCreateModuleScss import autoCreateModuleScss
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.createMyScssFile import createMyScssFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate


def componentFunc():
    config_txt = getSelectedTemplate()
    is_wp_module = config_txt == "wp" and detectModuleSystem()
    if is_wp_module:
        dir_path = getModulePath()
    else:
        dir_path = getConfigData(config_txt, path="components")
        dir_name = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{dir_name}"
    file_path = createFile(dir_path, "vue")
    print(f"file_path: {file_path}")
    Layout("vue", file_path)
    file_name = file_path.split("/")[-1].split(".")[0]
    class_name = camelToKebabCase(file_name)
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)
    if is_wp_module:
        create_scss = selectOne(["Yes", "No"])
        if create_scss == "Yes":
            autoCreateModuleScss(dir_path, class_name)
            my_scss_file = getConfigData(config_txt, "my.scss")
            createMyScssFile(my_scss_file)
            appendToFile(my_scss_file, f"@use '@/{dir_path}/{class_name}';")
