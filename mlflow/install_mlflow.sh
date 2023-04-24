echo $TEST

echo $MYSQL_USER
echo $MYSQL_PASSWORD
echo $MYSQL_DATABASE
echo $AWS_BUCKET_NAME

mlflow server --backend-store-uri mysql+pymysql://$MYSQL_USER:$MYSQL_PASSWORD@db:3306/$MYSQL_DATABASE  --default-artifact-root s3://$AWS_BUCKET_NAME/ --artifacts-destination s3://$AWS_BUCKET_NAME/ -h 0.0.0.0

# mlflow server --backend-store-uri mysql+pymysql://$MYSQL_USER:$MYSQL_PASSWORD@db:3306/$MYSQL_DATABASE  --default-artifact-root s3://test/ --artifacts-destination s3://test/ -h 0.0.0.0