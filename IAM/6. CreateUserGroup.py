import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError

#Create Client
iam = boto3.client('iam',verify=False)

def create_user_group(groupname):
    try:
        response = iam.create_group(GroupName = groupname)
        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')

        if status == 200:
            print('User Group created successfully')
    except ClientError as ErrorName:
        print(ErrorName)


create_user_group('S3Admins')
create_user_group('DynamoAdmins')