import os


def getLayoutPath(name):
    ROOT_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    if name == "vue":
        return f"{ROOT_DIR}/layouts/layout.vue"
    elif name == "scss":
        return f"{ROOT_DIR}/layouts/layout.scss"
    elif name == "ts":
        return f"{ROOT_DIR}/layouts/layout.interface.ts"
    else:
        exit('Invalid layout name')
