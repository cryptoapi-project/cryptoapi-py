# -*- coding: utf-8 -*-
import logging
from requests import get, post, delete
import urllib

log = logging.getLogger(__name__)


class Http:

    def __init__(self, url, debug, **kwargs):
        self._setup_proxy(kwargs)

        self.debug = debug
        self.api_key = kwargs.get("api_key")
        self.url = url

    # @property
    # def debug(self):
    #     return self._debug

    # @debug.setter
    # def debug(self, debug):
    #     self._debug = debug
    #     if debug:
    #         logging.basicConfig(
    #             level=logging.DEBUG,
    #             format='\n{}%(levelname)s:{} %(asctime)s - %(message)s'.format('\x1b[1;33m', '\x1b[0m'),
    #             datefmt='%d-%b-%y %H:%M:%S'
    #         )

    def _setup_proxy(self, options):
        proxy_url = options.pop("proxy", None)
        if proxy_url:
            url = urllib.parse.urlparse(proxy_url)
            self.proxy_host = url.hostname
            self.proxy_port = url.port
            self.proxy_type = url.scheme.lower()
            self.proxy_user = url.username
            self.proxy_pass = url.password
            self.proxy_rdns = True
            if not (url.scheme.endswith("h")):
                self.proxy_rdns = False
            else:
                self.proxy_type = self.proxy_type[0: len(self.proxy_type) - 1]
        else:
            self.proxy_host = options.pop("proxy_host", None)
            self.proxy_port = options.pop("proxy_port", 80)
            self.proxy_type = options.pop("proxy_type", "http")
            self.proxy_user = options.pop("proxy_user", None)
            self.proxy_pass = options.pop("proxy_pass", None)
            self.proxy_rdns = False
        log.info(
            "Using proxy %s:%d %s" % (self.proxy_host, self.proxy_port, self.proxy_type)
        )

    def _get_proxy_url(self):
        if not self.proxy_host:
            return None
        auth = ""
        if self.proxy_user:
            auth = "%s:%s@" % (self.proxy_user, self.proxy_pass)
        url = (
            self.proxy_type
            + "://"
            + auth
            + ("%s:%d" % (self.proxy_host, self.proxy_port))
        )
        return url

    def proxies(self):
        proxy_url = self._get_proxy_url()
        if proxy_url is None:
            return None
        return {"http": proxy_url, "https": proxy_url}

    def _make_request(self, method, url, data=None, params=None, validators={}):
        response = method(
            url=self.url + url,
            data=data,
            params=params,
            proxies=self.proxies()
        )
        status_code = response.status_code
        try:
            json_response = response.json()
        except Exception:
            raise Exception('{}: Web Server error'.format(status_code))

        if status_code in validators:
            validator = validators[status_code]
            if not validator.validate(json_response):
                raise Exception(validator.errors)

        return json_response

    def get(self, url, params=None, validators=[]):
        return self._make_request(
            method=get,
            url=url,
            params=params,
            validators=validators
        )

    def post(self, url, data=None, params=None, validators=[]):
        return self._make_request(
            method=post,
            url=url,
            data=data,
            params=params,
            validators=validators
        )

    def delete(self, url, params=None, validators=[]):
        return self._make_request(
            method=delete,
            url=url,
            params=params,
            validators=validators
        )
