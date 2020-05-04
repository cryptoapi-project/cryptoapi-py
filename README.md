# Python library for cryptoapi

Cryptoapi-py library can be used to use cryptoapi methods and events with python

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
BTC_address = client.api.btc.testnet.addresses #client.api.btc.mainnet.addresses to use with mainnet
outputs_by_addresses_and_status = BTC_address.get_outputs_by_addresses([<ADDRESSES>], <STATUS>)

```

To see `Api's` usage examples and information: look <b>[section](docs/Api.md)</b>.

To see `Events` usage examples and information: look <b>[section](docs/Events.md)</b>.

To run `unit tests`:

    $ python3 -m unittest