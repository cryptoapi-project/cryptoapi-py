import unittest

from cryptoapi.api import Api

from ..config import client_api_key, eth_block_number, eth_limit, mainnet


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = eth_block_number
        self.limit = eth_limit

        self.api = Api(client_api_key).eth
        if mainnet:
            self.api = self.api.blocks
        else:
            self.api = self.api.testnet.blocks

    def test_get_block(self):
        block_by_num = self.api.get_block(self.block_number)
        self.assertNotIn('errors', block_by_num)

        block_hash = block_by_num['hash']

        block_by_hash = self.api.get_block(block_hash)
        self.assertEqual(block_by_num, block_by_hash)

    def test_get_blocks(self):
        response = self.api.get_blocks(limit=self.limit)
        self.assertNotIn('errors', response)
