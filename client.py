# boto3 is the package to connect the aws resources with the AWS SDKs
import boto3

# select the service you want to access via the client
client = boto3.client('s3')

# list objects is an API from S3 and we are selecting the bucket that we want to apply the method
response = client.list_objects(Bucket = 'avillarreal-sagemaker')

# the ouput will be a python dictionary: we are iterating over all the files inside the bucket
for content in response['Contents']:
    obj_dict = client.get_object(Bucket = 'avillarreal-sagemaker', Key = content['Key'])
    print(content['Key'], obj_dict['LastModified'])
