import unittest
from cryptoapi import Client
from .config import address

class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    def test_get_transactions_by_addresses(self):
        response = self.cli.api.eth.addresses.get_transactions_by_addresses([address])
        self.assertNotIn("status", response)

    def test_get_transaction_intersections_by_addresses(self):
        response = self.cli.api.eth.addresses.get_transaction_intersections_by_addresses([address])
        self.assertNotIn("status", response)

    def test_get_balances_by_addresses(self):
        response = self.cli.api.eth.addresses.get_balances_by_addresses([address])
        self.assertNotIn("status", response)

    def test_get_general_information_by_addresses(self):
        response = self.cli.api.eth.addresses.get_general_information_by_addresses([address])
        self.assertNotIn("status", response)

    # def test_get_token_transfers_by_addresses(self):
    #     response = self.cli.api.eth.addresses.get_token_transfers_by_addresses([address], token)
    #     self.assertNotIn("status", response)

    def test_get_tokens_balances_by_holders(self):
        response = self.cli.api.eth.addresses.get_tokens_balances_by_holders([address])
        self.assertNotIn("status", response)

    # def test_get_token_balance_by_holders_and_token(self):
    #     response = self.cli.api.eth.addresses.get_token_balance_by_holders_and_token([address], token)
    #     self.assertNotIn("status", response)
