from ..learning.sequential.dqn import DeepQ, Memory, DQN_Learner
from ..learning.sequential.qlearn import QLearn
from ..run.MORLEnvironment import MORLEnvironment
import numpy as np
import gym
import pandas as p

class MountainCarConfig(MORLEnvironment):
    def __init__(self, learner=None, num_bins=1000):
        self.env = gym.make("MountainCar-v0")
        pos_bins = p.cut([-1.2, 0.6], bins=num_bins, retbins=True)[1][1:-1]
        vel_bins = p.cut([-0.07, 0.07], bins=num_bins, retbins=True)[1][1:-1]

        self.states_list = [(i, j) for i in xrange(len(pos_bins)) for j in xrange(len(vel_bins))]
        learn = learner
        if learner is None:
            learn = QLearn({}, 0, 0, 0, lambda x: x[1])
        self.learner_o = learn
        super(MountainCarConfig, self).__init__(learner_klass=DQN_Learner, n_learners=1)
        
        self.bins = [pos_bins, vel_bins]
        
        
    name = "Mountain Car Environment"
    _left = 0
    _none = 1
    _right = 2
    acts = [_left, _none, _right]
    default_actions = acts

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

"""
env = gym.make('MountainCar-v0')
# env.monitor.start('/tmp/mountaincar-experiment-1', force=True)

# Exploring the new environment observations and actions:
#
# >>> import gym
# env = gym.make('MountainCar-v0')>>> env = gym.make('MountainCar-v0')
# [2016-06-19 17:37:12,780] Making new env: MountainCar-v0
# >>> print env.observation_space
# Box(2,)
# >>> print env.action_space
# Discrete(3)


epochs = 1000
steps = 100000
updateTargetNetwork = 10000
explorationRate = 1
minibatch_size = 128
learnStart = 128
learningRate = 0.00025
discountFactor = 0.99
memorySize = 1000000

last100Scores = [0] * 100
last100ScoresIndex = 0
last100Filled = False

deepQ = DeepQ(2, 3, memorySize, discountFactor, learningRate, learnStart)
# deepQ.initNetworks([30,30,30])
deepQ.initNetworks([30,30])
# deepQ.initNetworks([300,300])

stepCounter = 0

# number of reruns
for epoch in xrange(epochs):
    observation = env.reset()
    print explorationRate
    # number of timesteps
    for t in xrange(steps):
        env.render()
        qValues = deepQ.getQValues(observation)

        action = deepQ.selectAction(qValues, explorationRate)

        newObservation, reward, done, info = env.step(action)

        if (t >= 199):
            print "Failed. Time out"
            done = True
            # reward = 200            

        if done and t < 199:
            print "Sucess!"
            # reward -= 200
        deepQ.addMemory(observation, action, reward, newObservation, done)

        if stepCounter >= learnStart:
            if stepCounter <= updateTargetNetwork:
                deepQ.learnOnMiniBatch(minibatch_size, False)
            else :
                deepQ.learnOnMiniBatch(minibatch_size, True)

        observation = newObservation

        if done:
            last100Scores[last100ScoresIndex] = t
            last100ScoresIndex += 1
            if last100ScoresIndex >= 100:
                last100Filled = True
                last100ScoresIndex = 0
            if not last100Filled:
                print "Episode ",epoch," finished after {} timesteps".format(t+1)
            else :
                print "Episode ",epoch," finished after {} timesteps".format(t+1)," last 100 average: ",(sum(last100Scores)/len(last100Scores))
            break

        stepCounter += 1
        if stepCounter % updateTargetNetwork == 0:
            deepQ.updateTargetNetwork()
            print "updating target network"

    explorationRate *= 0.995
    # explorationRate -= (2.0/epochs)
    explorationRate = max (0.05, explorationRate)

# env.monitor.close()
"""