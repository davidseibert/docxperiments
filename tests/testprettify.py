# coding: utf-8

import context, testutils, unittest
from docxperiments import prettify

class PrettifyTest(unittest.TestCase):

    def test_prettify_makes_xml_pretty(self):
        xml_file_path = 'testdata/ugly.xml'
        pretty_xml_str = prettify.prettify(xml_file_path)
        with open('testdata/pretty.xml') as f:
            txt = f.read().decode('utf-8')
        self.assertEqual(pretty_xml_str, txt[:-1])

def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=4, testRunner=runner)

if __name__ == '__main__':
    test()
