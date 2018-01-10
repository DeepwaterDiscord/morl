import os

class Config(object):
    """ Config contains configuration defaults and environment
        variables to override.  It functions as a static class
        with class variables.  Don't make instances or try to
        access config variablses as member variables.
    """
    SPARK_MASTER = os.environ.get('SPARK_MASTER', 'local')
    SPARK_APP_NAME = os.environ.get('SPARK_APP_NAME', 'morl')
