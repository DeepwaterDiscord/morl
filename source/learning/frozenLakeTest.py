import gym
from vmayoral_qlearn import QLearn
import re
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')
space = env.action_space
acts = range(space.n)
num_epochs = 2000
num_tests = 200

reward_per_epoch = []

q = QLearn(acts, epsilon=0, alpha=0.9, gamma=0.9)
for epoch in range(num_epochs):
    
    epoch_reward = 0
    
    prev_observation = env.reset()
    #env.render()
    
    # Learning 
    for t in range(100):
    
        action = q.chooseAction(prev_observation)
        
        observation, reward, done, info = env.step(action)
        
        epoch_reward += reward
        
        sars = (prev_observation, action, reward, observation)
        
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
            
    # Testing
    for i in range(num_tests):
        for t in range(100):
    
        action = q.chooseAction(prev_observation)
        
        observation, reward, done, info = env.step(action)
        
        epoch_reward += reward
        
        sars = (prev_observation, action, reward, observation)
        
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
                
                
    print("Epoch {} finished".format(epoch+1))
    avg_reward = epoch_reward / (epoch + 1)
    
    reward_per_epoch.append(avg_reward)      
       

plt.plot(range(num_epochs), reward_per_epoch)
plt.show()
        
s = range(16)
aa = range(4)
a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
pa = {('1','a'): {'a': 1, 'b': 0},('1','b'): {'a': 0, 'b': 1},('2','c'): {'c': 1, 'd': 0},('2','d'): {'c': 0, 'd': 1},('3','e'): {'e': 1, 'f': 0}, ('3','f'): {'e': 0, 'f': 1}}
dest = {('1','a'): '2',('1','b'): '3',('2','c'): '1',('2','d'): '3',('3','e'): '1', ('3','f'): '3'}
df = 0.9
r = {'1': -5,'2': 0,'3': 5}
stop = 0.1

