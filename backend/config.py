import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    def __init__(
        self,
        postgres_user,
        postgres_password,
        postgres_port,
        postgres_host,
        postgres_name,
        aws_access_key_id,
        aws_secret_access_key,
        aws_endpoint_url,
        aws_bucket_name
    ):
        self.DB_PORT = postgres_port
        self.DB_HOST = postgres_host
        self.DB_NAME = postgres_name
        self.DB_USER = postgres_user
        self.DB_PASSWORD = postgres_password
        self.AWS_ACCESS_KEY = aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY = aws_secret_access_key
        self.AWS_ENDPOINT_URL = aws_endpoint_url
        self.AWS_BUCKET_NAME = aws_bucket_name

config = Config(
    postgres_user=os.getenv("DB_USER"),
    postgres_password=os.getenv("DB_PASSWORD"),
    postgres_port=os.getenv("DB_PORT"),
    postgres_host=os.getenv("DB_HOST"),
    postgres_name=os.getenv("DB_NAME"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_bucket_name=os.getenv("AWS_BUCKET_NAME")
)



