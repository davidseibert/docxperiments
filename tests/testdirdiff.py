# coding: utf-8

import context, testutils, unittest
from docxperiments import dirdiff
import filecmp

class DirDiffTest(unittest.TestCase):
    maxDiff = None
    a_path = 'testdata/diffsampleA'
    b_path = 'testdata/diffsampleB'

    def test_dir_walk_A(self):
        dir_listing_A_target = [
            'testdata/diffsampleA/file1.txt',
            'testdata/diffsampleA/file2.txt',
            'testdata/diffsampleA/subdir1',
            'testdata/diffsampleA/subdir1/file3.txt',
            'testdata/diffsampleA/subdir1/file4.txt',
            'testdata/diffsampleA/subdir2',
            'testdata/diffsampleA/subdir2/.file5.txt',
            'testdata/diffsampleA/subdir2/file6.txt',
            'testdata/diffsampleA/subdir2/file7.txt',
            'testdata/diffsampleA/subdir2/subdir3',
            'testdata/diffsampleA/subdir2/subdir3/file8.txt',
            ]
        dir_listing_A_result = dirdiff.walk_dir(self.a_path)
        self.assertEqual(dir_listing_A_target, dir_listing_A_result)

    def test_dir_walk_B(self):
        dir_listing_B_target = [
            'testdata/diffsampleB/file1.txt',
            'testdata/diffsampleB/file2.txt',
            'testdata/diffsampleB/subdir1',
            'testdata/diffsampleB/subdir1/file3.txt',
            'testdata/diffsampleB/subdir1/file4.txt',
            'testdata/diffsampleB/subdir2',
            'testdata/diffsampleB/subdir2/.file6.txt',
            'testdata/diffsampleB/subdir2/subdir3',
            'testdata/diffsampleB/subdir2/subdir3/file7.txt',
            'testdata/diffsampleB/subdir2/subdir3/file9.txt',
            'testdata/diffsampleB/subdir4',
            'testdata/diffsampleB/subdir4/file5.txt',
            ]
        dir_listing_B_result = dirdiff.walk_dir(
                'testdata/diffsampleB'
                )
        self.assertEqual(dir_listing_B_target, dir_listing_B_result)

    def test_get_left_only(self):
        left_only_target = [
            'subdir2/.file5.txt',
            'subdir2/file6.txt',
            'subdir2/file7.txt',
            'subdir2/subdir3/file8.txt',
            ]
        left_only_result = dirdiff.get_left_only(self.a_path, self.b_path)
        self.assertItemsEqual(left_only_target, left_only_result)

    def test_get_right_only(self):
        right_only_target = [
            'subdir2/.file6.txt',
            'subdir2/subdir3/file7.txt',
            'subdir2/subdir3/file9.txt',
            'subdir4',
            'subdir4/file5.txt',
            ]
        right_only_result = dirdiff.get_right_only(self.a_path, self.b_path)
        self.assertItemsEqual(right_only_target, right_only_result)
    
    def test_get_common(self):
        common_target = [
            'file1.txt',
            'file2.txt',
            'subdir1',
            'subdir1/file3.txt',
            'subdir1/file4.txt',
            'subdir2',
            'subdir2/subdir3',
            ]
        common_result = dirdiff.get_common(self.a_path, self.b_path)
        self.assertItemsEqual(common_target, common_result)

def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=4, testRunner=runner)

if __name__ == '__main__':
    test()
