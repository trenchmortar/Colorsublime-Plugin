'''
Global settings module
By @blopker
'''
import sublime
import os

plugin_name = 'Colorsublime'

PLUGIN_PREF = plugin_name + '.sublime-settings'
SUBLIME_PREF = 'Preferences.sublime-settings'


def get(*args):
    return sublime.load_settings(PLUGIN_PREF).get(*args)


def _get_abs_path(path):
    if path[0] != '/':
        path = os.path.join(sublime.packages_path(), path)
    return path


def get_cache_path():
    return _get_abs_path(get('cache_folder'))


def get_install_path():
    return _get_abs_path(get('install_folder'))


def get_color_scheme():
    return sublime.load_settings(SUBLIME_PREF).get('color_scheme', '')


def set_color_scheme(path):
    return sublime.load_settings(SUBLIME_PREF).set('color_scheme', path)


def save_user():
    sublime.save_settings(SUBLIME_PREF)


def isDebug():
    return get('debug')


def platform():
    return sublime.platform()


def sublime_version():
    return int(sublime.version())
