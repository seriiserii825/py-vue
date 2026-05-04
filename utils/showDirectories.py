import os

from rich import print


def showDirectories(basepath):
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()
    print(f"[green]Directories in ================ {basepath}")
    for directory in directories:
        print(f"  [blue]{directory}")
    print(f"[green]================================")
