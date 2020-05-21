import unittest

from cryptoapi.api import Api

from ..config import client_api_key, klay_amount, klay_bytecode, klay_contract, klay_sender


class ContractsTestCase(unittest.TestCase):

    def setUp(self):
        self.contract = klay_contract
        self.sender = klay_sender
        self.amount = klay_amount
        self.bytecode = klay_bytecode

        self.api = Api(client_api_key).klay.testnet.contracts

    def test_get_contracts_logs(self):
        contracts_logs = self.api.get_contracts_logs()
        self.assertNotIn('errors', contracts_logs)

    def test_contract_call(self):
        contract_call = self.api.contract_call(self.contract, self.sender, self.amount, self.bytecode)
        self.assertNotIn('errors', contract_call)
        self.assertIs(type(contract_call), str)

    def test_get_contract_general_information(self):
        contract_general_information = self.api.get_contract_general_information(self.contract)
        self.assertNotIn('errors', contract_general_information)
