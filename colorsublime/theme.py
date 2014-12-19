import functools
from . import settings


class Path(object):
    def __init__(self, abs_base, file_name):
        self.file_name = file_name
        self.abs_base = abs_base

    @property
    def abs(self):
        return self.abs_base + '/' + self.file_name

    @property
    def rel(self):
        path = self.abs.replace(settings.packages_path(), '')
        return 'Packages' + path


@functools.total_ordering
class Theme(object):
    def __init__(self, name=None, author=None, description=None,
                 file_name=None):
        self.name = name
        self.author = author
        self.description = description
        self.file_name = file_name

        self.cache_path = Path(settings.repo_path() + '/themes', self.file_name)
        self.install_path = Path(settings.install_path(), self.file_name)

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    @classmethod
    def from_json(cls, theme_json):
        t = theme_json
        return cls(name=t['Title'],
                   author=t['Author'],
                   description=t['Description'],
                   file_name=t['FileName'])
