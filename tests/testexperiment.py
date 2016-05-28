# coding: utf-8

import context, testutils, unittest
from docxperiments import experiment, PROJECT_DIR, PACKAGE_DIR, DATA_DIR
import os

def project_relative(path):
    return os.path.relpath(path, PROJECT_DIR)

def package_relative(path):
    return os.path.relpath(path, PACKAGE_DIR)

def data_relative(path):
    if isinstance(path, basestring):
        return os.path.relpath(path, DATA_DIR)
    else:
        return [os.path.relpath(i, DATA_DIR) for i in path]

class ExperimentPathTest(unittest.TestCase):
    maxDiff = None
    
    def setUp(self):
        self.exp = experiment.Experiment('0-blank', '1-para')
    
    def test_config_docx_path_left(self):
        docx_path_target = '0-blank/0-blank.docx'
        docx_path_result = self.exp.docx_paths[0]
        self.assertEqual(docx_path_target, data_relative(docx_path_result))

    def test_config_docx_path_right(self):
        docx_path_target = '1-para/1-para.docx'
        docx_path_result = self.exp.docx_paths[1]
        self.assertEqual(docx_path_target, data_relative(docx_path_result))

    def test_config_exp_dir_path(self):
        exp_dir_path_target = '0-blank_1-para'
        exp_dir_path_result = self.exp.exp_dir_path
        self.assertEqual(exp_dir_path_target, data_relative(exp_dir_path_result))

    def test_config_ugly_dir_path_left(self):
        extract_dest_path_target = '0-blank/ugly'
        extract_dest_path_result = self.exp.ugly_dir_paths[0]
        self.assertEqual(extract_dest_path_target, data_relative(extract_dest_path_result))

    def test_config_ugly_dir_path_right(self):
        extract_dest_path_target = '1-para/ugly'
        extract_dest_path_result = self.exp.ugly_dir_paths[1]
        self.assertEqual(extract_dest_path_target, data_relative(extract_dest_path_result))

    def test_config_prettify_ugly_file_paths_left(self):
        ugly_file_paths_target = [
            '0-blank/ugly/[Content_Types].xml',
            '0-blank/ugly/_rels',
            '0-blank/ugly/_rels/.rels',
            '0-blank/ugly/docProps',
            '0-blank/ugly/docProps/app.xml',
            '0-blank/ugly/docProps/core.xml',
            '0-blank/ugly/docProps/thumbnail.jpeg',
            '0-blank/ugly/word',
            '0-blank/ugly/word/_rels',
            '0-blank/ugly/word/_rels/document.xml.rels',
            '0-blank/ugly/word/document.xml',
            '0-blank/ugly/word/fontTable.xml',
            '0-blank/ugly/word/settings.xml',
            '0-blank/ugly/word/styles.xml',
            '0-blank/ugly/word/theme',
            '0-blank/ugly/word/theme/theme1.xml',
            '0-blank/ugly/word/webSettings.xml',
            ]
        ugly_file_paths_result = self.exp.ugly_file_paths[0]
        #self.assertEqual(len(ugly_file_paths_result), 5)
        self.assertItemsEqual(ugly_file_paths_target, data_relative(ugly_file_paths_result))

    @unittest.skip("Not Implemented")
    def test_config_prettify_ugly_passthrough_pathsA(self):
        passthrough_paths_target = [
            'exp/0-blank_1-para/a/ugly/docProps/thumbnail.jpeg',
            ]
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_prettify_ugly_pathsB(self):
        ugly_paths_target = [
            'exp/0-blank_1-para/b/ugly/[Content_Types].xml',
            'exp/0-blank_1-para/b/ugly/_rels/.rels',
            'exp/0-blank_1-para/b/ugly/docProps/app.xml',
            'exp/0-blank_1-para/b/ugly/docProps/core.xml',
            'exp/0-blank_1-para/b/ugly/docProps/thumbnail.jpeg',
            'exp/0-blank_1-para/b/ugly/word/_rels/document.xml.rels',
            'exp/0-blank_1-para/b/ugly/word/document.xml',
            'exp/0-blank_1-para/b/ugly/word/fontTable.xml',
            'exp/0-blank_1-para/b/ugly/word/settings.xml',
            'exp/0-blank_1-para/b/ugly/word/styles.xml',
            'exp/0-blank_1-para/b/ugly/word/theme/theme1.xml',
            'exp/0-blank_1-para/b/ugly/word/webSettings.xml',
            ]
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_prettify_ugly_passthrough_pathsB(self):
        passthrough_paths_target = [
            'exp/0-blank_1-para/b/ugly/docProps/thumbnail.jpeg',
            ]
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_prettify_pretty_pathsA(self):
        pretty_paths_target = [
            'exp/0-blank_1-para/a/pretty/[Content_Types].xml',
            'exp/0-blank_1-para/a/pretty/_rels/.rels',
            'exp/0-blank_1-para/a/pretty/docProps/app.xml',
            'exp/0-blank_1-para/a/pretty/docProps/core.xml',
            'exp/0-blank_1-para/a/pretty/docProps/thumbnail.jpeg',
            'exp/0-blank_1-para/a/pretty/word/_rels/document.xml.rels',
            'exp/0-blank_1-para/a/pretty/word/document.xml',
            'exp/0-blank_1-para/a/pretty/word/fontTable.xml',
            'exp/0-blank_1-para/a/pretty/word/settings.xml',
            'exp/0-blank_1-para/a/pretty/word/styles.xml',
            'exp/0-blank_1-para/a/pretty/word/theme/theme1.xml',
            'exp/0-blank_1-para/a/pretty/word/webSettings.xml',
            ]
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_prettify_pretty_pathsB(self):
        pretty_paths_target = [
            'exp/0-blank_1-para/b/pretty/[Content_Types].xml',
            'exp/0-blank_1-para/b/pretty/_rels/.rels',
            'exp/0-blank_1-para/b/pretty/docProps/app.xml',
            'exp/0-blank_1-para/b/pretty/docProps/core.xml',
            'exp/0-blank_1-para/b/pretty/docProps/thumbnail.jpeg',
            'exp/0-blank_1-para/b/pretty/word/_rels/document.xml.rels',
            'exp/0-blank_1-para/b/pretty/word/document.xml',
            'exp/0-blank_1-para/b/pretty/word/fontTable.xml',
            'exp/0-blank_1-para/b/pretty/word/settings.xml',
            'exp/0-blank_1-para/b/pretty/word/styles.xml',
            'exp/0-blank_1-para/b/pretty/word/theme/theme1.xml',
            'exp/0-blank_1-para/b/pretty/word/webSettings.xml',
            ]
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_analysis_dir_path(self):
        analysis_dir_path_target = 'exp/0-blank_1-para/analysis'
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_diff_report_dir_path(self):
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_config_diff_report_file_path(self):
        raise self.failureException("not implemented")

    def test_orient_to_project_dir(self):
        self.assertEqual(
            experiment.PROJECT_DIR,
            '/Users/david/dev/docxperiments'
        )

    def test_orient_to_package_dir(self):
        self.assertEqual(
            experiment.PACKAGE_DIR,
            '/Users/david/dev/docxperiments/docxperiments'
        )

    def test_orient_to_data_dir(self):
        self.assertEqual(
            experiment.DATA_DIR,
            '/Users/david/dev/docxperiments/docxperiments/data'
        )

class ExperimentFileOperationsTest(unittest.TestCase):

    @unittest.skip("Not Implemented")
    def test_prettify_preserves_dir_structure(self):
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_new_file_detection(self):
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_changed_file_detection(self):
        raise self.failureException("not implemented")

    @unittest.skip("Not Implemented")
    def test_report_dir_structure_as_expected(self):
        raise self.failureException("not implemented")

def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=0, testRunner=runner)

if __name__ == '__main__':
    test()




