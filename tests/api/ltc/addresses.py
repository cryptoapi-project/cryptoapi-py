import unittest

from cryptoapi import Client

from ..config import client_api_key, ltc_address, ltc_status


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = ltc_address
        self.status = ltc_status

        self.client = Client(client_api_key).api.ltc.testnet.addresses

    def test_get_outputs_by_addresses(self):
        outputs = self.client.get_outputs_by_addresses([self.address], self.status)
        self.assertNotIn('errors', outputs)

    def test_get_utxo_coin_addresses_info(self):
        utxo_coin_addresses_info = self.client.get_utxo_coin_addresses_info([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_info)

    def test_get_utxo_coin_addresses_history(self):
        utxo_coin_addresses_history = self.client.get_utxo_coin_addresses_history([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_history)
