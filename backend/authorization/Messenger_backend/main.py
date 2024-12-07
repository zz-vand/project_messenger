
from fastapi import FastAPI, HTTPException, Path, status, Request
from fastapi.responses import Response
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from repository.auth import Messenger
from infrastructure_bd.connection import create_all, async_connection
from sqlalchemy import insert, select, update
from persistent.db import User, Member, Message, Chat
import uuid
import bcrypt
from datetime import datetime
from passlib.hash import sha256_crypt
from fastapi import Cookie

app = FastAPI()

def hash_password(password: str):
    hashed = sha256_crypt.using(rounds=5000).hash(password)  
    return hashed

def get_token(request: Request):
    token = request.cookies.get('users_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found')
    return token





messenger_class = Messenger()
create_all()

@app.post("/users/")
async def create_user(_user_name: str, _password: str):
    _sessionmaker = async_connection()

    stmt = select(User).filter_by(username = _user_name) 

    async with _sessionmaker() as session:
        result = await session.execute(stmt) #True or False
    result1 = result.scalar()
    if result1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="USER ALREADY EBLAN")
    # item already exists
    else:

        hashed_password = hash_password(_password)
        stmp = insert(User).values( username = _user_name, password = hashed_password)
        

        async with _sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
        return {"message: ", "Upload good"}
    


@app.get("/users/vxod")
async def get_user(_user_name: str, _password: str, response:Response):
    _sessionmaker = async_connection()
    stmt = select(User).filter_by(username = _user_name) 
    async with _sessionmaker() as session:
        result = await session.execute(stmt) #True or False
    result1 = result.scalar()
    if not(result1):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="USERA NET")
    else:
        stmt = select(User.password).filter_by(username = _user_name) 
        async with _sessionmaker() as session:
            result10 = await session.execute(stmt) #True or Fals
        result100 = result10.scalar()

        result_password = sha256_crypt.verify(_password, result100)

        if result_password:

            access_token = str(uuid.uuid4())

            response.set_cookie(key="token", value=access_token)
            stmp1 = update(User).where(User.username == _user_name).values(coockie_token = access_token)
            async with _sessionmaker() as session:
                await session.execute(stmp1)
                await session.commit()
            

            return {'access_token': response, 'refresh_token': None}
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="WRONG")


       
@app.post("/logout/")
async def logout(response: Response):
    response.delete_cookie(key="token")  # Удаляем cookie с токеном
    return {"message", "coockie was deleted"}


@app.get("/authorize/")
async def authorize(request: Request):
    token = request.cookies.get('token')
    if token == None:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = "Unauthorized")
    else:
        _sessionmaker = async_connection()
        stmp = select(User).where(User.coockie_token == token)
        async with _sessionmaker() as session:
            answer = await session.execute(stmp)
        if not answer:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        else:
            return {"message": "Authorized"}
