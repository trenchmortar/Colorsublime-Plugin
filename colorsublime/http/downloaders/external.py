import traceback
import subprocess
import shutil

from colorsublime import logger
log = logger.get(__name__)
from colorsublime import settings

from .downloader_base import DownloaderBase


def check_output(*popenargs, **kwargs):
    # Python 3
    if hasattr(subprocess, 'check_output'):
        return subprocess.check_output(*popenargs, **kwargs)

    # Python 2
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd, output)
    return output


class ExternalDownloader(DownloaderBase):
    """Abstract Base class for downloading through an external utility"""
    program = None
    args = []

    @staticmethod
    def _which(command):
        # Python 3
        if hasattr(shutil, 'which'):
            return shutil.which(command)

        # Python 2
        try:
            subprocess.call([command])
        except OSError:
            return False
        return True

    @classmethod
    def is_available(cls):
        return not settings.is_windows() and cls._which(cls.program)

    def get(self, url):
        try:
            log.debug('%s downloader getting url %s', self.program, url)
            call = [self.program] + self.args + [url]
            result = check_output(call)
        except subprocess.CalledProcessError:
            log.error('%s downloader failed.', self.program)
            traceback.print_exc()
            result = False
        return result
