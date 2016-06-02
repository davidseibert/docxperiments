# coding: utf-8

from unittest import TestSuite
import unittest
import context
from tests.testutils import CustomResult
from html2ooxml import Html2OOXMLTest
from ooxml2html import OOXML2HTMLTest

def run_synth_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(Html2OOXMLTest)
    suite.addTest(OOXML2HTMLTest('test_ooxml2html'))
    unittest.TextTestRunner(verbosity=2, resultclass=CustomResult).run(suite)

def main():
    run_synth_suite()

if __name__ == '__main__':
    main()