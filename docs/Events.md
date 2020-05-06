### Events

Basic examples of using events for supported networks.


#### BCH Events

```python
from cryptoapi import Client

# mainnet
client_bch_events = Client(<YOUR_API_KEY>).events.bch
client_bch_events.connect()
subscription_id = client_bch_events.on_block(<callback_function>)

# testnet
client_bch_testnet_events = Client(<YOUR_API_KEY>).events.bch.testnet
client_bch_testnet_events.connect()
testnet_subscription_id = client_bch_testnet_events.on_block(<callback_function>)

# unsubscribe
client_bch_events.unsubscribe(subscription_id)
client_bch_testnet_events.unsubscribe(testnet_subscription_id)
```

#### BTC Events

```python
from cryptoapi import Client

# mainnet
client_btc_events = Client(<YOUR_API_KEY>).events.btc
client_btc_events.connect()
subscription_id = client_btc_events.on_block(<callback_function>)

# testnet
client_btc_testnet_events = Client(<YOUR_API_KEY>).events.btc.testnet
client_btc_testnet_events.connect()
testnet_subscription_id = client_btc_testnet_events.on_block(<callback_function>)

# unsubscribe
client_btc_events.unsubscribe(subscription_id)
client_btc_testnet_events.unsubscribe(testnet_subscription_id)
```

Available events for bch/btc networks: `on_block, on_address_transactions, on_address_balance, on_transaction_confirmations, on_connected, on_disconnected, unsubscribe`

#### ETH Events

```python
from cryptoapi import Client

# mainnet
client_eth_events = Client(<YOUR_API_KEY>).events.eth
client_eth_events.connect()
subscription_id = client_eth_events.on_block(<callback_function>)

# testnet
client_eth_testnet_events = Client(<YOUR_API_KEY>).events.eth.testnet
client_eth_testnet_events.connect()
testnet_subscription_id = client_eth_testnet_events.on_block(<callback_function>)

# unsubscribe
client_eth_events.unsubscribe(subscription_id)
client_eth_testnet_events.unsubscribe(testnet_subscription_id)
```

#### KLAY Events

```python
from cryptoapi import Client

# mainnet
client_klay_events = Client(<YOUR_API_KEY>).events.klay
client_klay_events.connect()
subscription_id = client_klay_events.on_block(<callback_function>)

# testnet
client_klay_testnet_events = Client(<YOUR_API_KEY>).events.klay.testnet
client_klay_testnet_events.connect()
testnet_subscription_id = client_klay_testnet_events.on_block(<callback_function>)

# unsubscribe
client_klay_events.unsubscribe(subscription_id)
client_klay_testnet_events.unsubscribe(testnet_subscription_id)
```

#### LTC Events

```python
from cryptoapi import Client

# mainnet
client_ltc_events = Client(<YOUR_API_KEY>).events.ltc
client_ltc_events.connect()
subscription_id = client_ltc_events.on_block(<callback_function>)

# testnet
client_ltc_testnet_events = Client(<YOUR_API_KEY>).events.ltc
client_ltc_testnet_events.connect()
testnet_subscription_id = client_ltc_testnet_events.on_block(<callback_function>)

# unsubscribe
client_ltc_events.unsubscribe(subscription_id)
client_ltc_testnet_events.unsubscribe(testnet_subscription_id)
```

Available events for eth/klay networks: `on_block, on_address_transactions, on_address_balance, on_transaction_confirmations, on_connected, on_disconnected, unsubscribe, on_token_transfers, on_token_balance, on_contract_log`
