import CommonImport
import boto3

s3_resource = boto3.resource('s3',verify=False)


def clean_bucket(s3_bucket):

    #delete all objects
    s3_objects = s3_bucket.objects.all()
    for item in s3_objects:
        item.delete()


def delete_bucket(bucketname):

    try:
        s3_bucket = s3_resource.Bucket(bucketname)
        s3_bucket.delete()

    except CommonImport.ClientError as error:
        if error.response['Error']['Code'] == 'BucketNotEmpty':
            clean_bucket(s3_bucket)
            print('Bucket clean up has been completed!')
            s3_bucket.delete()
        else:
            raise error
        

delete_bucket('boto3democlient0823')

    



    