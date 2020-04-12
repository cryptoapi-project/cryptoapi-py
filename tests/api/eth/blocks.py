import unittest
from cryptoapi import Client
from .config import block_hash, block_number, limit

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    def test_get_block(self):
        block_by_hash = self.cli.api.eth.blocks.get_block(block_hash)
        self.assertNotIn("status", block_by_hash)
        block_by_num = self.cli.api.eth.blocks.get_block(block_number)
        self.assertEqual(block_by_num, block_by_hash)

    def test_get_blocks(self):
        response = self.cli.api.eth.blocks.get_blocks(limit=limit)
        self.assertNotIn("status", response)
