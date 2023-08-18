import boto3

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError


def update_user(old_username,new_username):
    #Create an client
    iam = boto3.client('iam',
                       verify = False)

    #Update old username with new username
    try:
        response = iam.update_user(UserName=old_username, NewUserName=new_username)
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200: 
            print(f'The user name {old_username} has been updated to {new_username}!')
    except ClientError as e:
        #NoSuchEntity Exception
        if e.response["Error"]["Code"] == "NoSuchEntity":
            print(f'The user with name {old_username} cannot be found!')
        else:
            # this is not the exception we are looking for
            raise e



#update_user('developer','testuser')
update_user('testuser','developer')
