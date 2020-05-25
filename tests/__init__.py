# type: ignore
from .api.bch.addresses import AddressesTestCase as BchAddressesTestCase
from .api.bch.blocks import BlocksTestCase as BchBlocksTestCase
from .api.bch.common import CommonTestCase as BchCommonTestCase
from .api.bch.transactions import TransactionsTestCase as BchTransactionsTestCase
from .api.btc.addresses import AddressesTestCase as BtcAddressesTestCase
from .api.btc.blocks import BlocksTestCase as BtcBlocksTestCase
from .api.btc.common import CommonTestCase as BtcCommonTestCase
from .api.btc.transactions import TransactionsTestCase as BtcTransactionsTestCase
from .api.common import CommonTestCase
# from .api.config import mainnet
from .api.eth.addresses import AddressesTestCase as EthAddressesTestCase
from .api.eth.blocks import BlocksTestCase as EthBlocksTestCase
from .api.eth.common import CommonTestCase as EthCommonTestCase
from .api.eth.contracts import ContractsTestCase as EthContractsTestCase
from .api.eth.tokens import TokensTestCase as EthTokensTestCase
from .api.eth.transactions import TransactionsTestCase as EthTransactionsTestCase
from .api.ltc.addresses import AddressesTestCase as LtcAddressesTestCase
from .api.ltc.blocks import BlocksTestCase as LtcBlocksTestCase
from .api.ltc.common import CommonTestCase as LtcCommonTestCase
from .api.ltc.transactions import TransactionsTestCase as LtcTransactionsTestCase
from .api.rates import RatesTestCase

imported_tests = [
    CommonTestCase, RatesTestCase, BtcAddressesTestCase, BtcBlocksTestCase, BtcCommonTestCase,
    BtcTransactionsTestCase, BchAddressesTestCase, BchBlocksTestCase, BchCommonTestCase, BchTransactionsTestCase,
    EthAddressesTestCase, EthBlocksTestCase, EthCommonTestCase, EthContractsTestCase, EthTokensTestCase,
    EthTransactionsTestCase, LtcAddressesTestCase, LtcBlocksTestCase, LtcCommonTestCase, LtcTransactionsTestCase
]
"""
if not mainnet:
    from .api.klay.addresses import AddressesTestCase as KlayAddressesTestCase
    from .api.klay.blocks import BlocksTestCase as KlayBlocksTestCase
    from .api.klay.common import CommonTestCase as KlayCommonTestCase
    from .api.klay.contracts import ContractsTestCase as KlayContractsTestCase
    from .api.klay.tokens import TokensTestCase as KlayTokensTestCase
    from .api.klay.transactions import TransactionsTestCase as KlayTransactionsTestCase
    imported_tests.extend([
        KlayAddressesTestCase,
        KlayBlocksTestCase,
        KlayCommonTestCase,
        KlayContractsTestCase,
        KlayTokensTestCase,
        KlayTransactionsTestCase,
    ])
"""

__all__ = imported_tests
