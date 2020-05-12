import os

mainnet = os.environ.get('MAINNET', False)

client_api_key = '51228473d659eb21da3696f25e36d2d364225a9c80d52988ac2a711f1eb3d5d1'

# eth
if mainnet:
    eth_address = '0x31B98D14007bDEe637298086988A0bBd31184523'
    eth_addresses = [eth_address, '0x3FdF73b0D6b61959d5C5ce5f456508AB6BFD7Bb9']
    eth_token = '0x1AA950bD468997A28927434cB4F030AE0f19c8a7'
    eth_block_number = 100000
    eth_limit = 2
    eth_contract = '0x3561178a9c214dd5b8d8c9e1eed31210f068633b'
    eth_sender = '0x3561178a9c214dd5b8d8c9e1eed31210f068633b'
    eth_amount = 0
    eth_bytecode = '0x18160ddd'
    eth_from = '0x4C8Ef3BCDc62bc8Bae02f46D56c975AB78947405'
    eth_to = '0xffbf52733195ccafea7be8d871f5c8be7ca360cf'
    eth_data = '0xc6888fa10000000000000000000000000000000000000000000000000000000000000003'
    eth_value = '0x45D964B800'
    eth_trx_hex = '0xf86e8386ca038602bba7f5220083632ea0941de29f644d555fe9cc3241e1083d' +\
        'e0868f959bfa8545d964b800801ca04ef1f13c58af9a9ac4be66b838a238b24db798d585' +\
        'd882865637fdc35bdc49c4a04b7d1dfc3d9672080347a0d3559628f5f757bd6f6a005d1c' +\
        '4f7cdccce020ea02'
    eth_trx_hash = '0x305f0bbe3a008f2e078895c709c8fc436a6216afa3340cc764daa0f5bed7aa2a'
else:
    eth_address = '0x31B98D14007bDEe637298086988A0bBd31184523'
    eth_addresses = [eth_address, '0x3FdF73b0D6b61959d5C5ce5f456508AB6BFD7Bb9']
    eth_token = '0x1AA950bD468997A28927434cB4F030AE0f19c8a7'
    eth_block_number = 100000
    eth_limit = 2
    eth_contract = '0x957ebaac28080bdb246e5a956661a9dd60d51223'
    eth_sender = '0x957ebaac28080bdb246e5a956661a9dd60d51223'
    eth_amount = 0
    eth_bytecode = '0x18160ddd'
    eth_from = '0x4C8Ef3BCDc62bc8Bae02f46D56c975AB78947405'
    eth_to = '0xffbf52733195ccafea7be8d871f5c8be7ca360cf'
    eth_data = '0xc6888fa10000000000000000000000000000000000000000000000000000000000000003'
    eth_value = '0x45D964B800'
    eth_trx_hex = '0xf86e8386ca038602bba7f5220083632ea0941de29f644d555fe9cc3241e1083d' +\
        'e0868f959bfa8545d964b800801ca04ef1f13c58af9a9ac4be66b838a238b24db798d585' +\
        'd882865637fdc35bdc49c4a04b7d1dfc3d9672080347a0d3559628f5f757bd6f6a005d1c' +\
        '4f7cdccce020ea02'
    eth_trx_hash = '0x305f0bbe3a008f2e078895c709c8fc436a6216afa3340cc764daa0f5bed7aa2a'

# klay
if not mainnet:
    klay_from = '0x4C8Ef3BCDc62bc8Bae02f46D56c975AB78947405'
    klay_to = '0xffbf52733195ccafea7be8d871f5c8be7ca360cf'
    klay_data = '0xc6888fa10000000000000000000000000000000000000000000000000000000000000003'
    klay_value = '0x45D964B800'
    klay_address = '0x8d09819b35c28280bf6fbcef84d01645ec974559'
    klay_addresses = [klay_address, '0x8d09819b35c28280bf6fbcef84d01645ec974559']
    klay_token = '0x77ac6721fd5c5e5e2b3169ffd648d1e419ae0353'
    klay_block_number = 100000
    klay_limit = 2
    klay_contract = '0x9fdd7a341308e969527bd6c928068edee8399807'
    klay_sender = '0x9fdd7a341308e969527bd6c928068edee8399807'
    klay_amount = 0
    klay_bytecode = '0x18160ddd'
    klay_trx_hex = '0xf86e8386ca038602bba7f5220083632ea0941de29f644d555fe9cc3241e1083d' +\
        'e0868f959bfa8545d964b800801ca04ef1f13c58af9a9ac4be66b838a238b24db798d585' +\
        'd882865637fdc35bdc49c4a04b7d1dfc3d9672080347a0d3559628f5f757bd6f6a005d1c' +\
        '4f7cdccce020ea02'
    klay_trx_hash = '0x879c7099922be963176af976022a858e02fd0b4f1923b9f5bf48c9099b305d07'


# btc
if mainnet:
    btc_address = '2N9Rcb3Vz5g8Do51usJ8ywJ4oCZJ2RBs469'
    btc_status = 'unspent'

    btc_block_number = 100

    btc_trx_hash = 'e845c15f1d415c901fb8abd04018d6b6abcb0ef3a3855b7b24cda9866902e7d1'
    btc_trx_hex = '01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff' +\
        '6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78' +\
        'c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5' +\
        'c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a' +\
        '25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81c' +\
        'fee868b7f123b97288ac00000000'
else:
    btc_address = '2N9Rcb3Vz5g8Do51usJ8ywJ4oCZJ2RBs469'
    btc_status = 'unspent'

    btc_block_number = 100

    btc_trx_hash = 'e845c15f1d415c901fb8abd04018d6b6abcb0ef3a3855b7b24cda9866902e7d1'
    btc_trx_hex = '01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff' +\
        '6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78' +\
        'c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5' +\
        'c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a' +\
        '25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81c' +\
        'fee868b7f123b97288ac00000000'

# bch
if mainnet:
    bch_address = 'qqpz7r5k72e07j0syq26f0h8srvdqeqjg50wg9fp3z'
    bch_status = 'unspent'
    bch_block_number = 100
    bch_trx_hash = '4821aac1650f6bc28daea22d70358021b9021567f07015562ab861cc14bfd393'
    bch_trx_hex = '01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff' +\
        '6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78' +\
        'c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5' +\
        'c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a' +\
        '25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81c' +\
        'fee868b7f123b97288ac00000000'
else:
    bch_address = 'qqpz7r5k72e07j0syq26f0h8srvdqeqjg50wg9fp3z'
    bch_status = 'unspent'
    bch_block_number = 100
    bch_trx_hash = '4821aac1650f6bc28daea22d70358021b9021567f07015562ab861cc14bfd393'
    bch_trx_hex = '01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff' +\
        '6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78' +\
        'c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5' +\
        'c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a' +\
        '25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81c' +\
        'fee868b7f123b97288ac00000000'

# ltc
if not mainnet:
    ltc_address = 'msiJHQf1BVXD6fuUyLn9D8mD6gMbPibiDV'
    ltc_status = 'unspent'
    ltc_block_number = 100
    ltc_trx_hash = 'da8e89ebd76f82c0f5ed3855a8244aef4b4d069590b3a2ed9a9e2374c5b62380'
    ltc_trx_hex = '01000000014368d74c6a7b118610b325389613acff68a324eb86caf61e1494d1ff' +\
        '6bcb07e9010000006a4730440220463a47bd9ba114ba919b7bb6fc4f9e97754fb1e8eb78' +\
        'c5d4803cb3208fea7c8c0220271174def0bf6499b09b48fa87ad6f3ae8e3f16217228ed5' +\
        'c722aa9a4e1180fd01210309a18fa38989b25a7cc4f66fb193a9a26842113874908c430a' +\
        '25d65f66e4e5fbffffffff0101000000000000001976a91492bf5261a59bd600825dc81c' +\
        'fee868b7f123b97288ac00000000'
