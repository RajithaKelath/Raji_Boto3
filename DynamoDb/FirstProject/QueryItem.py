import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from boto3.dynamodb.conditions import Key
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


def query_item(keyvalue):
    db = boto3.resource('dynamodb',verify=False)

    table = db.Table('Country')

    try:
        response = table.query(
            KeyConditionExpression=Key('CountryName').eq(keyvalue)
        )

    except ClientError as ErrorName:
        print(ErrorName.response['Error']['Message'])

    else:
        return response['Items']
    

if __name__=='__main__':
    updated_response =  query_item('China')
    pprint(updated_response)
