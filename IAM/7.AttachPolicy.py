import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError 


iam = boto3.client('iam',verify=False)


def attach_policy(policy_arn, groupname):
    try:
        response = iam.attach_group_policy(
            GroupName=groupname,
            PolicyArn = policy_arn
        )

        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')

        if status == 200:
            print(f'Policy attached to User group {groupname} successfully')

    except ClientError as ErrorName:
        print(ErrorName)

def detach_policy(policy_arn, groupname):
    try:
        response = iam.detach_group_policy(
            GroupName=groupname,
            PolicyArn = policy_arn
        )

        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')

        if status == 200:
            print(f'Policy detached from User group {groupname}')

    except ClientError as ErrorName:
        print(ErrorName)


attach_policy('arn:aws:iam::aws:policy/AmazonS3FullAccess','S3Admins')
attach_policy('arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess','DynamoAdmins')
#detach_policy('arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess','DynamoAdmins')
#detach_policy('arn:aws:iam::aws:policy/AmazonS3FullAccess','S3Admins')