import unittest

from cryptoapi.api import Api

from .config import client_api_key, mainnet, rates_coins


class RatesTestCase(unittest.TestCase):

    def setUp(self):
        self.coins = rates_coins

        self.api = Api(client_api_key).rates
        if not mainnet:
            self.api = self.api.testnet

    def test_get_coins_history(self):
        coins_history = self.api.get_coins_history(self.coins)
        self.assertNotIn('errors', coins_history)

    def test_get_coins_rates(self):
        coins_rates = self.api.get_coins_rates(self.coins)
        self.assertNotIn('errors', coins_rates)
