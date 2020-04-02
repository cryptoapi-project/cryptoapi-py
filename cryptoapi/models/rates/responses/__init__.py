from .schemes import get_coins_rates, get_coin_rates_history


class Responses:

    def __init__(self, model_wrapper):
        self.get_coins_rates = model_wrapper(get_coins_rates)
        self.get_coin_rates_history = model_wrapper(get_coin_rates_history)
