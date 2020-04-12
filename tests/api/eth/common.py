import unittest
from cryptoapi import Client
from .config import _from, to, data, value

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    def test_get_network_info(self):
        block_by_hash = self.cli.api.eth.common.get_network_info()
        self.assertNotIn("status", block_by_hash)

    def test_estimate_gas(self):
        response = self.cli.api.eth.common.estimate_gas(_from=_from,
                                                        to=to,
                                                        data=data,
                                                        value=value)
        self.assertNotIn("status", response)
