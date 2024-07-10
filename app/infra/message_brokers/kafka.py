from dataclasses import dataclass, field
from typing import Callable, AsyncIterator

import orjson
from aiokafka import AIOKafkaConsumer
from aiokafka.producer import AIOKafkaProducer

from infra.message_brokers.base import BaseMessageBroker


@dataclass
class KafkaMessageBroker(BaseMessageBroker):
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    async def send_message(self, key: bytes, topic: str, value: bytes):
        await self.producer.send(topic=topic, key=key, value=value)

    async def start_consuming(self, topic: str) -> AsyncIterator[dict]:
        self.consumer.subscribe(topics=[topic])

        async for message in self.consumer:
            yield orjson.loads(message.value)


        # self.consumer.subscribe()
        #
        # self.consumer.unsubscribe()


    async def stop_consuming(self):
        self.consumer.unsubscribe()

    # async def stop_consuming(self, topic: str):
    #     return await super().stop_consuming(topic)

    async def close(self):
        await self.producer.stop()
        await self.consumer.stop()

    async def start(self):
        await self.producer.start()
        await self.consumer.start()
