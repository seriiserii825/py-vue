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
            "Api",
            "Store"
            ]

    menu_entry_index = fzf.prompt(menu_items)

    if menu_entry_index[0] == 'View(vue)':
        viewFunc()
    elif menu_entry_index[0] == 'Component(vue)':
        componentFunc()
    elif menu_entry_index[0] == 'Icon(vue)':
        iconFunc()
    elif menu_entry_index[0] == 'Scss file':
        scssFunc()
    elif menu_entry_index[0] == 'Interface':
        interfaceFunc()
    elif menu_entry_index[0] == 'Type':
        typeFunc()
    elif menu_entry_index[0] == 'Hook':
        composableFunc()
    elif menu_entry_index[0] == 'Api':
        apiFunc()
    elif menu_entry_index[0] == 'Store':
        storeFunc()
    else:
        exit()

if __name__ == "__main__":
    menu()
