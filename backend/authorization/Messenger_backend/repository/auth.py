from infrastructure_bd.connection import async_connection, create_all
from sqlalchemy import insert, select
from persistent.db import User, Member, Message, Chat
import uuid
import bcrypt
from datetime import datetime
from passlib.hash import sha256_crypt

#def hash_paasword(password: str):
    #hashed = sha256_crypt.using(rounds=5000).hash(password)  # вывод хэшированного пароля
    #print("Hashed:", hashed)  # проверка соответствия хэшированного пароля исходному
    #print("Verified:", sha256_crypt.verify(password, hashed)) 

def hash_password(password: str):
    hashed = sha256_crypt.using(rounds=5000).hash(password)  
    return hashed








class Messenger:

    def __init__(self) -> None:
        self._sessionmaker = async_connection()
        create_all()

    async def put_user(self, _user_name:str, _password:str):

        hashed_password = hash_password(_password)
        stmp = insert(User).values( username = _user_name, password = hashed_password)
        print(stmp.compile())
        

        async with self._sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()