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
            'diffsampleA/file1.txt',
            'diffsampleA/file2.txt',
            'diffsampleA/subdir1',
            'diffsampleA/subdir1/file3.txt',
            'diffsampleA/subdir1/file4.txt',
            'diffsampleA/subdir2',
            'diffsampleA/subdir2/.file5.txt',
            'diffsampleA/subdir2/file6.txt',
            'diffsampleA/subdir2/file7.txt',
            'diffsampleA/subdir2/subdir3',
            'diffsampleA/subdir2/subdir3/file8.txt',
            ]
        dir_listing_A_result = dirdiff.walk_dir(self.a_path)
        self.assertEqual(dir_listing_A_target, dir_listing_A_result)

    def test_dir_walk_B(self):
        dir_listing_B_target = [
            'diffsampleB/file1.txt',
            'diffsampleB/file2.txt',
            'diffsampleB/subdir1',
            'diffsampleB/subdir1/file3.txt',
            'diffsampleB/subdir1/file4.txt',
            'diffsampleB/subdir2',
            'diffsampleB/subdir2/.file6.txt',
            'diffsampleB/subdir2/subdir3',
            'diffsampleB/subdir2/subdir3/file7.txt',
            'diffsampleB/subdir2/subdir3/file9.txt',
            'diffsampleB/subdir4',
            'diffsampleB/subdir4/file5.txt',
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
