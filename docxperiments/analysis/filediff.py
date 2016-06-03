from difflib import context_diff, ndiff, unified_diff
from pathutils import mkpath, specimens_rel
import os, filecmp
import logging

logger = logging.getLogger(__name__)

class Diff(object):
    def __init__(self, a_path, b_path):
        self.a_path = a_path
        self.b_path = b_path

    def __str__(self):
        return ''.join([line for line in self.get()])
    def get(self):
        a_lines = _readlines(self.a_path)
        b_lines = _readlines(self.b_path)
        return self.gen(a_lines, b_lines)

    def write(self, exp_dir, filename):
        report_path = self._make_report_path(exp_dir, filename)
        with open(report_path, 'w') as f:
            f.write(str(self))
    def _make_report_path(self, exp_dir, filename):
        report_path = "{}__{}.xml".format(
            filename.replace("/", "__").replace(".", "_"),
            self.label
            )
        return mkpath(exp_dir, report_path)

class ContextDiff(Diff):
    label = 'context_diff'
    def gen(self, a_lines, b_lines):
        return context_diff(a_lines, b_lines)
class UnifiedDiff(Diff):
    label = 'unified_diff'
    def gen(self, a_lines, b_lines):
        return unified_diff(a_lines, b_lines)
class NDiff(Diff):
    label = 'ndiff'
    def gen(self, a_lines, b_lines):
        return ndiff(a_lines, b_lines)

def get_diff_battery(*paths):
    return (ContextDiff(*paths), NDiff(*paths), UnifiedDiff(*paths))
def get_context_diff(a_path, b_path):
    return str(ContextDiff(a_path, b_path))
def get_ndiff(a_path, b_path):
    return str(NDiff(a_path, b_path))
def get_unified_diff(a_path, b_path):
    return str(UnifiedDiff(a_path, b_path))

def _readlines(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        return lines

def changed(a_path, b_path):
    logger.info("Checking for changes in '{}' and '{}'...".format(specimens_rel(a_path), specimens_rel(b_path)))
    if os.path.isdir(a_path) or os.path.isdir(b_path):
        logger.info("Dir detected in '{}' or '{}'; returning False".format(specimens_rel(a_path), specimens_rel(b_path)))
        return False
    else:
        diff = ContextDiff(a_path, b_path)
        diffstr = str(diff)
        if len(diffstr) == 0:
            change_detected = False
        else:
            change_detected = True
        logger.info("Changed = {}".format(change_detected))
        return change_detected

def main():
    a_path = '../tests/testdata/a.xml'
    b_path = '../tests/testdata/b.xml'
    #diff_result = get_diff_battery(a_path, b_path)
    diff_result = get_diff_battery(a_path, b_path)
    print diff_result


if __name__ == '__main__':
    main()
