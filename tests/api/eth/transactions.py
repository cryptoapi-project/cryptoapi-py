import unittest

from cryptoapi import Client

from .config import client_api_key, trx_hash, trx_hex


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.transactions

    def test_get_transactions(self):
        trx = self.client.get_transactions()
        self.assertNotIn('errors', trx)

    def test_get_transaction_information(self):
        trx_information = self.client.get_transaction_information(trx_hash)
        self.assertNotIn('errors', trx_information)

    def test_get_transaction_receipt(self):
        trx_receipt = self.client.get_transaction_receipt(trx_hash)
        self.assertIn('contract_address', trx_receipt)

    @unittest.skip('Future')
    def test_send_transaction(self):
        pass

    def test_decode_transaction(self):
        decode_transactions = self.client.decode_transaction(trx_hex)
        self.assertNotIn('errors', decode_transactions)
