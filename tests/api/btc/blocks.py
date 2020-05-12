import unittest

from cryptoapi import Client

from ..config import btc_block_number, client_api_key, mainnet


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = btc_block_number

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.btc.blocks
        else:
            self.client = self.client.api.btc.testnet.blocks

    def test_get_block(self):
        block_by_number = self.client.get_block(self.block_number)
        self.assertNotIn('errors', block_by_number)

        block_hash = block_by_number['hash']

        block_by_hash = self.client.get_block(block_hash)
        self.assertEqual(block_by_number, block_by_hash)

    def test_get_blocks(self):
        blocks = self.client.get_blocks()
        self.assertNotIn('errors', blocks)
