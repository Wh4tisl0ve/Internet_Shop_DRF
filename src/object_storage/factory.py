from .s3_service import S3Service
from .client import create_s3_client


class S3ServiceFactory:
    def __init__(self, endpoint_url: str, access_key: str, secret_key: str) -> None:
        self.endpoint_url = endpoint_url
        self.access_key = access_key
        self.secret_key = secret_key

    def create_service(self, bucket_name: str) -> S3Service:
        client = create_s3_client(self.endpoint_url, self.access_key, self.secret_key)

        return S3Service(bucket_name, client)
