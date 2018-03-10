from morl.run.MORLEnvironment import MORLEnvironment
from morl.learning.sequential.multilearn import MultiLearn
from morl.learning.sequential.qlearn import QLearn
import gym
import sys

class FrozenLakeConfig(MORLEnvironment):
    def __init__(self):
        self.env = gym.make("FrozenLake-v0")
        super(FrozenLakeConfig, self).__init__(learner_klass=QLearn, n_learners=1)

    name = "Frozen Lake Environment"
    _left = 0
    _down = 1
    _right = 2
    _up = 3
    acts = [_left, _down, _right, _up]
    default_actions = acts

    def step(self, action):
        return self.env.step(action)[0:3]

    def reset(self):
        return self.env.reset()

    def states(self):
        return range(self.env.observation_space.n)

def Run_Example():
    flc = FrozenLakeConfig()
    sys.stdout.write(str(flc.learner()))
    flc.run(num_epochs=2000, num_tests=50, test_length=100)
