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
        'type': 'src/types',
        'icons': 'src/icons',
        'scss': 'src/scss/blocks',
        'my.scss': 'src/scss/my.scss',
        }
config['wp'] = {
        'pages': 'src/vue/views',
        'components': 'src/vue/components',
        'store': 'src/vue/store',
        'api': 'src/vue/api',
        'hooks': 'src/vue/hooks',
        'interfaces': 'src/vue/interfaces',
        'type': 'src/vue/types',
        'icons': 'src/vue/icons',
        'scss': 'src/vue/scss/blocks',
        'my.scss': 'src/vue/scss/my.scss',
        }
config['nuxt'] = {
        'pages': 'pages',
        'components': 'components',
        'store': 'store',
        'api': 'api',
        'hooks': 'hooks',
        'composables': 'composables',
        'interfaces': 'interfaces',
        'type': 'types',
        'icons': 'components/icons',
        'scss': 'assets/scss/blocks',
        'my.scss': 'assets/scss/my.scss',
        }

with open(f"{SCRIPT_DIR}/config.ini", 'w') as configfile:
    config.write(configfile)
    print(f"[green]config.ini file created")
