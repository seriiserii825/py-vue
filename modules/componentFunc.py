from utils.createDir import createDir
from utils.createFile import createFile

def componentFunc():
   dir_path = createDir('src/components')
   print(f"dir_path: {dir_path}")
   file_path = createFile(dir_path, 'vue')
   print(f"file_path: {file_path}")
