import unittest

from cryptoapi.api import Api

from ..config import client_api_key, klay_contract, klay_token


class TokensTestCase(unittest.TestCase):

    def setUp(self):
        self.contract = klay_contract
        self.token = klay_token

        self.api = Api(client_api_key).klay.testnet.tokens

    def test_get_tokens(self):
        tokens = self.api.get_tokens()
        self.assertNotIn('errors', tokens)

    def test_get_token_transfers_by_token_address(self):
        token_transfers = self.api.get_token_transfers_by_token_address(self.token)
        self.assertNotIn('errors', token_transfers)

    def test_get_token_contract(self):
        token_contract = self.api.get_token_contract(self.contract)
        self.assertNotIn('errors', token_contract)
