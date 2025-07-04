from configparser import ConfigParser

from config import SCRIPT_DIR


def getConfigData(template, path):
    # Read the configuration file
    config = ConfigParser()
    config.read(f"{SCRIPT_DIR}/config.ini")
    return config[template][path]
