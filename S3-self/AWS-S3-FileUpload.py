"""
Uploading a csv file to S3 bucket
"""

import io

import boto3
import pandas as pd

#Create key variables

AWS_S3_BUCKET = "files-raji-demo"
AWS_ACCESS_KEY_ID = "AKIA5GQXEJPF5OQ3BK5W"
AWS_SECRET_ACCESS_KEY  = "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"

#Create a s3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

#Read a csv file from local filesystem that has to be moved to s3 bucket.
df = pd.read_csv("HSUPopulation.csv")

#Now send the put_object request to write the file on s3 bucket.
with io.StringIO() as csv_buffer:
    df.to_csv(csv_buffer, index=False)

    response = s3_client.put_object(
        Bucket=AWS_S3_BUCKET, Key="HSUPopulation_boto3.csv", Body=csv_buffer.getvalue()
    )
   
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 put_object response. Status - {status}")
    else:
        print(f"Unsuccessful S3 put_object response. Status - {status}")


#lets use pandas s3fs to upload file on s3
    df.to_csv(
        f"s3://{AWS_S3_BUCKET}/HSUPopulation_s3fs.csv",
        index=False,\
        storage_options={
            "key": AWS_ACCESS_KEY_ID,
            "secret": AWS_SECRET_ACCESS_KEY,
            }
    )
