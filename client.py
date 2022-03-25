import boto3

client = boto3.client('s3')

response = client.list_objects(Bucket = 'avillarreal-sagemaker')

for content in response['Contents']:
    obj_dict = client.get_object(Bucket = 'avillarreal-sagemaker', Key = content['Key'])
    print(content['Key'], obj_dict['LastModified'])