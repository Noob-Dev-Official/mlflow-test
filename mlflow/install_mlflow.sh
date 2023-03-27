echo $TEST

mlflow server --backend-store-uri=sqlite:///mlflow-gridicity.db --default-artifact-root=s3://test_bucket --host 0.0.0.0 --port 5000