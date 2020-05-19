from typing import Any, Callable

from .schemes import get_coins_history, get_coins_rates


class Requests:

    def __init__(self, validator: Callable) -> None:
        self.get_coins_rates: Any = validator(get_coins_rates)
        self.get_coins_history: Any = validator(get_coins_history)
