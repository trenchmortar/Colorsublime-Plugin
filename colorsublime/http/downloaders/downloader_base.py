from abc import ABCMeta, abstractmethod

from ... import logger
log = logger.get(__name__)


class DownloaderBase(object):
    """Abstract base class for downloaders. Downloaders must implement these
    methods."""
    __metaclass__ = ABCMeta

    @classmethod
    def is_available(cls):
        """ Is this downloader available?"""
        raise NotImplementedError()

    @abstractmethod
    def get(self, url):
        """Get string content from URL"""
        raise NotImplementedError()
