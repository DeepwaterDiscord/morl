import random
from ..sequential.multilearn import MultiLearn
#from ...config import Config
from ..sequential.qlearn import QLearn
from pyspark import SparkContext

class Config(object):
    SPARK_MASTER = "localhost"
    SPARK_APP_NAME = "morl"

class MultiLearnP(MultiLearn):
    def __init__(self, actions, epsilon, alpha, gamma, reward_functions):
        super(MultiLearnP, self).__init__(actions, epsilon, alpha, gamma, reward_functions)
        self.sc = SparkContext(Config.SPARK_MASTER, Config.SPARK_APP_NAME)
        self.QLearnersRDD = self.sc.parallelize([(n, QLearn(actions, epsilon, alpha, gamma, reward_functions[n])) for n in range(self.nrewards)])

    @property
    def epsilon(self):
        return self._epsilon

    @epsilon.setter
    def epsilon(self, value):
        self._epsilon = value
        self.QLearnersRDD = self.QLearnersRDD.map(lambda QL: (QL[0], QL[1].update(epsilon=value)))
        return self._epsilon

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value
        self.QLearnersRDD = self.QLearnersRDD.map(lambda QL: (QL[0], QL[1].update(alpha=value)))
        return self._alpha

    @property
    def gamma(self):
        return self._gamma

    @gamma.setter
    def gamma(self, value):
        self._gamma = value
        self.QLearnersRDD = self.QLearnersRDD.map(lambda QL: (QL[0], QL[1].update(gamma=value)))
        return self._gamma

    def getQ(self, state):
        """
            Returns q values for all q learners and actions from a given state as
            List(Dictionary(action: Qvalue)) with 1 element per QLearner
            Dictionary(action: List(Qvalues))
        """
        self.QLearners = self.QLearnersRDD.map(lambda QL: QL[1]).collect()
        return {a:[QL.getQ(state, a) for QL in self.QLearners] for a in self.actions[state]}
            
        

    def choose_actions(self, state, return_q=False):
        q = self.getQ(state)
        actions = self.filter(q, state)

        if return_q:
            return actions, q
        return actions

    def choose_action_maxutil(self, state, return_q=False):
        q = self.getQ(state)
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
        q = self.getQ(state)
        action_list = self.filter(q, state)
        action = random.choice(action_list)
        if return_q:
            return action, q
        return action

    def choose_action_vote(self, state, return_q=False):
        q = self.getQ(state)
        qmaxes = self.QLearnersRDD.map(lambda QL: (max([QL[1].getQ(state,a) for a in QL[1].actions[state]]))).collect()

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

    def learn(self, state1, action1, results, state2):
        self.QLearnersRDD = self.QLearnersRDD.map(lambda QL: QL[1].learn(state1, action1, results, state2))
