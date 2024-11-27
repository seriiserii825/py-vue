import subprocess
from utils.createDir import createDir
from utils.createFile import createFile
from utils.getLayoutPath import getLayoutPath
from utils.layoutToFile import layoutToFile

def interfaceFunc():
    dir_path = createDir('src/interfaces')
    print(f"dir_path: {dir_path}")
    file_path = createFile(dir_path, 'ts')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('ts')
    layoutToFile(layout_path, file_path)
    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    class_name = file_name
    subprocess.run(["sed", "-i", f"s|IVue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

