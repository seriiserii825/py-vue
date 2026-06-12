from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from rich import print

MODULES_DIR = "modules"


def getModulePath(return_created=False):
    # show message to press enter
    print("[yellow]Its a module system, press enter to continue")
    input()
    if return_created:
        module_name, created = chooseOrCreateDirectory(MODULES_DIR, return_created=True)
        return f"{MODULES_DIR}/{module_name}", created
    module_name = chooseOrCreateDirectory(MODULES_DIR)
    return f"{MODULES_DIR}/{module_name}"
