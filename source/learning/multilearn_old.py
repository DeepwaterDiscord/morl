import numpy as np

def expected_utility(utility, actions, state, prob_actions, destinations, choice):
    """ expected_utility returns the utility of the next state given the probability of actions """
    # utility - Dictionary of Key: (state, action), Value: Real Number utility
    # actions - Dictionary of Key: (state), Value: List of actions
    # state - List of states
    # prob_actions - Dictionary of Key: (state, action), Value: 0-1
    # destinations - Dictionary of Key: (state, action), Value: destination_state
    # choice - chosen action
    # return prob_choice * util
    return sum([utility[(destinations[(state, act)], act)] * prob_actions[(state, choice)][act] \
                    for act in actions[state]])

def multilearn(states, all_actions, actions, prob_actions, destinations, discount, rewardslist, stop, learning_rate = 0.9, max_iter = 10000, debug = False):
    """ multilearn chooses a multipolicy based on multiple utilities from the various reward functions """
    # states - List of states
    # all_actions - List of actions
    # actions - Dictionary of Key: (state), Value: List of actions
    # prob_actions - Dictionary of Key: (state, action), Value: Dictionary of Key: (action), Value: 0-1
    # destinations - Dictionary of Key: (state, action), Value: destination_state
    # discount - discount factor 0-1
    # rewardslist - list of Dictionaries of Key: (state), Value: Real Number reward
    # stop - stop epsilon for utility convergence
    # max_iter - maximum number of iterations to run q-learning (in case it doesn't converge)
    # debug - Bool for showing debug statements
    
    utilities = [ qlearn_util(states, all_actions, actions, prob_actions, destinations, discount, rewards, stop, learning_rate, max_iter, debug) for rewards in rewardslist]
    
            
            
def test():
    s = ['1','2','3']
    aa = ['a','b','c','d','e','f']
    a = {'1':['a','b'], '2':['c','d'], '3':['e','f']}
    pa = {('1','a'): {'a': 1, 'b': 0},('1','b'): {'a': 0, 'b': 1},('2','c'): {'c': 1, 'd': 0},('2','d'): {'c': 0, 'd': 1},('3','e'): {'e': 1, 'f': 0}, ('3','f'): {'e': 0, 'f': 1}}
    dest = {('1','a'): '2',('1','b'): '3',('2','c'): '1',('2','d'): '3',('3','e'): '1', ('3','f'): '3'}
    df = 0.9
    r = {'1': -5,'2': 0,'3': 5}
    stop = 0.1

    u = qlearn(s, aa, a, pa, dest, df, r, stop, debug=True)

    print u