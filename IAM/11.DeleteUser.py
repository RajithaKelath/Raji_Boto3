import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

#Create boto3 client
iam_client = boto3.client('iam',verify=False)

def delete_myuser(username):
    response = iam_client.delete_user(UserName = username)
    print(response)


delete_myuser('test')