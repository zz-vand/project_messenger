from fastapi import FastAPI, File, UploadFile, Form, Body, BackgroundTasks
from fastapi.responses import FileResponse
from typing import Union, Annotated
from pydantic import BaseModel
from config import config
from asyncs3client import S3Client
import os
import uuid

app = FastAPI()

S3_URL = "http://109.120.179.220:80/itam_storage/"

s3_client = S3Client(
    access_key=config.AWS_ACCESS_KEY,
    secret_key=config.AWS_SECRET_ACCESS_KEY,
    endpoint_url=config.AWS_ENDPOINT_URL,
    bucket_name=config.AWS_BUCKET_NAME)

def _create_unique_object_name(user_id, file_name) -> str:
    object_name = ">".join([str(uuid.uuid4()), user_id, file_name])
    return object_name

class FileObject(BaseModel):
    user_id: int
    file_path: str

@app.post("/itam_storage/")
async def add_file(user_id: str = Form(...), in_file: UploadFile=File(...)):
    unique_object_name =  _create_unique_object_name(user_id, in_file.filename)
    object_link = S3_URL + unique_object_name +"/"
    out_file_path = in_file.filename

    try:
        with open(out_file_path, "wb") as out_file:
            out_file.write(await in_file.read())
        print(unique_object_name)
        await s3_client.upload_file(
            file_path=out_file_path,
            object_name=unique_object_name
        )
    except:
         ...
         ### todo нормальную обработку ошибки
    
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
            
    return {"object_source":object_link}

@app.get("/itam_storage/{unique_object_name}/")
async def get_file(unique_object_name: str, background_tasks: BackgroundTasks):
    print(unique_object_name)
    await s3_client.get_file(unique_object_name, unique_object_name)

    def remove_file(file_path: str):
        if os.path.exists(file_path):
            os.remove(file_path)

    background_tasks.add_task(remove_file, unique_object_name)

    return FileResponse(unique_object_name)
