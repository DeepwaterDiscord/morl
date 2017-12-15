# Implementation from https://github.com/vmayoral/basic_reinforcement_learning
# Modified to allow for state-specific actions

import random

class QLearn:
    def __init__(self, actions, epsilon, alpha, gamma, reward_function):
        self.q = {}
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions  # action is a dictionary of key(State):value(List(Action))
        self.reward_function = reward_function # reward function that takes results tuple

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learnQ(self, state, action, reward, value):
        '''
        Q-learning:
            Q(s, a) += alpha * (reward(s,a) + max(Q(s') - Q(s,a))            
        '''
        oldv = self.q.get((state, action), None)
        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)

    def choose_action(self, state, return_q=False):
        q = [self.getQ(state, a) for a in self.actions[state]]
        maxQ = max(q)

        if random.random() < self.epsilon:
            # altered to remove magic numbers and change back to a truly random choice
            if return_q:
                return random.choice(self.actions[state]), q
            return random.choice(self.actions[state])

        count = q.count(maxQ)
        # In case there're several state-action max values 
        # we select a random one among them
        if count > 1:
            best = [i for i in range(len(self.actions[state])) if q[i] == maxQ]
            i = random.choice(best)
        else:
            i = q.index(maxQ)

        action = self.actions[state][i]        
        if return_q: # if they want it, give it!
            return action, q
        return action

    def learn(self, state1, action1, results, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions[state2]])
        reward = self.reward_function(results)
        self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)
    
    def train(self, start_state, environment, max_iter=None, state_function=lambda results: results[0], done_function=lambda results: results[2]):
        use_max_iter = max_iter is not None
        iterations = 0
        new_state = start_state
        done = False
        while not done and (not use_max_iter or iterations < max_iter):
            new_state, done = self.train_step(new_state, environment, state_function, done_function)

    def train_step(self, state, environment, state_function=lambda results: results[0], done_function=lambda results: results[2]):
        # Choose the action
        action = self.choose_action(state, False)

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