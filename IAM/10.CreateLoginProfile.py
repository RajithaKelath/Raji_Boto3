import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

iam = boto3.client('iam',verify=False)

def create_profile(username,password):
    login_response = iam.create_login_profile(
        UserName = username,
        Password = password,
        PasswordResetRequired = False
        )
        
    print(login_response)

def delete_profile(username):
    delete_response = iam.delete_login_profile(
        UserName = username
        )
        
    print(delete_response)


#create_profile('test','Mypassword@123')
delete_profile('test')