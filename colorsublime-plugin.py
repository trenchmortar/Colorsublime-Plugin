import imp
import sys

import sublime_plugin

from .colorsublime import commands
from .colorsublime import status
from . import colorsublime

NO_SELECTION = -1

# Make sure all dependencies are reloaded on upgrade
reloader_path = 'Colorsublime.colorsublime.reloader'
if reloader_path in sys.modules:
    imp.reload(sys.modules[reloader_path])
from .colorsublime import reloader


class ColorsublimeInstallThemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        print('Running install command.')
        self.theme_status = {}
        self.status = status.loading('Getting Theme list')
        self.original_theme = commands.get_current_theme()
        commands.fetch_themes(self.display_list)

    def display_list(self, themes):
        self.status.stop()
        if not themes:
            status.error('Theme list not found. Please check internet ' +
                         'connection or enable debug in the settings and ' +
                         'report the stack traces.')
            return
        self.themes = themes
        self.window.show_quick_panel(themes.quick_list(),
                                     self.on_select,
                                     on_highlight=self.on_highlighted)

    def on_highlighted(self, theme_index):
        commands.set_theme(self.themes[theme_index])

    def on_select(self, theme_index):
        if theme_index is NO_SELECTION:
            commands.set_theme(self.original_theme)
            status.message('Theme selection canceled.')
            return

        theme = self.themes[theme_index]
        commands.set_theme(theme, commit=True)
        status.message('Theme %s installed successfully!' % theme.name)


def plugin_loaded():
    colorsublime.init()
