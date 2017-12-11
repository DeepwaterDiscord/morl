import numpy as np

def expected_utility(utility, actions, state, prob_actions, destinations, choice):
    """ expected_utility returns the utility of the next state given the probability of actions """
    # utility - Dictionary of Key: (state, action), Value: Real Number utility
    # actions - List of actions
    # state - List of states
    # prob_actions - Dictionary of Key: (state, action), Value: 0-1
    # destinations - Dictionary of Key: (state, action), Value: destination_state
    # choice - chosen action
    return sum([utility[(destinations[(state, act)], act)] * prob_actions[(state, choice)] \
                    for act in actions[state]])

def qlearn(states, actions, prob_actions, destinations, discount, rewards, stop, max_iter = 10000, debug = False):
    """ qlearn updates utilities until they change less than the amount specified by stop """
    # states - List of states
    # actions - List of actions
    # prob_actions - Dictionary of Key: (state, action), Value: 0-1
    # destinations - Dictionary of Key: (state, action), Value: destination_state
    # discount - discount factor 0-1
    # rewards - Dictionary of Key: (state), Value: Real Number reward
    # stop - stop epsilon for utility convergence
    # max_iter - maximum number of iterations to run q-learning (in case it doesn't converge)
    # debug - Bool for showing debug statements
    # initialize to 0:
    utility = {(s, a): 0 for s in states for a in actions}
    print "Utility Start: "+str(utility)
    num_its = 0
    while True:
        # initialize delta
        num_its += 1
        delta = 0
        for state in states:
            for act in actions[state]:
                previous = utility[(state, act)]
                current = rewards[state] + float(discount) * \
                    max([expected_utility(utility, actions, state, prob_actions, destinations, choice) for choice in actions[state]])
                utility[(state, act)] = current
                
                if (debug):
                  print "Utility for (%s, %s) updated to %0.4f" % (state, act, utility[(state, act)])
                  
                delta = max(delta, np.abs(previous - current))
        if delta < stop or num_its > max_iter:
            return utility
        print ""
