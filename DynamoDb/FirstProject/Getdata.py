import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


def get_data(countryname):

    db = boto3.resource('dynamodb',verify=False)

    table = db.Table('Country')

    try:
        response = table.get_item(
            Key = {
                'CountryName' : countryname
            }
        )
    
    except ClientError as ErrorName:
        print(ErrorName.response['Error']['Message'])

    else:
        return response
    

country_list = ['China','India']

if __name__ == '__main__':
    for country in country_list:
        response_data = get_data(country)
        if response_data['Item']:
            pprint(response_data['Item'])
        else:
            print('Item not found')