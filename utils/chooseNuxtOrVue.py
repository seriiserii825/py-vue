from constants import CONFIG_TXT_PATH, SCRIPT_DIR
from utils.getSelectedTemplate import getSelectedTemplate


def chooseNuxtOrVue():
    toggle = input("Do you want to change the template? (y/n) or Enter: ")
    config_txt = getSelectedTemplate()
    if toggle == 'y':
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", 'w') as file:
            file.write('nuxt' if config_txt == 'vue' else 'vue')
    else:
        print("[red]Template not changed")
