import sys
from .examples import frozenlake
from .examples import mountaincar
from .examples import frozenlake_config
from .examples import ddpg_mujoco
from .examples import dqn_mountaincar
from .examples import ddpg_pendulum
from .util import parse_args

# Main Execution:
if len(sys.argv) < 2:
    sys.stderr.write("Please specify running mode:"+
                     "\n\tfrozenlake\n\tmountaincar"+
                     "\n\tmujoco\n\tcustom"+
                     "\n\tfrozenlake_config\n\tdqn_mountaincar\n")
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
            sys.stderr.write("Unknown algorithm specification.  Please specify algorithm:"+
                             "\n\tmultilearn\n\tqlearn\n")
    elif sys.argv[1] == "mountaincar":
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
            mountaincar.run_mountain_car_multilearn(ARGUMENTS["epsilon"],
                                                    ARGUMENTS["gamma"],
                                                    ARGUMENTS["alpha"],
                                                    ARGUMENTS["reward_functions"],
                                                    ARGUMENTS["num_epochs"],
                                                    ARGUMENTS["num_tests"],
                                                    ARGUMENTS["incr_alpha"],
                                                    ARGUMENTS["show_plots"],
                                                    ARGUMENTS["plot_name_prefix"])
        elif sys.argv[2] == "qlearn":
            mountaincar.run_mountain_car_qlearn(ARGUMENTS["epsilon"],
                                                ARGUMENTS["gamma"],
                                                ARGUMENTS["alpha"],
                                                ARGUMENTS["reward_function"],
                                                ARGUMENTS["num_epochs"],
                                                ARGUMENTS["num_tests"],
                                                ARGUMENTS["incr_alpha"],
                                                ARGUMENTS["show_plots"],
                                                ARGUMENTS["plot_name_prefix"])
        else:
            sys.stderr.write("Unknown algorithm specification.  Please specify algorithm:"+
                             "\n\tmultilearn\n\tqlearn\n")
    elif sys.argv[1] == "mujoco":
        ddpg_mujoco.Run_Example()
    elif sys.argv[1] == "custom":
        sys.stderr.write("Feature Not Available: MORL mujoco is coming soon.\n"+
                         "Thank you for your patience.\n")
    elif sys.argv[1] == "frozenlake_config":
        frozenlake_config.Run_Example()
    elif sys.argv[1] == "dqn_mountaincar":
        dqn_mountaincar.Run_Example()
    elif sys.argv[1] == "ddpg_pendulum":
        ddpg_pendulum.Run_Example()
    else:
        sys.stderr.write("Feature Not Available: MORL " + sys.argv[1] +
                         " is not a known command.\n")
