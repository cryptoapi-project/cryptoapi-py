from typing import Any

from .schemes import get_coins_history, get_coins_rates


class Responses:

    def __init__(self, utils: Any) -> None:
        self.get_coins_rates: Any = utils.validator(get_coins_rates, True)
        self.get_coins_history: Any = utils.validator(get_coins_history, True)
