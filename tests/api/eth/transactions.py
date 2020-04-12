import unittest
from cryptoapi import Client
from .config import trx_hex

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    # def test_get_transactions(self):
    #     block_by_hash = self.cli.api.eth.transactions.get_transactions()
    #     self.assertNotIn("status", block_by_hash)

    # def test_get_transaction_information(self):
    #     response = self.cli.api.eth.transactions.get_transaction_information(tx_hash)
    #     self.assertNotIn("status", response)

    # def test_get_transaction_receipt(self):
    #     response = self.cli.api.eth.transactions.get_transaction_receipt(tx_hash)
    #     self.assertNotIn("status", response)

    # def test_send_transaction(self):
    #     response = self.cli.api.eth.transactions.send_transaction()
    #     self.assertNotIn("status", response)

    def test_decode_transaction(self):
        response = self.cli.api.eth.transactions.decode_transaction(trx_hex)
        self.assertNotIn("status", response)
