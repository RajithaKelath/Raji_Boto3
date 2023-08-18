import CommonImport
import boto3


def copy_object(src_bucket,src_key,des_bucket,des_key):
    s3_client = boto3.client('s3',verify=False)

    #S3.Client.copy(CopySource, Bucket, Key, ExtraArgs=None, Callback=None, SourceClient=None, Config=None)
    copy_source = {
        'Bucket': src_bucket,
        'Key' : src_key
    }
    s3_client.copy_object(
        CopySource = copy_source,
        Bucket = des_bucket,
        Key = des_key)
    print(f'Object has been copied from {src_bucket} tp {des_bucket}')


copy_object('files-raji-demo','Employee.json','boto3democlient0823','employee.json')

