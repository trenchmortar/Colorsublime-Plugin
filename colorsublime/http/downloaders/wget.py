from .external import ExternalDownloader


class WgetDownloader(ExternalDownloader):
    """Downloader that uses the command line program wget."""
    program = 'wget'
    args = ['-qO-']
