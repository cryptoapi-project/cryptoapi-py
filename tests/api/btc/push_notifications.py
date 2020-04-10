
# import unittest
# from cryptoapi import Client


# class AddressesTestCase(unittest.TestCase):
#     def setUp(self):
#         self.cli = Client("51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1")

#     def test_subscribe_to_addresses_notifications(self):
#         response = self.cli.api.btc.push_notifications.subscribe_to_addresses_notifications('51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1')
#         self.assertIs(type(response), float)

#     def test_unsubscribe_from_addresses_notifications(self):
#         response = self.cli.api.btc.push_notifications.unsubscribe_from_addresses_notifications('51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1')
#         self.assertNotIn("status", response)
