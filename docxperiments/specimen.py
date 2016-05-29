# coding: utf-8

from pathutils import mkpath, data_abs, ls, mkrel, mkdir, specimens_abs
from extract import extract_docx
from prettify import prettify_xml


class Specimen(object):
    def __init__(self, name):
        self.name = name

    def extract(self):
        extract_docx(self.docx, self.ugly)

    def prettify(self):
        mkdir(self.pretty)
        for ugly, pretty in zip(self.uglies, self.pretties):
            try:
                pretty_str = prettify_xml(ugly)
            except IOError:
                mkdir(pretty)
            else:
                with open(pretty, 'w') as f:
                    f.write(pretty_str.encode('utf-8'))

    @property
    def path(self):
        return specimens_abs(self.name)
    @property
    def docx(self):
        return mkpath(self.path, self.name+'.docx')
    @property
    def ugly(self):
        return mkpath(self.path, 'ugly')
    @property
    def pretty(self):
        return mkpath(self.path, 'pretty')
    @property
    def uglies(self):
        return ls(self.ugly)
    @property
    def pretties(self):
        return [self._transpose(path) for path in self.uglies]

    def _transpose(self, path):
        return mkpath(self.pretty, mkrel(path, self.ugly))
