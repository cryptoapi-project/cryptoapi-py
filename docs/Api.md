### Api

This examples of using all available api methods.

#### BCH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
outputs_by_addresses_and_status = client.api.bch.testnet.blocks.get_block(<BLOCK_NUMBER>)

```

#### BTC Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
outputs_by_addresses_and_status = client.api.btc.testnet.blocks.get_block(<BLOCK_NUMBER>)

```

#### ETH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
transaction_by_address = client.api.eth.testnet.blocks.get_block(<BLOCK_NUMBER>)

```
#### KLAY Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
transaction_by_address = client.api.klay.testnet.blocks.get_block(<BLOCK_NUMBER>)

```

#### Web Hooks

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
KLAY_address_methods = 
outputs_by_addresses_and_status = client.api.whooks.testnet.whooks.get_webhook(<PROJECT_ID>)

```

More information about `API methods` can be browsed by <b><a href="https://testnet-api.apikey.io/api/">link</a></b>.

More information about `Web Hooks` can be browsed by <b><a href="https://api.apikey.io/whooks-api/">link</a></b>.
