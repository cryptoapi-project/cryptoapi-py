import unittest

from cryptoapi import Client

from ..config import client_api_key, eth_from, eth_data, eth_to, eth_value, mainnet


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self._from = eth_from
        self.data = eth_data
        self.to = eth_to
        self.value = eth_value

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.eth.common
        else:
            self.client = self.client.api.eth.testnet.common

    def test_get_network_info(self):
        network_info = self.client.get_network_info()
        self.assertNotIn('errors', network_info)

    def test_estimate_gas(self):
        estimate_gas = self.client.estimate_gas(_from=self._from, to=self.to, data=self.data, value=self.value)
        self.assertNotIn('errors', estimate_gas)
