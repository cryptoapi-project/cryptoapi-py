import unittest

from cryptoapi import Client


from ..config import client_api_key, eth_address, eth_addresses, eth_token, mainnet


class AddressesTestCase(unittest.TestCase):

    def setUp(self):
        self.address = eth_address
        self.addresses = eth_addresses
        self.token = eth_token

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.eth.addresses
        else:
            self.client = self.client.api.eth.testnet.addresses

    def test_get_transactions_by_addresses(self):
        response = self.client.get_transactions_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_transaction_intersections_by_addresses(self):
        response = self.client.get_transaction_intersections_by_addresses(self.addresses)
        self.assertNotIn('errors', response)

    def test_get_balances_by_addresses(self):
        response = self.client.get_balances_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_general_information_by_addresses(self):
        response = self.client.get_general_information_by_addresses([self.address])
        self.assertNotIn('errors', response)

    def test_get_token_transfers_by_addresses(self):
        response = self.client.get_token_transfers_by_addresses([self.address], self.token)
        self.assertNotIn('errors', response)

    def test_get_tokens_balances_by_holders(self):
        response = self.client.get_tokens_balances_by_holders([self.address])
        self.assertNotIn('errors', response)

    def test_get_token_balance_by_holders_and_token(self):
        response = self.client.get_token_balance_by_holders_and_token([self.address], self.token)
        self.assertNotIn('errors', response)
