# coding: utf-8

import os
import context, unittest
from docxperiments import extract
import shutil

class ExtractTest(unittest.TestCase):

    def test_extract_docx_creates_a_new_dir(self):
        docx_path = 'testdata/extractme.docx'
        destination_dir_path = 'testdata/extracteddocx'

        if os.path.exists(destination_dir_path):
            shutil.rmtree(destination_dir_path)
        self.assertFalse(os.path.exists(destination_dir_path))

        extract.extract_docx(docx_path, destination_dir_path)
        self.assertTrue(os.path.exists(destination_dir_path))


def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=4, testRunner=runner)

if __name__ == '__main__':
    test()
