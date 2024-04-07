from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Any


@dataclass(frozen=True)
class BaseCommand(ABC):
    ...


CT = TypeVar(name='CT', bound=BaseCommand)
CR = TypeVar(name='CR', bound=Any)

@dataclass(frozen=True)
class CommandHandler(BaseCommand, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        ...
