import os
from rich import print
from libs.select import selectOne
from libs.selectWithFzf import selectWithFzf
from pyfzf.pyfzf import FzfPrompt

class FilesHandle:
    def __init__(self, basepath: str):
        self.basepath = basepath if basepath != '' else '.'

    def listFiles(self, dir_path=None):
        if dir_path is not None:
            self.basepath = dir_path
        print("Existing files:")
        print(f"[green]List files in ================= {self.basepath}")
        print("")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                print(f"[blue]{entry}")

        print("")
        print(f"[green]List files in ================= {self.basepath}")

    def listDir(self, dir_path=None):
        print(f"[blue]Listing directories in ================ {self.basepath}")
        directories = []
        if dir_path is not None:
            self.basepath = dir_path
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    directories.append(entry.name)
        directories.sort()
        for directory in directories:
            print(f"[yellow]{directory}")
        print(f"[blue]Listing directories in ================ {self.basepath}")

    def createOrChooseDirectory(self):
        self.listDir()
        select_or_create = selectOne(["Select", "Create"])
        if select_or_create == "Create":
            dir_name = input("Enter directory name:")
            if dir_name == '':
                print("Directory name is required")
                exit()
            else:
                os.makedirs(self.basepath + "/" + dir_name)
                print("Directory created")
                return dir_name
        else:
            selected_dir = self.chooseDir()
            return selected_dir

    def drawTree(self, dir_path=None):
        if dir_path is not None:
            self.basepath = dir_path
        os.system(f"tree {self.basepath}")

    def chooseDir(self):
        choosed_dir = []
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    choosed_dir.append(entry.name)
        choosed_dir.sort()
        selected_dir = selectWithFzf(choosed_dir)
        return selected_dir

    def listFilesWithPrefix(self, prefix):
        print(f"Listing directories in ================ {self.basepath}")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                for item in prefix:
                    if entry.startswith(item):
                        print(entry)
        print(f"Listing directories in ================ {self.basepath}")

    def selectWithFzf(self, items):
        fzf = FzfPrompt()
        selected_item = fzf.prompt(items)
        return selected_item[0]

    def chooseFile(self):
        choosed_files = []
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                choosed_files.append(entry)
        if len(choosed_files) == 0:
            exit("[red]No files found")
        else:
            return selectOne(choosed_files)

    def appendToFile(self, file_path, text):
        with open(file_path, "a") as f:
            f.write(text)
        os.system(f"bat {file_path}")

    def addFileName(self, dir_path, placeholder):
        file_name = input(f"Enter file name like, {placeholder}: ")
        if file_name != "":
            file_path = os.path.join(dir_path, file_name)+".php"
            if os.path.exists(file_path):
                print("[red]File already exists")
                exit()
            else:
                return file_name
        else:
            print("[red]File name is required")
            exit()

    def createFile(self, file_path):
        with open(file_path, "w") as f:
            f.write("")
        os.system(f"bat {file_path}")

    def getDir(self):
        selected_dir = self.createOrChooseDirectory()
        dir_path = self.basepath + "/" + selected_dir
        self.drawTree(dir_path)
        print(f"dir_path: {dir_path}")
        if not os.path.exists(dir_path):
            print("[red]Directory does not exist")
            exit()
        return {
            "dir_path": dir_path,
            "selected_dir": selected_dir
        }

    def filePathToNamespace(self, file_path):
        # split in to array file path
        file_path = file_path.split("/")
        new_file_path = file_path[1::]
        # remove last element
        new_file_path = new_file_path[:-1]
        # join the array with \
        new_file_path = "\\".join(new_file_path)
        new_file_path = f"namespace App\\{new_file_path};"
        return new_file_path
