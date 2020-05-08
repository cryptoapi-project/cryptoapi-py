import unittest

from cryptoapi import Client

from .config import _from, client_api_key, data, to, value


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(client_api_key).api.klay.testnet.common

    def test_get_network_info(self):
        network_info = self.client.get_network_info()
        self.assertNotIn('errors', network_info)

    @unittest.skip("TODO: fix test")
    def test_estimate_gas(self):
        estimate_gas = self.client.estimate_gas(_from=_from, to=to, data=data, value=value)
        self.assertNotIn('errors', estimate_gas)
