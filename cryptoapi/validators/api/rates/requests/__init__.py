from typing import Callable

from .schemes import get_coins_history, get_coins_rates


class Requests:

    def __init__(self, validator: Callable) -> None:
        self.get_coins_rates: Callable = validator(get_coins_rates)
        self.get_coins_history: Callable = validator(get_coins_history)
