import unittest

from cryptoapi import Client

from ..config import client_api_key, eth_amount, eth_bytecode, eth_contract, eth_sender, mainnet


class ContractsTestCase(unittest.TestCase):

    def setUp(self):
        self.contract = eth_contract
        self.sender = eth_sender
        self.amount = eth_amount
        self.bytecode = eth_bytecode

        self.client = Client(client_api_key)
        if mainnet:
            self.client = self.client.api.eth.contracts
        else:
            self.client = self.client.api.eth.testnet.contracts

    def test_get_contracts_logs(self):
        contracts_logs = self.client.get_contracts_logs()
        self.assertNotIn('errors', contracts_logs)

    def test_contract_call(self):
        contract_call = self.client.contract_call(self.contract, self.sender, self.amount, self.bytecode)
        self.assertNotIn('errors', contract_call)
        self.assertIs(type(contract_call), str)

    def test_get_contract_general_information(self):
        contract_general_information = self.client.get_contract_general_information(self.contract)
        self.assertNotIn('errors', contract_general_information)
