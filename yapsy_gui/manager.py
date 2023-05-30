import os
from yapsy.IPlugin import IPlugin
from yapsy.PluginManager import PluginManager
from yapsy.AutoInstallPluginManager import AutoInstallPluginManager

INSTALL_DIR = "plugins"
INFO_EXTENSION = "plugin"
PLUGINS_CATEGORY = "Default"


class Manager(PluginManager):

    def __init__(self):
        super().__init__()
        self.setPluginPlaces([INSTALL_DIR])
        self.setCategoriesFilter({PLUGINS_CATEGORY: IPlugin})
        self.setPluginInfoExtension(INFO_EXTENSION)

    @property
    def plugins(self):
        self.collectPlugins()
        return self.getAllPlugins()

    def removePlugin(self, plugin):
        self.removePluginFromCategory(plugin, PLUGINS_CATEGORY)
        prefix = os.path.basename(plugin.path)
        for item in os.listdir(INSTALL_DIR):
            if item.startswith(prefix):
                os.remove(os.path.join(INSTALL_DIR, item))


class Installer(AutoInstallPluginManager):

    def __init__(self):
        super().__init__(plugin_info_ext=INFO_EXTENSION)
        self.setInstallDir(INSTALL_DIR)

    def install(self, plugin_file):
        plugin_dir = os.path.dirname(plugin_file)
        try:
            if super().install(plugin_dir, plugin_file):
                return True
        except ValueError:
            return False