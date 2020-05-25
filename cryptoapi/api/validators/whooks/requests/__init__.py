from typing import Any

from .schemes import get_hook_events


class Requests:

    def __init__(self, utils: Any) -> None:
        self.get_hook_events: Any = utils.validator(get_hook_events)
