import CommonImport
import boto3


def list_objects_client(bucketname):
     s3_client = boto3.client('s3',verify=False)
     s3_objects = s3_client.list_objects(
          Bucket = bucketname
     )

     print('Listing the objects in Bucket: \n')
     for obj in s3_objects['Contents']:
          print(obj['Key'])

#list_objects_client('boto3democlient0823')



def list_objects_resource(bucketname):
    s3_resource = boto3.resource('s3',verify=False)
    s3_bucket = s3_resource.Bucket(bucketname,)


    print('Listing the objects in Bucket: \n')
    for obj in s3_bucket.objects.all():
        print(obj.key)

list_objects_resource('files-raji-demo')