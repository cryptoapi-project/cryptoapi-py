### Api

This library provides cryptoapi methods.

#### BCH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
BCH_address_methods = client.api.bch.testnet.addresses
outputs_by_addresses_and_status = BCH_address_methods.get_outputs_by_addresses([<ADDRESSES>], <STATUS>)

```

#### BTC Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
BTC_address_methods = client.api.btc.testnet.addresses
outputs_by_addresses_and_status = BTC_address_methods.get_outputs_by_addresses([<ADDRESSES>], <STATUS>)

```

#### ETH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
ETH_address_methods = client.api.eth.testnet.addresses
outputs_by_addresses_and_status = ETH_address_methods.get_transactions_by_addresses([<ADDRESSES>])

```
#### KLAY Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
KLAY_address_methods = client.api.klay.testnet.addresses
outputs_by_addresses_and_status = KLAY_address_methods.get_transactions_by_addresses([<ADDRESSES>])

```

More information about `API methods` can be browsed by <b><a href="https://testnet-api.apikey.io/api/">link</a></b>.