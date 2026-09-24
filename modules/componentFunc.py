import os

from classes.Layout import Layout
from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from py_libs.Command import Command
from py_libs.Print import Print
from py_libs.Select import Select
from utils.appendToFile import appendToFile
from utils.autoCreateModuleScss import autoCreateModuleScss
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.createMyScssFile import createMyScssFile
from utils.detectModuleSystem import detectModuleSystem
from utils.getConfigData import getConfigData
from utils.getModulePath import getModulePath
from utils.getSelectedTemplate import getSelectedTemplate
from utils.kebabToCamelCase import kebabToCamelCase


def componentFunc():
    config_txt = getSelectedTemplate()
    is_wp_module = config_txt == "wp" and detectModuleSystem()
    if is_wp_module:
        dir_path, dir_created = getModulePath(return_created=True)
        if dir_created:
            folder_name = dir_path.split("/")[-1]
            component_name = kebabToCamelCase(folder_name)
            class_name = camelToKebabCase(component_name)
            file_path = f"{dir_path}/{component_name}.vue"
            Command.run(f"touch '{file_path}'")
            Layout("vue", file_path)
            Command.run(f"sed -i 's|vue|{class_name}|g' '{file_path}'")
            Command.run(f"bat '{file_path}'")
            autoCreateModuleScss(dir_path, class_name)
            my_scss_file = getConfigData(config_txt, "my.scss")
            createMyScssFile(my_scss_file)
            appendToFile(my_scss_file, f"@use '@/{dir_path}/{class_name}';")
        else:
            component_name_input = input("Enter component name (kebab-case): ")
            if not component_name_input:
                folder_name = dir_path.split("/")[-1]
                component_name = kebabToCamelCase(folder_name)
            else:
                component_name = kebabToCamelCase(component_name_input)
            class_name = camelToKebabCase(component_name)
            file_path = f"{dir_path}/{component_name}.vue"
            Command.run(f"touch '{file_path}'")
            Layout("vue", file_path)
            Command.run(f"sed -i 's|vue|{class_name}|g' '{file_path}'")
            Command.run(f"bat '{file_path}'")
            Print.info("Do you want to create a SCSS file for this component?")
            create_scss = Select.select_one(["Yes", "No"])
            if create_scss == "Yes":
                autoCreateModuleScss(dir_path, class_name)
                my_scss_file = getConfigData(config_txt, "my.scss")
                createMyScssFile(my_scss_file)
                appendToFile(my_scss_file, f"@use '@/{dir_path}/{class_name}';")
    else:
        dir_path = getConfigData(config_txt, path="components")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        dir_name = chooseOrCreateDirectory(dir_path)
        dir_path = f"{dir_path}/{dir_name}"
        file_path = createFile(dir_path, "vue", placeholder="PascalCase (e.g. ContactForm -> ContactForm.vue)")
        Print.info(f"file_path: {file_path}")
        Layout("vue", file_path)
        file_name = file_path.split("/")[-1].split(".")[0]
        class_name = camelToKebabCase(file_name)
        Command.run(f"sed -i 's|vue|{class_name}|g' '{file_path}'")
        Command.run(f"bat '{file_path}'")
