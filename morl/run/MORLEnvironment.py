import pickle
import datetime

class MORLEnvironment:
    def __init__(self, learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9):
        # Initialize Configuration
        self._epsilon_start = epsilon_start
        self._alpha_start = alpha_start
        self._gamma_start = gamma_start
        self.nlearners = n_learners
        self.timestamp = datetime.time()
        if learner_klass.__name__ == "MultiLearn":
            reward_functions = [lambda results: results[1][x] for x in xrange(n_learners)]
            learner_klass.__init__(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_functions)
        elif: learner_klass.__name__ == "QLearn":
            if n_learners >= 1:
                reward_function = lambda results: sum([results[1][x] for x in xrange(n_learners)])
            else:
                reward_function = lambda results: results[1]
                learner_klass.__init__(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_function))

    name = "Generic MORL Environment"
    default_actions = [0,1]

    def step(self):
        # returns tuple of next_state, rewards, done
        return (self.states()[0], 0, False)

    def reset(self):
        # return start state
        return self.states()[0]
    
    def epsilon(self, epoch):
        return self._epsilon_start

    def gamma(self, epoch):
        return self._gamma_start

    def alpha(self, epoch):
        return self._alpha_start

    def states(self):
        return [0, 1, 2]

    def actions(self):
        # returns dictionary of state:[actions]
        return {s: type(self).default_actions for s in self.states()}

    def learner(self):
        return self.learner