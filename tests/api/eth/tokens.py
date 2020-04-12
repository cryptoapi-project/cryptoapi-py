import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    def test_get_tokens(self):
        block_by_hash = self.cli.api.eth.tokens.get_tokens()
        self.assertNotIn("status", block_by_hash)

    # def test_get_token_transfers_by_token_address(self):
    #     block_by_hash = self.cli.api.eth.tokens.get_token_transfers_by_token_address([address])
    #     self.assertNotIn("status", block_by_hash)

    # def test_get_token_contract(self):
    #     block_by_hash = self.cli.api.eth.tokens.get_token_contract()
    #     self.assertNotIn("status", block_by_hash)
