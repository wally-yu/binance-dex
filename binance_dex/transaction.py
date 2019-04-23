from binance_dex.tx_data_format import msg_transfer_pb2, stdSignature_pb2, stdTx_transfer_pb2
import binascii
# from binance_dex.lib.crypto import *
from secp256k1 import PrivateKey, ECDSA
from_addr = 'tbnb1r4gc5ftrkr9ez2khph4h5xxd0mf0hd75jf06gw'
to_addr = 'tbnb1fn9z9vn4f44ekz0a3pf80dcy2wh4d5988phjds'
pri_key = 'ef5b7ba4eb6a7add623315e1edc90b3fc24ff107bc874e168d188ab9bd4397b9'

from binance_dex.api import BinanceChainClient, api_types_instance
from binance_dex.lib.common import *
from binance_dex.lib import bech32
import varint
import json
from collections import OrderedDict

# Create API Client instance
api_client = BinanceChainClient(is_test_net=True)
account_info = api_client.get_account_info_by_address(address=from_addr)
sequence = account_info['result']['sequence']
account_number = account_info['result']['account_number']
node_info = api_client.get_node_info()
chain_id = node_info['result']['node_info']['network']
#
# # private_key_instance = HDPrivateKey(key=pri_key,
# #                                     chain_code=chain_id,
# #                                     depth=1)
# private_key_instance = PrivateKey(bytes(bytearray.fromhex(pri_key)))
# bytes_pub_key = private_key_instance.pubkey.serialize(compressed=True)



# Compose msg_transaction Protocol Buffer
msg_instance = msg_transfer_pb2.Send()

token_instance = msg_transfer_pb2.Send().Token()
token_instance.denom = 'DEX.B-C72'
token_instance.amount = int(0.77*100000000)

input_instance = msg_transfer_pb2.Send().Input()
input_instance.address = bech32.decode_address(from_addr)
input_instance.coins.extend([token_instance])

output_instance = msg_transfer_pb2.Send().Output()
output_instance.address = bech32.decode_address(to_addr)
output_instance.coins.extend([token_instance])

msg_instance.inputs.extend([input_instance])
msg_instance.outputs.extend([output_instance])


# Transfer Msg to dic
transfer_msg_to_dic = OrderedDict([
            ('inputs', [
                OrderedDict([
                    ('address', from_addr),
                    ('coins', [
                        OrderedDict([
                            ('amount', int(0.77*100000000)),
                            ('denom', 'DEX.B-C72')
                        ])
                    ])
                ])
            ]),
            ('outputs', [
                OrderedDict([
                    ('address', to_addr),
                    ('coins', [
                        OrderedDict([
                            ('amount', int(0.77*100000000)),
                            ('denom', 'DEX.B-C72')
                        ])
                    ])
                ])
            ])
        ])

# Compose stdSignature Protocol Buffer
pub_key_instance = stdSignature_pb2.StdSignature().PubKey()
pub_key_proto = bech32.decode_address(from_addr)
pub_key_type_bytes = binascii.unhexlify(b"EB5AE987")
pub_key_varint_length = varint.encode(len(pub_key_proto))
pub_key_message = pub_key_type_bytes + pub_key_varint_length + pub_key_proto

# Sign...
sign_str = json.dumps(OrderedDict([
            ('account_number', account_number),
            ('chain_id', chain_id),
            ('data', None),
            ('memo', 'memo wali'),
            ('msgs', transfer_msg_to_dic),
            ('sequence', sequence),
            ('source', 0)
        ]), separators=(',', ':'), ensure_ascii=False)
sign_str = sign_str.encode()
signed = PrivateKey().ecdsa_sign(msg=sign_str)
signed = PrivateKey().ecdsa_serialize_compact(signed)
signature = signed[-64:]

std_signature_instance = stdSignature_pb2.StdSignature()
std_signature_instance.pub_key = pub_key_message
std_signature_instance.signature = signature
std_signature_instance.account_number = account_number
std_signature_instance.sequence = sequence

# calc SIZE-OF-ENCODED
sig_proto = std_signature_instance.SerializeToString()
sig_varint_len = varint.encode(len(sig_proto))
sig_msg = b'' + sig_proto


# Compose stdTx_transfer Protocol Buffer
transfer_instance = stdTx_transfer_pb2.StdTx()
transfer_instance.msg.extend([msg_instance])
transfer_instance.signatures.extend([std_signature_instance])
transfer_instance.memo = 'trans by wally'
transfer_instance.source = 1
transfer_instance.data = ''

# calc SIZE-OF-ENCODED
tx_proto = transfer_instance.SerializeToString()
tx_varint_len = varint.encode(len(tx_proto))
tx_msg = b'' + tx_varint_len + tx_proto

broadcase_code = binascii.hexlify(tx_msg)

print(broadcase_code)
ret = api_client.post_broadcase(broadcase_code)
print(ret)
