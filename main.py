from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()
def menu():
    menu_items = [
            "View",
            "Component"
            ]
    selected_menu = fzf.prompt(menu_items)
    if selected_menu == "View":
        print("View")
    elif selected_menu == "Component":
        print("Component")
