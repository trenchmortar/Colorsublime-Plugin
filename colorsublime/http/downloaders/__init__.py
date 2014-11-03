"""
Module to determine the correct downloader to use.
"""
from . import urllib, wget, curl
from ... import logger
log = logger.get(__name__)


def get():
    if curl.CurlDownloader.is_available():
        log.debug('Using Curl downloader.')
        return curl.CurlDownloader()
    if wget.WgetDownloader.is_available():
        log.debug('Using WGET downloader.')
        return wget.WgetDownloader()
    if urllib.UrllibDownloader.is_available():
        log.debug('Using Urllib downloader.')
        return urllib.UrllibDownloader()
    log.error('No usable downloader found. Please open an issue and we\'ll see if your platform can be added.')
    return None
