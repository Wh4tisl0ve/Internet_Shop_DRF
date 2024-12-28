import boto3
from botocore.client import Config


def create_s3_client(endpoint: str, access_key: str, secret_key: str) -> boto3.client:
    client = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )
    return client
