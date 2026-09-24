import os

from py_libs.Command import Command


def createMyScssFile(file_path):
    if not os.path.exists(file_path):
        Command.run(f"touch '{file_path}'")
