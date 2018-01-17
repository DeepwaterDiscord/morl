# Implementation from https://github.com/vmayoral/basic_reinforcement_learning
# Modified to allow for state-specific actions

import random

class QLearn(object):
    """
        Traditional QLearning with Single-Policy Learning based on a
        linear combination of reward components.
    """
    def __init__(self, actions, epsilon, alpha, gamma, reward_function):
        self.q = {}
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions  # action is a dictionary of key(State):value(List(Action))
        self.reward_function = reward_function # reward function that takes results tuple

    def getQ(self, state, action):
        """ Returns Q value for state-action pair. """
        return self.q.get((state, action), 0.0)

    def learnQ(self, state, action, reward, value):
        """
        Q-learning:
            Q(s, a) += alpha * (reward(s,a) + max(Q(s') - Q(s,a))
        """
        oldv = self.q.get((state, action), None)
        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)

    def choose_action_egreedy(self, state, return_q=False):
        """ Chooses an action using the epsilon-greedy strategy. """
        if random.random() < self.epsilon:
            # altered to remove magic numbers and change back to a truly random choice
            if return_q:
                act = random.choice(self.actions[state])
                qval = self.getQ(state, act)
                return random.choice(self.actions[state]), qval
            return random.choice(self.actions[state])
        return None

    def choose_action(self, state, return_q=False, rand_method=choose_action_egreedy):
        """ Chooses an action using the random exploration strategy or the best possible
            if the exploration strategy fails to return an exploratory action
        """
        qvals = [self.getQ(state, a) for a in self.actions[state]]
        max_q = max(qvals)

        action = 0
        # altered to allow for various exploration strategies
        action = rand_method(self, state, return_q)

        if action is None:
            count = qvals.count(max_q)
            # In case there're several state-action max values
            # we select a random one among them
            if count > 1:
                best = [i for i in range(len(self.actions[state])) if qvals[i] == max_q]
                i = random.choice(best)
            else:
                i = qvals.index(max_q)

            action = self.actions[state][i]

        if return_q: # if they want it, give it!
            return action, qvals
        return action

    def learn(self, state1, action1, results, state2):
        """ Updates Q values based on maximizing the future Q values """
        maxqnew = max([self.getQ(state2, a) for a in self.actions[state2]])
        reward = self.reward_function(results)
        self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)

    def train(self, start_state, environment, max_iter=None,
              state_function=lambda results: results[0],
              done_function=lambda results: results[2]):
        """ Runs one training episode """
        use_max_iter = max_iter is not None
        iterations = 0
        new_state = start_state
        done = False
        while not done and (not use_max_iter or iterations < max_iter):
            new_state, done = self.train_step(new_state, environment, QLearn.choose_action_egreedy,
                                              state_function, done_function)
            iterations += 1
        return iterations

    def train_step(self, state, environment, rand_method=choose_action_egreedy,
                   state_function=lambda results: results[0],
                   done_function=lambda results: results[2]):
        """ Performs one step and learns from the results. """
        # Choose the action
        action = self.choose_action(state, False, rand_method)

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
