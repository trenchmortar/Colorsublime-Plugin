from abc import ABCMeta, abstractmethod
import json

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

    def get_json(self, url):
        resp = self.get(url)
        if resp:
            try:
                themes = json.loads(resp.decode('utf-8'))
            except ValueError:
                log.error('URL %s does not contain a JSON file.', url)
                return False
        return themes

    def get_file(self, url):
        return self.get(url)
