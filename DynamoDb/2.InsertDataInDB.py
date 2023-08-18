import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


#Insert using AWS resource
def put_item():

    db = boto3.client('dynamodb',verify=False)

    response = db.put_item (
        TableName = 'BookStore',
        Item =  {
            'Year' : {
                'N' : '2022'
            },
            'BookTitle' : {
                'S' : 'Rich Dad Poor Dad'
            }
        }
    )

    status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')
    if status == 200:
        print('Item added successfully')

put_item()

#Insert multiple items using batch Profile

Items_to_add = [
    {'Year': 2023,'BookTitle':'Ikigai'},
    {'Year': 2024,'BookTitle':'Plam Tree'},
    {'Year': 2025,'BookTitle':'Mangroove'}
]


def batch_write():
    dynamo = boto3.resource('dynamodb',verify=False)

    table = dynamo.Table('BookStore')

    with table.batch_writer() as batch:
        for item in Items_to_add:
            batch.put_item(Item = item)
        

batch_write()