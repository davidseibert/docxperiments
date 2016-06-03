# coding: utf-8

from pathutils import SPECIMENS_DIR, EXPERIMENTS_DIR, ls
from experiment import Experiment
from specimen import Specimen
import os


class Operator(object):
    def run_all(self):
        for exp in self.experiments:
            self.run(exp)

    def run(self, exp):
        self._extract(exp)
        self._prettify(exp)
        self._write_diff_reports(exp)

    def _extract(self, exp):
        exp.extract_left()
        exp.extract_right()
    def _prettify(self, exp):
        exp.prettify_left()
        exp.prettify_right()
    def _write_diff_reports(self, exp):
        exp.write_diff_reports()

    @property
    def specimens(self):
        try:
            return self._specimens
        except AttributeError:
            specs = []
            spec_paths = ls(SPECIMENS_DIR, depth=0)
            for path in spec_paths:
                spec = Specimen(os.path.basename(path))
                specs.append(spec)
            self._specimens = specs
            return self._specimens

    @property
    def experiments(self):
        try:
            return self._experiments
        except AttributeError:
            left_specimens = self.specimens[:-1]
            right_specimens = self.specimens[1:]
            self._experiments = [Experiment(left.name, right.name)
                    for left, right in zip(left_specimens, right_specimens)]
            return self._experiments
