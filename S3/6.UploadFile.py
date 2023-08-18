import CommonImport
import boto3


def upload_files(bucketname,file,objectname):
    if objectname is None:
        objectname = file

    s3_client = boto3.client('s3',verify=False)
    s3_client.upload_file(file, bucketname, objectname)

    print(f'File uploaded to {bucketname} bucket successfully!')

#upload_files('boto3democlient0823','C:/Users/rajir/Python/Udemy/Python sample programs/Boto3/S3/VaccineForDistribution.csv','VaccineForDistribution.csv')

#HSUPopulation

def upload_files_resource(bucketname,file,objectname):
    if objectname is None:
        objectname = file

    s3_resource = boto3.resource('s3',verify=False)
    s3_object = s3_resource.Object(bucketname,objectname)
    s3_object.upload_file(file)

    print(f'File uploaded to {bucketname} bucket successfully!')

upload_files_resource('boto3democlient0823','C:/Users/rajir/Python/Udemy/Python sample programs/Boto3/S3/HSUPopulation.csv','HSUPopulation.csv')
