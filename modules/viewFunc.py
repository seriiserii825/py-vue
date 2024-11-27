import subprocess
from utils.camelToKebabCase import camelToKebabCase
from utils.createFile import createFile
from utils.getLayoutPath import getLayoutPath
from utils.layoutToFile import layoutToFile
def viewFunc():
    dir_path = 'src/views'
    file_path = createFile(dir_path, 'vue')
    print(f"file_path: {file_path}")
    layout_path = getLayoutPath('vue')
    layoutToFile(layout_path, file_path)
    # get file name from file path without extension
    file_name = file_path.split('/')[-1].split('.')[0]
    class_name = camelToKebabCase(file_name)
    subprocess.run(["sed", "-i", f"s|vue|{class_name}|g", file_path], check=True)
    subprocess.run(["bat", file_path], check=True)

