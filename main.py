from pyfzf.pyfzf import FzfPrompt
from rich import print

from modules.componentFunc import componentFunc
from modules.viewFunc import viewFunc
fzf = FzfPrompt()
def menu():
    menu_items = [
            "View",
            "Component"
            ]
    selected_menu = fzf.prompt(menu_items)
    if selected_menu[0] == "View":
      viewFunc()
    elif selected_menu[0] == "Component":
      componentFunc()

if __name__ == "__main__":
    menu()
