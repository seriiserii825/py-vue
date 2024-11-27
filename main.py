from pyfzf.pyfzf import FzfPrompt

from modules.componentFunc import componentFunc
from modules.viewFunc import viewFunc
fzf = FzfPrompt()
def menu():
    menu_items = [
            "View",
            "Component"
            ]
    selected_menu = fzf.prompt(menu_items)
    print(f"selected_menu: {selected_menu}")
    if selected_menu[0] == "View":
      print("View")
      viewFunc()
    elif selected_menu[0] == "Component":
      print("Component")
      componentFunc()

if __name__ == "__main__":
    menu()
