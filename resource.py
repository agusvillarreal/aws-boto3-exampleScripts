# Boto3 is a python package for using the AWS resources and connect the API using the AWS SDKs
import boto3

# Resource is the service that we are going to connect via API 
s3 = boto3.resource('s3')
# this is the bucket that we are going to use
bucket = s3.Bucket('avillarreal-sagemaker')
# the objects are available as a collection on the bucket objects
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)
    
# access the client from the resource
s3_client = boto3.resource('s3').meta.client