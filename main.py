from pyfzf.pyfzf import FzfPrompt
from rich import print

from modules.componentFunc import componentFunc
from modules.hookFunc import hookFunc
from modules.interfaceFunc import interfaceFunc
from modules.scssFunc import scssFunc
from modules.viewFunc import viewFunc
fzf = FzfPrompt()
def menu():
    menu_items = [
            "View(vue)",
            "Component(vue)",
            "Scss file",
            "Interface",
            "Hook"
            ]
    selected_menu = fzf.prompt(menu_items)
    if selected_menu[0] == "View(vue)":
        viewFunc()
    elif selected_menu[0] == "Component(vue)":
        componentFunc()
    elif selected_menu[0] == "Scss file":
        scssFunc()
    elif selected_menu[0] == "Interface":
        interfaceFunc()
    elif selected_menu[0] == "Hook":
        hookFunc()
    else:
        print("Invalid selection")
        menu()

if __name__ == "__main__":
    menu()
