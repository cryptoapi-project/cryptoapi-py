import unittest
from cryptoapi import Client
from .config import _from, to, data, value, client_api_key


class CommonTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key)

    def test_get_network_info(self):
        network_info = self.client.api.eth.testnet.common.get_network_info()
        self.assertNotIn(
            'status',
            network_info
        )

    def test_estimate_gas(self):
        estimate_gas = self.client.api.eth.testnet.common.estimate_gas(
            _from=_from,
            to=to,
            data=data,
            value=value
        )
        self.assertNotIn(
            'status',
            estimate_gas
        )
