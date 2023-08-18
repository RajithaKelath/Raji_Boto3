import CommonImport
import boto3


def create_mybucket(bucketname,aclaccess):
    #Create s3 resource
    s3_client = boto3.resource('s3',verify = False)

    response = s3_client.create_bucket(
        Bucket = bucketname,
        ACL = aclaccess

        #Cannot specify default location
        # CreateBucketConfiguration ={
        #     'LocationConstraint' : 'us-east-1'
        # }
    )

    CommonImport.pprint(response)


#create_mybucket('boto3demo0823','private')


def create_mybucket_client(bucketname):
    #Create s3 client
    s3_client = boto3.client('s3',verify = False)

    response = s3_client.create_bucket(
        Bucket = bucketname,
        ACL = 'private', #default
        ObjectOwnership = 'ObjectWriter'

        #Cannot specify default location
        # CreateBucketConfiguration ={
        #     'LocationConstraint' : 'us-east-1'
        # }
    )

    set_acl = s3_client.put_public_access_block(
        Bucket = bucketname,
        PublicAccessBlockConfiguration = {
            'BlockPublicAcls': False,
            'IgnorePublicAcls' : False,
            'BlockPublicPolicy' : False,
            'RestrictPublicBuckets' : False

        }    
    )

    CommonImport.pprint(set_acl)

    set_public_access = s3_client.put_bucket_acl(
        ACL='public-read',
        Bucket=bucketname
    )

    CommonImport.pprint(set_public_access)
    CommonImport.pprint(response)


create_mybucket_client('boto3democlient0823')


# s3X.create_bucket(Bucket=’my_bucket_name’,ObjectOwnership='ObjectWriter')
# s3X.put_public_access_block(Bucket=bucket_name, PublicAccessBlockConfiguration={'BlockPublicAcls': False,'IgnorePublicAcls': False,'BlockPublicPolicy': False,'RestrictPublicBuckets': False})
# s3X.put_bucket_acl(ACL='public-read-write',Bucket=’my_bucket_name’)

