import unittest

from cryptoapi.api import Api

from ..config import client_api_key, klay_address, klay_addresses, klay_token


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = klay_address
        self.addresses = klay_addresses
        self.token = klay_token

        self.api = Api(client_api_key).klay.testnet.addresses

    def test_get_transactions_by_addresses(self):
        response = self.api.get_transactions_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_transaction_intersections_by_addresses(self):
        response = self.api.get_transaction_intersections_by_addresses(self.addresses)
        self.assertNotIn('errors', response)

    def test_get_balances_by_addresses(self):
        response = self.api.get_balances_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_general_information_by_addresses(self):
        response = self.api.get_general_information_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_token_transfers_by_addresses(self):
        response = self.api.get_token_transfers_by_addresses([self.address], self.token)
        self.assertNotIn('errors', response)

    def test_get_tokens_balances_by_holders(self):
        response = self.api.get_tokens_balances_by_holders([self.address])
        self.assertNotIn('errors', response)

    def test_get_token_balance_by_holders_and_token(self):
        response = self.api.get_token_balance_by_holders_and_token([self.address], self.token)
        self.assertNotIn('errors', response)
