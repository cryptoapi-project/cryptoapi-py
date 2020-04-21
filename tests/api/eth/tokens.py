import unittest
from cryptoapi import Client
from .config import token, client_api_key


class TokensTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.tokens

    def test_get_tokens(self):
        tokens = self.client.get_tokens()
        self.assertNotIn(
            'status',
            tokens
        )

    def test_get_token_transfers_by_token_address(self):
        token_transfers = self.client.get_token_transfers_by_token_address(
            token
        )
        self.assertNotIn(
            'status',
            token_transfers
        )

    def test_get_token_contract(self):
        token_contract = self.client.get_token_contract(
            token
        )
        self.assertNotIn(
            'status',
            token_contract
        )
