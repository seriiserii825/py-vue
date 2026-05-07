import os
import subprocess

from classes.Layout import Layout
from rich import print


def autoCreateModuleScss(dir_path: str, class_name: str) -> str:
    scss_path = f"{dir_path}/{class_name}.scss"
    if os.path.exists(scss_path):
        print(f"[yellow]SCSS already exists: {scss_path}")
        return scss_path
    os.system(f"touch {scss_path}")
    Layout("scss", scss_path)
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", scss_path], check=True)
    print(f"[green]Created scss: {scss_path}")
    subprocess.run(["bat", scss_path], check=True)
    return scss_path
