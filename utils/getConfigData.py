from configparser import ConfigParser
from config import SCRIPT_DIR


def getConfigData(is_vue, path):
    # Read the configuration file
    config = ConfigParser()
    config.read(f"{SCRIPT_DIR}/config.ini")
    if is_vue:
        return config['vue'][path]
    else:
        return config['nuxt'][path]
