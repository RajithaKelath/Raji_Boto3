import boto3
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

db = boto3.client('dynamodb',verify=False)

def describe_db_table():
    response = db.describe_table(
        TableName = 'BookStore'
    )

    pprint(response)

#describe_db_table()


def list_db_table():
    response = db.list_tables()

    pprint(response)

list_db_table()