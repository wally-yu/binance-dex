from binance_dex.tx_data_format import msg_transfer_pb2, stdSignature_pb2, stdTx_transfer_pb2

# Compose msg_transaction Protocol Buffer
msg_instance = msg_transfer_pb2.Send()

token_instance = msg_transfer_pb2.Send().Token()
token_instance.denom = 'BNB'
token_instance.amount = 10000

input_instance = msg_transfer_pb2.Send().Input()
input_instance.address = 'aa'
input_instance.coins.extend([token_instance])

output_instance = msg_transfer_pb2.Send().Output()
output_instance.address = 'bb'
output_instance.coins.extend([token_instance])

msg_instance.inputs.extend([input_instance])
msg_instance.outputs.extend([output_instance])

# Compose stdSignature Protocol Buffer
pub_key_instance = stdSignature_pb2.StdSignature().PubKey()
pub_key_instance.type = "tendermint/PubKeySecp256k1"
pub_key_instance.value = 'AoWY3eWBOnnvLPTz4RsUlX1pWCkLLPewu1vAAoTEzxzR'

std_signature_instance = stdSignature_pb2.StdSignature()
std_signature_instance.pub_key.CopyFrom(pub_key_instance)
std_signature_instance.signature = '6O2TQAgleFNPw4zIWBLaNvOf5dR7DHNSr2DwAPeFK6lokRqZd2KR2BD'
std_signature_instance.account_number = 666558
std_signature_instance.sequence = 26

# Compose stdTx_transfer Protocol Buffer
transfer_instance = stdTx_transfer_pb2.StdTx()
transfer_instance.msg.extend([msg_instance])
transfer_instance.signatures.extend([std_signature_instance])
transfer_instance.memo = 'trans by wally'
transfer_instance.source = 0
transfer_instance.data = ''

print(transfer_instance)