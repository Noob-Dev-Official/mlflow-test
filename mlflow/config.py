import os

MLFLOW_URL = os.getenv('MLFLOW_HOST_URL', default='http://localhost')
MLFLOW_PORT = os.getenv('MLFLOW_PORT', default=9000)
