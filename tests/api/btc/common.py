import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1")

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.btc.common.get_estimate_fee()
        self.assertIs(type(response), float)

    def test_get_utxo_coin_addresses_history(self):
        response = self.cli.api.btc.common.get_network_information()
        self.assertNotIn("status", response)
