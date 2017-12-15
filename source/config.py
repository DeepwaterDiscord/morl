import os

class Config(object):
    SPARK_MASTER = os.environ.get('SPARK_MASTER', 'local')
    SPARK_APP_NAME = os.environ.get('SPARK_APP_NAME', 'morl')