import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


#delete single item from table
def delete_item_from_db():
    db = boto3.client('dynamodb',verify=False)

    db.delete_item(
        TableName ='BookStore',
        Key = {
            'Year':{
                'N':'2025'
            }
        }
    )

delete_item_from_db()