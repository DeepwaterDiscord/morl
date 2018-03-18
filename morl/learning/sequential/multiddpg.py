import random
import numpy as np
import tensorflow as tf
from .ddpg import DDPG_Learner

class MultiDDPG(object):
    def __init__(self, actions, gamma, reward_functions, action_dim, action_bound, state_dim, minibatch_size=64, include_sum=False):
        self._gamma = gamma
        self.actions = actions
        self.graphs = []
        self.ddpglearners = []
        i = 0
        for r in reward_functions:
            g = tf.Graph()
            self.graphs.append(g)
            self.ddpglearners.append(DDPG_Learner(actions, gamma, r, action_dim, action_bound, state_dim, default_file_name="learner_" + str(i), save_dir="/home/parallels/Documents/", minibatch_size=minibatch_size, graph=g, load=True))
            i += 1
        if include_sum:
            g = tf.Graph()
            self.graphs.append(g)
            self.ddpglearners.append(DDPG_Learner(actions, gamma, lambda x: sum([r(x) for r in reward_functions]), action_dim, action_bound, state_dim, default_file_name="learner_" + str(i), save_dir="/home/parallels/Documents/", minibatch_size=minibatch_size, graph=g, load=True))
        self.nrewards = len(self.ddpglearners)

    @property
    def gamma(self):
        return self._gamma

    @gamma.setter
    def gamma(self, value):
        self._gamma = value
        for qlearner in self.ddpglearners:
            qlearner.alpha = value
        return self._gamma

    def getQ(self, state, action):
        return [ql.getQ(state, action) for ql in self.ddpglearners]

    def learn(self, state1, action1, results, state2, done):
        for i in range(self.nrewards):
            self.ddpglearners[i].learn(state1, action1, results, state2, done)
    
    def choose_action_random(self, state):
        return random.choice(self.filter(state))
    
    # def choose_action_mean(self, state):
    #     return [np.mean([action[col] for col in len(action)])
    
    # def choose_action_median(self, state):
    #     return n

    def choose_action(self, state):
        return self.choose_action_random(state)

    def train(self, start_state, environment, max_iter=None, method=choose_action_random,
              state_function=lambda results: results[0],
              done_function=lambda results: results[2]):
        use_max_iter = max_iter is not None
        iterations = 0
        new_state = start_state
        done = False
        while not done and (not use_max_iter or iterations < max_iter):
            new_state, done = self.train_step(new_state, environment, method,
                                              state_function, done_function)

    def train_step(self, state, environment, method=choose_action_random,
                   state_function=lambda results: results[0],
                   done_function=lambda results: results[2]):
        # Choose the action
        action = method(self, state)

        # Take the action
        results = environment.step(action)

        # Get state2
        state2 = state_function(results)

        # Evaluate doneness
        done = done_function(results)

        # Call learn
        self.learn(state, action, results, state2, done)

        # Return new state
        return state2, done
    
    def filter(self, state):
        # In the case of DDPG, it's only a pseudo-filter.  That is, it returns the choice of each network instead of options not dominated.
        # This is because the action space is assumed to be continuous and therefore impractical to compute the full pareto front
        return [ql.choose_action(state) for ql in self.ddpglearners]
    

