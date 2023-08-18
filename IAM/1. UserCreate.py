import boto3
from urllib3.exceptions import InsecureRequestWarning    
from urllib3 import disable_warnings    
disable_warnings(InsecureRequestWarning)

ACCESS_KEY_ID = "AKIA5GQXEJPFVO4JRCT4"
SECRET_ACCESS_KEY  = "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"

#Create a iam user

def create_user(username):
    #Create an client
    iam = boto3.client(
        "iam",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        verify=False)
    
    response = iam.create_user(UserName=username)
    print(response)


if __name__ == '__main__':
    create_user('test')
    #create_user('Dynamouser')
