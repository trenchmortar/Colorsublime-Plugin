from . import logger
from . import settings
log = logger.get(__name__)


def init():
    # Load dem settings
    settings.load()
    log.debug('Loaded.')
