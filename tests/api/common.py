import unittest

from cryptoapi import Client

from .config import client_api_key, mainnet


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api
        else:
            self.client = self.client.api.testnet

    def test_get_coins(self):
        coins = self.client.get_coins()
        self.assertNotIn('errors', coins)
