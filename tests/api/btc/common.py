import unittest
from cryptoapi import Client
from .config import api_key

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client(api_key)

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.btc.common.get_estimate_fee()
        self.assertIs(type(response), float)

    def test_get_utxo_coin_addresses_history(self):
        response = self.cli.api.btc.common.get_network_information()
        self.assertNotIn("status", response)
