import unittest as ut

class QLearnTestName(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here

class QLearnTestName2(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here

class QLearnSuite(ut.TestSuite):
    def __init__(self):
        super(ut.TestSuite, self)
        self.addTests((QLearnTestName(), QLearnTestName2()))