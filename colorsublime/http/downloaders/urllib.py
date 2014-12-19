from .downloader_base import DownloaderBase
from ... import logger
log = logger.get(__name__)
import traceback


try:
    from urllib import request
except ImportError:
    import urllib2 as request

try:
    import ssl
    SSL = True
except ImportError:
    SSL = False


class UrllibDownloader(DownloaderBase):
    """Downloader that uses the native Python HTTP library.
    WARNING: Does not verify HTTPS certificates."""

    @staticmethod
    def is_available():
        return SSL

    def get(self, url):
        # Proxy support
        request.install_opener(request.build_opener(request.ProxyHandler()))
        try:
            log.debug('Urllib downloader getting url %s', url)
            result = request.urlopen(url)
        except Exception as e:
            log.error('Urllib downloader failed: %s' % e.reason)
            traceback.print_exc()
            result = b''
        if result.getcode() >= 400:
            return b''
        return result.read()
