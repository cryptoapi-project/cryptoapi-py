from cryptoapi.models.model import Model
from cryptoapi.models.general import get_coins_rates_request, get_coin_rates_history_request, get_coins_response,\
    get_coins_rates_response, get_coin_rates_history_response


class Models:

    def __init__(self):
        # General requests
        self.get_coins_rates_request = Model(get_coins_rates_request)
        self.get_coin_rates_history_request = Model(get_coin_rates_history_request)

        # General responses
        self.get_coins_response = Model(get_coins_response)
        self.get_coins_rates_response = Model(get_coins_rates_response)
        self.get_coin_rates_history_response = Model(get_coin_rates_history_response)

        self.eth = None
        self.btc = None
        self.bch = None
        self.klay = None
