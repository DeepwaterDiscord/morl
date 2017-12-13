import random
from qlearn import QLearn

class MultiLearn():
    def __init__(self, actions, epsilon, alpha, gamma, nrewards):
        self.QLearners = [QLearn(actions, epsilon, alpha, gamma) for n in range(nrewards)]
        self.actions = actions
        self.epsilon = epsilon
    
    def choose_actions(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in QL.actions[state]}
        actions = self.filter(q, state)

        if return_q:
            return actions, q
        return actions

    def choose_action_maxutil(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in QL.actions[state]}
        action_list = self.filter(q, state)
        # Keep in mind that the scaling of rewards will affect the outcome of this function
        action_utilsums = {a:sum(q[a]) for a in self.actions[state]}
        max_utilsum = max(action_utilsums.values())
        best = [a for a in action_utilsums.keys() if action_utilsums[a] == max_utilsum]
        # If multiple actions maximize the sum of the utilities, return a randomly chosen one from those.
        action =  random.choice(best)

        if return_q:
            return action, q
        return action

    def choose_action_random(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in QL.actions[state]}
        action_list = self.filter(q, state)
        action = random.choice(action_list)
        if return_q:
            return action, q
        return action

    def choose_action_vote(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in QL.actions[state]}
        qmaxes = (max([QL.getQ(state,a) for a in QL.actions[state]]) for QL in self.QLearners)

        action_list = self.filter(q, state)

        # Take a poll of all QLearners.
        qvote = { a:[q[a][i] == qmaxes[i] for i in range(len(qmaxes))].count(True) for a in self.actions[state] }
        max_vote = max(qvote.values())
        best = [a for a in qvote.keys() if qvote[a]==max_vote]
        # If multiple actions maximize the sum of the utilities, return a randomly chosen one from those.
        action = random.choice(best)

        if return_q:
            return action, q
        return action

    def choose_action_random_nofilter(self, state, return_q=False):
        q = {a:(QL.getQ(state, a) for QL in self.QLearners) for a in QL.actions[state]}
        action = random.choice(self.actions[state])

        if return_q:
            return action, q
        return action

    def choose_action(self, state, return_q=False, method=self.choose_action_random):
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
