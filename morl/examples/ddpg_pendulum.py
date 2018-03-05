from ..learning.sequential.ddpg import ActorNetwork, CriticNetwork, DDPG_Learner
from ..learning.sequential.replay_buffer import ReplayBuffer
from ..learning.sequential.qlearn import QLearn
from ..run.MORLEnvironment import MORLEnvironment
import numpy as np
import gym
import pandas as p
import tensorflow as tf


class PendulumConfig(MORLEnvironment):
    def __init__(self, learner=None):
        self.env = gym.make("Pendulum-v0")
        self.states_list = []
        learn = learner
        if learner is None:
            learn = QLearn({}, 0, 0, 0, lambda x: x[1])
        self.learner_obj = learn
        super(PendulumConfig, self).__init__(learner_klass=DDPG_Learner, n_learners=3)

    def step(self, action):
        obs, rew, done, _ = self.env.step(action)
        return (obs, rew, done)
    
    def reset(self):
        return self.env.reset()

    def states(self):
        return self.states_list

def Run_Example():
    minibatch_size = 64
    pc = PendulumConfig()

    rand_seed = 1234

    env = pc.env

    np.random.seed(rand_seed)
    tf.set_random_seed(rand_seed)
    env.seed(rand_seed)
    
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.shape[0]
    action_bound = env.action_space.high

    with tf.Session() as sess:
        assert (env.action_space.high == -env.action_space.low)

        actor = ActorNetwork(sess=sess, state_dim=state_dim, action_dim=action_dim, 
                             action_bound=action_bound, learning_rate=0.0001, tau=0.001, 
                             batch_size=minibatch_size)
        critic = CriticNetwork(sess=sess, state_dim=state_dim, action_dim=action_dim, 
                             learning_rate=0.001, tau=0.001, gamma=0.99, 
                             num_actor_vars=actor.get_num_trainable_vars())
        
        sess.run(tf.global_variables_initializer())

        actor.update_target_network()
        critic.update_target_network()

        # Initialize replay memory
        replay_buffer = ReplayBuffer(1000000, rand_seed)

        ddpg_learner = DDPG_Learner(actions=env.action_space, epsilon=1,alpha=0.001,gamma=0.99,
                                    reward_function=lambda x: x[1], actor=actor, 
                                    critic=critic, buffer=replay_buffer, 
                                    action_dim=action_dim, minibatch_size=minibatch_size)
        pc.learner_obj = ddpg_learner
        pc.run(num_epochs=50000, num_tests=10, test_length=1000)

