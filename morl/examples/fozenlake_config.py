from ..run import MORLEnvironment
from ..learning.sequential.multilearn import MultiLearn
import gym


class FrozenLakeConfig(MORLEnvironment):
    def __init__(self):
        super.__init__(learner_klass="QLearn", n_learners=1)
        name = "Frozen Lake Environment"
        self.env = gym.make("FrozenLake-v0")

    _left = 0
    _down = 1
    _right = 2
    _up = 3
    acts = [_left, _down, _right, _up]
    default_actions = acts

    def step(self, action):
        return self.env.step(action)


