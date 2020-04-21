import unittest
from cryptoapi import Client
from .config import contract, client_api_key


class ContractsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.eth.testnet.contracts

    def test_get_contracts_logs(self):
        contracts_logs = self.client.get_contracts_logs()
        self.assertNotIn(
            'status',
            contracts_logs
        )

    # def test_contract_call(self):
    #     contract_call = self.client.api.eth.testnet.contracts.contract_call(
    #         [address],
    #         sender,
    #         amount,
    #         bytecode
    #     )
    #     self.assertNotIn(
    #         'status',
    #         response
    #     )

    def test_get_contract_general_information(self):
        contract_general_information = self.client.get_contract_general_information(
            contract
        )
        self.assertNotIn(
            'status',
            contract_general_information
        )
