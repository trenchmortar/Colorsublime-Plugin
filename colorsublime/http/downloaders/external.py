from .downloader_base import DownloaderBase

from ... import logger
log = logger.get(__name__)
import traceback
import subprocess
import shutil

from ... import settings


class ExternalDownloader(DownloaderBase):
    """Abstract Base class for downloading through an external utility"""
    program = None
    args = []

    @classmethod
    def is_available(cls):
        return not settings.is_windows() and shutil.which(cls.program)

    def get(self, url):
        try:
            log.debug('%s downloader getting url %s', self.program, url)
            call = [self.program] + self.args + [url]
            result = subprocess.check_output(call)
        except subprocess.CalledProcessError:
            log.error('%s downloader failed.', self.program)
            traceback.print_exc()
            result = False
        return result
