from pyfzf.pyfzf import FzfPrompt
from rich import print
from config import config

from simple_term_menu import TerminalMenu
from modules.apiFunc import apiFunc
from modules.componentFunc import componentFunc
from modules.composableFunc import composableFunc
from modules.hookFunc import hookFunc
from modules.iconFunc import iconFunc
from modules.interfaceFunc import interfaceFunc
from modules.scssFunc import scssFunc
from modules.storeFunc import storeFunc
from modules.typeFunc import typeFunc
from modules.viewFunc import viewFunc
fzf = FzfPrompt()
def menu():
    menu_items = [
            "View(vue)",
            "Component(vue)",
            "Icon(vue)",
            "Scss file",
            "Interface",
            "Type",
            "Hook",
            "Composable",
            "Api",
            "Store"
            ]

    terminal_menu = TerminalMenu(menu_items)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        viewFunc()
    elif menu_entry_index == 1:
        componentFunc()
    elif menu_entry_index == 2:
        iconFunc()
    elif menu_entry_index == 3:
        scssFunc()
    elif menu_entry_index == 4:
        interfaceFunc()
    elif menu_entry_index == 5:
        typeFunc()
    elif menu_entry_index == 6:
        hookFunc()
    elif menu_entry_index == 7:
        composableFunc()
    elif menu_entry_index == 8:
        apiFunc()
    elif menu_entry_index == 9:
        storeFunc()
    else:
        print("Invalid selection")
        menu()

if __name__ == "__main__":
    menu()
