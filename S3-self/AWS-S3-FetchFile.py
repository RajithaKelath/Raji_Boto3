"""
Fetching a csv file to S3 bucket
"""
import io
import os

import boto3
import pandas as pd

#Create key variables

AWS_S3_BUCKET = "files-raji-demo"
AWS_ACCESS_KEY_ID = "AKIA5GQXEJPFVO4JRCT4"
AWS_SECRET_ACCESS_KEY  = "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"

#Create a s3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

#lets read from s3 bucket.
response = s3_client.get_object(Bucket=AWS_S3_BUCKET, Key="HSUPopulation_boto3.csv")

status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
if status == 200:
    print(f"Successful S3 get_object response. Status - {status}")
    books_df = pd.read_csv(response.get("Body"))
    print(books_df)
else:
    print(f"Unsuccessful S3 get_object response. Status - {status}")

#lets read directly using pandas s3fs api
df = pd.read_csv(
    f"s3://{AWS_S3_BUCKET}/HSUPopulation_s3fs.csv",
    storage_options={
        "key": AWS_ACCESS_KEY_ID,
        "secret": AWS_SECRET_ACCESS_KEY,
        }
)
df.head()