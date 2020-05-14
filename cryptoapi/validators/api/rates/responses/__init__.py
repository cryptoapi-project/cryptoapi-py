from .schemes import get_coins_history, get_coins_rates


class Responses:

    def __init__(self, validator):
        self.get_coins_rates = validator(get_coins_rates, True)
        self.get_coins_history = validator(get_coins_history, True)
