import unittest as ut
from ..learning.sequential.multilearn import MultiLearn

class MultilearnAlpha(ut.case.TestCase):
    def runTest(self):
        multilearner = MultiLearn(None, 1, 0.9, 0.8, (lambda x: x[1]))
        self.assertAlmostEqual(multilearner._alpha, 0.8, 3)
        self.assertAlmostEqual(multilearner.alpha, 0.8, 3)
        self.assertAlmostEqual(multilearner.qlearners[0].alpha, 0.8, 3)

        multilearner.gamma = 0.78
        self.assertAlmostEqual(multilearner._alpha, 0.78, 3)
        self.assertAlmostEqual(multilearner.alpha, 0.78, 3)
        self.assertAlmostEqual(multilearner.qlearners[0].alpha, 0.78, 3)

class MultilearnGamma(ut.case.TestCase):
    def runTest(self):
        multilearner = MultiLearn(None, 1, 0.9, 0.8, (lambda x: x[1]))
        self.assertAlmostEqual(multilearner._gamma, 0.9, 3)
        self.assertAlmostEqual(multilearner.gamma, 0.9, 3)
        self.assertAlmostEqual(multilearner.qlearners[0].gamma, 0.9, 3)

        multilearner.gamma = 0.23
        self.assertAlmostEqual(multilearner._gamma, 0.23, 3)
        self.assertAlmostEqual(multilearner.gamma, 0.23, 3)
        self.assertAlmostEqual(multilearner.qlearners[0].gamma, 0.23, 3)

class MultilearnEpsilon(ut.case.TestCase):
    def runTest(self):
        multilearner = MultiLearn(None, 1, 0.9, 0.8, (lambda x: x[1]))
        self.assertAlmostEqual(multilearner._epsilon, 1, 3)
        self.assertAlmostEqual(multilearner.epsilon, 1, 3)
        self.assertAlmostEqual(multilearner.qlearners[0].epsilon, 1)

        multilearner.epsilon = 0.52
        self.assertAlmostEqual(multilearner._epsilon, 0.52)
        self.assertAlmostEqual(multilearner.epsilon, 0.52)
        self.assertAlmostEqual(multilearner.qlearners[0].epsilon, 0.52)

class MultilearnGetQ(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnChooseActions(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnChooseAction(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultiLearnChooseActionMaxutil(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnChooseActionRandom(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnChooseActionVote(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnChooseActionEgreedy(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnFilter(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnLearn(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnTrain(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class MultilearnTrainStep(ut.case.TestCase):
    def runTest(self):
        self.skipTest("Not Implemented")

class QLearnSuite(ut.TestSuite):
    def __init__(self):
        super(ut.TestSuite, self)
        self.addTests((MultilearnAlpha(),
                       MultilearnGamma(),
                       MultilearnEpsilon(),
                       MultilearnGetQ(),
                       MultilearnChooseActions(),
                       MultilearnChooseAction(),
                       MultiLearnChooseActionMaxutil(),
                       MultilearnChooseActionRandom(),
                       MultilearnChooseActionVote(),
                       MultilearnChooseActionEgreedy(),
                       MultilearnFilter(),
                       MultilearnLearn(),
                       MultilearnTrain(),
                       MultilearnTrainStep()))