echo $TEST

mlflow server --backend-store-uri=sqlite:///mlflow-gridicity.db --default-artifact-root=file:mlruns --host 0.0.0.0 --port 5000