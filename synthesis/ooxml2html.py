import re, difflib, unittest
from tests.testutils import DiffTest

OOXML_FILE = 'simplified.oo.xml'

DIFF_TYPE = difflib.unified_diff
INPUT_SOURCE_PATH = 'simplified.oo.xml'
TARGET_SOURCE_PATH = 'input.html'

with open(TARGET_SOURCE_PATH) as f:
    TARGET = f.read()
with open(INPUT_SOURCE_PATH) as f:
    INPUT = f.read()

rules = [
    (
        r' xmlns\S+"',
        r''
    ),
    (
        r'<w:document>',
        r'<html>'
    ),
    (
        r'</w:document>',
        r'</html>'
    ),
    (
        r'<\?xml[^<]+>',
        r'<!DOCTYPE html>'
    ),
    (
        r'<w:p>',
        r'<p>'
    ),
    (
        r'</w:p>',
        r'</p>'
    ),
    (
        r'<w:body>',
        r'<body>'
    ),
    (
        r'</w:body>',
        r'</body>'
    ),
    (
        ' mc:Ignorable="w14 w15 wp14"',
        ''
    ),
    (
        ' w14:\w+="\w{8}"',
        ''
    ),
    (
        ' rsid\w+="\w{8}"',
        ''
    ),
    (
        ' xml:space="preserve"',
        ''
    ),
    (
        r'<bookmark[^>]+>',
        ' '
    ),
    (
        r'<sectPr.+</sectPr>',
        ''
    ),
    (
        r'<w:r><w:rPr><w:b/></w:rPr><w:t>([^<]+)</w:t></w:r>',
        r'<b>\g<1></b>'
    ),
    (
        r'<w:r><w:rPr><w:i/></w:rPr><w:t>([^<]+)</w:t></w:r>',
        r'<i>\g<1></i>'
    ),
    (
        r'<w:r><w:t>([^<]+)</w:t></w:r>',
        r'\g<1>'
    ),
    (
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

class OOXML2HTMLTest(DiffTest):
    maxDiff = None

    def test_ooxml2html(self):
        diff_report = run_diff_report()
        self.assertNoDiff(diff_report)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
