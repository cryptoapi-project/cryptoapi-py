import unittest

from cryptoapi import Client

from .config import block_number, client_api_key, limit


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.blocks

    def test_get_block(self):
        block_by_num = self.client.get_block(block_number)
        self.assertNotIn('errors', block_by_num)

        block_hash = block_by_num['hash']

        block_by_hash = self.client.get_block(block_hash)
        self.assertEqual(block_by_num, block_by_hash)

    def test_get_blocks(self):
        response = self.client.get_blocks(limit=limit)
        self.assertNotIn('errors', response)
