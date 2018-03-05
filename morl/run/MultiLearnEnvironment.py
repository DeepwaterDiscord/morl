from ..learning.sequential.multilearn import MultiLearn
from .MORLEnvironment import MORLEnvironment

class MultiLearnEnvironment(MORLEnvironment):
    def __init__(self, learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9, doprint=True):
        self.ignore_learner_warning = True        
        super(MultiLearnEnvironment, self).__init__(None, n_learners, epsilon_start, alpha_start, gamma_start, doprint)
        reward_functions = [lambda results: results[1][x] for x in xrange(n_learners)]        
        self.learner_obj = MultiLearn(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_functions, klass=learner_klass)
