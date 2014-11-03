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
    args = None

    @classmethod
    def is_available(cls):
        return settings.platform() != 'windows' and shutil.which(cls.program)

    def get(self, url):
        try:
            log.debug('%s downloader getting url %s', self.program, url)
            result = subprocess.check_output([self.program, self.args, url])
        except subprocess.CalledProcessError:
            log.error('%s downloader failed.', self.program)
            traceback.print_exc()
            result = False
        return result
