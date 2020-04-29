import unittest
from cryptoapi import Client
from .config import client_api_key, project_id, url, coin, is_subscribe_block, is_subscribe_transfer,\
    is_subscribe_transaction, transaction_addresses, transfer_triggers, _id, hook_id


class WebhookTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(client_api_key).api.whooks.testnet.whooks

    def test_create_webhook(self):
        response = self.client.create_webhook(
            project_id=project_id,
            url=url,
            coin=coin,
            is_subscribe_block=is_subscribe_block,
            is_subscribe_transfer=is_subscribe_transfer,
            is_subscribe_transaction=is_subscribe_transaction,
            transaction_addresses=transaction_addresses,
            transfer_triggers=transfer_triggers
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_webhook(self):
        response = self.client.get_webhook(
            project_id=project_id
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_delete_webhook(self):
        response = self.client.delete_webhook(
            _id=_id
        )
        self.assertNotIn(
            'errors',
            response
        )

    def test_change_webhook(self):
        response = self.client.change_webhook(
            project_id=project_id,
            url=url,
            coin=coin,
            is_subscribe_block=is_subscribe_block,
            is_subscribe_transfer=is_subscribe_transfer,
            is_subscribe_transaction=is_subscribe_transaction,
            transaction_addresses=transaction_addresses,
            transfer_triggers=transfer_triggers,
            _id=_id
        )
        self.assertNotIn(
            'status',
            response
        )

    def test_get_events(self):
        response = self.client.get_events(
            hook_id=hook_id
        )
        self.assertNotIn(
            'status',
            response
        )
