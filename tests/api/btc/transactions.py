import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1")

    def test_get_transactions(self):
        response = self.cli.api.btc.transactions.get_transactions(6)
        self.assertNotIn("status", response)

    def test_get_transaction_by_hash(self):
        response = self.cli.api.btc.transactions.get_transaction_by_hash('e845c15f1d415c901fb8abd04018d6b6abcb0ef3a3855b7b24cda9866902e7d1')
        self.assertNotIn("status", response)

    # def test_send_transaction(self):
    #     response = self.cli.api.btc.transactions.send_transaction()
    #     self.assertNotIn("status", response)

    def test_decode_transaction(self):
        response = self.cli.api.btc.transactions.decode_transaction('01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81cfee868b7f123b97288ac00000000')
        self.assertNotIn("status", response)
