import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

iam = boto3.client('iam',verify=False)

def create_access_key(username):
    response = iam.create_access_key(UserName=username)
    access_key_id = response.get('AccessKey',{}).get('AccessKeyId')
    secret_access_key = response.get('AccessKey',{}).get('SecretAccessKey')
    status = response.get('AccessKey',{}).get('Status')
    print(f'Access_Key_Id: {access_key_id}, Secret_Access_Key: {secret_access_key}, Status: {status}')


def update_access_key(username,accesskeyid,status):
    iam.update_access_key(
        AccessKeyId = accesskeyid,
        Status = status,
        UserName = username
    )


def delete_myaccess_key(username,accesskeyid):
    response = iam.delete_access_key(
        UserName = username,
        AccessKeyId = accesskeyid
    )

    print(response)

#create_access_key('test')
#update_access_key('Dynamouser','AKIA5GQXEJPF5YKIVFG2','Active')
delete_myaccess_key('test','AKIA5GQXEJPFUFFRA5GK')