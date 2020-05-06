import unittest
from cryptoapi import Client
from .config import client_api_key, trx_hash, trx_hex, block_number


class TransactionsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.ltc.testnet.transactions

    def test_get_transactions(self):
        trx = self.client.get_transactions(
            block_number
        )
        self.assertNotIn(
            'errors',
            trx
        )

    def test_get_transaction_by_hash(self):
        trx = self.client.get_transaction_by_hash(
            trx_hash
        )
        self.assertNotIn(
            'errors',
            trx
        )

    def test_decode_transaction(self):
        decode_trx = self.client.decode_transaction(
            trx_hex
        )
        self.assertNotIn(
            'errors',
            decode_trx
        )

    @unittest.skip('Future')
    def test_send_transactions(self):
        pass
