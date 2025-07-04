import os


def getFromClipBoard():
    command = "xclip -o -selection clipboard"
    print(f"command from buffer: {command}")
    return os.popen(command).read().strip()
