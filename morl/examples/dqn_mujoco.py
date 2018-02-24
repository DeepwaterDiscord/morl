from ..learning.sequential.dqn import DeepQ, Memory, DQN_Learner
from ..learning.sequential.qlearn import QLearn
from ..run.MORLEnvironment import MORLEnvironment
import numpy as np
import gym
import pandas as p

class MujocoConfig(MORLEnvironment):
    def __init__(self, learner=None, num_bins=1000):
        self.env = gym.make("Humanoid-v1")

        learn = learner
        self.learner_obj = learn
        super(MujocoConfig, self).__init__(learner_klass=None, n_learners=1)
        
    name = "Mujoco Humanoid Environment"
    default_actions = []

    def make_state(self, bin_nums):
        #print "Bin Nums:", bin_nums
        return tuple(int(b) for b in bin_nums)

    def convert_to_bin(self, val, bins):
        return np.digitize(x=[val], bins=bins)[0]

    def get_state(self, observation, bin_collection, env):
        states = [self.convert_to_bin(observation[i], bin_collection[i]) for i
                  in range(env.observation_space.shape[0])]
        #print observation, bin_collection
        return self.make_state(states)

    def step(self, action):
        obs, rew, done, _ = self.env.step(action)
        state = self.get_state(obs, self.bins, self.env)
        return (state, rew, done)
    
    def reset(self):
        return self.get_state(self.env.reset(), self.bins, self.env)

    def states(self):
        return self.states_list

def Run_Example():
    learnStart = 128
    learningRate = 0.00025
    discountFactor = 0.99
    memorySize = 1000000
    deepQ = DeepQ(2, 3, memorySize, discountFactor, learningRate, learnStart)
    deepQ.initNetworks([30,30])

    learner = DQN_Learner(actions=[0, 1, 2], epsilon=1, alpha=learningRate, gamma=discountFactor, reward_function=lambda x: x[1], deepQNetwork=deepQ)
    mcc = MountainCarConfig(learner=learner, num_bins=1000)
    mcc.run(num_epochs=1000, num_tests=10, test_length=200)