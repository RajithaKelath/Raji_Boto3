import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

dynamodb_client = boto3.client('dynamodb',verify=False)

def create_table_in_db():

    table_creation = dynamodb_client.create_table(
        #The name of the table to create
        TableName = 'BookStore',
        # 'KeySchema' Specifies the attributes that make up the primary key for a table or an index
        # Each KeySchemaElement in the array is composed of:

        # AttributeName - The name of this key attribute.

        # KeyType - The role that the key attribute will assume:

        # HASH - partition key

        # RANGE - sort key
        KeySchema = [
            {
                'AttributeName': 'Year',
                'KeyType' : 'HASH'  #Partition Key
            },
            {
                'AttributeName' : 'BookTitle',
                'KeyType' : 'RANGE' #sort key
            }
        ],
        #'AttributeDefinitions' An array of attributes that describe the key schema for the table and indexes.
        #AttributeName - A name for the attribute
        #AttributeType - The data type for the attribute, S|N|B - String | Number | Binary
        AttributeDefinitions = [
            {
                'AttributeName' : 'Year',
                'AttributeType' : 'N'
            },
            {
                'AttributeName' : 'BookTitle',
                'AttributeType' : 'S'
            }
        ],
        #For current minimum and maximum provisioned throughput values
        #RCU - The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException
        #WCU - The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException
        ProvisionedThroughput = {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits' : 1
        }
    )

    print(table_creation)


create_table_in_db()