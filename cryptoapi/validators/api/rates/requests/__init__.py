from .schemes import get_coins_history, get_coins_rates


class Requests:

    def __init__(self, validator):
        self.get_coins_rates = validator(get_coins_rates)
        self.get_coins_history = validator(get_coins_history)
