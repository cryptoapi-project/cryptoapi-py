from typing import Callable

from .schemes import get_coins_history, get_coins_rates


class Responses:

    def __init__(self, validator: Callable) -> None:
        self.get_coins_rates: Callable = validator(get_coins_rates, True)
        self.get_coins_history: Callable = validator(get_coins_history, True)
