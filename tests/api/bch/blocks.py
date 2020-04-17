import unittest
from cryptoapi import Client
from .config import block_hash, block_height, client_api_key


class BlocksTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.bch.testnet.blocks

    def test_get_block(self):
        block_by_height = self.client.get_block(
            block_height
        )
        self.assertNotIn(
            'status',
            block_by_height
        )

        block_by_hash = self.client.get_block(
            block_hash
        )
        self.assertEqual(
            block_by_height,
            block_by_hash
        )

    def test_get_blocks(self):
        blocks = self.client.get_blocks()
        self.assertNotIn(
            'status',
            blocks
        )
