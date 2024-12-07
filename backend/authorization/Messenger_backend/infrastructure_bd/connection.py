from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession

from persistent.db import Base
'''
host: 89.111.154.221
port: 5432
username: mirkuriit
password: meow
db_name: itam_messenger
'''

host_db = "89.111.154.221"
password_db = "meow"
name_db = "itam_messenger"
user_db = "mirkuriit"
port_db = "5432"

DATABASE_URL_ASYNC=f"postgresql+asyncpg://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}"
DATABASE_URL_SYNC=f"postgresql+psycopg://{user_db}:{password_db}@{host_db}:{port_db}/{name_db}"


def async_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=DATABASE_URL_ASYNC)
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_all() -> None:
    engine = create_engine(url=DATABASE_URL_SYNC)
    Base.metadata.create_all(engine)


