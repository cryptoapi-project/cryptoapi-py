import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1")

    def test_get_outputs_by_addresses(self):
        response_block_height = self.cli.api.btc.blocks.get_block(6)
        self.assertNotIn("status", response_block_height)
        response_block_hash = self.cli.api.btc.blocks.get_block("000000006633685edce4fa4d8f12d001781c6849837d1632c4e2dd6ff2090a7b")
        self.assertEqual(response_block_height, response_block_hash)

    def test_get_utxo_coin_addresses_info(self):
        response = self.cli.api.btc.blocks.get_blocks()
        self.assertNotIn("status", response)
