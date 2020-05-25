import unittest

from cryptoapi.api import Api

from ..config import client_api_key, mainnet


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Api(client_api_key).ltc
        if mainnet:
            self.api = self.api.common
        else:
            self.api = self.api.testnet.common

    def test_get_estimate_fee(self):
        estimate_fee = self.api.get_estimate_fee()
        self.assertIs(type(estimate_fee), float)

    def test_get_network_information(self):
        network_information = self.api.get_network_information()
        self.assertNotIn('errors', network_information)
