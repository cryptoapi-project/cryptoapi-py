# -*- coding: utf-8 -*-
import logging
import requests
from .rpc import Rpc

log = logging.getLogger(__name__)


class Http(Rpc):

    def proxies(self):
        proxy_url = self.get_proxy_url()
        if proxy_url is None:
            return None
        return {"http": proxy_url, "https": proxy_url}

    def _make_request(self, method, url, data=None, params=None, validators=[]):
        response = method(
            url=self.url,
            data=data,
            params=params,
            proxies=self.proxies
        )

        for validator in validators:
            validator(response)

        return response.json()

    def get(self, params=None, validators=[]):
        return self._make_request(
            method=requests.get,
            url=self.url,
            params=params,
            validators=validators
        )

    def post(self, data=None, params=None, validators=[]):
        return self._make_request(
            method=requests.post,
            url=self.url,
            data=data,
            params=params,
            validators=validators
        )

    def delete(self, params=None, validators=[]):
        return self._make_request(
            method=requests.delete,
            url=self.url,
            params=params,
            validators=validators
        )
