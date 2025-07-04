import os


class Layout:
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, name, file_path: str):
        self.name = name
        self.file_path = file_path
        self.layout_path = ""
        self.getLayoutPath()
        self.layoutToFile()

    def getLayoutPath(self):
        if self.name == "vue":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.vue"
        elif self.name == "scss":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.scss"
        elif self.name == "interface":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.interface.ts"
        elif self.name == "type":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.type.ts"
        elif self.name == "hook":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.hook.ts"
        elif self.name == "api":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.api.ts"
        elif self.name == "store":
            self.layout_path = f"{self.ROOT_DIR}/layouts/layout.store.ts"
        else:
            self.layout_path = ""

    def layoutToFile(self):
        layout_file_content = ""
        with open(self.layout_path, "r") as file:
            layout_file_content = file.read()
        with open(self.file_path, "w") as file:
            file.write(layout_file_content)
