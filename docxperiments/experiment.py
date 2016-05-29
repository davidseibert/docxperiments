# coding: utf-8

import dirdiff, filediff

# convenience aliases for os.path functions
from pathutils import mkdir, mkpath, experiments_abs, experiments_rel
from specimen import Specimen
LEFT = 0
RIGHT = 1

class Experiment (object):
    def __init__(self, left_name, right_name):
        self.left = Specimen(left_name)
        self.right = Specimen(right_name)

    # essential progression
    def extract_left(self):
        self.left.extract()
    def extract_right(self):
        self.right.extract()
    def prettify_left(self):
        self.left.prettify()
    def prettify_right(self):
        self.right.prettify()
    def write_diff_reports(self):
        mkdir(self.path)
        for f in self.changed:
            diffs = filediff.get_diff_battery(self._left(f), self._right(f))
            for diff in diffs:
                diff.write(self.path, f)

    # basic info
    @property
    def name(self):
        return "{}_{}".format(self.left.name, self.right.name)
    @property
    def path(self):
        return experiments_abs(self.name)

    # path aliases for original and extracted docx files
    @property
    def docx(self):
        return (self.left.docx, self.right.docx)
    @property
    def ugly(self):
        return (self.left.ugly, self.right.ugly)
    @property
    def pretty(self):
        return (self.left.pretty, self.right.pretty)

    # lists of paths for individual xml files
    @property
    def uglies(self):
        return (self.left.uglies, self.right.uglies)
    @property
    def pretties(self):
        return (self.left.pretties, self.right.pretties)

    # diff analysis
    @property
    def common(self):
        return dirdiff.get_common(self.left.pretty, self.right.pretty)
    @property
    def changed(self):
        return [f for f in self.common
                if filediff.changed(self._left(f), self._right(f))]

    # path aliases for convenience
    def _left(self, f):
        return mkpath(self.left.pretty, f)
    def _right(self, f):
        return mkpath(self.right.pretty, f)
    def _exp(self, f):
        return mkpath(self.path, f)





