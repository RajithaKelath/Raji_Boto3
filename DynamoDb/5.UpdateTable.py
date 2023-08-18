import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

#In DynamoDB, you can not directly rename an existing attribute.

def update_table_db():
    db = boto3.client('dynamodb',verify=False)

    response = db.update_table(
        TableName = 'BookStore',
        BillingMode = 'PROVISIONED',
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 2,
            'WriteCapacityUnits' : 2
        }
    )

    print(response)
