import pickle
import datetime

class MORLEnvironment(object):
    def __init__(self, learner_klass, n_learners=0, epsilon_start=0.1, alpha_start=0.9, gamma_start=0.9):
        # Initialize Configuration
        self._epsilon_start = epsilon_start
        self._alpha_start = alpha_start
        self._gamma_start = gamma_start
        self.nlearners = n_learners
        self.timestamp = datetime.time()
        if learner_klass.__name__ == "MultiLearn":
            reward_functions = [lambda results: results[1][x] for x in xrange(n_learners)]
            learner_klass.__init__(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_functions)
        elif: learner_klass.__name__ == "QLearn":
            if n_learners >= 1:
                reward_function = lambda results: sum([results[1][x] for x in xrange(n_learners)])
            else:
                reward_function = lambda results: results[1]
                learner_klass.__init__(self.actions(), self.epsilon(), self.alpha(), self.gamma(), reward_function))

    name = "Generic MORL Environment"
    default_actions = [0,1]

    def step(self, action):
        # returns tuple of next_state, rewards, done
        return (self.states()[0], 0, False)

    def reset(self):
        # return start state
        return self.states()[0]
    
    def epsilon(self, epoch):
        return self._epsilon_start

    def gamma(self, epoch):
        return self._gamma_start

    def alpha(self, epoch):
        return self._alpha_start

    def states(self):
        return [0, 1, 2]

    def actions(self):
        # returns dictionary of state:[actions]
        return {s: type(self).default_actions for s in self.states()}

    def learner(self):
        return self.learner

    def run(self, num_epochs, num_tests, test_length):
    acts_dict = self.actions
    learner = self.learner
    reward_per_epoch = []
  
    for epoch in xrange(num_epochs):
        epoch_reward = 0
        prev_state = self.reset()
        
        # Learning
        learner.train(start_state=prev_state, environment=self)
        
        
        # Testing
        learner.epsilon = 0.00
        for _i in range(num_tests):
            prev_state = self.reset()
            for _t in range(test_length):
                action = learner.choose_action(prev_state)
                new_state, reward, done, _ = self.step(action)
                epoch_reward += sum(reward)
                prev_state = new_state
                
                if done:
                    break
        
        if epoch % 10 == 0:
            print("Epoch %i finished, total reward: %0.6f" 
                    % (epoch+1, epoch_reward))
                    
        reward_per_epoch.append(epoch_reward/num_tests)