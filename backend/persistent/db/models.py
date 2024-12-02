from sqlalchemy import Text, ForeignKey, DateTime, BigInteger, Column
from sqlalchemy.orm import relationship
from datetime import datetime
from persistent.db.base import Base
import uuid


class User(Base):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    username = Column(Text, nullable=False)
    short_username = Column(Text)
    status = Column(Text)
    photo = Column(Text) #text_link
    password = Column(Text, nullable=False) #text_hash
    created_at = Column(DateTime, nullable=False)
    coockie_token = Column(Text) #uuid 
    

    messages = relationship("Message", back_populates="user")
    members = relationship("Member", back_populates="user")

class Message(Base):
    __tablename__ = "message"
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    chat_id = Column(BigInteger, ForeignKey("chat.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="messages")
    chat = relationship("Chat", back_populates="messages")


class Chat(Base):
    __tablename__ = "chat"
    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    chat_name = Column(Text)
    photo = Column(Text) # Pohot link
    created_at = Column(DateTime, nullable=False)

    messages = relationship("Message", back_populates="chat")
    members = relationship("Member", back_populates="chat")


class Member(Base):
    __tablename__ = "member"
    id = Column(BigInteger, autoincrement=True, primary_key=True, nullable=False)
    chat_id = Column(BigInteger, ForeignKey("chat.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    added_at = Column(DateTime, nullable=False)
    role = Column(Text) # owner, admin, plain

    chat = relationship("Chat", back_populates="members")
    user = relationship("User", back_populates="members")


