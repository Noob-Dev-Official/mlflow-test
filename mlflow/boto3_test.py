import logging

import boto3
from botocore.exceptions import ClientError


# Print out bucket names
def upload_file():
   s3 = boto3.resource(
      's3',
      endpoint_url='http://localhost:9000',
      aws_access_key_id='adminuser',
      aws_secret_access_key='adminuser',
      aws_session_token=None,
      config=boto3.session.Config(signature_version='s3v4'),
      verify=False
   )
   
   for bucket in s3.buckets.all():
      print(bucket.name)
   
   s3.Bucket('test').upload_file(Filename='test.txt', Key='test2.txt')


upload_file()

