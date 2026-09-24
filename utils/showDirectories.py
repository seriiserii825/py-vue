import os

from rich import print

from py_libs.Print import Print


def showDirectories(basepath):
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()
    Print.info(f"Directories in {basepath}")
    for directory in directories:
        print(f"  [blue]{directory}")
