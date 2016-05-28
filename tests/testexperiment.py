# coding: utf-8

import context, testutils, unittest
from docxperiments import Experiment

class ExperimentPathTest(unittest.TestCase):
    
    def setUp(self):
        self.exp = Experiment('0-blank', '1-para')
    
    def test_config_docx_pathA(self):
        docx_path_target = 'docxfiles/0-blank.docx'
        docx_path_result = self.exp.a_docx_path
        self.assertEqual(docx_path_target, docx_path_result)

    def test_config_docx_pathB(self):
        docx_path_target = 'docxfiles/1-para.docx'
        docx_path_result = self.exp.b_docx_path
        self.assertEqual(docx_path_target, docx_path_result)
        
    def test_config_exp_dir_path(self):
        exp_dir_path_target = 'exp/0-blank_1-para'
        exp_dir_path_result = self.exp.exp_dir_path
        self.assertEqual(exp_dir_path_target, exp_dir_path_result)
    
    def test_config_extract_dest_pathA(self):
        extract_dest_path_target = 'exp/0-blank_1-para/a/ugly'
        extract_dest_path_result = self.exp.a_ugly_dir_path
        self.assertEqual(extract_dest_path_target, extract_dest_path_result)

    def test_config_extract_dest_pathB(self):
        extract_dest_path_target = 'exp/0-blank_1-para/b/ugly'
        extract_dest_path_result = self.exp.b_ugly_dir_path
        self.assertEqual(extract_dest_path_target, extract_dest_path_result)
        
    def test_config_prettify_ugly_paths(self):
        ugly_paths_target = [
            '[Content_Types].xml',
            '_rels/.rels',
            'word/_rels/document.xml.rels',
            'docProps/app.xml',
            'docProps/core.xml',
            'word/document.xml',
            'word/fontTable.xml',
            'word/settings.xml',
            'word/styles.xml',
            'word/stylesWithEffects.xml',
            'word/webSettings.xml',
            'word/_rels/document.xml.rels',
            'word/theme/theme1.xml',
            ]    
    def test_config_prettify_pretty_paths(self):
        pass
    
    def test_config_analysis_dir_path(self):
        pass
        
    def test_config_diff_report_dir_path(self):
        pass
    
    def test_config_diff_report_file_path(self):
        pass
    
    def test_path_config_ignores_working_dir(self):
        pass

class ExperimentFileOperationsTest(unittest.TestCase):
    
    def test_prettify_preserves_dir_structure(self):
        pass
    
    def test_new_file_detection(self):
        pass
    
    def test_changed_file_detection(self):
        pass
    
    def test_report_dir_structure_as_expected(self):
        pass 

def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=0, testRunner=runner)

if __name__ == '__main__':
    test()