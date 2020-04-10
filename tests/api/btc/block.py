import unittest
from cryptoapi import Client
from .config import block_hash, api_key, block_height

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client(api_key)

    def test_get_outputs_by_addresses(self):
        response_block_height = self.cli.api.btc.blocks.get_block(block_height)
        self.assertNotIn("status", response_block_height)
        response_block_hash = self.cli.api.btc.blocks.get_block(block_hash)
        self.assertEqual(response_block_height, response_block_hash)

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.btc.blocks.get_blocks()
        self.assertNotIn("status", response)
