from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError

import boto3


def create_Country_table():
    db_client = boto3.client('dynamodb',verify=False)
    
    try:
        response = db_client.create_table(
            TableName = 'Country',
            KeySchema = [
                {
                    'AttributeName':'CountryName',
                    'KeyType' : 'HASH'
                }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName' : 'CountryName',
                    'AttributeType' : 'S'
                }
            ],
            ProvisionedThroughput = {
                'ReadCapacityUnits' : 2,
                'WriteCapacityUnits' : 2
            }
        )

        pprint(response['TableDescription']['TableStatus'])
    
    except ClientError as Error:
        pprint(Error.response['Error']['Message'])

create_Country_table()