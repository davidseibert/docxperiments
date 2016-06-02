import re, difflib, unittest
from tests.testutils import DiffTest

DIFF_TYPE = difflib.unified_diff

TARGET_SOURCE_PATH = 'simplified.oo.xml'
INPUT_SOURCE_PATH = 'input.html'

with open(TARGET_SOURCE_PATH) as f:
    TARGET = f.read()
with open(INPUT_SOURCE_PATH) as f:
    INPUT = f.read()

def group(n=None):
    if isinstance(n, int):
        return r'\g<{}>'.format(n)
    else:
        return r'({})'.format(n)

p = r'<p>', r'</p>'
b = r'<b>', r'</b>'
i = r'<i>', r'</i>'
_p = r'<w:p>', r'</w:p>'
_r = r'<w:r>', r'</w:r>'
_t = r'<w:t xml:space="preserve">', r'</w:t>'
_rPr = r'<w:rPr>', r'</w:rPr>'
_b = r'<w:b/>'
_i = r'<w:i/>'
not_lt = r'[^<]+'
_prt = _p[0] + _r[0] + _t[0]
_trp = _t[1] + _r[1] + _p[1]
_trr = _t[1] + _r[1] + _r[0]
_tr = _t[1] + _r[1]
_rrt = _r[1] + _r[0] + _t[0]
txt_in = group(not_lt)
txtout = group(1)

def run_property(property):
    return _rPr[0] + property + _rPr[1]

rules = [
    (
        r'<!DOCTYPE html>',
        r'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    ),
    (
        r'<html>',
        r'<w:document>'
    ),
    (
        r'</html>',
        r'</w:document>'
    ),
    (
        r'<head></head>',
        r''
    ),
    (
        r'<body>',
        r'<w:body>'
    ),
    (
        r'</body>',
        r'</w:body>'
    ),
    (
        b[0],
        _r[0] + run_property(_b) + _t[0]
    ),
    (
        b[1],
        _tr
    ),
    (
        i[0],
        _r[0] + run_property(_i) + _t[0]
    ),
    (
        i[1],
        _tr
    ),
    ( # expand plain paragraphs
        p[0] + txt_in + p[1],       #
        _prt + txtout + _trp
    ),
    ( # wrap paragraph-initial plain runs
        p[0] + txt_in + _r[0],
        _prt + txtout + _trr
    ),
    ( # wrap paragraph-medial plain runs
        _r[1] + txt_in + _r[0],
        _rrt + txtout + _trr
    ),
    ( # wrap paragraph-final plain runs
        _r[1] + txt_in + p[1],
        _rrt + txtout + _trp
    ),
    ( # remove excess space
        ' {2,}',
        ' '
    ),
]

def process(input):
    intermediate = input
    for rule in rules:
        intermediate = re.sub(rule[0], rule[1], intermediate)
    output = intermediate
    return output

def run_diff_report():
    result = process(INPUT).split('><')
    target = TARGET.split('><')
    diff_gen = DIFF_TYPE(result, target)
    diff_str = '\n'.join([line for line in diff_gen])
    return diff_str

class Html2OOXMLTest(DiffTest):
    maxDiff = None

    def test_html2ooxml(self):
        diff_report = run_diff_report()
        self.assertNoDiff(diff_report)

def main():
    unittest.main()

if __name__ == '__main__':
    main()