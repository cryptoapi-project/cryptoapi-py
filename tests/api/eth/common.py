import unittest

from cryptoapi.api import Api

from ..config import client_api_key, eth_data, eth_from, eth_to, eth_value, mainnet


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self._from = eth_from
        self.data = eth_data
        self.to = eth_to
        self.value = eth_value

        self.api = Api(client_api_key).eth
        if mainnet:
            self.api = self.api.common
        else:
            self.api = self.api.testnet.common

    def test_get_network_info(self):
        network_info = self.api.get_network_info()
        self.assertNotIn('errors', network_info)

    def test_estimate_gas(self):
        estimate_gas = self.api.estimate_gas(_from=self._from, to=self.to, data=self.data, value=self.value)
        self.assertNotIn('errors', estimate_gas)
