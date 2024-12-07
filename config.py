from configparser import ConfigParser
from rich import print

from constants import SCRIPT_DIR
from utils.checkConfigTxt import checkConfigTxt
from utils.chooseNuxtOrVue import chooseNuxtOrVue
from utils.getSelectedTemplate import getSelectedTemplate


checkConfigTxt()
config_txt = getSelectedTemplate()
chooseNuxtOrVue()

config = ConfigParser()

config['vue'] = {
        'pages': 'src/views',
        'components': 'src/components',
        'store': 'src/store',
        'api': 'src/api',
        'hooks': 'src/hooks',
        'interfaces': 'src/interfaces',
        'icons': 'src/icons',
        'scss': 'src/scss/blocks',
        'my.scss': 'src/scss/my.scss',
        }
config['nuxt'] = {
        'pages': 'pages',
        'components': 'components',
        'store': 'store',
        'api': 'api',
        'hooks': 'hooks',
        'interfaces': 'interfaces',
        'icons': 'components/icons',
        'scss': 'assets/scss/blocks',
        'my.scss': 'assets/scss/my.scss',
        }

with open(f"{SCRIPT_DIR}/config.ini", 'w') as configfile:
    config.write(configfile)
    print(f"[green]config.ini file created")
