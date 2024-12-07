import os
import subprocess
def createMyScssFile(file_path):
    if not os.path.exists(file_path):
        subprocess.run(["touch", file_path], check=True)
