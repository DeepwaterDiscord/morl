from ..learning.sequential.ddpg import ActorNetwork, CriticNetwork, DDPG_Learner
from ..learning.sequential.replay_buffer import ReplayBuffer
from ..learning.sequential.qlearn import QLearn
import numpy as np
import gym
import pandas as p
import tensorflow as tf
from ..run.MultiLearnEnvironment import MultiLearnEnvironment
from ..learning.sequential.multiddpg import MultiDDPG

class Config(MultiLearnEnvironment):
    def __init__(self, learner=None, render=False):
        self.env = gym.make("Humanoid-v1")
        self.states_list = []
        self.render = render
        super(MujocoConfig, self).__init__(learner_klass=None)
        minibatch_size = 64
        rand_seed = 1234
        np.random.seed(rand_seed)
        tf.set_random_seed(rand_seed)
        self.env.seed(rand_seed)
        state_dim = self.env.observation_space.shape[0]
        action_dim = self.env.action_space.shape[0]
        action_bound = self.env.action_space.high
        self.learner_obj = MultiDDPG(actions=self.env.action_space, gamma=0.8, reward_functions=self.rewards(), action_dim=action_dim, action_bound=action_bound, state_dim=state_dim, minibatch_size=minibatch_size)

    def step(self, action):
        obs, rew, done, dict_rew = self.env.step(action)
        dict_rew['total'] = rew
        if self.render:
            self.env.render()
        return (obs, dict_rew, done)
    
    def reset(self):
        return self.env.reset()

    def states(self):
        return self.states_list

    def rewards(self):
        reward_functions = (
            lambda x: x[1]['reward_impact'],
            lambda x: x[1]['reward_quadctrl'],
            lambda x: x[1]['reward_alive'],
            lambda x: x[1]['reward_linvel']
        )
        return reward_functions
