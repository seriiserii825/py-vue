import os

from rich import print

from py_libs.Command import Command
from py_libs.Print import Print
from py_libs.Select import Select


class FilesHandle:
    def __init__(self, basepath: str):
        self.basepath = basepath if basepath != "" else "."

    def listFiles(self, dir_path=None):
        if dir_path is not None:
            self.basepath = dir_path
        Print.info(f"List files in {self.basepath}")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                print(f"[blue]{entry}")

    def listDir(self, dir_path=None):
        if dir_path is not None:
            self.basepath = dir_path
        Print.info(f"Listing directories in {self.basepath}")
        directories = []
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    directories.append(entry.name)
        directories.sort()
        for directory in directories:
            print(f"[yellow]{directory}")

    def createOrChooseDirectory(self):
        self.listDir()
        select_or_create = Select.select_one(["Select", "Create"])
        if select_or_create == "Create":
            dir_name = input("Enter directory name:")
            if dir_name == "":
                Print.error("Directory name is required")
                exit()
            else:
                os.makedirs(self.basepath + "/" + dir_name)
                Print.success("Directory created")
                return dir_name
        else:
            selected_dir = self.chooseDir()
            return selected_dir

    def drawTree(self, dir_path=None):
        if dir_path is not None:
            self.basepath = dir_path
        Command.run(f"tree '{self.basepath}'")

    def chooseDir(self):
        choosed_dir = []
        with os.scandir(self.basepath) as entries:
            for entry in entries:
                if entry.is_dir():
                    choosed_dir.append(entry.name)
        choosed_dir.sort()
        selected_dir = Select.select_fzf_one(choosed_dir)
        return selected_dir

    def directoryIsEmpty(self):
        if os.path.exists(self.basepath):
            if len(os.listdir(self.basepath)) == 0:
                return True
            else:
                return False

    def listFilesWithPrefix(self, prefix):
        Print.info(f"Listing directories in {self.basepath}")
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                for item in prefix:
                    if entry.startswith(item):
                        print(entry)

    def chooseFile(self):
        choosed_files = []
        for entry in os.listdir(self.basepath):
            if os.path.isfile(os.path.join(self.basepath, entry)):
                choosed_files.append(entry)
        if len(choosed_files) == 0:
            exit("[red]No files found")
        else:
            return Select.select_one(choosed_files)

    def appendToFile(self, file_path, text):
        with open(file_path, "a") as f:
            f.write(text)
        Command.run(f"bat '{file_path}'")

    def addFileName(self, dir_path, placeholder):
        file_name = input(f"Enter file name like, {placeholder}: ")
        if file_name != "":
            file_path = os.path.join(dir_path, file_name) + ".php"
            if os.path.exists(file_path):
                Print.error("File already exists")
                exit()
            else:
                return file_name
        else:
            Print.error("File name is required")
            exit()

    def createFile(self, file_path):
        with open(file_path, "w") as f:
            f.write("")
        Command.run(f"bat '{file_path}'")

    def getDir(self):
        selected_dir = self.createOrChooseDirectory()
        dir_path = self.basepath + "/" + selected_dir
        self.drawTree(dir_path)
        Print.info(f"dir_path: {dir_path}")
        if not os.path.exists(dir_path):
            Print.error("Directory does not exist")
            exit()
        return {"dir_path": dir_path, "selected_dir": selected_dir}

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
