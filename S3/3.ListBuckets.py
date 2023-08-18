import CommonImport
import boto3

def list_all_buckets():
    s3_client = boto3.client('s3',verify=False)

    buckets = s3_client.list_buckets()

    print('List buckets for below user : \n')
    for bucket in buckets['Buckets']:
        CommonImport.pprint(bucket['Name'])

#list_all_buckets()


def list_buckets_resource():
    resource = boto3.resource('s3',verify=False)
    iterator = resource.buckets.all()

    print('Listing all buckets: \n')
    for bucket in iterator:
        print(bucket.name)

list_buckets_resource()