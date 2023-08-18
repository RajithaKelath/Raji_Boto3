from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)
from botocore.exceptions import ClientError
from decimal import Decimal

import boto3
import json

def load_json(CountryData):

    try:

        db_client = boto3.resource('dynamodb',verify=False)
        table = db_client.Table('Country')

        for country in CountryData:
            name = country['name']
            code = country['code']
            rank = country['rank']
            print('Adding Items: ', name,code,rank)
            table.put_item(
                Item = {
                        'CountryName': name,
                        'PostalCode': code,
                        'Rank': rank
                        })

    except ClientError as ErrorName:
        print(ErrorName)

if __name__ == '__main__':
    with open('C:/Users/rajir/Python/Udemy/Python sample programs/Boto3/DynamoDb/FirstProject/PostalCode.json',mode='r') as json_data:
        countrylist = json.load(json_data, parse_float=Decimal)
    
    print(countrylist['countries'])

    load_json(countrylist['countries'])




