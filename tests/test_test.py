# coding: utf-8

import context, testutils
from docxperiments import filediff
import unittest


# One Word
singleword_a = """
nought
"""
singleword_b = """
naught
"""
singleword_target = """
--- 
+++ 
@@ -1,5 +1,5 @@
 n-o+a u g h
"""

# One Line
singleline_a = """
by being a lot smarter
"""
singleline_b = """
by being a self-starter
"""
singleline_target = """
--- 
+++ 
@@ -9,12 +9,13 @@
   a  +s+e l-o+f+-+s t- -s-m a r t
"""

# Extra Line
extraline_a = """
by being a lot smarter
"""
extraline_b = """
by being a lot smarter
by being a self-starter
"""
extraline_target = """
--- 
+++ 
@@ -9,12 +9,13 @@
   a  +s+e l-o+f+-+s t- -s-m a r t
"""

class BasicDiffTest(testutils.DiffTest):
    def test_singleword(self):
        target = singleword_target[1:-1]
        result = filediff.check_diff(singleword_a[1:-1], singleword_b[1:-1])
        self.check(target, result)
    
    def test_singleline(self):
        target = singleline_target[1:-1]
        result = filediff.check_diff(singleline_a[1:-1], singleline_b[1:-1])
        self.check(target, result)

    def test_extraline(self):
        target = extraline_target[1:-1]
        result = filediff.check_diff(extraline_a[1:-1], extraline_b[1:-1])
        self.check(target, result)
        
def test():
    runner = unittest.TextTestRunner(resultclass=testutils.CustomResult)
    unittest.main(verbosity=4, testRunner=runner)

if __name__ == '__main__':
    test()