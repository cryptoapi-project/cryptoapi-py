# -*- coding: utf-8 -*-
import json
import logging
from threading import Lock, Thread
from typing import Any, Callable, Dict, List, Optional

from websocket import WebSocketApp  # type: ignore

log = logging.getLogger(__name__)


class WS:

    def __init__(self, url: str, api_key: str, debug: bool) -> None:
        self.__lock: Lock = Lock()

        self.url: str = url
        self.api_key: str = api_key
        self.debug: bool = debug
        self._thread: Optional[Thread] = None
        self._request_id: int = 0

        self._ws: WebSocketApp = WebSocketApp(url='{}?token={}'.format(self.url, self.api_key))
        self._connected: bool = False

        self.subscribers: Dict[int, List[Any]] = {}
        self.pending_subscribers: Dict[int, List[Any]] = {}
        self.message_status: Dict[int, Dict[Any, Any]] = {}

        self.on_connected_callbacks: List[Callable] = []
        self.on_disconnected_callbacks: List[Callable] = []
        self._callbacks_threads: List[Thread] = []
        self._joiner_thread: Optional[Thread] = None
        self._joiner_flag: bool = False

    def _on_message(ws: Any, message: Any) -> None:
        json_message: Dict[Any, Any] = json.loads(message)
        if 'result' in json_message:
            subscription_id: int = json_message['id']
            ws.message_status.update({
                subscription_id: {
                    'error': json_message['error'],
                    'result': json_message['result']
                }
            })
        else:
            message_id, message_object = json_message['params']
            _, callback, validator = ws.subscribers[message_id]
            # TODO: validator in action
            callback(message_object)

    def _on_open(ws: Any) -> None:
        ws._connected = True

    def _on_close(ws: Any) -> None:
        ws._connected = False
        ws.pending_subscribers = ws.subscribers
        ws.subscribers = {}

    def get_request_id(self) -> int:
        self._request_id += 1
        return self._request_id

    def _resubscribe(self) -> None:
        for subscription_id, subscription_info in self.pending_subscribers.items():
            self.on_event(subscription_info[0], subscription_info[1], subscription_info[2], subscription_id)
        if self.pending_subscribers:
            self._request_id = max(self.pending_subscribers)

        self.pending_subscribers = {}

    def _on_connected(self) -> None:
        for callback in self.on_connected_callbacks:
            thread: Thread = Thread(
                target=callback, args=(), kwargs={}
            )
            thread.start()
            self._callbacks_threads.append(thread)

    def _on_disconnected(self) -> None:
        for callback in self.on_disconnected_callbacks:
            thread: Thread = Thread(
                target=callback, args=(), kwargs={}
            )
            thread.start()
            self._callbacks_threads.append(thread)

    def _joiner(self) -> None:
        while self._joiner_flag:
            for thread in self._callbacks_threads:
                if not thread.is_alive():
                    thread.join()
                    self._callbacks_threads.remove(thread)

    def connect(self) -> None:
        if not self._connected:
            self._request_id = 0
            self._ws.on_message = self._on_message
            self._ws.on_open = self._on_open
            self._ws.on_close = self._on_close
            self._thread = Thread(
                target=self._ws.run_forever, args=(), kwargs={'ping_interval': 1}
            )
            self._thread.start()

            self._joiner_flag = True
            self._joiner_thread = Thread(
                target=self._joiner, args=(), kwargs={}
            )
            self._joiner_thread.start()

            while not self._connected:
                continue

            self._on_connected()
            self._resubscribe()

    def disconnect(self) -> None:
        while self._connected:
            self._ws.close()

        if self._thread:
            self._on_disconnected()
            self._thread.join()
            self._thread = None

        if self._joiner_flag:
            self._joiner_flag = False

        if self._joiner_thread:
            self._joiner_thread.join()
            self._joiner_thread = None

    def _send_message(self, method: Any, params: Any, _id: int) -> None:
        if not self._connected:
            self.connect()

        while not self._connected:
            continue

        self.__lock.acquire()
        try:
            payload: Dict[str, Any] = {
                'method': method,
                'params': params,
                'jsonrpc': '2.0',
                'id': _id
            }
            self._ws.send(json.dumps(payload, ensure_ascii=False).encode("utf8"))

        finally:
            # Release lock
            self.__lock.release()

    def on_event(
        self, params: Any, callback: Callable, validator: Callable, subscription_id: Optional[int] = None
    ) -> int:
        if not callable(callback):
            raise Exception('Callback must be callable object')

        if subscription_id is None:
            subscription_id = self.get_request_id()
        self._send_message('subscribe', params, subscription_id)

        while subscription_id not in self.message_status:
            continue

        message: Dict[str, Any] = self.message_status.pop(subscription_id)
        if message['result'] is None:
            raise Exception(message['error']['message'])

        self.subscribers[subscription_id] = [params, callback, validator]
        return subscription_id

    def unsubscribe(self, subscription_id: int) -> bool:
        subscription_info: Optional[List[Any]] = self.subscribers.get(subscription_id, None)
        if subscription_info is None:
            return False

        self._send_message('unsubscribe', subscription_info[0], subscription_id)

        while subscription_id not in self.message_status:
            continue

        message: Dict[str, Any] = self.message_status.pop(subscription_id)
        if message['result'] is None:
            return False

        del self.subscribers[subscription_id]
        return True
