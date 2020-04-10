import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1")

    def test_get_outputs_by_addresses(self):
        response = self.cli.api.btc.addresses.get_outputs_by_addresses(["2N9Rcb3Vz5g8Do51usJ8ywJ4oCZJ2RBs469"], "unspent")
        self.assertNotIn("status", response)

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.btc.addresses.get_utxo_coin_addresses_info(["2N9Rcb3Vz5g8Do51usJ8ywJ4oCZJ2RBs469"])
        self.assertNotIn("status", response)

    def test_get_utxo_coin_addresses_history(self):
        response = self.cli.api.btc.addresses.get_utxo_coin_addresses_history(["2N9Rcb3Vz5g8Do51usJ8ywJ4oCZJ2RBs469"])
        self.assertNotIn("status", response)
