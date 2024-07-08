from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.websockets import WebSocket
from punq import Container

from infra.message_brokers.base import BaseMessageBroker
from logic.init import init_container

router = APIRouter(tags=['chats'])


@router.websocket('/{chat_oid}/')
async def websocket_endpoint(
        chat_oid: UUID,
        websocket: WebSocket,
        container: Container = Depends(init_container),
):
    await websocket.accept()

    message_broker: BaseMessageBroker = container.resolve(BaseMessageBroker)

    async for consumed_message in message_broker.start_consuming(topic=chat_oid):
        await websocket.send_json(consumed_message)
    await websocket.close(reason='Dolbaeb')


