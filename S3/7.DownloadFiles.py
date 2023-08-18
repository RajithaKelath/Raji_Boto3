import CommonImport
import boto3

def download_file_client(bucketname,filename):
    s3_client = boto3.client('s3',verify=False)

    #S3.Client.download_file(Bucket, Key, Filename, ExtraArgs=None, Callback=None, Config=None)
    s3_client.download_file(bucketname, filename, filename)
    print('File got downloaded')


#download_file_client('boto3democlient0823','VaccineForDistribution.csv')

def download_file_resource(bucketname,filename):
    s3_resource = boto3.resource('s3',verify=False)

    #S3.Client.download_file(Bucket, Key, Filename, ExtraArgs=None, Callback=None, Config=None)
    s3_resource.meta.client.download_file(bucketname, filename, filename)
    print('File got downloaded')


download_file_resource('boto3democlient0823','VaccineForDistribution.csv')