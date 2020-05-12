import unittest

from cryptoapi import Client

from ..config import client_api_key, btc_block_number, btc_trx_hash, btc_trx_hex, mainnet


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = btc_block_number
        self.trx_hash = btc_trx_hash
        self.trx_hex = btc_trx_hex

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.btc.transactions
        else:
            self.client = self.client.api.btc.testnet.transactions

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
