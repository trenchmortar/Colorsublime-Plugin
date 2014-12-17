import imp
import sys

import sublime_plugin

from .colorsublime import commands
from .colorsublime import status

NO_SELECTION = -1

# Make sure all dependencies are reloaded on upgrade
reloader_path = 'Colorsublime.colorsublime.reloader'
if reloader_path in sys.modules:
    imp.reload(sys.modules[reloader_path])
from .colorsublime import reloader
reloader.reload()


class InstallThemeCommand(sublime_plugin.WindowCommand):
    def run(self):
        print('Running install command.')
        self.theme_status = {}
        self.status = status.loading('Getting Theme list')
        commands.fetch_repo(self.display_list)

    def display_list(self, themes):
        self.status.stop()
        if not themes:
            status.error('Theme list not found. Please check internet ' +
                         'connection or enable debug in the settings and ' +
                         'report the stack traces.')
            return

        self.themes = themes
        self.initial_theme = commands.get_current_theme()

        quick_list = [[theme.name,
                       theme.author,
                       theme.description] for theme in self.themes]
        quick_list.sort()

        self.window.show_quick_panel(quick_list,
                                     self.on_select,
                                     on_highlight=self.on_highlighted)

    def on_highlighted(self, theme_index):
        commands.preview_theme(self.themes[theme_index])

    def on_select(self, theme_index):
        if theme_index is NO_SELECTION:
            commands.revert_theme(self.initial_theme)
            status.message('Theme selection cancelled.')
            return

        theme = self.themes[theme_index]
        commands.install_theme(theme)
        status.message('Theme %s installed!' % theme.name)


class BrowseCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('open_url', {'url': 'http://colorsublime.com'})
