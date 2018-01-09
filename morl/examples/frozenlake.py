import matplotlib.pyplot as plt

from ..learning.sequential.qlearn import QLearn

from ..learning.sequential.multilearn import MultiLearn

import gym
#from source.config import Config

#import re

#import math

_LEFT = 0
_DOWN = 1
_RIGHT = 2
_UP = 3

ENV = gym.make('FrozenLake-v0')
ACTS_DICT = {}
ACTS = [_LEFT, _DOWN, _RIGHT, _UP]
for s in range(ENV.observation_space.n):
    ACTS_DICT[s] = ACTS

def punish_falls(reward_tuple):
    if (reward_tuple[2] and reward_tuple[1] != 1.0):
        return -10
    elif (reward_tuple[2] and reward_tuple[1] == 1.0):
        return 1.0
    else:
        return -1

def run_frozen_lake_qlearn(epsilon=1.0, gamma=0.95, alpha=0.4, 
        reward_function=lambda x: x[1], num_epochs=2000, num_tests=99, 
        increment_alpha=False, show_plots=False, plot_name_prefix="plot_learning_rate_"):
    learner = QLearn(actions=ACTS_DICT, epsilon=epsilon, alpha=alpha, gamma=gamma, reward_function=reward_function)
    run_frozen_lake(learner, num_epochs, num_tests, show_plots, plot_name_prefix, increment_alpha)

def run_frozen_lake_multilearn(epsilon=1.0, gamma=0.95, alpha=0.4, 
        reward_functions=[lambda x: x[1], punish_falls], num_epochs=2000, num_tests=99, 
        increment_alpha=False, show_plots=False, plot_name_prefix="plot_learning_rate_"):
    learner = MultiLearn(actions=ACTS_DICT, epsilon=epsilon, alpha=alpha, gamma=gamma, reward_functions=reward_functions)
    run_frozen_lake(learner, num_epochs, num_tests, show_plots, plot_name_prefix, increment_alpha)

def run_frozen_lake(qlearner, num_epochs, num_tests, increment_alpha, show_plots, plot_name_prefix):
    for trial in range(1, 10):
        epoch_only_rewards = []

        reward_per_epoch = []

        if increment_alpha == True:
            alph = trial / 10.0
        
        for epoch in range(num_epochs):
            epoch_reward = 0
            prev_observation = ENV.reset()
            
            #env.render()
            #q.epsilon = max(1 / (epoch + 1), 0.001)
            # temperature for boltzmann
            eps = max(1 / (epoch + 1), 0.01)
            qlearner.epsilon = eps
            #q.alpha = 1 / (epoch + 1)
            # Learning 
            qlearner.train(start_state=prev_observation, environment=ENV, max_iter=99)
            
            # Testing
            qlearner.epsilon = 0.00 # temperature for boltzmann
            #q.epsilon = 0.00 # epsilon for other methods
            for _i in range(num_tests):
                prev_observation = ENV.reset()
                for _t in range(100):
                    action = qlearner.choose_action(prev_observation)
                    
                    observation, reward, done, _ = ENV.step(action)
                    
                    epoch_reward += reward
                    
                    prev_observation = observation
                    
                    if done:
                        break
                        
            
            if (epoch % 10 == 0):          
                print("Epoch {} finished, total reward: {}".format(epoch+1, epoch_reward))
            
            reward_per_epoch.append(epoch_reward/num_tests)
            
            
        if show_plots:
            plt.plot(range(num_epochs), reward_per_epoch)
            #plt.show()
            plotname = plot_name_prefix + "{0:.1f}.png"
            plt.savefig(plotname.format(alph))
            plt.cla()
            plt.clf()
            plt.close()

        print sum(reward_per_epoch) / num_epochs
        print sum(epoch_only_rewards) / num_epochs
        
        break
        
"""
s = range(16)
aa = range(4)
a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
pa = {('1','a'): {'a': 1, 'b': 0},('1','b'): {'a': 0, 'b': 1},('2','c'): {'c': 1, 'd': 0},('2','d'): {'c': 0, 'd': 1},('3','e'): {'e': 1, 'f': 0}, ('3','f'): {'e': 0, 'f': 1}}
dest = {('1','a'): '2',('1','b'): '3',('2','c'): '1',('2','d'): '3',('3','e'): '1', ('3','f'): '3'}
df = 0.9
r = {'1': -5,'2': 0,'3': 5}
stop = 0.1
"""

