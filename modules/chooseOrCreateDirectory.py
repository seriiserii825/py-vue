import os

from rich import print

from modules.chooseDir import chooseDir
from modules.select import selectOne


def chooseOrCreateDirectory(basepath):
    print(f"[green]Listing directories in ================ {basepath}")
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()
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
