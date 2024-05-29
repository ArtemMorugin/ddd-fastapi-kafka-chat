from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class EventHandlersNotRegisteredException(LogicException):
    event_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчик для события {self.event_type}'


@dataclass(eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type: type

    @property
    def message(self):
        return f'Не удалось найти обработчик для комманды {self.command_type}'