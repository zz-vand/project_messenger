from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from persistent.db.base import Base
from persistent.db.models import User, Message, Chat, Member

from config import config


DB_HOST = config.DB_HOST
DB_PORT = config.DB_PORT
DB_NAME = config.DB_NAME
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD


DATABASE_URL_ASYNC=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_SYNC=f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def async_connection() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(url=DATABASE_URL_ASYNC)
    return async_sessionmaker(bind=engine, autocommit=False, expire_on_commit=False)

def create_all() -> None:
    engine = create_engine(url=DATABASE_URL_SYNC)
    Base.metadata.create_all(engine)

def delete_all() -> None:
    engine = create_engine(url=DATABASE_URL_SYNC)

    
    Member.__table__.drop(engine)
    Message.__table__.drop(engine)
    Chat.__table__.drop(engine)
    User.__table__.drop(engine)
    




