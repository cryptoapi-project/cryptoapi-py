import unittest

from cryptoapi import Client

from ..config import client_api_key, eth_block_number, eth_limit, mainnet


class BlocksTestCase(unittest.TestCase):

    def setUp(self):
        self.block_number = eth_block_number
        self.limit = eth_limit

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.eth.blocks
        else:
            self.client = self.client.api.eth.testnet.blocks

    def test_get_block(self):
        block_by_num = self.client.get_block(self.block_number)
        self.assertNotIn('errors', block_by_num)

        block_hash = block_by_num['hash']

        block_by_hash = self.client.get_block(block_hash)
        self.assertEqual(block_by_num, block_by_hash)

    def test_get_blocks(self):
        response = self.client.get_blocks(limit=self.limit)
        self.assertNotIn('errors', response)
