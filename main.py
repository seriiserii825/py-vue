from pyfzf.pyfzf import FzfPrompt
from rich import print
from config import config

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
    selected_menu = fzf.prompt(menu_items)
    if selected_menu[0] == "View(vue)":
        viewFunc()
    elif selected_menu[0] == "Component(vue)":
        componentFunc()
    elif selected_menu[0] == "Icon(vue)":
        iconFunc()
    elif selected_menu[0] == "Scss file":
        scssFunc()
    elif selected_menu[0] == "Interface":
        interfaceFunc()
    elif selected_menu[0] == "Type":
        typeFunc()
    elif selected_menu[0] == "Hook":
        hookFunc()
    elif selected_menu[0] == "Composable":
        composableFunc()
    elif selected_menu[0] == "Api":
        apiFunc()
    elif selected_menu[0] == "Store":
        storeFunc()
    else:
        print("Invalid selection")
        menu()

if __name__ == "__main__":
    menu()
