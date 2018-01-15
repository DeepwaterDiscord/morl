from ..learning.sequential.qlearn import QLearn
from ..learning.sequential.multilearn import MultiLearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
import gym
import re
import math



def make_state(bin_nums):
  return "(" + ",".join(map(lambda b: str(int(b)), bin_nums)) + ")"

def convert_to_bin(val, bins):
  return np.digitize(x=[val], bins=bins)[0]
  
def get_state(observation, bin_collection, env):
  pos_state = convert_to_bin(observation[0], bin_collection[0])
  vel_state = convert_to_bin(observation[1], bin_collection[1])
  states = map(lambda i: convert_to_bin(observation[i], bin_collection[i]), range(env.observation_space.shape[0]))
  return make_state(states)
 
 
def run_mountain_car_qlearn(epsilon=1.0, gamma=0.95, alpha=0.4,
                           reward_function=lambda x: x[1], num_epochs=2000,
                           num_tests=99, increment_alpha=False, show_plots=False,
                           plot_name_prefix="plot_learning_rate_"):
    num_bins = 1000 # 10,000 causes a memory error

    pos_bins = p.cut([-1.2, 0.6], bins=num_bins, retbins=True)[1][1:-1] # Limits found in literature and in other code
    vel_bins = p.cut([-0.07, 0.07], bins=num_bins, retbins=True)[1][1:-1] 

    bin_col = [pos_bins, vel_bins]

    _left = 0
    _none = 1
    _right = 2

    acts = [_left, _none, _right]

    env = gym.make('MountainCar-v0')
    acts_dict = {}
    for pos in xrange(len(pos_bins)):
        for vel in xrange(len(vel_bins)):
            acts_dict[make_state([pos,vel])] = acts

    learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                     reward_function=reward_function)
    run_mountain_car(learner, num_epochs, num_tests, increment_alpha, show_plots, plot_name_prefix, env, bin_col)
 
def run_mountain_car_multilearn(epsilon=1.0, gamma=0.95, alpha=0.4,
                               reward_functions=(lambda x: x[1]),
                               num_epochs=2000, num_tests=99, increment_alpha=False,
                               show_plots=False, plot_name_prefix="plot_learning_rate_"):
    num_bins = 1000 # 10,000 causes a memory error

    pos_bins = p.cut([-1.2, 0.6], bins=num_bins, retbins=True)[1][1:-1] # Limits found in literature and in other code
    vel_bins = p.cut([-0.07, 0.07], bins=num_bins, retbins=True)[1][1:-1] 

    bin_col = [pos_bins, vel_bins]

    _left = 0
    _none = 1
    _right = 2

    acts = [_left, _none, _right]

    env = gym.make('MountainCar-v0')
    acts_dict = {}
    for pos in xrange(len(pos_bins)):
        for vel in xrange(len(vel_bins)):
            acts_dict[make_state([pos,vel])] = acts

    learner = MultiLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                         reward_functions=reward_functions)
    run_mountain_car(learner, num_epochs, num_tests, increment_alpha, show_plots, plot_name_prefix, env, bin_col)

def run_mountain_car(qlearner, num_epochs, num_tests, increment_alpha, show_plots, plot_name_prefix, env, bin_col):
    for trial in range(1, 10):
        epoch_only_rewards = []

        reward_per_epoch = []

        if increment_alpha:
            alph = trial / 10.0
            
        for epoch in range(num_epochs):
            epoch_reward = 0
            prev_observation = env.reset()
            this_reward = 0
            #env.render()
            #q.epsilon = max(1 / (epoch + 1), 0.001)
            # temperature for boltzmann
            #q.epsilon = max(1 / (epoch + 1), 0.01)
            eps = max(1 / (epoch + 1), 0.01)
            qlearner.epsilon = eps
            #q.alpha = 1 / (epoch + 1)
            # Learning 
            ss = get_state(prev_observation, bin_col, env)
            qlearner.train(start_state=ss, environment=env, state_function=lambda results:get_state(results[0], bin_col, env))

            # Testing
            qlearner.epsilon = 0.00
            for _i in range(num_tests):
                prev_observation = env.reset()  
                for _t in range(200):
                    ss = get_state(prev_observation, bin_col, env)
                    action = qlearner.choose_action(ss)

                    observation, reward, done, _ = env.step(action)

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

run_mountain_car_qlearn()