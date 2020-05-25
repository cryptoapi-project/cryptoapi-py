import unittest

from cryptoapi.api import Api

from ..config import bch_block_number, client_api_key, mainnet


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = bch_block_number

        self.api = Api(client_api_key).bch
        if mainnet:
            self.api = self.api.blocks
        else:
            self.api = self.api.testnet.blocks

    def test_get_block(self):
        block_by_number = self.api.get_block(self.block_number)
        self.assertNotIn('errors', block_by_number)

        block_hash = block_by_number['hash']

        block_by_hash = self.api.get_block(block_hash)
        self.assertEqual(block_by_number, block_by_hash)

    def test_get_blocks(self):
        blocks = self.api.get_blocks()
        self.assertNotIn('errors', blocks)
