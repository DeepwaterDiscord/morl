import random
from .qlearn import QLearn

class MultiLearn(object):
    def __init__(self, actions, epsilon, alpha, gamma, reward_functions, default_actions={}, klass=QLearn):
        self.nrewards = len(reward_functions)
        self.qlearners = [klass(actions, epsilon, alpha, gamma, reward_functions[n], default_actions=default_actions)
                          for n in range(self.nrewards)]
        self.actions = {}
        self.actions.update(actions)
        self.default_actions = default_actions

        self._epsilon = epsilon
        self._alpha = alpha
        self._gamma = gamma
        self.reward_functions = reward_functions

    @property
    def epsilon(self):
        return self._epsilon

    @epsilon.setter
    def epsilon(self, value):
        self._epsilon = value
        for qlearner in self.qlearners:
            qlearner.epsilon = value
        return self._epsilon

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value
        for qlearner in self.qlearners:
            qlearner.alpha = value
        return self._alpha

    @property
    def gamma(self):
        return self._gamma

    @gamma.setter
    def gamma(self, value):
        self._gamma = value
        for qlearner in self.qlearners:
            qlearner.alpha = value
        return self._gamma

    def getQ(self, state):
        return {a:[qlearner.getQ(state, a) for qlearner in self.qlearners]
                for a in self.get_actions(state)}

    def choose_actions(self, state, return_q=False):
        qval = self.getQ(state)
        actions = self.filter(qval, state)

        if return_q:
            return actions, qval
        return actions

    def choose_action_maxutil(self, state, return_q=False):
        qval = self.getQ(state)
        action_list = self.filter(qval, state)
        # Keep in mind that the scaling of rewards will affect the outcome of this function
        action_utilsums = {a:sum(qval[a]) for a in action_list}
        max_utilsum = max(action_utilsums.values())
        best = [a for a in action_utilsums.keys() if action_utilsums[a] == max_utilsum]
        # If multiple actions maximize the sum of the utilities, return a
        # randomly chosen one from those.
        action = random.choice(best)

        if return_q:
            return action, qval
        return action

    def choose_action_random(self, state, return_q=False):
        qval = self.getQ(state)
        action_list = self.filter(qval, state)
        action = random.choice(action_list)
        if return_q:
            return action, qval
        return action

    def choose_action_vote(self, state, return_q=False):
        qval = self.getQ(state)
        qmaxes = (max([QL.getQ(state, a) for a in QL.get_actions[state]]) for QL in self.qlearners)

        action_list = self.filter(qval, state)

        # Take a poll of all qlearners.
        qvote = {a:[qval[a][i] == qmaxes[i] for i in range(len(qmaxes))].count(True)
                 for a in action_list}
        max_vote = max(qvote.values())
        best = [a for a in qvote.keys() if qvote[a] == max_vote]
        # If multiple actions maximize the sum of the utilities,
        # return a randomly chosen one from those.
        action = random.choice(best)

        if return_q:
            return action, qval
        return action

    def choose_action_egreedy(self, state, return_q=False):
        qval = self.getQ(state)
        action = random.choice(self.actions[state])

        if random.random() < self.epsilon:
            if return_q:
                return action, qval
            return action
        else:
            return None

    def choose_action(self, state, return_q=False, method=choose_action_random,
                      rand_method=choose_action_egreedy):
        action = rand_method(self, state, return_q)
        if action is None:
            action = method(self, state, return_q)
        return action
    
    def get_actions(self, state):
        return self.actions.get(state, self.default_actions)

    def filter(self, qarray, state):
        # Starft with an empty filter
        qfilter = []
        for act in self.actions[state]:
            # is the current action dominated by any action in the filter?
            dominated = {filtact: all([qarray[act][i] < qarray[filtact][i]
                                       for i in range(len(qarray[filtact]))])
                         for filtact in qfilter}

            # does the current action dominate any action in the filter?
            dominates = {filtact: all([qarray[act][i] > qarray[filtact][i]
                                       for i in range(len(qarray[filtact]))])
                         for filtact in qfilter}

            if any(dominated.values()):
                # if it's dominated by an action already in the filter, skip it.
                continue
            else:
                # otherwise, if it dominates something else remove it.
                for dominated_action in qfilter:
                    if dominates[dominated_action]:
                        qfilter.remove(dominated_action)
                # qfilter.remove(dominated_action for dominated_action
                # in qfilter if dominates[dominated_action])

                # regardless of whether it dominates something else, append it.
                qfilter.append(act)
        return qfilter

    def learn(self, state1, action1, results, state2):
        for i in range(self.nrewards):
            self.qlearners[i].learn(state1, action1, results, state2)

    def train(self, start_state, environment, max_iter=None, method=choose_action_random,
              rand_method=choose_action_egreedy, state_function=lambda results: results[0],
              done_function=lambda results: results[2]):
        use_max_iter = max_iter is not None
        iterations = 0
        new_state = start_state
        done = False
        while not done and (not use_max_iter or iterations < max_iter):
            new_state, done = self.train_step(new_state, environment, method,
                                              rand_method, state_function, done_function)

    def train_step(self, state, environment, method=choose_action_random,
                   rand_method=choose_action_egreedy, state_function=lambda results: results[0],
                   done_function=lambda results: results[2]):
        # Choose the action
        action = self.choose_action(state, False, method, rand_method)

        # Take the action
        results = environment.step(action)

        # Get state2
        state2 = state_function(results)

        # Call learn
        self.learn(state, action, results, state2)

        # Evaluate doneness
        done = done_function(results)

        # Return new state
        return state2, done
