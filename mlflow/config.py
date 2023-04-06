import os

MLFLOW_URL = os.getenv('MLFLOW_HOST_URL', default='http://127.0.0.1')
MLFLOW_PORT = os.getenv('MLFLOW_PORT', default=3000)
