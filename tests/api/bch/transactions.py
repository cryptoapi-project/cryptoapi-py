import unittest

from cryptoapi import Client

from ..config import bch_block_number, bch_trx_hash, bch_trx_hex, client_api_key, mainnet


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = bch_block_number
        self.trx_hash = bch_trx_hash
        self.trx_hex = bch_trx_hex

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.bch.transactions
        else:
            self.client = self.client.api.bch.testnet.transactions

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
