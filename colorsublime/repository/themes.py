import functools


class Themes(list):
    def __init__(self, themes):
        list.__init__(self, sorted(themes))

    def quick_list(self):
        return [[theme.name, theme.author, theme.description] for theme in self]


@functools.total_ordering
class Theme(object):
    def __init__(self, *, name, author, description, file_name, file_path):
        self.name = name
        self.author = author
        self.description = description
        self.file_name = file_name
        self.file_path = file_path

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    @classmethod
    def from_repo(cls, repo_dict, repo_path):
        r = repo_dict
        file_path = repo_path + '/themes/' + r['FileName']
        return cls(name=r['Title'],
                   author=r['Author'],
                   description=r['Description'],
                   file_name=r['FileName'],
                   file_path=file_path)
