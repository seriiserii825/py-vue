import os

from rich import print
from rich.console import Console
from rich.table import Table

from modules.chooseDir import chooseDir
from modules.select import selectOne

console = Console()


def _print_in_columns(items, color="blue"):
    import math
    term = os.get_terminal_size()
    max_len = max(len(i) for i in items) + 2
    num_cols = max(1, term.columns // max_len)
    num_rows = math.ceil(len(items) / num_cols)
    table = Table(show_header=False, show_edge=False, box=None, padding=(0, 1))
    for _ in range(num_cols):
        table.add_column()
    for row_i in range(num_rows):
        row = []
        for col_i in range(num_cols):
            idx = col_i * num_rows + row_i
            row.append(f"[{color}]{items[idx]}" if idx < len(items) else "")
        table.add_row(*row)
    console.print(table)


def chooseOrCreateDirectory(basepath, return_created=False):
    print(f"[green]Listing directories in ================ {basepath}")
    directories = []
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir():
                directories.append(entry.name)
    directories.sort()

    terminal_lines = os.get_terminal_size().lines
    if len(directories) > terminal_lines - 4:
        _print_in_columns(directories)
    else:
        for directory in directories:
            print(f"[blue]{directory}")

    print(f"[green]Listing directories in ================ {basepath}")

    select_or_create = selectOne(["Select", "Create"])
    if select_or_create == "Create":
        dir_name = input("Enter directory name (kebab-case): ")
        if dir_name == "":
            print("Directory name is required")
            exit()
        elif os.path.exists(basepath + "/" + dir_name):
            print(f"[red]Directory '{dir_name}' already exists")
            exit()
        else:
            os.makedirs(basepath + "/" + dir_name)
            print("Directory created")
            return (dir_name, True) if return_created else dir_name
    else:
        selected_dir = chooseDir(basepath)
        return (selected_dir, False) if return_created else selected_dir
