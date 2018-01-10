import sys
from .examples import frozenlake
from .examples import mountaincar
from .util import parse_args

# Main Execution:
if sys.argv[1] == "frozenlake":
    # Specify frozenlake defaults:
    defaults = {}
    # Parse command line args:
    arguments = parse_args(sys.argv[3:], defaults)
    
    # run multilearn or qlearn with arguments:
    if sys.argv[2] == "multilearn":
        frozenlake.run_frozen_lake_multilearn(arguments["epsilon"], arguments["gamma"],
                                              arguments["alpha"], arguments["reward_functions"],
                                              arguments["num_epochs"], arguments["num_tests"],
                                              arguments["incr_alpha"], arguments["show_plots"],
                                              arguments["plot_name_prefix"])
    elif sys.argv[2] == "qlearn":
        frozenlake.run_frozen_lake_qlearn(arguments["epsilon"], arguments["gamma"],
                                          arguments["alpha"], arguments["reward_function"],
                                          arguments["num_epochs"], arguments["num_tests"],
                                          arguments["incr_alpha"], arguments["show_plots"],
                                          arguments["plot_name_prefix"])
    else:
        print "Please specify:\"
