import unittest
from cryptoapi import Client
from .config import address, address2, token, client_api_key


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.addresses

    def test_get_transactions_by_addresses(self):
        response = self.client.get_transactions_by_addresses(
            [address]
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_transaction_intersections_by_addresses(self):
        response = self.client.get_transaction_intersections_by_addresses(
            [address, address2]
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_balances_by_addresses(self):
        response = self.client.get_balances_by_addresses(
            [address]
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_general_information_by_addresses(self):
        response = self.client.get_general_information_by_addresses(
            [address]
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_token_transfers_by_addresses(self):
        response = self.client.get_token_transfers_by_addresses(
            [address],
            token
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_tokens_balances_by_holders(self):
        response = self.client.get_tokens_balances_by_holders(
            [address]
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_token_balance_by_holders_and_token(self):
        response = self.client.get_token_balance_by_holders_and_token(
            [address],
            token
        )
        self.assertNotIn(
            'status',
            response
        )
