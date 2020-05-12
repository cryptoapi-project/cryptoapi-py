import unittest

from cryptoapi import Client

from ..config import client_api_key, klay_trx_hash, klay_trx_hex


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.trx_hash = klay_trx_hash
        self.trx_hex = klay_trx_hex

        self.client = Client(client_api_key).api.klay.testnet.transactions

    def test_get_transactions(self):
        trx = self.client.get_transactions()
        self.assertNotIn('errors', trx)

    def test_get_transaction_information(self):
        trx_information = self.client.get_transaction_information(self.trx_hash)
        self.assertNotIn('errors', trx_information)

    def test_get_transaction_receipt(self):
        trx_receipt = self.client.get_transaction_receipt(self.trx_hash)
        self.assertNotIn('errors', trx_receipt)

    @unittest.skip('Transfer')
    def test_send_transaction(self):
        pass

    def test_decode_transaction(self):
        decode_transactions = self.client.decode_transaction(self.trx_hex)
        self.assertNotIn('errors', decode_transactions)
