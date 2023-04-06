import boto3

s3 = boto3.resource(
   's3',
   endpoint_url='http://localhost:9000',
   aws_access_key_id='adminuser',
   aws_secret_access_key='adminuser',
   aws_session_token=None,
   config=boto3.session.Config(signature_version='s3v4'),
   verify=False
)

# Print out bucket names
for bucket in s3.buckets.all():
   print(bucket.name)


s3.Bucket('bucket').upload_file(Filename='test.txt', Key='test.txt')
