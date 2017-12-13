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

def qlearn_util(states, all_actions, actions, prob_actions, destinations, discount, rewards, stop, learning_rate = 0.9, debug = False, max_iter=None):
    """ qlearn_util updates utilities until they change less than the amount specified by stop """
    # states - List of states
    # all_actions - List of actions
    # actions - Dictionary of Key: (state), Value: List of actions
    # prob_actions - Dictionary of Key: (state, action), Value: Dictionary of Key: (action), Value: 0-1
    # destinations - Dictionary of Key: (state, action), Value: destination_state
    # discount - discount factor 0-1
    # rewards - Dictionary of Key: (state), Value: Real Number reward
    # stop - stop epsilon for utility convergence
    # debug - Bool for showing debug statements
    # initialize to 0:
    utility = {(s, a): 0 for s in states for a in actions[s]}
    prev_utility = {(s, a): 0 for s in states for a in actions[s]}
    if (debug):
        print "Utility Start: "+str(utility)
    num_its = 0
    while True:
        # initialize delta
        num_its += 1
        delta = 0
        for state in states:
            for act in actions[state]:
                destination = destinations[(state,act)]
                previous = prev_utility[(state, act)]
                
                
                #current = rewards[destinations[state, act]] + float(discount) * \
                #    max([expected_utility(utility, actions, state, prob_actions, destinations, choice) for choice in actions[state]])
                
                current = rewards[state] + float(discount) * \
                    max([prev_utility[destination, dest_act] for dest_act in actions[destination]])
                    
                new = (1 - learning_rate) * previous + learning_rate * current
                
                utility[(state, act)] = new
                  
                delta = max(delta, np.abs(previous - new))
                
                if (debug):
                  #print "Utility for (%s, %s) updated to %0.4f" % (state, act, utility[(state, act)])
                  print("Delta: ", delta)
                  xdsf = 0
                  
        prev_utility = utility
                  
        #print utility     
        if delta < stop:
            return utility
        if max_iter > 0 and num_its > max_iter:
            return utility

def qlearn(states, all_actions, actions, prob_actions, destinations, discount, rewards, stop, learning_rate = 0.9, debug = False, max_iter=None):
    """ qlearn returns a policy based on the utilities from qlearn_utility """
    utility = qlearn_util(states, all_actions, actions, prob_actions, destinations, discount, rewards, stop, learning_rate = 0.9, debug = False, max_iter=None)

    
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


