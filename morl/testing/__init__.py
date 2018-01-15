from . import dqlearn, genetic, multilearn, multilearnp, qlearn

def run(debug=False):
    qlearn.QLearnSuite().run(debug=debug)