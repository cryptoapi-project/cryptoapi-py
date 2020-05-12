import unittest

from cryptoapi import Client

from ..config import client_api_key, klay_from, klay_data, klay_to, klay_value


class CommonTestCase(unittest.TestCase):

    def setUp(self):
        self._from = klay_from
        self.data = klay_data
        self.to = klay_to
        self.value = klay_value

        self.client = Client(client_api_key).api.klay.testnet.common

    def test_get_network_info(self):
        network_info = self.client.get_network_info()
        self.assertNotIn('errors', network_info)

    @unittest.skip("TODO: fix test")
    def test_estimate_gas(self):
        estimate_gas = self.client.estimate_gas(_from=self._from, to=self.to, data=self.data, value=self.value)
        self.assertNotIn('errors', estimate_gas)
