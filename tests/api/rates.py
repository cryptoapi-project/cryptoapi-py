import unittest

from cryptoapi import Client

from .config import client_api_key, mainnet, rates_coins


class RatesTestCase(unittest.TestCase):

    def setUp(self):
        self.coins = rates_coins

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.rates
        else:
            self.client = self.client.api.rates.testnet

    def test_get_coins_history(self):
        coins_history = self.client.get_coins_history(self.coins)
        self.assertNotIn('errors', coins_history)

    def test_get_coins_rates(self):
        coins_rates = self.client.get_coins_rates(self.coins)
        self.assertNotIn('errors', coins_rates)
