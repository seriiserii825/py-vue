import os

from classes.Layout import Layout
from py_libs.Command import Command
from py_libs.Print import Print


def autoCreateModuleScss(dir_path: str, class_name: str) -> str:
    scss_path = f"{dir_path}/{class_name}.scss"
    if os.path.exists(scss_path):
        Print.warning(f"SCSS already exists: {scss_path}")
        return scss_path
    Command.run(f"touch '{scss_path}'")
    Layout("scss", scss_path)
    Command.run(f"sed -i 's|vue|{class_name}|g' '{scss_path}'")
    Print.success(f"Created scss: {scss_path}")
    Command.run(f"bat '{scss_path}'")
    return scss_path
