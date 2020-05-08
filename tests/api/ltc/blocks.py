import unittest

from cryptoapi import Client

from .config import block_number, client_api_key


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(client_api_key).api.ltc.testnet.blocks

    def test_get_block(self):
        block_by_number = self.client.get_block(block_number)
        self.assertNotIn('errors', block_by_number)

        block_hash = block_by_number['hash']

        block_by_hash = self.client.get_block(block_hash)
        self.assertEqual(block_by_number, block_by_hash)

    def test_get_blocks(self):
        blocks = self.client.get_blocks()
        self.assertNotIn('errors', blocks)
