import unittest

from cryptoapi import Client

from ..config import client_api_key, eth_token, mainnet


class TokensTestCase(unittest.TestCase):

    def setUp(self):
        self.token = eth_token

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.eth.tokens
        else:
            self.client = self.client.api.eth.testnet.tokens

    def test_get_tokens(self):
        tokens = self.client.get_tokens()
        self.assertNotIn('errors', tokens)

    def test_get_token_transfers_by_token_address(self):
        token_transfers = self.client.get_token_transfers_by_token_address(self.token)
        self.assertNotIn('errors', token_transfers)

    def test_get_token_contract(self):
        token_contract = self.client.get_token_contract(self.token)
        self.assertNotIn('errors', token_contract)
