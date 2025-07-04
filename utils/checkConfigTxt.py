import os

from constants import CONFIG_TXT_PATH, SCRIPT_DIR


def checkConfigTxt():
    if not os.path.exists(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}"):
        with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "w") as file:
            file.write("vue")
