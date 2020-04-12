# -*- coding: utf-8 -*-
import json
import logging
import websocket
import threading

log = logging.getLogger(__name__)


class WS:
    def __init__(self, url, api_key, debug):
        self.__lock = threading.Lock()

        self.url = url
        self.api_key = api_key
        self.debug = debug
        self._ws = None
        self._thread = None

        self._ws = websocket.WebSocketApp(
            url='{}?token={}'.format(
                self.url,
                self.api_key
            )
        )

        self.subscribers = {}
        self.pending_subscribers = {}
        self.message_status = {}

    def on_message(ws, message):
        message = json.loads(message)
        print(message)
        print(ws.__dict__)
        print('result' in message)
        if 'result' in message:
            subscription_id = message['id']
            ws.message_status.update(
                {
                    subscription_id: {
                        'error': message['error'],
                        'result': message['result']
                    }
                }
            )
            print(ws.message_status)

    @staticmethod
    def on_open(ws):
        print('ws open')

    @staticmethod
    def on_close(ws):
        print('ws close')

    def _get_request_id(self):
        self._request_id += 1
        return self._request_id

    def connect(self):
        self._request_id = 0
        self._ws.on_message = self.on_message
        self._ws.on_open = self.on_open
        self._ws.on_close = self.on_close
        self._thread = threading.Thread(
            target=self._ws.run_forever,
            args=(),
            kwargs={}
        )
        self._thread.start()

    def disconnect(self):
        if self._ws:
            try:
                while self._thread.is_alive():
                    self._ws.close()
                self._thread = None
            except Exception:
                pass

    def _send_message(self, method, params, _id):
        if not self._ws.keep_running:
            self.connect()

        self.__lock.acquire()
        try:
            payload = {
                'method': method,
                'params': params,
                'jsonrpc': '2.0',
                'id': _id
            }
            self._ws.send(
                json.dumps(
                    payload,
                    ensure_ascii=False
                ).encode("utf8")
            )

        finally:
            # Release lock
            self.__lock.release()

    def on_event(self, method, params, callback=None):
        subscription_id = self._get_request_id()
        self._send_message(
            method,
            params,
            subscription_id
        )
        self.pending_subscribers[subscription_id] = [params, callback]

        while subscription_id not in self.message_status:
            continue

        message = self.message_status.pop(subscription_id)
        pending_subscriber = self.pending_subscribers.pop(subscription_id)
        if message['result'] is None:
            raise Exception(message['error']['message'])

        self.subscribers[subscription_id] = pending_subscriber
        return subscription_id

    def on_block(self, callback):
        return self._on_event(
            method='subscribe',
            params=['new_block'],
            callback=callback
        )

    def unsubscribe(self, subscription_id):
        self._send_message(
            'unsubscribe',
            ['new_block'],
            subscription_id
        )

        while subscription_id not in self.message_status:
            continue

        message = self.message_status.pop(subscription_id)
        if message['result'] is None:
            return False

        self.subscribers.pop(subscription_id)
        return True
