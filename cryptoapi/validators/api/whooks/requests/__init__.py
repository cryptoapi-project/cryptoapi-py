from typing import Any, Callable

from .schemes import get_hook_events


class Requests:

    def __init__(self, validator: Callable) -> None:
        self.get_hook_events: Any = validator(get_hook_events)
