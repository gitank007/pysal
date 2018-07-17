from pysalnext.model.spvcm import upper_level as upper
from pysalnext.model.spvcm import utils
from pysalnext.model.spvcm.tests.utils import Model_Mixin
from pysalnext.model.spvcm.abstracts import Trace
import unittest as ut
import pandas as pd
import os

FULL_PATH = os.path.dirname(os.path.abspath(__file__))

class Test_Upper_SE(ut.TestCase, Model_Mixin):
    def setUp(self):
        super(Test_Upper_SE, self).build_self()
        self.cls = upper.SE
        del self.inputs["W"]
        self.inputs['n_samples'] = 0
        instance = self.cls(**self.inputs)
        self.answer_trace = Trace.from_csv(FULL_PATH + '/data/upper_se.csv')