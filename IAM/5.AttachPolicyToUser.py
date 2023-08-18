import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError

iam = boto3.client('iam',verify=False)


def attach_policy(policy_arn, username):
    
    try : 
        response = iam.attach_user_policy(
            UserName = username,
            PolicyArn = policy_arn
        )

        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')
        if status == 200:
            print('Policy attached successfully')
    
    except ClientError as ErrorName:
        print(ErrorName)


def detach_policy(policy_arn,username):
    try:
        response = iam.detach_user_policy(
            UserName = username,
            PolicyArn = policy_arn
        )
        
        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')
        if status == 200:
            print('Policy detached successfully')

    except ClientError as ErrorName:
        print(ErrorName)


attach_policy('arn:aws:iam::907360357323:policy/PyFullAccessCustomPolicy','developer')
attach_policy('arn:aws:iam::907360357323:policy/service-role/AWSLambdaBasicExecutionRole-b5ab4458-8559-47b8-9fbe-18f187c323bf','developer')
detach_policy('arn:aws:iam::907360357323:policy/service-role/AWSLambdaBasicExecutionRole-b5ab4458-8559-47b8-9fbe-18f187c323bf','developer')