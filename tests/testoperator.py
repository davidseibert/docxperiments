# coding: utf-8

import unittest

from docxperiments.analysis import operator


class OperatorTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.op = operator.Operator()

    def test_specimen_listing(self):
        listing_target = [
            '0-blank',
            '1-singlepara',
            '2-secondpara',
            '3-singlerun',
            '4-multirun',
            ]
        listing_result = [spec.name for spec in self.op.specimens ]
        self.assertItemsEqual(listing_target, listing_result)

    def test_experiment_listing(self):
        listing_target = [
            '0-blank_1-singlepara',
            '1-singlepara_2-secondpara',
            '2-secondpara_3-singlerun',
            '3-singlerun_4-multirun',
            ]
        listing_result = [exp.name for exp in self.op.experiments ]
        self.assertItemsEqual(listing_target, listing_result)

    def test_run_all_experiments(self):
        self.op.run_all()

