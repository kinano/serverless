import boto3
from botocore.client import Config

def download(key, bucket, local_file_name):

    client = boto3.client(
        bucket['service'],
        region_name=bucket['region'],
        config=Config(signature_version='s3v4')
    )

    client.download_file(
        Bucket=bucket['name'],
        Key=key,
        Filename=local_file_name
    )

def upload(key, bucket, local_file_name):

    client = boto3.client(
        bucket['service'],
        region_name=bucket['region'],
        config=Config(signature_version='s3v4')
    )

    client.upload_file(
        Bucket=bucket['name'],
        Key=key,
        Filename=local_file_name
    )

