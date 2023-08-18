import boto3
import json
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError 


def Create_Policy():

    #Create Client
    iam = boto3.client('iam',verify=False)
    
    #Create Custom policy with Allow full access on all resources
    user_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }


    #create policy
    try :
        response = iam.create_policy(
            PolicyName = "PyFullAccessCustomPolicy",
            PolicyDocument = json.dumps(user_policy)
        )
        print(response)
    except ClientError as ErrorName:
        if ErrorName.response["Error"]["Code"] == "MalformedPolicyDocument":
            print(ErrorName)
        else:
            raise ErrorName

def list_allPolicies():
    iam = boto3.client('iam',verify=False)

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope='Local'):
        for policy in response['Policies']:
            policyname = policy['PolicyName']
            arn = policy['Arn']
            print(f'PolicyName: {policyname}, Arn: {arn} ')

#Create_Policy()
list_allPolicies()