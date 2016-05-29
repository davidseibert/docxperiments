# coding: utf-8

import context, testutils, unittest
from docxperiments import experiment, PROJECT_DIR, PACKAGE_DIR, DATA_DIR, dirdiff
import os
import shutil
from docxperiments.pathutils import project_rel, package_rel, data_rel, mkrel, specimens_rel, experiments_rel



class ExperimentPathTest(unittest.TestCase):
    maxDiff = None
    
    def setUp(self):
        self.exp = experiment.Experiment('0-blank', '1-singlepara')

    def test_config_exp_dir_path(self):
        exp_dir_path_target = '0-blank_1-singlepara'
        exp_dir_path_result = self.exp.path
        self.assertEqual(exp_dir_path_target, experiments_rel(exp_dir_path_result))

    def test_config_docx_path_left(self):
        docx_path_target = '0-blank/0-blank.docx'
        docx_path_result = self.exp.docx[0]
        self.assertEqual(docx_path_target, specimens_rel(docx_path_result))

    def test_config_docx_path_right(self):
        docx_path_target = '1-singlepara/1-singlepara.docx'
        docx_path_result = self.exp.docx[1]
        self.assertEqual(docx_path_target, specimens_rel(docx_path_result))

    def test_config_ugly_dir_path_left(self):
        extract_dest_path_target = '0-blank/ugly'
        extract_dest_path_result = self.exp.ugly[0]
        self.assertEqual(extract_dest_path_target, specimens_rel(extract_dest_path_result))

    def test_config_ugly_dir_path_right(self):
        extract_dest_path_target = '1-singlepara/ugly'
        extract_dest_path_result = self.exp.ugly[1]
        self.assertEqual(extract_dest_path_target, specimens_rel(extract_dest_path_result))

    def test_config_pretty_dir_path_left(self):
        extract_dest_path_target = '0-blank/pretty'
        extract_dest_path_result = self.exp.pretty[0]
        self.assertEqual(extract_dest_path_target, specimens_rel(extract_dest_path_result))

    def test_config_pretty_dir_path_right(self):
        extract_dest_path_target = '1-singlepara/pretty'
        extract_dest_path_result = self.exp.pretty[1]
        self.assertEqual(extract_dest_path_target, specimens_rel(extract_dest_path_result))

    def test_config_ugly_file_paths_left(self):
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
        ugly_file_paths_result = self.exp.uglies[0]
        self.assertItemsEqual(ugly_file_paths_target, specimens_rel(ugly_file_paths_result))

    def test_config_ugly_file_paths_right(self):
        ugly_file_paths_target = [
            '1-singlepara/ugly/[Content_Types].xml',
            '1-singlepara/ugly/_rels',
            '1-singlepara/ugly/_rels/.rels',
            '1-singlepara/ugly/docProps',
            '1-singlepara/ugly/docProps/app.xml',
            '1-singlepara/ugly/docProps/core.xml',
            '1-singlepara/ugly/docProps/thumbnail.jpeg',
            '1-singlepara/ugly/word',
            '1-singlepara/ugly/word/_rels',
            '1-singlepara/ugly/word/_rels/document.xml.rels',
            '1-singlepara/ugly/word/document.xml',
            '1-singlepara/ugly/word/fontTable.xml',
            '1-singlepara/ugly/word/settings.xml',
            '1-singlepara/ugly/word/styles.xml',
            '1-singlepara/ugly/word/theme',
            '1-singlepara/ugly/word/theme/theme1.xml',
            '1-singlepara/ugly/word/webSettings.xml',
        ]
        ugly_file_paths_result = self.exp.uglies[1]
        self.assertItemsEqual(ugly_file_paths_target, specimens_rel(ugly_file_paths_result))

    def test_config_pretty_file_paths_left(self):
        pretty_file_paths_target = [
            '0-blank/pretty/[Content_Types].xml',
            '0-blank/pretty/_rels',
            '0-blank/pretty/_rels/.rels',
            '0-blank/pretty/docProps',
            '0-blank/pretty/docProps/app.xml',
            '0-blank/pretty/docProps/core.xml',
            '0-blank/pretty/docProps/thumbnail.jpeg',
            '0-blank/pretty/word',
            '0-blank/pretty/word/_rels',
            '0-blank/pretty/word/_rels/document.xml.rels',
            '0-blank/pretty/word/document.xml',
            '0-blank/pretty/word/fontTable.xml',
            '0-blank/pretty/word/settings.xml',
            '0-blank/pretty/word/styles.xml',
            '0-blank/pretty/word/theme',
            '0-blank/pretty/word/theme/theme1.xml',
            '0-blank/pretty/word/webSettings.xml',
        ]
        pretty_file_paths_result = self.exp.pretties[0]
        self.assertItemsEqual(pretty_file_paths_target, specimens_rel(pretty_file_paths_result))

    def test_config_pretty_file_paths_right(self):
        pretty_file_paths_target = [
            '1-singlepara/pretty/[Content_Types].xml',
            '1-singlepara/pretty/_rels',
            '1-singlepara/pretty/_rels/.rels',
            '1-singlepara/pretty/docProps',
            '1-singlepara/pretty/docProps/app.xml',
            '1-singlepara/pretty/docProps/core.xml',
            '1-singlepara/pretty/docProps/thumbnail.jpeg',
            '1-singlepara/pretty/word',
            '1-singlepara/pretty/word/_rels',
            '1-singlepara/pretty/word/_rels/document.xml.rels',
            '1-singlepara/pretty/word/document.xml',
            '1-singlepara/pretty/word/fontTable.xml',
            '1-singlepara/pretty/word/settings.xml',
            '1-singlepara/pretty/word/styles.xml',
            '1-singlepara/pretty/word/theme',
            '1-singlepara/pretty/word/theme/theme1.xml',
            '1-singlepara/pretty/word/webSettings.xml',
        ]
        pretty_file_paths_result = self.exp.pretties[1]
        self.assertItemsEqual(pretty_file_paths_target, specimens_rel(pretty_file_paths_result))

    def test_orient_to_project_dir(self):
        self.assertEqual(
            PROJECT_DIR,
            '/Users/david/dev/docxperiments'
        )

    def test_orient_to_package_dir(self):
        self.assertEqual(
            PACKAGE_DIR,
            '/Users/david/dev/docxperiments/docxperiments'
        )

    def test_orient_to_data_dir(self):
        self.assertEqual(
            DATA_DIR,
            '/Users/david/dev/docxperiments/docxperiments/data'
        )

class ExperimentFileOperationsTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.exp = experiment.Experiment('0-blank', '1-singlepara')

    def test_extract_docx_file_left(self):
        if os.path.exists(self.exp.ugly[0]):
            shutil.rmtree(self.exp.ugly[0])
        self.assertFalse(os.path.exists(self.exp.ugly[0]))

        self.exp.extract_left()
        self.assertTrue(os.path.exists(self.exp.ugly[0]), "docx file not extracted or extracted to the wrong place.")

    def test_extract_docx_file_right(self):
        if os.path.exists(self.exp.ugly[1]):
            shutil.rmtree(self.exp.ugly[1])
        self.assertFalse(os.path.exists(self.exp.ugly[1]))

        self.exp.extract_right()
        self.assertTrue(os.path.exists(self.exp.ugly[1]), "docx file not extracted or extracted to the wrong place.")

    def test_prettify_preserves_dir_structure_left(self):
        self.exp.prettify_left()
        for path in self.exp.pretties[0]:
            self.assertTrue(os.path.isfile(path) or os.path.isdir(path), "Couldn't find dir or file at {}".format(specimens_rel(path)))

    def test_prettify_preserves_dir_structure_right(self):
        self.exp.prettify_right()
        for path in self.exp.pretties[1]:
            self.assertTrue(os.path.isfile(path) or os.path.isdir(path), "Couldn't find dir or file at {}".format(specimens_rel(path)))

    def test_changed_files_detection(self):
        changed_files_target = [
            'docProps/app.xml',
            'word/document.xml',
            'word/settings.xml',
        ]
        changed_files_result = self.exp.changed
        self.assertItemsEqual(changed_files_target, changed_files_result)

    def test_diff_reports_created(self):
        diff_reports_target = [
            'docProps__app_xml__context_diff.xml',
            'docProps__app_xml__ndiff.xml',
            'docProps__app_xml__unified_diff.xml',
            'word__document_xml__context_diff.xml',
            'word__document_xml__ndiff.xml',
            'word__document_xml__unified_diff.xml',
            'word__settings_xml__context_diff.xml',
            'word__settings_xml__ndiff.xml',
            'word__settings_xml__unified_diff.xml',
        ]
        if os.path.exists(self.exp.path):
            shutil.rmtree(self.exp.path)
        self.exp.write_diff_reports()
        diff_reports_result = dirdiff.walk_dir(self.exp.path)
        self.assertItemsEqual(diff_reports_target, mkrel(diff_reports_result, self.exp.path))

def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=0, testRunner=runner)

if __name__ == '__main__':
    test()




