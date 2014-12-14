"""
Collection of functions the plugin can invoke. Most if not all should be
non-blocking (@async) functions to keep the main UI thread from freezing.

These functions should catch all unexpected exceptions so the plugin does not
have to. Unexpected exceptions should return False. Expected exceptions should
be caught by other modules this module uses. Log all unusual behavior.

All @async functions have an optional callback parameter as the last argument.
"""

from . import logger
log = logger.get(__name__)
from . import settings
from . import http
from . import io
from .async import async
from .theme import Theme


def get_current_theme():
    return settings.get_current_theme()


@async
def fetch_repo():
    """ Get current theme archive """
    archive = http.get(settings.repo_url())
    io.extract(archive, settings.cache_path())
    themes_list = io.read_json(settings.themes_list_path())
    themes = [Theme.from_json(theme) for theme in themes_list]
    return themes


def preview_theme(theme):
    log.debug('Previewing theme %s at %s', theme.name, theme.cache_path.abs)
    settings.set_theme(theme.cache_path.rel)


def install_theme(theme):
    log.debug('Installing theme %s to %s', theme.name, theme.install_path.abs)
    io.copy(theme.cache_path.abs, theme.install_path.abs)
    settings.set_theme(theme.install_path.rel)
    settings.commit()


def revert_theme(path):
    log.debug('Reverting theme at path %s', path)
    settings.set_theme(path)
