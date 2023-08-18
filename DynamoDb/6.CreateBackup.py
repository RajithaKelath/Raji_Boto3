import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

def create_backup_table(tablename,backuptablename):
    db = boto3.client('dynamodb',verify = False)

    resposne = db.create_backup(
        TableName = tablename,
        BackupName = backuptablename
    )

    return resposne.get('BackupDetails',{}).get('BackupArn')


#arn = create_backup_table('BookStore','BookStoreBackup')
#print(arn)

#Delete BackupTable
def delete_backup_table(backuparn):
    dyn = boto3.client('dynamodb',verify=False)

    dyn.delete_backup(
        BackupArn = backuparn
    )

arn = 'arn:aws:dynamodb:us-east-1:907360357323:table/BookStore/backup/01691997367347-8a27bf85'
delete_backup_table(arn)

