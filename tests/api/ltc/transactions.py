import unittest

from cryptoapi import Client

from ..config import client_api_key, ltc_block_number, ltc_trx_hash, ltc_trx_hex


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = ltc_block_number
        self.trx_hash = ltc_trx_hash
        self.trx_hex = ltc_trx_hex

        self.client = Client(client_api_key).api.ltc.testnet.transactions

    def test_get_transactions(self):
        trx = self.client.get_transactions(self.block_number)
        self.assertNotIn('errors', trx)

    def test_get_transaction_by_hash(self):
        trx = self.client.get_transaction_by_hash(self.trx_hash)
        self.assertNotIn('errors', trx)

    def test_decode_transaction(self):
        decode_trx = self.client.decode_transaction(self.trx_hex)
        self.assertNotIn('errors', decode_trx)

    @unittest.skip('Transfer')
    def test_send_transactions(self):
        pass
