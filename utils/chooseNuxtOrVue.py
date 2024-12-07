import os
from constants import CONFIG_TXT_PATH, SCRIPT_DIR
from utils.getSelectedTemplate import getSelectedTemplate
from rich import print


def chooseNuxtOrVue():
    config_txt = getSelectedTemplate()
    print(f"[green]Current template: ([blue]{config_txt})")

#if in root dir is src folder then it is vue project
    if os.path.isdir('src'):
        print("[green]Vue project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", 'w') as file:
            file.write('vue')
    else:
        print("[green]Nuxt project detected")
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", 'w') as file:
            file.write('nuxt')

    config_txt = getSelectedTemplate()
    print(f"[green]Current template: ([blue]{config_txt})")
    input("[green]Press Enter to continue...")
