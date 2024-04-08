from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(default='', alias='MONGO_DB_CONNECTION_URI')
    # mongodb_connection_uri: str = 'mongodb://mongodb:27017'
    mongodb_chat_database: str = Field(default='chat', alias='MONGODB_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='chat', alias='MONGODB_CHAT_COLLECTION')
    mongodb_messages_collection: str = Field(default='messages', alias='MONGODB_MESSAGES_COLLECTION')
