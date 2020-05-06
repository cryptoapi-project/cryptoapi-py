import unittest
from cryptoapi import Client
from .config import contract, client_api_key


class ContractsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.contracts

    def test_get_contracts_logs(self):
        contracts_logs = self.client.get_contracts_logs()
        self.assertNotIn(
            'errors',
            contracts_logs
        )

    @unittest.skip('Future')
    def test_contract_call(self):
        pass

    def test_get_contract_general_information(self):
        contract_general_information = self.client.get_contract_general_information(
            contract
        )
        self.assertNotIn(
            'errors',
            contract_general_information
        )
