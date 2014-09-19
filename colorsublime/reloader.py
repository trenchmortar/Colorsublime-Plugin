import sys
import imp

from . import logger
log = logger.get(__name__)

# Dependecy reloader stolen from the Emmet plugin
parent = 'Colorsublime.colorsublime'

reload_mods = []
for mod in sys.modules:
    if mod.startswith(parent) and sys.modules[mod] is not None:
        reload_mods.append(mod)

mods_load_order = [
    'logger',
    'async',
    'commands',
    'io',
    'settings',
    'status',

    'repository',
    'repository.themes',

    'http',
    'http.cache',
    'http.downloaders',
    'http.downloaders.downloader_base',
    'http.downloaders.curl',
    'http.downloaders.urllib',
    'http.downloaders.wget',
]

mods_load_order = [parent + '.' + mod for mod in mods_load_order]

log.debug('reloading')
for mod in mods_load_order:
    if mod in reload_mods:
        imp.reload(sys.modules[mod])
