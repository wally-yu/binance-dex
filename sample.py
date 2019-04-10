# Global setting to indicate if test net
# If not specify and pass to "Class", default value would be "False"
IS_TEST_NET = True

# ---------------- API Sample -------------------

from binance_dex.api import Client, api_types_instance

# Create API Client instance
api_client = Client(is_test_net=IS_TEST_NET)

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
#
# # Get Listing Tokens
# print('Token Listed: ')
# print(api_client.get_tokens())
#
# # Get Account Info By Address
# address = 'tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw'
# print('Account info for %s:' % address)
# print(api_client.get_account_info_by_address(address=address))
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

# # Get KLines
# trading_pair = 'DEX.B-C72_BNB'
# print("Last 100 4hour Klines with trading Pair '%s':" % trading_pair)
# print(api_client.get_klines(trading_pair=trading_pair,
#                             interval=api_types_instance.KLine.interval_4hour,
#                             limit=100))

# ------------ End of API Sample ----------------


# -------------- Crypto Sample ------------------

# from binance_dex.crypto import Crypto
#
# # Create crypto instance
# crypto_instance = Crypto(is_test_net=IS_TEST_NET)
#
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
