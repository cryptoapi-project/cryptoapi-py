import unittest
from cryptoapi import Client


class AddressesTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = Client("347d123568e7f83f7971fe7d19366c04258ed62b5a80925b87545a2bb87e57eb")

    def test_get_contracts_logs(self):
        block_by_hash = self.cli.api.eth.contracts.get_contracts_logs()
        self.assertNotIn("status", block_by_hash)

    # def test_contract_call(self):
    #     response = self.cli.api.eth.contracts.contract_call([address], sender, amount, bytecode)
    #     self.assertNotIn("status", response)

    # def test_get_contract_general_information(self):
    #     response = self.cli.api.eth.contracts.get_contract_general_information(["address"])
    #     self.assertNotIn("status", response)
