import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


def updating_item(keyvalue, newitem):
    db = boto3.resource('dynamodb',verify=False)

    table = db.Table('Country')

    try:
        response = table.update_item(
            Key = {
                'CountryName' : keyvalue
            },
            UpdateExpression = "set PostalCode= :ps",
            ExpressionAttributeValues = {
                ":ps" : newitem
            },

            ReturnValues = 'UPDATED_NEW'
        )

    except ClientError as ErrorName:
        print(ErrorName.response['Error']['Message'])

    else:
        return response
    

if __name__=='__main__':
    updated_response = updating_item('Switzerland','SW')
    pprint(updated_response)
