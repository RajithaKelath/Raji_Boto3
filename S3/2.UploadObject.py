import CommonImport
import boto3

def upload_image(objectname,bucketname):
    s3_client =  boto3.client('s3',verify=False)


    with open(objectname,mode='rb') as f:
        data = f.read()

    response = s3_client.put_object(
        Bucket= bucketname,
        ACL = 'public-read',
        Key = 'image',
        Body = data
    )

    CommonImport.pprint(response)


upload_image('C:/Users/rajir/Python/Udemy/Python sample programs/Boto3/S3/Rajitha.png','boto3democlient0823')