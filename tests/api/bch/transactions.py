import unittest

from cryptoapi.api import Api

from ..config import bch_block_number, bch_trx_hash, bch_trx_hex, client_api_key, mainnet


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = bch_block_number
        self.trx_hash = bch_trx_hash
        self.trx_hex = bch_trx_hex

        self.api = Api(client_api_key).bch
        if mainnet:
            self.api = self.api.transactions
        else:
            self.api = self.api.testnet.transactions

    def test_get_transactions(self):
        trx = self.api.get_transactions(self.block_number)
        self.assertNotIn('errors', trx)

    def test_get_transaction_by_hash(self):
        trx = self.api.get_transaction_by_hash(self.trx_hash)
        self.assertNotIn('errors', trx)

    def test_decode_transaction(self):
        decode_trx = self.api.decode_transaction(self.trx_hex)
        self.assertNotIn('errors', decode_trx)

    @unittest.skip('Transfer')
    def test_send_transactions(self):
        pass
