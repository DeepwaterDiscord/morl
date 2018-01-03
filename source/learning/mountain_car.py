import gym
from qlearn import QLearn
import re
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as p

#LEFT = 0
#DOWN = 1
#RIGHT = 2
#UP = 3

def make_state(bin_nums):
  return "(" + ",".join(map(lambda b: str(int(b)), bin_nums)) + ")"
  
print make_state([1, 2])

def convert_to_bin(val, bins):
  return np.digitize(x=[val], bins=bins)[0]
  
def get_state(observation, bin_collection):
  pos_state = convert_to_bin(observation[0], bin_collection[0])
  vel_state = convert_to_bin(observation[1], bin_collection[1])
  states = map(lambda i: convert_to_bin(observation[i], bin_collection[i]), range(env.observation_space.shape[0]))
  return make_state(states)
 
 
 

env = gym.make('MountainCar-v0')
eps = 1.0
gam = 0.85
space = env.action_space
num_bins = 1000 # 10,000 causes a memory error

pos_bins = p.cut([-1.2, 0.6], bins=num_bins, retbins=True)[1][1:-1] # Limits found in literature and in other code
vel_bins = p.cut([-0.07, 0.07], bins=num_bins, retbins=True)[1][1:-1] 

bin_col = [pos_bins, vel_bins]

print space
print env.observation_space.shape[0]
acts = range(space.n)

acts_dict = {}
for p in xrange(len(pos_bins)):
  for v in xrange(len(vel_bins)):
    acts_dict[make_state([p,v])] = acts

#print convert_to_bin(0.59, pos_bins)

  
num_epochs = 2000
num_tests = 99

for trial in range(1, 10):
    epoch_only_rewards = []

    reward_per_epoch = []

    prev_reward = 0

    alph = trial / 10.0
    print alph
    q = QLearn(acts_dict, epsilon=eps, alpha=0.5, gamma=gam, reward_function=lambda x: x[1] + abs(10*x[0][1]*x[0][1]))
    for epoch in range(num_epochs):
        epoch_reward = 0
        prev_observation = env.reset()
        this_reward = 0
        #env.render()
        #q.epsilon = max(1 / (epoch + 1), 0.001)
        # temperature for boltzmann
        #q.epsilon = max(1 / (epoch + 1), 0.01)
        q.epsilon = 1 / (epoch + 1)
        #q.alpha = 1 / (epoch + 1)
        # Learning 
        ss = get_state(prev_observation, bin_col)
        q.train(start_state=ss, environment=env, state_function=lambda results:get_state(results[0], bin_col))
        
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
        """
        # Testing
        q.epsilon = 0.00 # temperature for boltzmann
        #q.epsilon = 0.00 # epsilon for other methods
        for i in range(num_tests):
            prev_observation = env.reset()
            for t in range(100):
                s = get_state(prev_observation, bin_col)
                action = q.choose_action(s)
                
                observation, reward, done, info = env.step(action)
                
                epoch_reward += reward
                
                sars = (prev_observation, action, reward, observation)
                
                prev_observation = observation
                
                if done:
                    #print("Episode finished after {} timesteps".format(t+1))
                    break
        """
                    
          
        if (epoch % 10 == 0):          
            print("Epoch {} finished, total reward: {}".format(epoch+1, epoch_reward))
        
        reward_per_epoch.append(epoch_reward/num_tests)    
        
        #print q.q  
        
           

    """
    plt.plot(range(num_epochs), reward_per_epoch)
    #plt.show()
    plt.savefig("plot_learning_rate_{0:.1f}.png".format(alph))
    plt.cla()
    plt.clf()
    plt.close()
    """

    print sum(reward_per_epoch) / num_epochs
    print sum(epoch_only_rewards) / num_epochs
    
    break

