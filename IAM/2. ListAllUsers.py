import boto3
from urllib3.exceptions import InsecureRequestWarning    
from urllib3 import disable_warnings    
disable_warnings(InsecureRequestWarning)


ACCESS_KEY_ID = "AKIA5GQXEJPFVO4JRCT4"
SECRET_ACCESS_KEY  = "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"

def all_users():
    #Create an client
    iam = boto3.client(
        "iam",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        verify=False)

    # Create a reusable Paginator
    paginator = iam.get_paginator('list_users')

    # Create a PageIterator from the Paginator
    for response in paginator.paginate():
        print(response)
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print(f'User Name: {username}, Arn: {Arn}')

all_users()
