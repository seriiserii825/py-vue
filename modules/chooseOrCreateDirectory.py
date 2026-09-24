import os

from rich import print

from modules.chooseDir import chooseDir
from py_libs.Menu import Menu
from py_libs.Print import Print
from py_libs.Select import Select


def chooseOrCreateDirectory(basepath, return_created=False):
    Print.info(f"Listing directories in {basepath}")
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()

    terminal_lines = os.get_terminal_size().lines
    if len(directories) > terminal_lines - 4:
        Menu.print_grid(directories)
    else:
        for directory in directories:
            print(f"[blue]{directory}")

    select_or_create = Select.select_one(["Select", "Create"])
    if select_or_create == "Create":
        dir_name = input("Enter directory name (kebab-case): ")
        if dir_name == "":
            Print.error("Directory name is required")
            exit()
        elif os.path.exists(basepath + "/" + dir_name):
            Print.error(f"Directory '{dir_name}' already exists")
            exit()
        else:
            os.makedirs(basepath + "/" + dir_name)
            Print.success("Directory created")
            return (dir_name, True) if return_created else dir_name
    else:
        selected_dir = chooseDir(basepath)
        return (selected_dir, False) if return_created else selected_dir
