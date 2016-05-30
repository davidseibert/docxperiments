# coding: utf-8

import dirdiff, filediff
import logging

# convenience aliases for os.path functions
from pathutils import mkdir, mkpath, experiments_abs, experiments_rel
from specimen import Specimen
LEFT = 0
RIGHT = 1

logger = logging.getLogger(__name__)

class Experiment (object):
    def __init__(self, left_name, right_name):
        self.name = "{}_{}".format(left_name, right_name)
        self.logger = logging.getLogger('EXP: ' + self.name)
        self.logger.debug("Setting up specimens")
        self.left = Specimen(left_name)
        self.logger.info("Left specimen set to {}".format(self.left))
        self.right = Specimen(right_name)
        self.logger.info("Right specimen set to {}".format(self.right))
        self.path = experiments_abs(self.name)
        self.logger.info("Path set to {}".format(self.path))
        self.docx = (self.left.docx, self.right.docx)
        self.logger.debug("Docx files set to {} and {}".format(*self.docx))
        self.ugly = (self.left.ugly, self.right.ugly)
        self.logger.debug("Ugly directories set to {} and {}".format(*self.ugly))
        self.pretty = (self.left.pretty, self.right.pretty)
        self.logger.debug("Pretty directories set to {} and {}".format(*self.pretty))
        self.uglies = (self.left.uglies, self.right.uglies)
        self.logger.debug("Pretty files set to {} and {}".format(*self.uglies))
        self.pretties = (self.left.pretties, self.right.pretties)
        self.logger.debug("Pretty files set to {} and {}".format(*self.pretties))

    # essential progression
    def extract_left(self):
        self.logger.debug("Extracting left specimen")
        self.left.extract()
    def extract_right(self):
        self.logger.debug("Extracting right specimen")
        self.right.extract()
    def prettify_left(self):
        self.logger.debug("Prettifying left specimen")
        self.left.prettify()
    def prettify_right(self):
        self.logger.debug("Prettifying right specimen")
        self.right.prettify()
    def write_diff_reports(self):
        mkdir(self.path)
        changed = self.get_changed()
        for f in changed:
            diffs = filediff.get_diff_battery(self._left(f), self._right(f))
            for diff in diffs:
                diff.write(self.path, f)
    def get_common(self):
        common = dirdiff.get_common(self.left.pretty, self.right.pretty)
        self.logger.info("Got common files: {}".format(common))
        return common
    def get_changed(self):
        changed = [f for f in self.get_common()
                if filediff.changed(self._left(f), self._right(f))]
        self.logger.info("Got changed files: {}".format(changed))
        return changed

    # path aliases for convenience
    def _left(self, f):
        path = mkpath(self.left.pretty, f)
        self.logger.debug("Left path requested: {}".format(path))
        return path
    def _right(self, f):
        path = mkpath(self.right.pretty, f)
        self.logger.debug("Right path requested: {}".format(path))
        return path
    def _exp(self, f):
        path = mkpath(self.path, f)
        self.logger.debug("Exp path requested: {}".format(path))
        return path





