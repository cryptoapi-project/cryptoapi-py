# Python library for cryptoapi

Cryptoapi-py library can be used to use cryptoapi methods and events subscriptions with python

## Installation

### Install with pip3:
	
	$ pip3 install cryptoapi-py

### Manual installation:

    $ git clone https://gitlab.pixelplex.by/697-crypto-api/cryptoapi-py.git
    $ cd cryptoapi-py
    $ python3 setup.py install
    or
    $ pip3 install .

## Usage

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
network_information = client.api.btc.testnet.common.get_network_information()

```

To see `Api's` usage examples and information: look <b>[section](docs/Api.md)</b>.

To see `Events` usage examples and information: look <b>[section](docs/Events.md)</b>.

To run `unit tests`:

    $ python3 -m unittest

### License

A copy of the license is available in the repository's
[LICENSE](LICENSE.txt) file.
