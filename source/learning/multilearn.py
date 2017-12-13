import random
from qlearn import QLearn

class MultiLearn:
    def __init__(self, actions, epsilon, alpha, gamma, nrewards):
        self.QLearners = [QLearn(actions, epsilon, alpha, gamma) for n in range(nrewards)]
        self.actions = actions
        self.epsilon = epsilon
        self.nrewards = nrewards

    def choose_actions(self, state, return_q=False):
        q = {a:[QL.getQ(state, a) for QL in self.QLearners] for a in QL.actions[state]}
        actions = self.filter(q, state)

        if return_q:
            return actions, q
        return actions

    def choose_action_maxutil(self, state, return_q=False):
        q = {a:[QL.getQ(state, a) for QL in self.QLearners] for a in self.actions[state]}
        action_list = self.filter(q, state)
        # Keep in mind that the scaling of rewards will affect the outcome of this function
        action_utilsums = {a:sum(q[a]) for a in action_list}
        max_utilsum = max(action_utilsums.values())
        best = [a for a in action_utilsums.keys() if action_utilsums[a] == max_utilsum]
        # If multiple actions maximize the sum of the utilities, return a randomly chosen one from those.
        action =  random.choice(best)

        if return_q:
            return action, q
        return action

    def choose_action_random(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in self.actions[state]}
        action_list = self.filter(q, state)
        action = random.choice(action_list)
        if return_q:
            return action, q
        return action

    def choose_action_vote(self, state, return_q=False):
        q = {a:[QL.getQ(state, a) for QL in self.QLearners] for a in self.actions[state]}
        qmaxes = (max([QL.getQ(state,a) for a in QL.actions[state]]) for QL in self.QLearners)

        action_list = self.filter(q, state)

        # Take a poll of all QLearners.
        qvote = { a:[q[a][i] == qmaxes[i] for i in range(len(qmaxes))].count(True) for a in action_list }
        max_vote = max(qvote.values())
        best = [a for a in qvote.keys() if qvote[a]==max_vote]
        # If multiple actions maximize the sum of the utilities, return a randomly chosen one from those.
        action = random.choice(best)

        if return_q:
            return action, q
        return action

    def choose_action_random_nofilter(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in self.actions[state]}
        action = random.choice(self.actions[state])

        if return_q:
            return action, q
        return action

    def choose_action(self, state, return_q=False, method=choose_action_random):
        if random.random() < self.epsilon:
            return self.choose_action_random_nofilter(state, return_q)
        else:
            return method(state, return_q)
    
    def filter(self, qarray, state):
        # Starft with an empty filter
        qfilter = []
        for a in self.actions[state]:
            # is the current action dominated by any action in the filter?
            dominated = {filtact: all([qarray[a][i]<qarray[filtact][i] for i in range(len(qarray[filtact]))]) for filtact in qfilter}

            # does the current action dominate any action in the filter?
            dominates = {filtact: all([qarray[a][i]>qarray[filtact][i] for i in range(len(qarray[filtact]))]) for filtact in qfilter}

            if any(dominated.values()):
                # if it's dominated by an action already in the filter, skip it.
                continue
            else:
                # otherwise, if it dominates something else remove it.
                qfilter.remove(dominated_action for dominated_action in qfilter if dominates[dominated_action])

                # regardless of whether it dominates something else, append it.
                qfilter.append(a)
        return qfilter

    def learn(self, state1, action1, rewards, state2):
        if len(rewards) != self.nrewards:
            raise "Reward List Error: Lenght of rewards list is not equal to the number of rewards."
        for i in range(len(rewards)):
            self.QLearners[i].learn(state1, action1, rewards[i], state2)

    def train(self, start_state, environment, reward_functions, max_iter=None, method=choose_action_random, state_function=lambda results: results[0], done_function=lambda results: results[2]):
        use_max_iter = max_iter is not None
        iterations = 0
        new_state = start_state
        done = False
        while not done and (not use_max_iter or iterations < max_iter):
            new_state, done = self.train_step(new_state, environment, reward_functions, method, state_function, done_function)

    def train_step(self, state, environment, reward_functions, method=choose_action_random, state_function=lambda results: results[0], done_function=lambda results: results[2]):
        # Choose the action
        action = self.choose_action(state, False, method)

        # Take the action
        results = environment.step(action)

        # Process results
        rewards = [f(results) for f in reward_functions]

        # Get state2
        state2 = state_function(results)

        # Call learn
        self.learn(state, action, rewards, state2)

        # Evaluate doneness
        done = done_function(results)

        # Return new state
        return state2, done