import unittest
from cryptoapi import Client
from .config import client_api_key


class CommonTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.btc.testnet.common

    def test_get_estimate_fee(self):
        estimate_fee = self.client.get_estimate_fee()
        self.assertIs(
            type(estimate_fee),
            float
        )

    def test_get_network_information(self):
        network_information = self.client.get_network_information()
        self.assertNotIn(
            'errors',
            network_information
        )
