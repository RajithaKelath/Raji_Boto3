import BaseImports
import boto3


def get_item_from_db():

    db=boto3.client('dynamodb',verify=False)

    response = db.get_item(
        TableName = 'BookStore',
        Key = {
            'Year' : {
                'N' : '2022'
            },
            'BookTitle' : {
                'S' : 'Mangroove'
            }
        }
    )

    BaseImports.pprint(response)

get_item_from_db()



def get_item_response():
    dyn = boto3.resource('dynamodb',verify=False)

    table = dyn.Table('BookStore')

    reponse = table.get_item(
        Key = {
            'Year' : 2025,
            'BookTitle' : 'Mangroove'
        }
    )
    
    print(reponse)

get_item_response()