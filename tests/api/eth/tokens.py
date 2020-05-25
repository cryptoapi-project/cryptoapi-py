import unittest

from cryptoapi.api import Api

from ..config import client_api_key, eth_token, mainnet


class TokensTestCase(unittest.TestCase):

    def setUp(self):
        self.token = eth_token

        self.api = Api(client_api_key).eth
        if mainnet:
            self.api = self.api.tokens
        else:
            self.api = self.api.testnet.tokens

    def test_get_tokens(self):
        tokens = self.api.get_tokens()
        self.assertNotIn('errors', tokens)

    def test_get_token_transfers_by_token_address(self):
        token_transfers = self.api.get_token_transfers_by_token_address(self.token)
        self.assertNotIn('errors', token_transfers)

    def test_get_token_contract(self):
        token_contract = self.api.get_token_contract(self.token)
        self.assertNotIn('errors', token_contract)
