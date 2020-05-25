import unittest

from cryptoapi.api import Api

from ..config import client_api_key, ltc_block_number, ltc_trx_hash, ltc_trx_hex, mainnet


class TransactionsTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = ltc_block_number
        self.trx_hash = ltc_trx_hash
        self.trx_hex = ltc_trx_hex

        self.api = Api(client_api_key).ltc
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
