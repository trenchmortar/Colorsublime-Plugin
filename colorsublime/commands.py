'''
Collection of functions the plugin can invoke. Most if not all should be
non-blocking (@async) functions to keep the main UI thread from freezing.

These functions should catch all unexpected exceptions so the plugin does not
have to. Unexpected exceptions should return False. Expected exceptions should
be caught by other modules this module uses. Log all unusual behavior.

All @async functions have an optional callback parameter as the last argument.
'''

from . import logger
log = logger.get(__name__)
from . import settings
from . import http
from . import io
from .async import async
from .repository import Theme, Themes


def get_current_theme():
    current_path = settings.get_color_scheme()
    return Theme(file_path=current_path)


@async
def fetch_themes():
    """ Get current theme archive """
    repo = settings.get('repo')
    archive = http.get(repo)
    cache_path = settings.get_cache_path()
    io.extract(archive, cache_path)
    json = io.read_json(cache_path, 'themes.json')
    themes = [Theme.from_repo(j, cache_path) for j in json]
    return Themes(themes)


def set_theme(theme, commit=False):
    settings.set_color_scheme(theme.file_path)
    if commit:
        settings.save_user()
