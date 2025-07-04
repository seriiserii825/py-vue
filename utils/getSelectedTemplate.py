from constants import CONFIG_TXT_PATH, SCRIPT_DIR


def getSelectedTemplate():
    with open(f"{SCRIPT_DIR}/{CONFIG_TXT_PATH}", "r") as file:
        config_txt = file.read()
    return config_txt
