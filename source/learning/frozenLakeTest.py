import gym
from sequential.qlearn import QLearn

import sys
sys.path.append("../../")

from sequential.multilearn import MultiLearn

#from source.config import Config

import re
import matplotlib.pyplot as plt
import math

#LEFT = 0
#DOWN = 1
#RIGHT = 2
#UP = 3

env = gym.make('FrozenLake-v0')
menv = gym.make('FrozenLake-v0')
eps = 1.0
gam = 0.95
space = env.action_space
acts = range(space.n)
acts_dict = {}
for s in range(env.observation_space.n):
  acts_dict[s] = acts
  
def punish_falls(x):
  if (x[2] == True and x[1] != 1.0):
    return -10
  elif (x[2] == True and x[1] == 1.0):
    return 1.0
  else:
    return -1
  
num_epochs = 2000
num_tests = 99

for trial in range(1, 10):
    epoch_only_rewards = []

    reward_per_epoch = []

    prev_reward = 0

    alph = trial / 10.0
    q = QLearn(acts_dict, epsilon=eps, alpha=alph, gamma=gam, reward_function=lambda x: x[1])
    reward_funcs = [lambda x: x[1], punish_falls ]
    mq = MultiLearn(actions=acts_dict, epsilon=eps, alpha=alph, gamma=gam, reward_functions=reward_funcs)
    for epoch in range(num_epochs):
        epoch_reward = 0
        mepoch_reward = 0
        prev_observation = env.reset()
        mprev_observation = menv.reset()
        this_reward = 0
        #env.render()
        #q.epsilon = max(1 / (epoch + 1), 0.001)
        # temperature for boltzmann
        ep = max(1 / (epoch + 1), 0.01)
        q.epsilon = ep
        mq.epsilon = ep
        #q.alpha = 1 / (epoch + 1)
        # Learning 
        q.train(start_state=prev_observation, environment=env, max_iter=99)
        mq.train(start_state=prev_observation, environment=menv, max_iter=99)
        
        
        
        """
        for t in range(99):
        
            action = q.choose_action(prev_observation)
            
            observation, reward, done, info = env.step(action)
            
            #epoch_reward += reward
            
            sars = (prev_observation, action, reward, observation)
            
            this_reward += reward
            
            q.learn(prev_observation, action, reward, observation)
            #print sars #SARS aka Q-Learning
            #print("action: ", action)
            #print("observation: ", observation)
            #print("reward: ", reward)
            #print("done: ", done)
            #print("info: ", info)
            
            prev_observation = observation
            
            if done:
                #print("Episode finished after {} timesteps".format(t+1))
                break
        
        epoch_only_rewards.append(this_reward)
        """        
        
        # Testing
        q.epsilon = 0.00 # temperature for boltzmann
        mq.epsilon = 0.00
        #q.epsilon = 0.00 # epsilon for other methods
        for i in range(num_tests):
            prev_observation = env.reset()
            mprev_observation = menv.reset()
            for t in range(100):
                action = q.choose_action(prev_observation)
                maction = mq.choose_action(mprev_observation)
                
                observation, reward, done, info = env.step(action)
                mobservation, mreward, mdone, minfo = menv.step(maction)
                
                epoch_reward += reward
                mepoch_reward += mreward
                
                sars = (prev_observation, action, reward, observation)
                
                msars = (mprev_observation, maction, mreward, mobservation)
                
                prev_observation = observation
                mprev_observation = mobservation
                
                if done:
                    #print("Episode finished after {} timesteps".format(t+1))
                    break
                    
          
        if (epoch % 10 == 0):          
            print("Epoch {} finished, total reward: {}".format(epoch+1, epoch_reward))
        
        reward_per_epoch.append(epoch_reward/num_tests)    
        
        #print q.q  
        
           

    plt.plot(range(num_epochs), reward_per_epoch)
    #plt.show()
    plt.savefig("plot_learning_rate_{0:.1f}.png".format(alph))
    plt.cla()
    plt.clf()
    plt.close()

    print sum(reward_per_epoch) / num_epochs
    print sum(epoch_only_rewards) / num_epochs
    
    break
        
s = range(16)
aa = range(4)
a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
pa = {('1','a'): {'a': 1, 'b': 0},('1','b'): {'a': 0, 'b': 1},('2','c'): {'c': 1, 'd': 0},('2','d'): {'c': 0, 'd': 1},('3','e'): {'e': 1, 'f': 0}, ('3','f'): {'e': 0, 'f': 1}}
dest = {('1','a'): '2',('1','b'): '3',('2','c'): '1',('2','d'): '3',('3','e'): '1', ('3','f'): '3'}
df = 0.9
r = {'1': -5,'2': 0,'3': 5}
stop = 0.1

