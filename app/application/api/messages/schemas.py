from datetime import datetime
from typing import Iterable

from pydantic import BaseModel

from application.api.schemas import BaseQueryResponseSchema
from domain.entities.messages import Chat, Message


class CreateChatRequestSchema(BaseModel):
    title: str


class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str

    @classmethod
    def from_entity(cls, chat: Chat) -> 'CreateChatResponseSchema':
        return CreateChatResponseSchema(
            oid=chat.oid,
            title=chat.title.as_generic_type(),
        )


class CreateMessageSchema(BaseModel):
    text: str


class CreateMessageResponseSchema(BaseModel):
    oid: str
    text: str

    @classmethod
    def from_entity(cls, message: Message) -> 'CreateMessageResponseSchema':
        return cls(oid=message.oid, text=message.text.as_generic_type())


class MessageDetailSchema(BaseModel):
    oid: str
    text: str
    created_at: datetime

    @classmethod
    def from_entity(cls, message: Message) -> 'MessageDetailSchema':
        return cls(
            oid=message.oid,
            text=message.text.as_generic_type(),
            created_at=message.created_at,
        )


class ChatDetailSchema(BaseModel):
    oid: str
    title: str
    messages: list[MessageDetailSchema]
    created_at: datetime

    @classmethod
    def from_entity(cls, chat: Chat) -> 'ChatDetailSchema':
        return cls(
            oid=chat.oid,
            title=chat.title.as_generic_type(),
            messages=[MessageDetailSchema.from_entity(message) for message in chat.messages],
            created_at=chat.created_at,
        )


class GetMessagesQueryResponseSchema(BaseQueryResponseSchema):
    items: list[MessageDetailSchema]
