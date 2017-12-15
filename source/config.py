import os

class Config:
    SPARK_MASTER = os.environ.get('SPARK_MASTER', 'local')
    SPARK_APP_NAME = os.environ.get('SPARK_APP_NAME', 'morl')