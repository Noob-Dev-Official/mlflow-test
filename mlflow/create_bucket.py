import random

import mlflow

import config


# mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)
mlflow.set_tracking_uri('http://localhost:3000')


s3_bucket = "s3://bucket"  # replace this value
mlflow.create_experiment(f'hello{random.randint(0, 40)}', s3_bucket)