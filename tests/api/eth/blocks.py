import unittest
from cryptoapi import Client
from .config import block_hash, block_number, limit, client_api_key


class BlocksTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key)

    def test_get_block(self):
        block_by_hash = self.client.api.eth.testnet.blocks.get_block(
            block_hash
        )
        self.assertNotIn(
            'status',
            block_by_hash
        )

        block_by_num = self.client.api.eth.testnet.blocks.get_block(
            block_number
        )
        self.assertEqual(
            block_by_num,
            block_by_hash
        )

    def test_get_blocks(self):
        response = self.client.api.eth.testnet.blocks.get_blocks(
            limit=limit
        )
        self.assertNotIn(
            'status',
            response
        )
