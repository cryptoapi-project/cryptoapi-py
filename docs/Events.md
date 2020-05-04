### Api

This library provides cryptoapi events.


#### BCH Api

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.bch
client_bch_events.connect()
client_bch_events.on_block(<callback_function>, confirmations=0)

```

#### BTC Api

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.btc
client_bch_events.connect()
client_bch_events.on_block(<callback_function>, confirmations=0)

```

#### ETH Api

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.eth
client_bch_events.connect()
client_bch_events.on_block(<callback_function>, confirmations=0)

```

#### KLAY Api

```python
from cryptoapi import Client

client_bch_events = Client(<YOUR_API_KEY>).events.klay
client_bch_events.connect()
client_bch_events.on_block(<callback_function>, confirmations=0)

```