from ..learning.sequential.ddpg import ActorNetwork, CriticNetwork, DDPG_Learner
from ..learning.sequential.replay_buffer import ReplayBuffer
from ..learning.sequential.qlearn import QLearn
import numpy as np
import gym
import pandas as p
import tensorflow as tf
from ..run.MultiLearnEnvironment import MultiLearnEnvironment
from ..learning.sequential.multiddpg import MultiDDPG

class MujocoConfig(MultiLearnEnvironment):
    def __init__(self, learner=None, render=False):
        self.env = gym.make("Humanoid-v1")
        self.states_list = []
        self.render = render
        learn = learner
        if learner is None:
            learn = QLearn({}, 0, 0, 0, lambda x: x[1])
        self.learner_obj = learn
        super(MujocoConfig, self).__init__(learner_klass=None)

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

def Run_Example():
    minibatch_size = 64
    pc = MujocoConfig(render=True)

    rand_seed = 1234

    env = pc.env

    np.random.seed(rand_seed)
    tf.set_random_seed(rand_seed)
    env.seed(rand_seed)
    
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]
    action_bound = env.action_space.high

    # with tf.Session() as sess:
    #     assert (env.action_space.high == -env.action_space.low)
        
    #     sess.run(tf.global_variables_initializer())

    #     actor.update_target_network()
    #     critic.update_target_network()

    #     # Initialize replay memory
    #     replay_buffer = ReplayBuffer(1000000)

        # ddpg_learner = DDPG_Learner(actions=env.action_space, epsilon=1,alpha=0.001,gamma=0.99,
        #                             reward_function=lambda x: x[1], actor=actor, 
        #                             critic=critic, buffer=replay_buffer, 
        #                             action_dim=action_dim, minibatch_size=minibatch_size)
    reward_functions = (
        lambda x: x[1]['reward_impact'],
        lambda x: x[1]['reward_quadctrl'],
        lambda x: x[1]['reward_alive'],
        lambda x: x[1]['reward_linvel']
    )
    """
    reward_functions = (
        lambda x: x[3]['reward_alive'],
    )
    """
    ddpg_multilearner = MultiDDPG(actions=env.action_space, gamma=0.8, reward_functions=reward_functions, action_dim=action_dim, action_bound=action_bound, state_dim=state_dim, minibatch_size=minibatch_size)
    pc.learner_obj = ddpg_multilearner
    pc.run(num_epochs=50000, num_tests=10, test_length=1000)
