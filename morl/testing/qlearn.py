import unittest as ut
from ..learning.sequential.qlearn import QLearn

# Test getQ function in QLearn class
class QLearn_getQ(ut.case.TestCase):
    def runTest(self):
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)
        learner.q[(1, 0)] = 3.0
        self.assertAlmostEquals(learner.getQ(0, 1), 0.0)
        self.assertAlmostEquals(learner.getQ(1, 0), 3.0)

class QLearnTest_learnQ(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)
        learner.learnQ(0, 1, 5, 5+0)
        self.assertAlmostEquals(learner.q[(0, 1)], 5.0)
        learner.learnQ(0, 1, 5, 5+1)
        self.assertAlmostEquals(learner.q[(0,1)], 5.5) # 5 + 0.5*(6 - 5) = 5.5
        
class QLearnTest_choose_action_egreedy(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.0
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)

        act = learner.choose_action_egreedy(0)
        self.assertEquals(act, None)
        learner.epsilon = 1.0
        act2 = learner.choose_action_egreedy(0)
        self.assertNotEquals(act2, None)

class QLearnTest_choose_action(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)

        act = learner.choose_action(0)
        self.assertNotEquals(act, None)
        act2, qdict = learner.choose_action(0, return_q=True)
        self.assertNotEquals(qdict, None)

class QLearnTest_learn(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)

        learner.learn(0, 1, (0, 5, False, None), 0)
        self.assertAlmostEquals(learner.getQ(0, 1), 5.0)

class QLearnTest_train(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)

        start = env.reset()
        iters = learner.train(start, env, max_iter=1)
        self.assertEquals(iters, 1)

class QLearnTest_train_step(ut.case.TestCase):
    def runTest(self):
        # Test stuff Here
        _left = 0
        _down = 1
        _right = 2
        _up = 3
        acts_dict = {}
        acts = [_left, _down, _right, _up]
        epsilon = 0.1
        alpha = 0.5
        gamma = 0.5
        env = gym.make('FrozenLake-v0')
        for state in range(env.observation_space.n):
            acts_dict[state] = acts
        learner = QLearn(actions=acts_dict, epsilon=epsilon, alpha=alpha, gamma=gamma,
                        reward_function=reward_function)

        start = env.reset()
        new_state, done = learner.train_step(start, env)
        self.assertNotEquals(new_state, None)
        self.assertFalse(done)

class QLearnSuite(ut.TestSuite):
    def __init__(self):
        super(ut.TestSuite, self)
        self.addTests((QLearn_getQ(), QLearnTest_learnQ(), QLearnTest_choose_action_egreedy(), QLearnTest_choose_action(), QLearnTest_learn(), QLearnTest_train(), QLearnTest_train_step()))