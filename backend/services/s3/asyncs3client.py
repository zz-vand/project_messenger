from aiobotocore.session import get_session
from contextlib import asynccontextmanager
import uuid

class S3Client:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint_url: str,
        bucket_name:str 
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        """Создает подключение к S3 хранилищу."""
        async with self.session.create_client('s3', **self.config) as client:
            yield client

    async def upload_file(
        self, 
        file_path: str,
        object_name: str
    ):
        try:
            async with self.get_client() as client:
                with open(file_path, "rb") as file:
                    await client.put_object(
                        Bucket=self.bucket_name,
                        Key=object_name,
                        Body=file
                    )
        except ClientError as error:
            print(f'Error while uploading a file: {error}') 

    async def get_file(self, object_name: str, destination_path: str):
        try:
            async with self.get_client() as client:
                response = await client.get_object(
                    Bucket=self.bucket_name, Key=object_name
                )
                data = await response['Body'].read()
                with open(destination_path, 'wb') as file:
                    file.write(data)
                print(f'File {object_name} has been downloaded'
                      f'to {destination_path}')
        except ClientError as error:
            print(f'Error while downloading file: {error}')

    async def delete_file(self, object_name: str):
        """Позволяет удалить файл."""
        try:
            async with self.get_client() as client:
                await client.delete_object(
                    Bucket=self.bucket_name,
                    Key=object_name
                )
                print(f'File {object_name} has been deleted'
                      f'from {self.bucket_name}')
        except ClientError as error:
            print(f'Error while deleting file: {error}')


