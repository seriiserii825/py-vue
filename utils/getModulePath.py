from modules.chooseOrCreateDirectory import chooseOrCreateDirectory

MODULES_DIR = "modules"


def getModulePath() -> str:
    module_name = chooseOrCreateDirectory(MODULES_DIR)
    return f"{MODULES_DIR}/{module_name}"
