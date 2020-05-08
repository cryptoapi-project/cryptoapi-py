from .schemes import get_coins_history, get_coins_rates


class Responses:

    def __init__(self, model_wrapper):
        self.get_coins_rates = model_wrapper(get_coins_rates, True)
        self.get_coins_history = model_wrapper(get_coins_history, True)
