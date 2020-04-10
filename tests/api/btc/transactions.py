import unittest
from cryptoapi import Client
from .config import api_key, trx_hash, trx_hex

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client(api_key)

    def test_get_transactions(self):
        response = self.cli.api.btc.transactions.get_transactions(6)
        self.assertNotIn("status", response)

    def test_get_transaction_by_hash(self):
        response = self.cli.api.btc.transactions.get_transaction_by_hash(trx_hash)
        self.assertNotIn("status", response)

    def test_decode_transaction(self):
        response = self.cli.api.btc.transactions.decode_transaction(trx_hex)
        self.assertNotIn("status", response)
