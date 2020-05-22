import os
import unittest

import HtmlTestRunner  # type: ignore

unittest.main(
    module='tests',
    testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports', report_name='mainnet' if 'MAINNET' in os.environ else 'testnet', combine_reports=True
    )
)
