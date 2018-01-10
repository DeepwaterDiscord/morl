import copy

def parse_args(remaining_args, default=None):
    """
        Parses command line arguments and fills out a dictionary,
        overriding defaults when necessary
    """
    if not default:
        default = {}

    arguments = copy.deepcopy(default)
    for arg in remaining_args:
        key, value = arg.split("=")
        arguments[key] = value
    return arguments
