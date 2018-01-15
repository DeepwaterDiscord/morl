import sys
from .examples import frozenlake
# from .examples import mountaincar
from .util import parse_args

# Main Execution:
if len(sys.argv) < 2:
    sys.stderr.write("Please specify running mode:"+
                     "\n\tfrozenlake\n\tmountaincar"+
                     "\n\tmujoco\n\tcustom\n")
else:
    if sys.argv[1] == "frozenlake":
        # Specify frozenlake defaults:
        DEFAULTS = {"epsilon": 1.0, "gamma": 0.95, "alpha": 0.4,
                    "reward_function": lambda x: x[1], # qlearn only takes 1
                    "reward_functions": (lambda x: x[1], frozenlake.punish_falls), # multilearn
                    "num_epochs": 2000, "num_tests": 99, "incr_alpha": False,
                    "show_plots": False, "plot_name_prefix": "plot_learning_rate_"}
        # Parse command line args:
        ARGUMENTS = parse_args(sys.argv[3:], DEFAULTS)

        if len(sys.argv) < 3:
            sys.stderr.write("Please specify algorithm:\n\tmultilearn\n\tqlearn\n")
        # run multilearn or qlearn with ARGUMENTS:
        elif sys.argv[2] == "multilearn":
            frozenlake.run_frozen_lake_multilearn(ARGUMENTS["epsilon"], ARGUMENTS["gamma"],
                                                  ARGUMENTS["alpha"], ARGUMENTS["reward_functions"],
                                                  ARGUMENTS["num_epochs"], ARGUMENTS["num_tests"],
                                                  ARGUMENTS["incr_alpha"], ARGUMENTS["show_plots"],
                                                  ARGUMENTS["plot_name_prefix"])
        elif sys.argv[2] == "qlearn":
            frozenlake.run_frozen_lake_qlearn(ARGUMENTS["epsilon"], ARGUMENTS["gamma"],
                                              ARGUMENTS["alpha"], ARGUMENTS["reward_function"],
                                              ARGUMENTS["num_epochs"], ARGUMENTS["num_tests"],
                                              ARGUMENTS["incr_alpha"], ARGUMENTS["show_plots"],
                                              ARGUMENTS["plot_name_prefix"])
        else:
            sys.stderr.write("Unknown algorithm specification.  Please specify algorithm:\n\tmultilearn\n\tqlearn\n")
    elif sys.argv[1] == "mountaincar":
        sys.stderr.write("")
    elif sys.argv[1] == "mujoco":
        sys.stderr.write("Feature Not Available: MORL mujoco is coming soon.\
                          Thank you for your patience.\n")
    elif sys.argv[1] == "custom":
        sys.stderr.write("Feature Not Available: MORL custom is coming soon.\
                          Thank you for your patience.\n")
    else:
        sys.stderr.write("Feature Not Available: MORL "+ sys.argv[1] + \
                            "is not a known command.\n")
