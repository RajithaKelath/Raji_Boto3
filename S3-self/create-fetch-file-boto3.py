import logging
import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name,region=None):
    """
    Create S3 bucket in a specified region
    
    If region is not specified, create in a S3 default region(us-east-1)

    :param bucket_name: Bucket to create
    :param region: region where bucket need to be created
    :return : True if bucket is created else false
    """
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name) 
        else:
            s3_client = boto3.client('s3', region_name = region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration = location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

#create_s3_bucket("raji-demo-bucket-boto3-again")

    """List the existing bucket list of the user
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """

#Create key variables

AWS_S3_BUCKET = "raji-demo-bucket-boto3"
AWS_ACCESS_KEY_ID = "AKIA5GQXEJPF5OQ3BK5W"
AWS_SECRET_ACCESS_KEY  = "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"

#Create a s3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

response = s3.get_object(Bucket=AWS_S3_BUCKET,Key=)

print(response)
# print('Existing Files:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')
