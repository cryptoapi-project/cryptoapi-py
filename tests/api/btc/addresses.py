import unittest

from cryptoapi import Client

from ..config import client_api_key, btc_address, btc_status, mainnet


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = btc_address
        self.status = btc_status

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.btc.addresses
        else:
            self.client = self.client.api.btc.testnet.addresses

    def test_get_outputs_by_addresses(self):
        outputs = self.client.get_outputs_by_addresses([self.address], self.status)
        self.assertNotIn('errors', outputs)

    def test_get_utxo_coin_addresses_info(self):
        utxo_coin_addresses_info = self.client.get_utxo_coin_addresses_info([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_info)

    def test_get_utxo_coin_addresses_history(self):
        utxo_coin_addresses_history = self.client.get_utxo_coin_addresses_history([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_history)
