import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


def deleting_item(keyvalue):
    db = boto3.resource('dynamodb',verify=False)

    table = db.Table('Country')

    try:
        response = table.delete_item(
            Key = {
                'CountryName' : keyvalue
            }
        )

    except ClientError as ErrorName:
        print(ErrorName.response['Error']['Message'])

    else:
        return response
    

if __name__=='__main__':
    updated_response = deleting_item('Switzerland')
    pprint(updated_response)
