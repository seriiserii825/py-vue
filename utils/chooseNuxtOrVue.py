import os

from py_libs.Print import Print

from constants import CONFIG_TXT_PATH, SCRIPT_DIR
from utils.getSelectedTemplate import getSelectedTemplate


def chooseNuxtOrVue():
    config_txt = getSelectedTemplate()
    Print.info(f"Current template: ({config_txt})")

    # if in root dir is src folder then it is vue project
    if os.path.isdir("src/vue/"):
        Print.success("Wp project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("wp")
    elif os.path.isdir("app") or os.path.isdir("src/app/"):
        Print.success("Nuxt4 project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("nuxt4")
    elif os.path.isdir("src"):
        Print.success("Vue project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("vue")
    elif os.path.isdir("resources/js/"):
        Print.success("Laravel project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("laravel")
    else:
        Print.success("Nuxt project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("nuxt")

    config_txt = getSelectedTemplate()
    Print.info(f"Current template: ({config_txt})")
    input("Press Enter to continue...")
