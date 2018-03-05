from .MORLEnvironment import MORLEnvironment

class SingleLearnEnvironment(MORLEnvironment):
    def __init__(self, learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9, doprint=True):
        super(SingleLearnEnvironment, self).__init__(learner_klass, n_learners, epsilon_start, alpha_start, gamma_start, doprint)
