# Global setting to indicate if test net
# If not specify and pass to "Class", default value would be "False"
IS_TEST_NET = True

# ---------------- API Sample -------------------

from binance_dex.api import BinanceChainClient, api_types_instance

# Create API Client instance
api_client = BinanceChainClient(is_test_net=IS_TEST_NET)

# # Get Block time
# print('Block Time: ')
# print(api_client.get_block_time())
#
# # Get Node Info
# print('Node Info: ')
# print(api_client.get_node_info())
#
# # Get Validator
# print('Validators: ')
# print(api_client.get_validators())

# # Get Validator
# print('Peers: ')
# print(api_client.get_peers())

#
# # Get Listing Tokens
# print('Token Listed: ')
# print(api_client.get_tokens())
#
# # Get Account Info By Address
# address = 'tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw'
# print('Account info for %s:' % address)
# print(api_client.get_account_info_by_address(address=address))

# # Get Account Sequence By Address
# address = 'tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw'
# print('Account sequence for %s:' % address)
# print(api_client.get_account_sequence_by_address(address=address))

#
# # Get Transaction Info By TxId
# tx_id = '35B8D4070200FFBE045432AC9D87232BEC1FFAD9E6A6C8979CE2FE631B644B9E'
# print("Transaction details with txid: %s:" % tx_id)
# print(api_client.get_transaction(tx_hash=tx_id))
#
# # Get Market Trading Pairs List
# print('Trading Pairs:')
# print(api_client.get_markets())
#
# # Get Binance Chain Fees
# print('Fees:')
# print(api_client.get_fees())

# # Get order book
# print('Orders:')
# print(api_client.get_depth("NNB-0AD_BNB", 5))

# # Get KLines
# trading_pair = 'DEX.B-C72_BNB'
# print("Last 100 4hour Klines with trading Pair '%s':" % trading_pair)
# print(api_client.get_klines(trading_pair=trading_pair,
#                             interval=api_types_instance.KLine.interval_4hour,
#                             limit=100))

# ------------ End of API Sample ----------------


# -------------- Crypto Sample ------------------

from binance_dex.crypto import BinanceChainCrypto

# Create crypto instance
crypto_instance = BinanceChainCrypto(is_test_net=IS_TEST_NET)

# # Generate Mnemonic words
# mnemonic_words = crypto_instance.generate_mnemonic()
# print("Generating Mnemonic Words: ")
# print(mnemonic_words)
#
# # Generate Private Key, Public Address and mnemonic
# key = crypto_instance.generate_key()
# print('Generating Private Key / Public Key / Mnemonic words: ')
# print(key)
#
# # Generate Private Key, Public Address from mnemonic
# mnemonic_words = crypto_instance.generate_mnemonic()
# key = crypto_instance.generate_key_from_mnemoic(mnemonic_words)
# print("Mnemonic Words: %s" % mnemonic_words)
# print("Keys: %s" % key)
#
# # Generat Bunch of Private Keys, Public Address from one set of Mnemonic words
# mnemonic_words = crypto_instance.generate_mnemonic()
# keys = crypto_instance.generate_keys_from_mnemonic(mnemonic_words, 10)
# print("Mnemonic Words: %s" % mnemonic_words)
# print("Keys: ")
# for key in keys:
#     print(key)

# ------------ End of Crypto Sample ---------------


# -------------- Socket Sample ------------------

from binance_dex.sockets import BinanceChainSocket


# Sample of Customized Callback function to handle received data
def customized_msg_handler(ws, received_message):
    ''' Simply print out '''
    print('----- Customized handler -----')
    print(str(received_message))


# Create Socket Instance
socket_instance = BinanceChainSocket(IS_TEST_NET)

# # -- Sample of Short-lived (one-off / send-receive) Connection ----
# print(socket_instance.fetch_block_height_updates())
#
# # -- Sample of Long Lived Connection WITHOUT customized Callback ----
# # If callback function not provided, will simply print out
# socket_instance.fetch_block_height_updates(one_off=False)
#
# # If callback function provided, can customized handle received data
# socket_instance.fetch_block_height_updates(one_off=False, callback_function=customized_msg_handler)
#
#
# # !!! Note: below samples only provide "long-lived" calls. But actually both are supported !!!
# # <--- Here we go --->

# Fetch Account Updates, Including: Orders, Transfer, Balance
# socket_instance.fetch_account_updates(user_address='tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw',
#                                       one_off=False,
#                                       callback_function=customized_msg_handler)

# Fetch Market Trades Information by Trading Pair
# socket_instance.fetch_trades_updates(trading_pairs='100K-9BC_BNB',
#                                      one_off=False,
#                                      callback_function=customized_msg_handler)

# Fetch Market Trading Depth Stream by Trading Pair
# socket_instance.fetch_market_diff_stream(trading_pairs='100K-9BC_BNB',
#                                          one_off=False,
#                                          callback_function=customized_msg_handler)

# Fetch Market Top 20 Levels of Bids and Asks
# socket_instance.fetch_market_depth_stream(trading_pairs='100K-9BC_BNB',
#                                           one_off=False,
#                                           callback_function=customized_msg_handler)

# Fetch fetch_kline_updates
# from binance_dex.api import api_types_instance
# kline_intervals = api_types_instance.KLine()
# socket_instance.fetch_kline_updates(trading_pair='100K-9BC_BNB',
#                                     interval=kline_intervals.interval_1hour,
#                                     callback_function=customized_msg_handler)

# 24hr Ticker statistics for a single symbol are pushed every second
# socket_instance.fetch_ticker_streams(trading_pair='100K-9BC_BNB',
#                                      is_full_data=True,
#                                      one_off=False,
#                                      callback_function=customized_msg_handler)

# # 24hr Ticker statistics for ALL symbols are pushed every second
# socket_instance.fetch_ticker_streams(one_off=False,
#                                      callback_function=customized_msg_handler)


# -------------- Node RPC Sample ------------------

from binance_dex.node_rpc import BinanceChainNodeRPC

# Create Instance

# # OPTION 1: using existing RPC node
node_rpc_instance = BinanceChainNodeRPC(is_test_net=True,
                                        node_rpc_url=None)

# #OPTION 2: using your own node
# node_rpc_instance = BinanceChainNodeRPC(node_rpc_url='https://seed-pre-s3.binance.org')

# # Get available RPC endpoints (HTML format)
# print(node_rpc_instance.get_list())
#
# # Get info about the application
# print(node_rpc_instance.abci_info())
#
# # Get block at a given height. If no height is provided, it will fetch the latest block
# print(node_rpc_instance.block(height=10))
#
# # gets ABCIResults at a given height
# print(node_rpc_instance.block_results(height=100))
#
# # Broadcast Transaction (Async),
# print(node_rpc_instance.broadcast_tx_async(tx_id='123'))
#
# # Broadcast Transaction Sync,
# print(node_rpc_instance.broadcast_tx_sync(tx_id='123'))
#
# # Broadcast Trsaction Commit
# print(node_rpc_instance.broadcast_tx_commit(tx_id='123'))
#
# # Get block commit at a given height.
# print(node_rpc_instance.get_commit(height=10))
#
# # Get the consensus parameters at the given block height
# print(node_rpc_instance.consensus_params(height=100))
#
# # ConsensusState returns a concise summary of the consensus state.
# print(node_rpc_instance.consensus_state())
#
# # Get genesis file
# print(node_rpc_instance.genesis())
#
# # Get network info
# print(node_rpc_instance.net_info())
#
# # Get number of unconfirmed transactions
# print(node_rpc_instance.num_unconfirmed_txs())
#
# # Get Tendermint status including node info, pubkey, latest block hash, app hash, block height and time
# print(node_rpc_instance.status())
#
# # Query the transaction results by Hash
# print(node_rpc_instance.transaction(hash='C3FF309D7226768FC48B5E2D2D91719D77BAFA66DF7D3C53FCB212075DA83EA3'))
#
# # Get unconfirmed transactions (maximum ?limit entries) including their number
# print(node_rpc_instance.unconfirmed_txs())
#
# # Get the validator set at the given block height. If no height is provided, it will fetch the current validator set
# print(node_rpc_instance.validators(height=10))

# ----------- End of Node RPC Sample --------------
