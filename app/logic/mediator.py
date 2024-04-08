from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from domain.events.base import BaseEvent
from logic.commands.base import CommandHandler, CT, BaseCommand, CR
from logic.events.base import EventHandler, ET, ER
from logic.exceptions.mediator import EventHandlersNotRegistered, CommandHandlersNotRegistered


@dataclass
class Mediator:
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET]]):
        self.events_map[event.__class__].append(event_handlers)

    def register_command(self, command: CT, command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.events_map[command].extend(command_handlers)

    async def publish(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        event_type = events.__class__
        handlers = self.events_map.get(events.__class__)

        if not handlers:
            raise EventHandlersNotRegistered(event_type)

        result = []

        for event in events:
            result.extend([await handler.handle(event) for handler in handlers])

        return result

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.events_map.get(command_type)
        if not handlers:
            raise CommandHandlersNotRegistered(command_type)

        return [await handler.handle(command) for handler in handlers]
