import BaseImports
import boto3



def scan_complete_table(tablename):
    db = boto3.client('dynamodb',verify=False)
    response = db.scan(
        TableName = tablename
    )

    for item in response['Items']:
        BaseImports.pprint(item)
                         
scan_complete_table('BookStore')
