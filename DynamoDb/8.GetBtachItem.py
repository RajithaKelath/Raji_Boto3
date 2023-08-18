import BaseImports
import boto3

db = boto3.client('dynamodb',verify = False)

def get_batch_item():
    item_list = db.batch_get_item(
        RequestItems = {
            'BookStore':{
                'Keys':[
                    {
                        'Year': {'N' :'2022'},
                        'BookTitle' : {'S':'Rich Dad Poor Dad'}
                    },
                    {
                        'Year' : {'N':'2025'},
                        'BookTitle' : {'S':'Mangroove'}
                    }
                ]
            }

        }
    )

    BaseImports.pprint(item_list['Responses']['BookStore'])


#get_batch_item()



dyn = boto3.resource('dynamodb',verify = False)

def get_batch_item_resource():
    item_list = dyn.batch_get_item(
        RequestItems = {
            'BookStore':{
                'Keys':[
                    {
                        'Year': 2022,
                        'BookTitle' : 'Rich Dad Poor Dad'
                    },
                    {
                        'Year' : 2025,
                        'BookTitle' : 'Mangroove'
                    }
                ]
            }

        }
    )

    for item in item_list['Responses']['BookStore']:
        BaseImports.pprint(item)


get_batch_item_resource()