import os
from random import random, randint

import mlflow
from mlflow import log_metric, log_param, log_artifacts

mlflow.set_tracking_uri('http://localhost:3000')

print(mlflow.get_artifact_uri())

if __name__ == "__main__":
   mlflow.end_run()
   with mlflow.start_run() as run:
      print("Running mlflow_tracking.py")

      log_param("param1", randint(0, 100))
      
      log_metric("foo", random())
      log_metric("foo", random() + 1)
      log_metric("foo", random() + 2)

      if not os.path.exists("outputs"):
         os.makedirs("outputs")
      with open("outputs/test.txt", "w") as f:
         f.write("hello world!")

      log_artifacts("outputs")