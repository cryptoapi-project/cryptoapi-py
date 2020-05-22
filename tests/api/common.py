import unittest

from cryptoapi.api import Api

from .config import client_api_key, mainnet


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Api(client_api_key)
        if not mainnet:
            self.api = self.api.testnet

    def test_get_coins(self):
        coins = self.api.get_coins()
        self.assertNotIn('errors', coins)
