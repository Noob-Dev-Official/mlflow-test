echo $TEST

# mlflow server --backend-store-uri=sqlite:///mlflow-gridicity.db --default-artifact-root=s3://test_bucket --host 0.0.0.0 --port 5000

mlflow server --backend-store-uri mysql+pymysql://$MYSQL_USER:$MYSQL_PASSWORD@db:3306/$MYSQL_DATABASE --default-artifact-root s3://$AWS_BUCKET_NAME/ --artifacts-destination s3://$AWS_BUCKET_NAME/ -h 0.0.0.0