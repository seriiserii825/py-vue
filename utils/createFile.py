import os

from pyfzf.pyfzf import FzfPrompt
from rich import print
from rich.console import Console

console = Console()
fzf = FzfPrompt()


def createFile(basepath, ext, placeholder=None, suffix=""):
    files = []
    if not os.path.exists(basepath):
        print(f"[red]Path does not exist: {basepath}, create folder?")
        os.makedirs(basepath)
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
    for file in files:
        print(f"[blue]{file}")
    if placeholder:
        print(f"[yellow]{placeholder}")
    new_file = console.input("[green]Enter new filename: ")
    # add suffix (e.g. 'View') unless the user already typed it
    if suffix and not new_file.endswith(suffix):
        new_file = f"{new_file}{suffix}"
    if f"{new_file}.{ext}" in files:
        print("[red]File already exists, try again.")
        return createFile(basepath, ext, placeholder, suffix)
    os.system(f"touch {basepath}/{new_file}.{ext}")
    return basepath + "/" + new_file + "." + ext
