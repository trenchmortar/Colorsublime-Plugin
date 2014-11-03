from .external import ExternalDownloader


class CurlDownloader(ExternalDownloader):
    """Downloader that uses the command line program curl."""
    program = 'curl'
    args = '--fail'
