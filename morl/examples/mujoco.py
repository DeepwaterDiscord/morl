from ..run.MORLEnvironment import MORLEnvironment
from ..learning.sequential.multilearn import MultiLearn
from ..learning.sequential.qlearn import QLearn
import gym
import sys

class FrozenLakeConfig(MORLEnvironment):
    def __init__(self):
        self.env = gym.make("Humanoid-v1")
        super(FrozenLakeConfig, self).__init__(learner_klass=MultiLearn, n_learners=1)   

    name = "Mujoco Humanoid Environment"
    default_actions = acts

    def step(self, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def states(self):
        return range(self.env.observation_space.n)

def Run_Example():
    mjc = FrozenLakeConfig()
    sys.stdout.write(mjc.learner())
    mjc.run(num_epochs=2000, num_tests=50, test_length=100)
