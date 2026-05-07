from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from rich import print

MODULES_DIR = "modules"


def getModulePath() -> str:
    # show message to press enter
    print("[yellow]Its a module system, press enter to continue")
    input()
    module_name = chooseOrCreateDirectory(MODULES_DIR)
    return f"{MODULES_DIR}/{module_name}"
