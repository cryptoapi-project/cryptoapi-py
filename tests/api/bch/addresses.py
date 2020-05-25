import unittest

from cryptoapi.api import Api

from ..config import bch_address, bch_status, client_api_key, mainnet


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = bch_address
        self.status = bch_status

        self.api = Api(client_api_key).bch
        if mainnet:
            self.api = self.api.addresses
        else:
            self.api = self.api.testnet.addresses

    def test_get_outputs_by_addresses(self):
        outputs = self.api.get_outputs_by_addresses([self.address], self.status)
        self.assertNotIn('errors', outputs)

    def test_get_utxo_coin_addresses_info(self):
        utxo_coin_addresses_info = self.api.get_utxo_coin_addresses_info([self.address])
        self.assertNotIn('errors', utxo_coin_addresses_info)

    def test_get_utxo_coin_addresses_history(self):
        utxo_coin_addresses_history = self.api.get_utxo_coin_addresses_history([self.address], limit=1)
        self.assertNotIn('errors', utxo_coin_addresses_history)
