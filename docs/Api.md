### Api

This examples of using all available api methods.

#### BCH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)

# testnet example
block = client.api.bch.testnet.blocks.get_block(<BLOCK_NUMBER>)

# mainnet example
block = client.api.bch.blocks.get_block(<BLOCK_NUMBER>)

```

#### BTC Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)

# testnet example
block = client.api.btc.testnet.blocks.get_block(<BLOCK_NUMBER>)

# mainnet example
block = client.api.btc.blocks.get_block(<BLOCK_NUMBER>)

```

#### ETH Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)

# testnet example
block = client.api.eth.testnet.blocks.get_block(<BLOCK_NUMBER>)

# mainnet example
block = client.api.eth.blocks.get_block(<BLOCK_NUMBER>)

```

#### KLAY Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)

# testnet example
block = client.api.klay.testnet.blocks.get_block(<BLOCK_NUMBER>)

```

#### LTC Api

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)

# testnet example
block = client.api.ltc.testnet.blocks.get_block(<BLOCK_NUMBER>)
```

#### Web Hooks

```python
from cryptoapi import Client

client = Client(<YOUR_API_KEY>)
hook_events = client.api.whooks.get_hook_events(<HOOK_ID>)

```

More information about `API methods` can be browsed by <b><a href="https://testnet-api.apikey.io/api/">link</a></b>.

More information about `Web Hooks` can be browsed by <b><a href="https://api.apikey.io/whooks-api/">link</a></b>.
