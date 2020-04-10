import unittest
from cryptoapi import Client
from .config import address, status, api_key

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client(api_key)

    def test_get_outputs_by_addresses(self):
        response = self.cli.api.bch.addresses.get_outputs_by_addresses([address], status)
        self.assertNotIn("status", response)

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.bch.addresses.get_utxo_coin_addresses_info([address])
        self.assertNotIn("status", response)

    def test_get_utxo_coin_addresses_history(self):
        response = self.cli.api.bch.addresses.get_utxo_coin_addresses_history([address], limit=1)
        self.assertNotIn("status", response)
