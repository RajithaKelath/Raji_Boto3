import CommonImport
import boto3

def filter_file_list(bucketname):

    s3_client = boto3.client('s3',verify=False)

    s3_object = s3_client.list_objects(Bucket=bucketname)

    #CommonImport.pprint(s3_object['Contents'])

    csv_obj = filter(lambda csvobj : csvobj['Key'].endswith('.csv'), s3_object['Contents'] )

    for item in csv_obj:
        print(item['Key'])

#filter_file_list('s3_resource')

def filter_with_client(bucketname):
    s3_resource = boto3.resource('s3',verify=False)

    s3_object = s3_resource.Bucket(bucketname)
    
    for obj in s3_object.objects.filter(Prefix='files-input-json/'):
        CommonImport.pprint(obj.key)

filter_with_client('files-raji-demo')