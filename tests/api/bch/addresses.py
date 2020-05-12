import unittest

from cryptoapi import Client

from ..config import client_api_key, bch_address, bch_status, mainnet


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = bch_address
        self.status = bch_status

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.bch.addresses
        else:
            self.client = self.client.api.bch.testnet.addresses

    def test_get_outputs_by_addresses(self):
        outputs = self.client.get_outputs_by_addresses([self.address], self.status)
        self.assertNotIn('errors', outputs)

    def test_get_utxo_coin_addresses_info(self):
        utxo_coin_addresses_info = self.client.get_utxo_coin_addresses_info([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_info)

    def test_get_utxo_coin_addresses_history(self):
        utxo_coin_addresses_history = self.client.get_utxo_coin_addresses_history([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_history)
