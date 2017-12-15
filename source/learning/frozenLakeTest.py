import gym
from qlearn_sars import QLearn
import re
import matplotlib.pyplot as plt
import math

#LEFT = 0
#DOWN = 1
#RIGHT = 2
#UP = 3

env = gym.make('FrozenLake-v0')
eps = 1.0
gam = 0.95
space = env.action_space
acts = range(space.n)
num_epochs = 2000
num_tests = 99
epoch_only_rewards = []

reward_per_epoch = []

prev_reward = 0

q = QLearn(acts, epsilon=eps, alpha=0.8, gamma=gam)
for epoch in range(num_epochs):
    
    epoch_reward = 0
    
    prev_observation = env.reset()
    
    this_reward = 0
    #env.render()
    
    q.epsilon = max(1 / (epoch + 1), 0.001)
    #q.alpha = 1 / (epoch + 1)
    # Learning 
    for t in range(99):
    
        action = q.chooseAction(prev_observation)
        
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
            
    
    # Testing
    q.epsilon = 0.00
    for i in range(num_tests):
        prev_observation = env.reset()
        for t in range(100):
            action = q.chooseAction(prev_observation)
            
            observation, reward, done, info = env.step(action)
            
            epoch_reward += reward
            
            sars = (prev_observation, action, reward, observation)
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
                
                
    print("Epoch {} finished, total reward: {}".format(epoch+1, epoch_reward))
    
    reward_per_epoch.append(epoch_reward/num_tests)    
    
    #print q.q  
    
       

plt.plot(range(num_epochs), reward_per_epoch)
plt.show()

print sum(reward_per_epoch) / num_epochs
print sum(epoch_only_rewards) / num_epochs
        
s = range(16)
aa = range(4)
a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
pa = {('1','a'): {'a': 1, 'b': 0},('1','b'): {'a': 0, 'b': 1},('2','c'): {'c': 1, 'd': 0},('2','d'): {'c': 0, 'd': 1},('3','e'): {'e': 1, 'f': 0}, ('3','f'): {'e': 0, 'f': 1}}
dest = {('1','a'): '2',('1','b'): '3',('2','c'): '1',('2','d'): '3',('3','e'): '1', ('3','f'): '3'}
df = 0.9
r = {'1': -5,'2': 0,'3': 5}
stop = 0.1

