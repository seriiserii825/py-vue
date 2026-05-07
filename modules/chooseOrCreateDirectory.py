import os

from rich import print
from rich.columns import Columns
from rich.console import Console

from modules.chooseDir import chooseDir
from modules.select import selectOne

console = Console()


def chooseOrCreateDirectory(basepath):
    print(f"[green]Listing directories in ================ {basepath}")
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()

    terminal_lines = os.get_terminal_size().lines
    # 4 lines reserved for headers, prompt, etc.
    if len(directories) > terminal_lines - 4:
        console.print(Columns([f"[blue]{d}" for d in directories], equal=True, expand=True))
    else:
        for directory in directories:
            print(f"[blue]{directory}")

    print(f"[green]Listing directories in ================ {basepath}")

    select_or_create = selectOne(["Select", "Create"])
    if select_or_create == "Create":
        dir_name = input("Enter directory name:")
        if dir_name == "":
            print("Directory name is required")
            exit()
        else:
            os.makedirs(basepath + "/" + dir_name)
            print("Directory created")
            return dir_name
    else:
        selected_dir = chooseDir(basepath)
        return selected_dir
