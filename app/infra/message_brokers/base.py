from abc import ABC, abstractmethod
from dataclasses import dataclass

from aiokafka import AIOKafkaConsumer
from aiokafka.producer import AIOKafkaProducer


@dataclass
class BaseMessageBroker(ABC):
    producer: AIOKafkaProducer
    # consumer: AIOKafkaConsumer

    @abstractmethod
    async def send_message(self, key: str, topic: str, value: bytes):
        ...

    @abstractmethod
    async def consume(self, topic: str):
        ...
