from .api.btc.addresses import AddressesTestCase as BtcAddressesTestCase
from .api.btc.blocks import BlocksTestCase as BtcBlocksTestCase
from .api.btc.common import CommonTestCase as BtcCommonTestCase
from .api.btc.transactions import TransactionsTestCase as BtcTransactionsTestCase

from .api.bch.addresses import AddressesTestCase as BchAddressesTestCase
from .api.bch.blocks import BlocksTestCase as BchBlocksTestCase
from .api.bch.common import CommonTestCase as BchCommonTestCase
from .api.bch.transactions import TransactionsTestCase as BchTransactionsTestCase

from .api.eth.addresses import AddressesTestCase as EthAddressesTestCase
from .api.eth.blocks import BlocksTestCase as EthBlocksTestCase
from .api.eth.common import CommonTestCase as EthCommonTestCase
from .api.eth.contracts import ContractsTestCase as EthContractsTestCase
from .api.eth.tokens import TokensTestCase as EthTokensTestCase
from .api.eth.transactions import TransactionsTestCase as EthTransactionsTestCase

from .api.whooks.whooks import WebhookTestCase
