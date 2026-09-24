from modules.chooseOrCreateDirectory import chooseOrCreateDirectory
from py_libs.Print import Print

MODULES_DIR = "modules"


def getModulePath(return_created=False):
    # show message to press enter
    Print.warning("Its a module system, press enter to continue")
    input()
    if return_created:
        module_name, created = chooseOrCreateDirectory(MODULES_DIR, return_created=True)
        return f"{MODULES_DIR}/{module_name}", created
    module_name = chooseOrCreateDirectory(MODULES_DIR)
    return f"{MODULES_DIR}/{module_name}"
