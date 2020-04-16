import unittest
from cryptoapi import Client
from .config import trx_hex, client_api_key


class TransactionsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    # def test_get_transactions(self):
    #     trx = self.client.api.eth.testnet.transactions.get_transactions()
    #     self.assertNotIn(
    #         'status',
    #         trx
    #     )

    # def test_get_transaction_information(self):
    #     trx_information = self.client.api.eth.testnet.transactions.get_transaction_information(
    #         tx_hash
    #     )
    #     self.assertNotIn(
    #         'status',
    #         trx_information
    #     )

    # def test_get_transaction_receipt(self):
    #     trx_receipt = self.client.api.eth.testnet.transactions.get_transaction_receipt(
    #         tx_hash
    #     )
    #     self.assertNotIn(
    #         'status',
    #         trx_receipt
    #     )

    # def test_send_transaction(self):
    #     send_transaction = self.client.api.eth.testnet.transactions.send_transaction()
    #     self.assertNotIn(
    #         'status',
    #         send_transaction
    #     )

    def test_decode_transaction(self):
        decode_transactions = self.client.api.eth.testnet.transactions.decode_transaction(
            trx_hex
        )
        self.assertNotIn(
            'status',
            decode_transactions
        )
