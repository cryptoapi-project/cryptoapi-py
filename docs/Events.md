### Events

Basic examples of using events for supported networks.


#### BCH Events

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.bch
client_bch_events.connect()
subscription_id = client_bch_events.on_block(<callback_function>)

```

#### BTC Events

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.btc
client_bch_events.connect()
subscription_id = client_btc_events.on_block(<callback_function>)

```

Available events for bch/btc networks: `on_block, on_address_transactions, on_address_balance, on_transaction_confirmations, on_connected, on_disconnected, unsubscribe`

#### ETH Events

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.eth
client_bch_events.connect()
subscription_id = client_eth_events.on_block(<callback_function>)

```

#### KLAY Events

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.klay
client_bch_events.connect()
subscription_id = client_klay_events.on_block(<callback_function>)

```

Available events for eth/klay networks: `on_block, on_address_transactions, on_address_balance, on_transaction_confirmations, on_connected, on_disconnected, unsubscribe, on_token_transfers, on_token_balance, on_contract_log`