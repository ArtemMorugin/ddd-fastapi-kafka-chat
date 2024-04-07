from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar, Any

from domain.events.base import BaseEvent


ET = TypeVar('ET', bound=BaseEvent)
ER = TypeVar('ER', bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET]):
    def handle(self, event: ET) -> ER:
        ...
