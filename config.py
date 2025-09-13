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

config["vue"] = {
    "pages": "src/views",
    "components": "src/components",
    "store": "src/store",
    "api": "src/api",
    "hooks": "src/hooks",
    "interfaces": "src/interfaces",
    "type": "src/types",
    "icons": "src/icons",
    "scss": "src/scss/blocks",
    "my.scss": "src/scss/my.scss",
}
config["wp"] = {
    "pages": "src/vue/views",
    "components": "src/vue/components",
    "store": "src/vue/store",
    "api": "src/vue/api",
    "hooks": "src/vue/composables",
    "composables": "src/vue/composables",
    "interfaces": "src/vue/interfaces",
    "type": "src/vue/types",
    "icons": "src/vue/icons",
    "scss": "src/vue/scss/blocks",
    "my.scss": "src/vue/scss/my.scss",
}
config["nuxt"] = {
    "pages": "pages",
    "components": "components",
    "store": "store",
    "api": "api",
    "hooks": "hooks",
    "composables": "composables",
    "interfaces": "interfaces",
    "type": "types",
    "icons": "icons",
    "scss": "assets/scss/blocks",
    "my.scss": "assets/scss/my.scss",
}
config["nuxt4"] = {
    "pages": "app/pages",
    "components": "app/components",
    "store": "app/store",
    "api": "app/api",
    "hooks": "app/hooks",
    "composables": "app/composables",
    "interfaces": "app/interfaces",
    "type": "app/types",
    "icons": "app/icons",
    "scss": "app/assets/scss/blocks",
    "my.scss": "app/assets/scss/my.scss",
}
config["laravel"] = {
    "pages": "resources/js/Pages",
    "components": "resources/js/Components",
    "store": "resources/js/Store",
    "api": "resources/js/Api",
    "hooks": "resources/js/Hooks",
    "composables": "resources/js/Composables",
    "interfaces": "resources/js/Interfaces",
    "type": "resources/js/Types",
    "icons": "resources/js/Icons",
    "scss": "resources/js/Scss/blocks",
    "my.scss": "resources/js/Scss/my.scss",
}

with open(f"{SCRIPT_DIR}/config.ini", "w") as configfile:
    config.write(configfile)
    print(f"[green]config.ini file created")
