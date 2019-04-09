# Global setting to indicate if test net
# If not specify and pass to "Class", default value would be "False"
IS_TEST_NET = True

# ---------------- API Sample -------------------

from binance_dex.api import Client

# Create API Client instance
api_client = Client(is_test_net=IS_TEST_NET)

# # Get Binance Chain Fees
# print('Fees:')
# print(api_client.get_fees())

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
