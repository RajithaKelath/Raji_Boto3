import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

iam = boto3.client('iam',verify=False)

def add_user_to_group(username, groupname):
    response = iam.add_user_to_group(
        UserName = username,
        GroupName = groupname
    )

    print(response)
    print(f'User {username} has been added to group {groupname}')

def remove_Myuser_from_group(username,groupname):
    response = iam.remove_user_from_group(
        UserName = username,
        GroupName = groupname
    )
    print(response)

# add_user_to_group('Dynamouser','DynamoAdmins')
# add_user_to_group('S3user','S3Admins')
#add_user_to_group('test','DynamoAdmins')
remove_Myuser_from_group('test','DynamoAdmins')
