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
        self._request_id = 0

        self._ws = websocket.WebSocketApp(
            url='{}?token={}'.format(
                self.url,
                self.api_key
            )
        )
        self._connected = False

        self.subscribers = {}
        self.pending_subscribers = {}
        self.message_status = {}

        self.on_connected_callbacks = []
        self.on_disconnected_callbacks = []
        self._callbacks_threads = []
        self._joiner_thread = None
        self._joiner_flag = False

    def _on_message(ws, message):
        message = json.loads(message)
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
        else:
            message_id, message_object = message['params']
            ws.subscribers[message_id][1](message_object)

    def _on_open(ws):
        ws._connected = True

    def _on_close(ws):
        ws._connected = False
        ws.pending_subscribers = ws.subscribers
        ws.subscribers = {}

    def get_request_id(self):
        self._request_id += 1
        return self._request_id

    def _resubscribe(self):
        for subscription_id, subscription_info in self.pending_subscribers.items():
            self.on_event(
                subscription_info[0],
                subscription_info[1],
                subscription_id
            )
        if self.pending_subscribers:
            self._request_id = max(self.pending_subscribers)

        self.pending_subscribers = {}

    def _on_connected(self):
        for callback in self.on_connected_callbacks:
            thread = threading.Thread(
                target=callback,
                args=(),
                kwargs={}
            )
            thread.start()
            self._callbacks_threads.append(thread)

    def _on_disconnected(self):
        for callback in self.on_disconnected_callbacks:
            thread = threading.Thread(
                target=callback,
                args=(),
                kwargs={}
            )
            thread.start()
            self._callbacks_threads.append(thread)

    def _joiner(self):
        while self._joiner_flag:
            for thread in self._callbacks_threads:
                if not thread.is_alive():
                    thread.join()
                    self._callbacks_threads.remove(thread)

    def connect(self):
        if not self._connected:
            self._request_id = 0
            self._ws.on_message = self._on_message
            self._ws.on_open = self._on_open
            self._ws.on_close = self._on_close
            self._thread = threading.Thread(
                target=self._ws.run_forever,
                args=(),
                kwargs={'ping_interval': 1}
            )
            self._thread.start()

            self._joiner_flag = True
            self._joiner_thread = threading.Thread(
                target=self._joiner,
                args=(),
                kwargs={}
            )
            self._joiner_thread.start()

            while not self._connected:
                continue

            self._on_connected()
            self._resubscribe()

    def disconnect(self):
        while self._connected:
            self._ws.close()

        self._on_disconnected()
        self._thread.join()
        self._thread = None

        self._joiner_flag = False
        self._joiner_thread.join()
        self._joiner_thread = None

    def _send_message(self, method, params, _id):
        if not self._connected:
            self.connect()

        while not self._connected:
            continue

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

    def on_event(self, params, callback, subscription_id=None):
        if not callable(callback):
            raise Exception('Callback must be callable object')

        if subscription_id is None:
            subscription_id = self.get_request_id()
        self._send_message(
            'subscribe',
            params,
            subscription_id
        )

        while subscription_id not in self.message_status:
            continue

        message = self.message_status.pop(subscription_id)
        if message['result'] is None:
            raise Exception(message['error']['message'])

        self.subscribers[subscription_id] = [params, callback]
        return subscription_id

    def unsubscribe(self, subscription_id):
        subscription_info = self.subscribers.get(subscription_id, None)
        if subscription_info is None:
            return False

        self._send_message(
            'unsubscribe',
            subscription_info[0],
            subscription_id
        )

        while subscription_id not in self.message_status:
            continue

        message = self.message_status.pop(subscription_id)
        if message['result'] is None:
            return False

        del self.subscribers[subscription_id]
        return True
