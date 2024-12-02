FROM python:3.12.7

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./s3 ./code/s3

CMD ["fastapi", "run", "./code/s3/app.py", "--port", "80"]