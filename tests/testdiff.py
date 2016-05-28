# coding: utf-8

import context, testutils, unittest
from docxperiments import filediff

class NDiffTest(testutils.DiffTest):

    def test_get_ndiff_returns_utf_8(self):
        diff_result = filediff.get_ndiff('testdata/a.xml', 'testdata/b.xml')
        diff_result.decode('utf-8')
    
    def test_get_ndiff_returns_str(self):
        diff_result = filediff.get_ndiff('testdata/a.xml', 'testdata/b.xml')
        self.assertIsInstance(diff_result, str)
    
    def test_get_ndiff(self):
        diff_result = filediff.get_ndiff('testdata/a.xml', 'testdata/b.xml')
        with open('testdata/ndiff.txt') as f:
            txt = f.read()
        self.assertEqual(diff_result, txt[:-1])

class UnifiedDiffTest(testutils.DiffTest):

    def test_get_unified_diff_returns_utf_8(self):
        diff_result = filediff.get_unified_diff('testdata/a.xml', 'testdata/b.xml')
        diff_result.decode('utf-8')
    
    def test_get_unified_diff_returns_str(self):
        diff_result = filediff.get_unified_diff('testdata/a.xml', 'testdata/b.xml')
        self.assertIsInstance(diff_result, str)
    
    def test_get_unified_diff(self):
        diff_result = filediff.get_unified_diff('testdata/a.xml', 'testdata/b.xml')
        with open('testdata/unified_diff.txt') as f:
            txt = f.read()
        self.assertEqual(diff_result, txt[:-1])

class ContextDiffTest(testutils.DiffTest):

    def test_get_context_diff_returns_utf_8(self):
        diff_result = filediff.get_context_diff('testdata/a.xml', 'testdata/b.xml')
        diff_result.decode('utf-8')
    
    def test_get_context_diff_returns_str(self):
        diff_result = filediff.get_context_diff('testdata/a.xml', 'testdata/b.xml')
        self.assertIsInstance(diff_result, str)
    
    def test_get_context_diff(self):
        diff_result = filediff.get_context_diff('testdata/a.xml', 'testdata/b.xml')
        with open('testdata/context_diff.txt') as f:
            txt = f.read()
        self.assertEqual(diff_result, txt[:-1])

class ReadLinesTest(unittest.TestCase):

    def test_readlines_return_type_is_list(self):
        lines = filediff._readlines('testdata/diffsampleA.txt')
        self.assertIsInstance(lines, list)

    def test_readlines_return_type_is_list_of_strings(self):
        lines = filediff._readlines('testdata/diffsampleA.txt')
        for line in lines:
            self.assertIsInstance(line, str)

    def test_readlines_lengthA(self):
        lines = filediff._readlines('testdata/diffsampleA.txt')
        self.assertEqual(len(lines), 24)

    def test_readlines_lengthB(self):
        lines = filediff._readlines('testdata/diffsampleB.txt')
        self.assertEqual(len(lines), 22)

    def test_readlines_returns_utf_8(self):
        lines = filediff._readlines('testdata/diffsampleA.txt')
        for line in lines:
            line.decode('utf-8')
    
def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=4, testRunner=runner)

if __name__ == '__main__':
    test()
