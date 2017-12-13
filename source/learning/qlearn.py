import numpy as np

def expected_utility(utility, actions, state, prob_actions, destinations, choice):
    """ expected_utility returns the utility of the next state given the probability of actions """
    return sum([utility[(destinations[(state, act)], act)] * prob_actions[(state, choice)] \
                    for act in actions[state]])

def qlearn(states, actions, prob_actions, destinations, discount, rewards, stop):
    """ qlearn updates utilities until they change less than the amount specified by stop """
    # initialize to 0:
    utility = {(s, a): 0 for s in states for a in actions}
    print "Utility Start: "+str(utility)
    while True:
        # initialize delta
        delta = 0
        for state in states:
            for act in actions[state]:
                previous = utility[(state, act)]
                current = rewards[state] + float(discount) * \
                    max([expected_utility(utility, actions, state, prob_actions, destinations, choice) for choice in actions[state]])
                utility[(state, act)] = current
                print "Utility for (%s, %s) updated to %0.4f" % (state, act, utility[(state, act)])
                delta = max(delta, np.abs(previous - current))
        if delta < stop:
            return utility
        print ""
