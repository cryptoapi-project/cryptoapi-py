import unittest
from cryptoapi import Client
from .config import address, status, client_api_key


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.bch.testnet.addresses

    def test_get_outputs_by_addresses(self):
        outputs = self.client.get_outputs_by_addresses(
            [address],
            status
        )
        self.assertNotIn(
            'status',
            outputs
        )

    def test_get_utxo_coin_addresses_info(self):
        utxo_coin_addresses_info = self.client.get_utxo_coin_addresses_info(
            [address]
        )
        self.assertNotIn(
            'status',
            utxo_coin_addresses_info
        )

    def test_get_utxo_coin_addresses_history(self):
        utxo_coin_addresses_history = self.client.get_utxo_coin_addresses_history(
            [address]
        )
        self.assertNotIn(
            'status',
            utxo_coin_addresses_history
        )
