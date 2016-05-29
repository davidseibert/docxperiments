from difflib import context_diff, ndiff, unified_diff
from pathutils import mkpath
import os, filecmp

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
    if os.path.isdir(a_path) or os.path.isdir(b_path):
        return False
    else:
        return not filecmp.cmp(a_path, b_path)

def main():
    a_path = '../tests/testdata/a.xml'
    b_path = '../tests/testdata/b.xml'
    #diff_result = get_diff_battery(a_path, b_path)
    diff_result = get_diff_battery(a_path, b_path)
    print diff_result


if __name__ == '__main__':
    main()
