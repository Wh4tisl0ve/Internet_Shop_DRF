from io import BytesIO
from pathlib import Path
from typing import Union


class S3Service:
    def __init__(self, bucket_name: str, client) -> None:
        self.bucket_name = bucket_name
        self.client = client

    def upload_file_object(
        self, prefix: str, source_file_name: str, content: Union[str, bytes]
    ) -> None:
        destination_path = str(Path(prefix, source_file_name))

        if isinstance(content, bytes):
            buffer = BytesIO(content)
        else:
            buffer = BytesIO(content.encode("utf-8"))
        self.client.upload_fileobj(buffer, self.bucket_name, destination_path)

    def list_objects(self, prefix: str) -> list[str]:
        response = self.client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        storage_content: list[str] = []

        try:
            contents = response["Contents"]
        except KeyError:
            return storage_content

        for item in contents:
            storage_content.append(item["Key"])

        return storage_content

    def delete_file_object(self, prefix: str, source_file_name: str) -> None:
        path_to_file = str(Path(prefix, source_file_name))
        self.client.delete_object(Bucket=self.bucket_name, Key=path_to_file)
