import os
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()
def createDir(basepath):
    dirs = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                dirs.append(entry.name)
    for dir in dirs:
        print(dir)
    choose = input("Create or select, c/s: ")
    if choose == "c":
        new_dir = input("Enter new directory name: ")
        os.mkdir(basepath + "/" + new_dir)
    elif choose == "s":
        selected_dir = fzf.prompt(dirs)
        print(f"selected_dir: {selected_dir}")
        if selected_dir:
            print(f"selected_dir[0]: {selected_dir[0]}")
            return selected_dir[0]
        else:
            print("No directory selected, try again.")
            createDir(basepath)
    else:
        print("Invalid input, try again.")
        createDir(basepath)
