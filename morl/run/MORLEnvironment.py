import sys
import pickle
import datetime
from ..learning.sequential.qlearn import QLearn
from ..learning.sequential.multilearn import MultiLearn

class MORLEnvironment(object):
    def __init__(self, learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9, doprint=True):
        # Initialize Configuration
        self._epsilon_start = epsilon_start
        self._alpha_start = alpha_start
        self._gamma_start = gamma_start
        self.nlearners = n_learners
        self.timestamp = datetime.time()
        self.doprint = doprint
        if learner_klass is None:
            if not self.ignore_learner_warning:
                sys.stderr.write("WARNING: Learner class is not defined, hopefully the learner_obj is set manually.\n")
        elif learner_klass.__name__ == MultiLearn.__name__:
            reward_functions = [lambda results: results[1][x] for x in xrange(n_learners)]
            self.learner_obj = MultiLearn(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_functions)
        elif learner_klass.__name__ == QLearn.__name__:
            if n_learners > 1:
                reward_function = lambda results: sum([results[1][x] for x in xrange(n_learners)])
                self.learner_obj = QLearn(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_function)
            else:
                reward_function = lambda results: results[1]
                self.learner_obj = QLearn(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_function)

    name = "Generic MORL Environment"
    default_actions = [0,1]
    ignore_learner_warning = False

    def step(self, action):
        # returns tuple of next_state, rewards, done
        return (self.states()[0], 0, False)

    def reset(self):
        # return start state
        return self.states()[0]
    
    def epsilon(self, epoch=0):
        return self._epsilon_start

    def gamma(self, epoch=0):
        return self._gamma_start

    def alpha(self, epoch=0):
        return self._alpha_start

    def states(self):
        return [0, 1, 2]

    def actions(self):
        # returns dictionary of state:[actions]
        return {s: type(self).default_actions for s in self.states()}

    def learner(self):
        return self.learner_obj

    def run(self, num_epochs, num_tests, test_length):
        learner = self.learner()
        reward_per_epoch = []
    
        for epoch in xrange(num_epochs):
            epoch_reward = 0
            prev_state = self.reset()
            
            # Learning
            learner.train(start_state=prev_state, environment=self)

            # Testing
            learner.epsilon = 0.00
            for _i in range(num_tests):
                prev_state = self.reset()
                for _t in range(test_length):
                    action = learner.choose_action(prev_state)
                    new_state, reward, done = self.step(action)
                    try:
                        epoch_reward += sum(reward)
                    except:
                        epoch_reward += reward
                    prev_state = new_state

                    if done:
                        break

            if epoch % 10 == 0 and self.doprint:
                sys.stdout.write("Epoch %i finished, total reward: %0.6f\n" 
                        % (epoch+1, epoch_reward))
    
            reward_per_epoch.append(epoch_reward/num_tests)