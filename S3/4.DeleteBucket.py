import CommonImport
import boto3


def delete_bucket(bucketname):

    client = boto3.client('s3',verify=False)

    try : 
        response = client.delete_bucket(Bucket=bucketname)

        status = response.get('ResponseMetadata',{}).get('HTTPStatusCode')

        if status == '200':
            print(f'Bucket {bucketname} has been deleted')

    except CommonImport.ClientError as error:
        print(error)

delete_bucket('boto3demo0823')



def delete_bucket_resource(bucketname):

    resource = boto3.resource('s3',verify=False)

    try :
        s3_bucket = resource.bucket(Bucket=bucketname)
        response = s3_bucket.delete()
        print(response)

    except CommonImport.ClientError as error:
        print(error)
