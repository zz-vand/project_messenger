import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    def __init__(
        self,
        aws_access_key_id,
        aws_secret_access_key,
        aws_endpoint_url,
        aws_bucket_name
    ):
        self.AWS_ACCESS_KEY = aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY = aws_secret_access_key
        self.AWS_ENDPOINT_URL = aws_endpoint_url
        self.AWS_BUCKET_NAME = aws_bucket_name

config = Config(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_bucket_name=os.getenv("AWS_BUCKET_NAME")
)



